---
title: udp_efficient_streams
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.asyncio<wbr>.efficient_streams<wbr>.versions<wbr>.v_0<wbr>.udp_efficient_streams    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-udp_efficient_streams-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-udp_efficient_streams-view-source"><span>View Source</span></label>

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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.2.0&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;StreamType&#39;</span><span class="p">,</span> <span class="s1">&#39;GateSecurityPolicy&#39;</span><span class="p">,</span> <span class="s1">&#39;StreamManagerIOCoreMemoryManagement&#39;</span><span class="p">,</span> <span class="s1">&#39;UdpStreamManager&#39;</span><span class="p">,</span> <span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;UdpStreamReaderProtocol&#39;</span><span class="p">,</span> <span class="s1">&#39;UdpStreamWriter&#39;</span><span class="p">]</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">import</span> <span class="nn">warnings</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">asyncio.exceptions</span> <span class="kn">import</span> <span class="n">IncompleteReadError</span><span class="p">,</span> <span class="n">LimitOverrunError</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">streams</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">asyncio.streams</span> <span class="kn">import</span> <span class="n">StreamWriter</span> <span class="k">as</span> <span class="n">OriginalStreamWriter</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">asyncio.streams</span> <span class="kn">import</span> <span class="n">StreamReader</span> <span class="k">as</span> <span class="n">OriginalStreamReader</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">asyncio.streams</span> <span class="kn">import</span> <span class="n">StreamReaderProtocol</span> <span class="k">as</span> <span class="n">OriginalStreamReaderProtocol</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">events</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">proactor_events</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">selector_events</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">unix_events</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="k">pass</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">coroutines</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="kn">from</span> <span class="nn">asyncio.tasks</span> <span class="kn">import</span> <span class="n">sleep</span><span class="p">,</span> <span class="n">Task</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="kn">from</span> <span class="nn">asyncio.futures</span> <span class="kn">import</span> <span class="n">Future</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="kn">from</span> <span class="nn">copy</span> <span class="kn">import</span> <span class="n">copy</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="kn">from</span> <span class="nn">cengal.io.asock_io.versions.v_1.recv_buff_size_computer.recv_buff_size_computer__python</span> <span class="kn">import</span> <span class="n">RecvBuffSizeComputer</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="c1"># from cengal.io.asock_io.versions.v_1.base import IOCoreMemoryManagement</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.asyncio.atasks</span> <span class="kn">import</span> <span class="n">create_task</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.asyncio.timed_yield</span> <span class="kn">import</span> <span class="n">TimedYield</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="kn">from</span> <span class="nn">cengal.hardware.info.cpu</span> <span class="kn">import</span> <span class="n">cpu_info</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="c1"># from cengal.data_containers.dynamic_list_of_pieces import DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="c1"># from cengal.data_containers.fast_fifo import FIFODequeWithLengthControl, FIFOIsEmpty</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="c1"># from cengal.data_manipulation.front_triggerable_variable import FrontTriggerableVariable, FrontTriggerableVariableType</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="kn">from</span> <span class="nn">cengal.data_containers.dynamic_list_of_pieces.versions.v_1.dynamic_list_of_pieces__python</span> <span class="kn">import</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values.versions</span> <span class="kn">import</span> <span class="n">ValueExistence</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">List</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="kn">from</span> <span class="nn">.efficient_streams_base_internal</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="kn">from</span> <span class="nn">.efficient_streams_base</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="kn">from</span> <span class="nn">.efficient_streams_abstract</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="k">class</span> <span class="nc">UdpStreamManager</span><span class="p">(</span><span class="n">StreamManagerAbstract</span><span class="p">):</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">io_memory_management</span><span class="p">:</span> <span class="n">StreamManagerIOCoreMemoryManagement</span> <span class="o">=</span> <span class="n">StreamManagerIOCoreMemoryManagement</span><span class="p">()</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mf">10.0</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client_container_type</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client_container_type</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">open_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>                            <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;A wrapper for create_connection() returning a (reader, writer) pair.</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="sd">        The reader returned is a UdpStreamReader instance; the writer is a</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a><span class="sd">        UdpStreamWriter instance.</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="sd">        The arguments are all the usual arguments to create_connection()</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="sd">        except protocol_factory; most common are positional host and port,</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="sd">        with various optional keyword arguments following.</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a><span class="sd">        UdpStreamReader).</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="sd">        (If you want to customize the UdpStreamReader and/or</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a><span class="sd">        UdpStreamReaderProtocol classes, just copy the code -- there&#39;s</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a><span class="sd">        really nothing special here except some convenience.)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="k">if</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">gate</span> <span class="o">==</span> <span class="n">stream_type</span><span class="p">:</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong stream_type value: client can not be a &quot;gate&quot;.&#39;</span><span class="p">)</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">UdpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">UdpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="n">transport</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_connection</span><span class="p">(</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>            <span class="k">lambda</span><span class="p">:</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">UdpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">start_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>                        <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>                        <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>                        <span class="n">gate_security_policy</span><span class="p">:</span> <span class="n">GateSecurityPolicy</span> <span class="o">=</span> <span class="n">GateSecurityPolicy</span><span class="o">.</span><span class="n">disabled</span><span class="p">,</span> <span class="n">policy_managed_stream_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>                        <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>                        <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>                        <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Start a socket server, call back for each client connected.</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a><span class="sd">        The first parameter, `client_connected_cb`, takes two parameters:</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a><span class="sd">        client_reader, client_writer.  client_reader is a UdpStreamReader</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="sd">        object, while client_writer is a UdpStreamWriter object.  This</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a><span class="sd">        parameter can either be a plain callback function or a coroutine;</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a><span class="sd">        if it is a coroutine, it will be automatically converted into a</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a><span class="sd">        Task.</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a><span class="sd">        The rest of the arguments are all the usual arguments to</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a><span class="sd">        loop.create_server() except protocol_factory; most common are</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a><span class="sd">        positional host and port, with various optional keyword arguments</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a><span class="sd">        following.  The return value is the same as loop.create_server().</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a><span class="sd">        UdpStreamReader).</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a><span class="sd">        The return value is the same as loop.create_server(), i.e. a</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a><span class="sd">        Server object which can be used to stop the service.</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>        <span class="k">def</span> <span class="nf">factory</span><span class="p">():</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>            <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>            <span class="n">reader</span> <span class="o">=</span>  <span class="n">UdpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="n">protocol</span> <span class="o">=</span> <span class="n">UdpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>                                            <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>            <span class="k">return</span> <span class="n">protocol</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_server</span><span class="p">(</span><span class="n">factory</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>    
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_server_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;UdpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>    
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_client_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;UdpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a><span class="k">class</span> <span class="nc">Server</span><span class="p">(</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractServer</span><span class="p">):</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">,</span> <span class="n">sockets</span><span class="p">,</span> <span class="n">protocol_factory</span><span class="p">,</span> <span class="n">ssl_context</span><span class="p">,</span> <span class="n">backlog</span><span class="p">,</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>                 <span class="n">ssl_handshake_timeout</span><span class="p">):</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span> <span class="o">=</span> <span class="n">loop</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_sockets</span> <span class="o">=</span> <span class="n">sockets</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_active_count</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_waiters</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_protocol_factory</span> <span class="o">=</span> <span class="n">protocol_factory</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_ssl_context</span> <span class="o">=</span> <span class="n">ssl_context</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_ssl_handshake_timeout</span> <span class="o">=</span> <span class="n">ssl_handshake_timeout</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serving</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;&lt;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1"> sockets=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">sockets</span><span class="si">!r}</span><span class="s1">&gt;&#39;</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">get_loop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    <span class="k">def</span> <span class="nf">is_serving</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serving</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>    <span class="nd">@property</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>    <span class="k">def</span> <span class="nf">sockets</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sockets</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>            <span class="k">return</span> <span class="p">()</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">trsock</span><span class="o">.</span><span class="n">TransportSocket</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sockets</span><span class="p">)</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>    <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="n">sockets</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sockets</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="k">if</span> <span class="n">sockets</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="k">return</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_sockets</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="k">for</span> <span class="n">sock</span> <span class="ow">in</span> <span class="n">sockets</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">_stop_serving</span><span class="p">(</span><span class="n">sock</span><span class="p">)</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serving</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>                <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span><span class="o">.</span><span class="n">done</span><span class="p">()):</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span><span class="o">.</span><span class="n">cancel</span><span class="p">()</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_active_count</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_wakeup</span><span class="p">()</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">start_serving</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_serving</span><span class="p">()</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>        <span class="c1"># Skip one loop iteration so that all &#39;loop.add_reader&#39;</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>        <span class="c1"># go through.</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="k">await</span> <span class="n">tasks</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">serve_forever</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>                <span class="sa">f</span><span class="s1">&#39;server </span><span class="si">{</span><span class="bp">self</span><span class="si">!r}</span><span class="s1"> is already being awaited on serve_forever()&#39;</span><span class="p">)</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sockets</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;server </span><span class="si">{</span><span class="bp">self</span><span class="si">!r}</span><span class="s1"> is closed&#39;</span><span class="p">)</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_serving</span><span class="p">()</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        <span class="k">except</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">CancelledError</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">wait_closed</span><span class="p">()</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            <span class="k">finally</span><span class="p">:</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>                <span class="k">raise</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_serving_forever_fut</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">wait_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sockets</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_waiters</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>            <span class="k">return</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="n">waiter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_waiters</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">waiter</span><span class="p">)</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="k">await</span> <span class="n">waiter</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a><span class="k">class</span> <span class="nc">UdpStreamReader</span><span class="p">(</span><span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">StreamReaderAbstract</span><span class="p">):</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">input_from_client_container_type</span><span class="p">(</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span> <span class="o">=</span> <span class="n">RecvBuffSizeComputer</span><span class="p">()</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>        <span class="n">cpu_info_inst</span> <span class="o">=</span> <span class="n">cpu_info</span><span class="p">()</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l2_cache_size_per_virtual_core</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size_per_virtual_core</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 3145728</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">max_recv_buff_size</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 1024</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="c1"># print(f&#39;max_recv_buff_size: {self.recv_buff_size_computer.max_recv_buff_size}&#39;)</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>    
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>    
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>    
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_with_counter</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>        <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>        <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>            <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_max</span><span class="p">()</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>            <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                <span class="k">break</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>            <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">),</span> <span class="n">counter</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>        <span class="n">info</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">]</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span><span class="si">}</span><span class="s1"> bytes&#39;</span><span class="p">)</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;eof&#39;</span><span class="p">)</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span> <span class="o">!=</span> <span class="n">DEFAULT_LIMIT</span><span class="p">:</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;limit=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_waiter</span><span class="p">:</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;waiter=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiter</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span><span class="p">:</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;exception=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_exception</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">:</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;transport=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span><span class="p">:</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;paused&#39;</span><span class="p">)</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="k">return</span> <span class="s1">&#39;&lt;</span><span class="si">{}</span><span class="s1">&gt;&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">info</span><span class="p">))</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>    <span class="k">def</span> <span class="nf">_maybe_resume_transport</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">,</span> <span class="p">(</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>            <span class="n">proactor_events</span><span class="o">.</span><span class="n">_ProactorDatagramTransport</span><span class="p">,</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>            <span class="n">selector_events</span><span class="o">.</span><span class="n">_SelectorTransport</span><span class="p">,</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>            <span class="n">unix_events</span><span class="o">.</span><span class="n">_UnixReadPipeTransport</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>            <span class="p">)):</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>            <span class="c1"># if hasattr(self._transport, &#39;max_size&#39;):</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">max_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">recv_buff_size</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>                <span class="c1"># print(f&#39;max_size: {self._transport.max_size}&#39;)</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>                <span class="k">pass</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> \
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>            <span class="ow">and</span> <span class="p">(</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>                <span class="p">((</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">))</span> \
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">))</span> \
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">))</span> \
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="p">))</span> \
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">))</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>            <span class="p">):</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>    <span class="k">def</span> <span class="nf">at_eof</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Return True if the buffer is empty and &#39;feed_eof&#39; was called.&quot;&quot;&quot;</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>    <span class="k">def</span> <span class="nf">feed_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="k">assert</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">,</span> <span class="s1">&#39;feed_data after feed_eof&#39;</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>            <span class="k">return</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>        <span class="n">data_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">data_len</span><span class="p">)</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_wakeup_waiter</span><span class="p">()</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>                <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> 
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>                <span class="ow">and</span> <span class="p">(</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>                    <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">)))</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>                <span class="p">)):</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>                <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>                <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>                <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readline</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read chunk of data from the stream until newline (b&#39;\n&#39;) is found.</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a><span class="sd">        On success, return chunk that ends with newline. If only partial</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a><span class="sd">        line can be read due to EOF, return incomplete line without</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a><span class="sd">        terminating newline. When EOF was reached while no bytes read, empty</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a><span class="sd">        bytes object is returned.</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a><span class="sd">        If limit is reached, ValueError will be raised. In that case, if</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a><span class="sd">        newline was found, complete line including newline will be removed</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a><span class="sd">        from internal buffer. Else, internal buffer will be cleared. Limit is</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a><span class="sd">        compared against part of the line without newline.</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a><span class="sd">        needed.</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        <span class="n">sep</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>            <span class="n">line</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readuntil</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="k">except</span> <span class="n">IncompleteReadError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>            <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">partial</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>        <span class="k">except</span> <span class="n">LimitOverrunError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">sep</span><span class="p">,</span> <span class="n">e</span><span class="o">.</span><span class="n">consumed</span><span class="p">):</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">consumed</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>            
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        <span class="k">return</span> <span class="n">line</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readuntil</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">separator</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read data from the stream until ``separator`` is found.</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a><span class="sd">        On success, the data and separator will be removed from the</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a><span class="sd">        internal buffer (consumed). Returned data will include the</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a><span class="sd">        separator at the end.</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a><span class="sd">        Configured stream limit is used to check result. Limit sets the</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a><span class="sd">        maximal length of data that can be returned, not counting the</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a><span class="sd">        separator.</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a><span class="sd">        If an EOF occurs and the complete separator is still not found,</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a><span class="sd">        an IncompleteReadError exception will be raised, and the internal</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a><span class="sd">        buffer will be reset.  The IncompleteReadError.partial attribute</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a><span class="sd">        may contain the separator partially.</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a><span class="sd">        If the data cannot be read because of over limit, a</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a><span class="sd">        LimitOverrunError exception  will be raised, and the data</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a><span class="sd">        will be left in the internal buffer, so it can be read again.</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">separator</span><span class="p">)</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="k">if</span> <span class="n">seplen</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;Separator should be at least one-byte string&#39;</span><span class="p">)</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>        <span class="c1"># Consume whole buffer except last bytes, which length is</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="c1"># one less than seplen. Let&#39;s check corner cases with</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        <span class="c1"># separator=&#39;SEPARATOR&#39;:</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>        <span class="c1"># * we have received almost complete separator (without last</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>        <span class="c1">#   byte). i.e buffer=&#39;some textSEPARATO&#39;. In this case we</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>        <span class="c1">#   can safely consume len(separator) - 1 bytes.</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="c1"># * last byte of buffer is first byte of separator, i.e.</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>        <span class="c1">#   buffer=&#39;abcdefghijklmnopqrS&#39;. We may safely consume</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>        <span class="c1">#   everything except that last byte, but this require to</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>        <span class="c1">#   analyze bytes of buffer that match partial separator.</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>        <span class="c1">#   This is slow and/or require FSM. For this case our</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="c1">#   implementation is not optimal, since require rescanning</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="c1">#   of data that is known to not belong to separator. In</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>        <span class="c1">#   real world, separator will not be so long to notice</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>        <span class="c1">#   performance problems. Even when reading MIME-encoded</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="c1">#   messages :)</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>        <span class="c1"># `offset` is the number of bytes from the beginning of the buffer</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        <span class="c1"># where there is no occurrence of `separator`.</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>        <span class="c1"># Loop until we find `separator` in the buffer, exceed the buffer size,</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>        <span class="c1"># or an EOF has happened.</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>            <span class="n">buflen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>            <span class="c1"># Check if we now have enough data in the buffer for `separator` to</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>            <span class="c1"># fit.</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>            <span class="k">if</span> <span class="n">buflen</span> <span class="o">-</span> <span class="n">offset</span> <span class="o">&gt;=</span> <span class="n">seplen</span><span class="p">:</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>                <span class="n">isep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">separator</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>                <span class="k">if</span> <span class="n">isep</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>                    <span class="c1"># `separator` is in the buffer. `isep` will be used later</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>                    <span class="c1"># to retrieve the data.</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>                    <span class="k">break</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>                <span class="c1"># see upper comment for explanation.</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>                <span class="n">offset</span> <span class="o">=</span> <span class="n">buflen</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">-</span> <span class="n">seplen</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>                <span class="k">if</span> <span class="n">offset</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>                    <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>                        <span class="s1">&#39;Separator is not found, and chunk exceed the limit&#39;</span><span class="p">,</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>                        <span class="n">offset</span><span class="p">)</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>            <span class="c1"># Complete message (with full separator) may be present in buffer</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>            <span class="c1"># even when EOF flag is set. This may happen when the last chunk</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>            <span class="c1"># adds data which makes separator be found. That&#39;s why we check for</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>            <span class="c1"># EOF *ater* inspecting the buffer.</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>                <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>            <span class="c1"># _wait_for_data() will resume reading if stream was paused.</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readuntil&#39;</span><span class="p">)</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>        <span class="k">if</span> <span class="n">isep</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>            <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>                <span class="s1">&#39;Separator is found, but chunk is longer than limit&#39;</span><span class="p">,</span> <span class="n">isep</span><span class="p">)</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>        <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">isep</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a><span class="sd">        object.</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a><span class="sd">        creation.</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a><span class="sd">        needed.</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>                    <span class="k">break</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a><span class="sd">        object.</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a><span class="sd">        creation.</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a><span class="sd">        needed.</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>                    <span class="k">break</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data_nearly</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read exactly `n` bytes.</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a><span class="sd">        Raise an IncompleteReadError if EOF is reached before `n` bytes can be</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a><span class="sd">        read. The IncompleteReadError.partial attribute of the exception will</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a><span class="sd">        contain the partial read bytes.</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a><span class="sd">        if n is zero, return empty bytes object.</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a><span class="sd">        creation.</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a><span class="sd">        needed.</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a>
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a>
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a>    
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readonly_exactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a>
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos">659</span></a>    
</span><span id="L-660"><a href="#L-660"><span class="linenos">660</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_message</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-661"><a href="#L-661"><span class="linenos">661</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span><span class="p">)</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos">662</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos">663</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="n">message_len</span><span class="p">)</span>
</span><span id="L-664"><a href="#L-664"><span class="linenos">664</span></a>    
</span><span id="L-665"><a href="#L-665"><span class="linenos">665</span></a>    <span class="k">def</span> <span class="nf">message_awailable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos">666</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos">667</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">message_size_len</span><span class="p">:</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos">668</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-669"><a href="#L-669"><span class="linenos">669</span></a>
</span><span id="L-670"><a href="#L-670"><span class="linenos">670</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos">671</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-672"><a href="#L-672"><span class="linenos">672</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="p">(</span><span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_len</span><span class="p">):</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos">673</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos">674</span></a>        
</span><span id="L-675"><a href="#L-675"><span class="linenos">675</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-676"><a href="#L-676"><span class="linenos">676</span></a>    
</span><span id="L-677"><a href="#L-677"><span class="linenos">677</span></a>    <span class="k">def</span> <span class="nf">transport_pause_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos">678</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-679"><a href="#L-679"><span class="linenos">679</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos">680</span></a>        <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos">681</span></a>            <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos">682</span></a>            <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos">683</span></a>            <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="L-684"><a href="#L-684"><span class="linenos">684</span></a>            <span class="k">pass</span>
</span><span id="L-685"><a href="#L-685"><span class="linenos">685</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos">686</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos">687</span></a>    
</span><span id="L-688"><a href="#L-688"><span class="linenos">688</span></a>    <span class="k">def</span> <span class="nf">transport_resume_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos">689</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos">690</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span><span id="L-691"><a href="#L-691"><span class="linenos">691</span></a>
</span><span id="L-692"><a href="#L-692"><span class="linenos">692</span></a>
</span><span id="L-693"><a href="#L-693"><span class="linenos">693</span></a><span class="k">class</span> <span class="nc">UdpStreamReaderProtocol</span><span class="p">(</span><span class="n">OriginalStreamReaderProtocol</span><span class="p">,</span> <span class="n">StreamReaderProtocolAbstract</span><span class="p">):</span>
</span><span id="L-694"><a href="#L-694"><span class="linenos">694</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-695"><a href="#L-695"><span class="linenos">695</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos">696</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="L-697"><a href="#L-697"><span class="linenos">697</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-698"><a href="#L-698"><span class="linenos">698</span></a>
</span><span id="L-699"><a href="#L-699"><span class="linenos">699</span></a>    <span class="k">def</span> <span class="nf">connection_made</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="L-700"><a href="#L-700"><span class="linenos">700</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reject_connection</span><span class="p">:</span>
</span><span id="L-701"><a href="#L-701"><span class="linenos">701</span></a>            <span class="n">context</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos">702</span></a>                <span class="s1">&#39;message&#39;</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;An open stream was garbage collected prior to &#39;</span>
</span><span id="L-703"><a href="#L-703"><span class="linenos">703</span></a>                            <span class="s1">&#39;establishing network connection; &#39;</span>
</span><span id="L-704"><a href="#L-704"><span class="linenos">704</span></a>                            <span class="s1">&#39;call &quot;stream.close()&quot; explicitly.&#39;</span><span class="p">)</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos">705</span></a>            <span class="p">}</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos">706</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span><span class="p">:</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos">707</span></a>                <span class="n">context</span><span class="p">[</span><span class="s1">&#39;source_traceback&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span>
</span><span id="L-708"><a href="#L-708"><span class="linenos">708</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">call_exception_handler</span><span class="p">(</span><span class="n">context</span><span class="p">)</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos">709</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">abort</span><span class="p">()</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos">710</span></a>            <span class="k">return</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos">711</span></a>        
</span><span id="L-712"><a href="#L-712"><span class="linenos">712</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="n">transport</span>
</span><span id="L-713"><a href="#L-713"><span class="linenos">713</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_reader</span>
</span><span id="L-714"><a href="#L-714"><span class="linenos">714</span></a>        <span class="k">if</span> <span class="n">reader</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-715"><a href="#L-715"><span class="linenos">715</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">set_transport</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span>
</span><span id="L-716"><a href="#L-716"><span class="linenos">716</span></a>
</span><span id="L-717"><a href="#L-717"><span class="linenos">717</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_over_ssl</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">get_extra_info</span><span class="p">(</span><span class="s1">&#39;sslcontext&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</span><span id="L-718"><a href="#L-718"><span class="linenos">718</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-719"><a href="#L-719"><span class="linenos">719</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span> <span class="o">=</span> <span class="n">UdpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span>
</span><span id="L-720"><a href="#L-720"><span class="linenos">720</span></a>                                               <span class="n">reader</span><span class="p">,</span>
</span><span id="L-721"><a href="#L-721"><span class="linenos">721</span></a>                                               <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>
</span><span id="L-722"><a href="#L-722"><span class="linenos">722</span></a>            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span><span class="p">(</span><span class="n">reader</span><span class="p">,</span>
</span><span id="L-723"><a href="#L-723"><span class="linenos">723</span></a>                                            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span><span class="p">)</span>
</span><span id="L-724"><a href="#L-724"><span class="linenos">724</span></a>            <span class="k">if</span> <span class="n">coroutines</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">res</span><span class="p">):</span>
</span><span id="L-725"><a href="#L-725"><span class="linenos">725</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">res</span><span class="p">)</span>
</span><span id="L-726"><a href="#L-726"><span class="linenos">726</span></a>            
</span><span id="L-727"><a href="#L-727"><span class="linenos">727</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_strong_reader</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-728"><a href="#L-728"><span class="linenos">728</span></a>
</span><span id="L-729"><a href="#L-729"><span class="linenos">729</span></a>
</span><span id="L-730"><a href="#L-730"><span class="linenos">730</span></a><span class="k">class</span> <span class="nc">UdpStreamWriter</span><span class="p">(</span><span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="n">StreamWriterAbstract</span><span class="p">):</span>
</span><span id="L-731"><a href="#L-731"><span class="linenos">731</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-732"><a href="#L-732"><span class="linenos">732</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-733"><a href="#L-733"><span class="linenos">733</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_stream_manager</span>
</span><span id="L-734"><a href="#L-734"><span class="linenos">734</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">output_to_client_container_type</span><span class="p">(</span>
</span><span id="L-735"><a href="#L-735"><span class="linenos">735</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_out__data_full_size</span><span class="p">)</span>
</span><span id="L-736"><a href="#L-736"><span class="linenos">736</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="p">:</span> <span class="n">ValueExistence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span>
</span><span id="L-737"><a href="#L-737"><span class="linenos">737</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">:</span> <span class="n">Task</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-738"><a href="#L-738"><span class="linenos">738</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-739"><a href="#L-739"><span class="linenos">739</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Future</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-740"><a href="#L-740"><span class="linenos">740</span></a>    
</span><span id="L-741"><a href="#L-741"><span class="linenos">741</span></a>    <span class="k">def</span> <span class="nf">optimized_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-742"><a href="#L-742"><span class="linenos">742</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-743"><a href="#L-743"><span class="linenos">743</span></a>        <span class="c1"># self.write(data)</span>
</span><span id="L-744"><a href="#L-744"><span class="linenos">744</span></a>
</span><span id="L-745"><a href="#L-745"><span class="linenos">745</span></a>    <span class="k">def</span> <span class="nf">owrite</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-746"><a href="#L-746"><span class="linenos">746</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-747"><a href="#L-747"><span class="linenos">747</span></a>
</span><span id="L-748"><a href="#L-748"><span class="linenos">748</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">partial_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-749"><a href="#L-749"><span class="linenos">749</span></a>        <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-750"><a href="#L-750"><span class="linenos">750</span></a>        <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="L-751"><a href="#L-751"><span class="linenos">751</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="L-752"><a href="#L-752"><span class="linenos">752</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="L-753"><a href="#L-753"><span class="linenos">753</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-754"><a href="#L-754"><span class="linenos">754</span></a>
</span><span id="L-755"><a href="#L-755"><span class="linenos">755</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-756"><a href="#L-756"><span class="linenos">756</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_drain</span><span class="p">()</span>
</span><span id="L-757"><a href="#L-757"><span class="linenos">757</span></a>
</span><span id="L-758"><a href="#L-758"><span class="linenos">758</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">full_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-759"><a href="#L-759"><span class="linenos">759</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">pdrain</span><span class="p">()</span>
</span><span id="L-760"><a href="#L-760"><span class="linenos">760</span></a>        <span class="n">rest_of_the_data_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="L-761"><a href="#L-761"><span class="linenos">761</span></a>        <span class="k">if</span> <span class="n">rest_of_the_data_size</span><span class="p">:</span>
</span><span id="L-762"><a href="#L-762"><span class="linenos">762</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">rest_of_the_data_size</span><span class="p">)</span>
</span><span id="L-763"><a href="#L-763"><span class="linenos">763</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="L-764"><a href="#L-764"><span class="linenos">764</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="L-765"><a href="#L-765"><span class="linenos">765</span></a>
</span><span id="L-766"><a href="#L-766"><span class="linenos">766</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">fdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-767"><a href="#L-767"><span class="linenos">767</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="L-768"><a href="#L-768"><span class="linenos">768</span></a>    
</span><span id="L-769"><a href="#L-769"><span class="linenos">769</span></a>    <span class="k">def</span> <span class="nf">_release_autonomous_writer_waiters</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-770"><a href="#L-770"><span class="linenos">770</span></a>        <span class="n">current_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="L-771"><a href="#L-771"><span class="linenos">771</span></a>        <span class="n">autonomous_writer_drain_enough_futures_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span>
</span><span id="L-772"><a href="#L-772"><span class="linenos">772</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">autonomous_writer_drain_enough_futures_buff</span><span class="p">)()</span>
</span><span id="L-773"><a href="#L-773"><span class="linenos">773</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">autonomous_writer_drain_enough_futures_buff</span><span class="p">:</span>
</span><span id="L-774"><a href="#L-774"><span class="linenos">774</span></a>            <span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="L-775"><a href="#L-775"><span class="linenos">775</span></a>            <span class="k">if</span> <span class="n">current_size</span> <span class="o">&lt;</span> <span class="n">lower_water_size</span><span class="p">:</span>
</span><span id="L-776"><a href="#L-776"><span class="linenos">776</span></a>                <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">done</span><span class="p">())</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="L-777"><a href="#L-777"><span class="linenos">777</span></a>                    <span class="n">future</span><span class="o">.</span><span class="n">set_result</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="L-778"><a href="#L-778"><span class="linenos">778</span></a>
</span><span id="L-779"><a href="#L-779"><span class="linenos">779</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">done</span><span class="p">())</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="L-780"><a href="#L-780"><span class="linenos">780</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
</span><span id="L-781"><a href="#L-781"><span class="linenos">781</span></a>    
</span><span id="L-782"><a href="#L-782"><span class="linenos">782</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">_autonomous_writer_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-783"><a href="#L-783"><span class="linenos">783</span></a>        <span class="n">ty</span> <span class="o">=</span> <span class="n">TimedYield</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="L-784"><a href="#L-784"><span class="linenos">784</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span>
</span><span id="L-785"><a href="#L-785"><span class="linenos">785</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-786"><a href="#L-786"><span class="linenos">786</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_release_autonomous_writer_waiters</span><span class="p">()</span>
</span><span id="L-787"><a href="#L-787"><span class="linenos">787</span></a>            <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="L-788"><a href="#L-788"><span class="linenos">788</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="L-789"><a href="#L-789"><span class="linenos">789</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="L-790"><a href="#L-790"><span class="linenos">790</span></a>                <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-791"><a href="#L-791"><span class="linenos">791</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_release_autonomous_writer_waiters</span><span class="p">()</span>
</span><span id="L-792"><a href="#L-792"><span class="linenos">792</span></a>            
</span><span id="L-793"><a href="#L-793"><span class="linenos">793</span></a>            <span class="k">await</span> <span class="n">ty</span><span class="p">()</span>
</span><span id="L-794"><a href="#L-794"><span class="linenos">794</span></a>    
</span><span id="L-795"><a href="#L-795"><span class="linenos">795</span></a>    <span class="k">def</span> <span class="nf">start_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-796"><a href="#L-796"><span class="linenos">796</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_impl</span><span class="p">)</span>
</span><span id="L-797"><a href="#L-797"><span class="linenos">797</span></a>    
</span><span id="L-798"><a href="#L-798"><span class="linenos">798</span></a>    <span class="k">def</span> <span class="nf">start_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-799"><a href="#L-799"><span class="linenos">799</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span><span id="L-800"><a href="#L-800"><span class="linenos">800</span></a>    
</span><span id="L-801"><a href="#L-801"><span class="linenos">801</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-802"><a href="#L-802"><span class="linenos">802</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="L-803"><a href="#L-803"><span class="linenos">803</span></a>
</span><span id="L-804"><a href="#L-804"><span class="linenos">804</span></a><span class="sd">        Args:</span>
</span><span id="L-805"><a href="#L-805"><span class="linenos">805</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="L-806"><a href="#L-806"><span class="linenos">806</span></a>
</span><span id="L-807"><a href="#L-807"><span class="linenos">807</span></a><span class="sd">        Returns:</span>
</span><span id="L-808"><a href="#L-808"><span class="linenos">808</span></a><span class="sd">            _type_: _description_</span>
</span><span id="L-809"><a href="#L-809"><span class="linenos">809</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-810"><a href="#L-810"><span class="linenos">810</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-811"><a href="#L-811"><span class="linenos">811</span></a>        <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-812"><a href="#L-812"><span class="linenos">812</span></a>            <span class="n">timeout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span>
</span><span id="L-813"><a href="#L-813"><span class="linenos">813</span></a>        
</span><span id="L-814"><a href="#L-814"><span class="linenos">814</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">):</span>
</span><span id="L-815"><a href="#L-815"><span class="linenos">815</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-816"><a href="#L-816"><span class="linenos">816</span></a>            <span class="k">if</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="L-817"><a href="#L-817"><span class="linenos">817</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">wait_for</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>
</span><span id="L-818"><a href="#L-818"><span class="linenos">818</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-819"><a href="#L-819"><span class="linenos">819</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span>
</span><span id="L-820"><a href="#L-820"><span class="linenos">820</span></a>            
</span><span id="L-821"><a href="#L-821"><span class="linenos">821</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-822"><a href="#L-822"><span class="linenos">822</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-823"><a href="#L-823"><span class="linenos">823</span></a>        
</span><span id="L-824"><a href="#L-824"><span class="linenos">824</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-825"><a href="#L-825"><span class="linenos">825</span></a>    
</span><span id="L-826"><a href="#L-826"><span class="linenos">826</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-827"><a href="#L-827"><span class="linenos">827</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="L-828"><a href="#L-828"><span class="linenos">828</span></a>
</span><span id="L-829"><a href="#L-829"><span class="linenos">829</span></a><span class="sd">        Args:</span>
</span><span id="L-830"><a href="#L-830"><span class="linenos">830</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="L-831"><a href="#L-831"><span class="linenos">831</span></a>
</span><span id="L-832"><a href="#L-832"><span class="linenos">832</span></a><span class="sd">        Returns:</span>
</span><span id="L-833"><a href="#L-833"><span class="linenos">833</span></a><span class="sd">            _type_: _description_</span>
</span><span id="L-834"><a href="#L-834"><span class="linenos">834</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-835"><a href="#L-835"><span class="linenos">835</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
</span><span id="L-836"><a href="#L-836"><span class="linenos">836</span></a>    
</span><span id="L-837"><a href="#L-837"><span class="linenos">837</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lower_water_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-838"><a href="#L-838"><span class="linenos">838</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-839"><a href="#L-839"><span class="linenos">839</span></a>            <span class="n">lower_water_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span> <span class="o">*</span> <span class="mi">3</span>
</span><span id="L-840"><a href="#L-840"><span class="linenos">840</span></a>            <span class="c1"># print(f&#39;lower_water_size: {lower_water_size}&#39;)</span>
</span><span id="L-841"><a href="#L-841"><span class="linenos">841</span></a>            <span class="c1"># lower_water_size = cpu_info().l3_cache_size</span>
</span><span id="L-842"><a href="#L-842"><span class="linenos">842</span></a>        
</span><span id="L-843"><a href="#L-843"><span class="linenos">843</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="L-844"><a href="#L-844"><span class="linenos">844</span></a>            <span class="n">future</span><span class="p">:</span> <span class="n">Future</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="L-845"><a href="#L-845"><span class="linenos">845</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span><span class="p">))</span>
</span><span id="L-846"><a href="#L-846"><span class="linenos">846</span></a>            <span class="k">await</span> <span class="n">future</span>
</span><span id="L-847"><a href="#L-847"><span class="linenos">847</span></a>    
</span><span id="L-848"><a href="#L-848"><span class="linenos">848</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aw_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-849"><a href="#L-849"><span class="linenos">849</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_drain_enough</span><span class="p">()</span>
</span><span id="L-850"><a href="#L-850"><span class="linenos">850</span></a>    
</span><span id="L-851"><a href="#L-851"><span class="linenos">851</span></a>    <span class="k">def</span> <span class="nf">optimized_write_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-852"><a href="#L-852"><span class="linenos">852</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span><span id="L-853"><a href="#L-853"><span class="linenos">853</span></a>    
</span><span id="L-854"><a href="#L-854"><span class="linenos">854</span></a>    <span class="k">def</span> <span class="nf">owrite_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-855"><a href="#L-855"><span class="linenos">855</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-856"><a href="#L-856"><span class="linenos">856</span></a>    
</span><span id="L-857"><a href="#L-857"><span class="linenos">857</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">send_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-858"><a href="#L-858"><span class="linenos">858</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-859"><a href="#L-859"><span class="linenos">859</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">fdrain</span><span class="p">()</span>
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
                <section id="UdpStreamManager">
                            <input id="UdpStreamManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UdpStreamManager</span><wbr>(<span class="base">cengal.parallel_execution.asyncio.efficient_streams.versions.v_0.efficient_streams_abstract.StreamManagerAbstract</span>):

                <label class="view-source-button" for="UdpStreamManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamManager-77"><a href="#UdpStreamManager-77"><span class="linenos"> 77</span></a><span class="k">class</span> <span class="nc">UdpStreamManager</span><span class="p">(</span><span class="n">StreamManagerAbstract</span><span class="p">):</span>
</span><span id="UdpStreamManager-78"><a href="#UdpStreamManager-78"><span class="linenos"> 78</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamManager-79"><a href="#UdpStreamManager-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">io_memory_management</span><span class="p">:</span> <span class="n">StreamManagerIOCoreMemoryManagement</span> <span class="o">=</span> <span class="n">StreamManagerIOCoreMemoryManagement</span><span class="p">()</span>
</span><span id="UdpStreamManager-80"><a href="#UdpStreamManager-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mf">10.0</span>
</span><span id="UdpStreamManager-81"><a href="#UdpStreamManager-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client_container_type</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="UdpStreamManager-82"><a href="#UdpStreamManager-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client_container_type</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="UdpStreamManager-83"><a href="#UdpStreamManager-83"><span class="linenos"> 83</span></a>
</span><span id="UdpStreamManager-84"><a href="#UdpStreamManager-84"><span class="linenos"> 84</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">open_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="UdpStreamManager-85"><a href="#UdpStreamManager-85"><span class="linenos"> 85</span></a>                            <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="UdpStreamManager-86"><a href="#UdpStreamManager-86"><span class="linenos"> 86</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="UdpStreamManager-87"><a href="#UdpStreamManager-87"><span class="linenos"> 87</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager-88"><a href="#UdpStreamManager-88"><span class="linenos"> 88</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager-89"><a href="#UdpStreamManager-89"><span class="linenos"> 89</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="UdpStreamManager-90"><a href="#UdpStreamManager-90"><span class="linenos"> 90</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;A wrapper for create_connection() returning a (reader, writer) pair.</span>
</span><span id="UdpStreamManager-91"><a href="#UdpStreamManager-91"><span class="linenos"> 91</span></a>
</span><span id="UdpStreamManager-92"><a href="#UdpStreamManager-92"><span class="linenos"> 92</span></a><span class="sd">        The reader returned is a UdpStreamReader instance; the writer is a</span>
</span><span id="UdpStreamManager-93"><a href="#UdpStreamManager-93"><span class="linenos"> 93</span></a><span class="sd">        UdpStreamWriter instance.</span>
</span><span id="UdpStreamManager-94"><a href="#UdpStreamManager-94"><span class="linenos"> 94</span></a>
</span><span id="UdpStreamManager-95"><a href="#UdpStreamManager-95"><span class="linenos"> 95</span></a><span class="sd">        The arguments are all the usual arguments to create_connection()</span>
</span><span id="UdpStreamManager-96"><a href="#UdpStreamManager-96"><span class="linenos"> 96</span></a><span class="sd">        except protocol_factory; most common are positional host and port,</span>
</span><span id="UdpStreamManager-97"><a href="#UdpStreamManager-97"><span class="linenos"> 97</span></a><span class="sd">        with various optional keyword arguments following.</span>
</span><span id="UdpStreamManager-98"><a href="#UdpStreamManager-98"><span class="linenos"> 98</span></a>
</span><span id="UdpStreamManager-99"><a href="#UdpStreamManager-99"><span class="linenos"> 99</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="UdpStreamManager-100"><a href="#UdpStreamManager-100"><span class="linenos">100</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="UdpStreamManager-101"><a href="#UdpStreamManager-101"><span class="linenos">101</span></a><span class="sd">        UdpStreamReader).</span>
</span><span id="UdpStreamManager-102"><a href="#UdpStreamManager-102"><span class="linenos">102</span></a>
</span><span id="UdpStreamManager-103"><a href="#UdpStreamManager-103"><span class="linenos">103</span></a><span class="sd">        (If you want to customize the UdpStreamReader and/or</span>
</span><span id="UdpStreamManager-104"><a href="#UdpStreamManager-104"><span class="linenos">104</span></a><span class="sd">        UdpStreamReaderProtocol classes, just copy the code -- there&#39;s</span>
</span><span id="UdpStreamManager-105"><a href="#UdpStreamManager-105"><span class="linenos">105</span></a><span class="sd">        really nothing special here except some convenience.)</span>
</span><span id="UdpStreamManager-106"><a href="#UdpStreamManager-106"><span class="linenos">106</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamManager-107"><a href="#UdpStreamManager-107"><span class="linenos">107</span></a>        <span class="k">if</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">gate</span> <span class="o">==</span> <span class="n">stream_type</span><span class="p">:</span>
</span><span id="UdpStreamManager-108"><a href="#UdpStreamManager-108"><span class="linenos">108</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong stream_type value: client can not be a &quot;gate&quot;.&#39;</span><span class="p">)</span>
</span><span id="UdpStreamManager-109"><a href="#UdpStreamManager-109"><span class="linenos">109</span></a>        
</span><span id="UdpStreamManager-110"><a href="#UdpStreamManager-110"><span class="linenos">110</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamManager-111"><a href="#UdpStreamManager-111"><span class="linenos">111</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="UdpStreamManager-112"><a href="#UdpStreamManager-112"><span class="linenos">112</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamManager-113"><a href="#UdpStreamManager-113"><span class="linenos">113</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="UdpStreamManager-114"><a href="#UdpStreamManager-114"><span class="linenos">114</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="UdpStreamManager-115"><a href="#UdpStreamManager-115"><span class="linenos">115</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="UdpStreamManager-116"><a href="#UdpStreamManager-116"><span class="linenos">116</span></a>        
</span><span id="UdpStreamManager-117"><a href="#UdpStreamManager-117"><span class="linenos">117</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="UdpStreamManager-118"><a href="#UdpStreamManager-118"><span class="linenos">118</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">UdpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager-119"><a href="#UdpStreamManager-119"><span class="linenos">119</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">UdpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager-120"><a href="#UdpStreamManager-120"><span class="linenos">120</span></a>        <span class="n">transport</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_connection</span><span class="p">(</span>
</span><span id="UdpStreamManager-121"><a href="#UdpStreamManager-121"><span class="linenos">121</span></a>            <span class="k">lambda</span><span class="p">:</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="UdpStreamManager-122"><a href="#UdpStreamManager-122"><span class="linenos">122</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">UdpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager-123"><a href="#UdpStreamManager-123"><span class="linenos">123</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span><span id="UdpStreamManager-124"><a href="#UdpStreamManager-124"><span class="linenos">124</span></a>
</span><span id="UdpStreamManager-125"><a href="#UdpStreamManager-125"><span class="linenos">125</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">start_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="UdpStreamManager-126"><a href="#UdpStreamManager-126"><span class="linenos">126</span></a>                        <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="UdpStreamManager-127"><a href="#UdpStreamManager-127"><span class="linenos">127</span></a>                        <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="UdpStreamManager-128"><a href="#UdpStreamManager-128"><span class="linenos">128</span></a>                        <span class="n">gate_security_policy</span><span class="p">:</span> <span class="n">GateSecurityPolicy</span> <span class="o">=</span> <span class="n">GateSecurityPolicy</span><span class="o">.</span><span class="n">disabled</span><span class="p">,</span> <span class="n">policy_managed_stream_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager-129"><a href="#UdpStreamManager-129"><span class="linenos">129</span></a>                        <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager-130"><a href="#UdpStreamManager-130"><span class="linenos">130</span></a>                        <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager-131"><a href="#UdpStreamManager-131"><span class="linenos">131</span></a>                        <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="UdpStreamManager-132"><a href="#UdpStreamManager-132"><span class="linenos">132</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Start a socket server, call back for each client connected.</span>
</span><span id="UdpStreamManager-133"><a href="#UdpStreamManager-133"><span class="linenos">133</span></a>
</span><span id="UdpStreamManager-134"><a href="#UdpStreamManager-134"><span class="linenos">134</span></a><span class="sd">        The first parameter, `client_connected_cb`, takes two parameters:</span>
</span><span id="UdpStreamManager-135"><a href="#UdpStreamManager-135"><span class="linenos">135</span></a><span class="sd">        client_reader, client_writer.  client_reader is a UdpStreamReader</span>
</span><span id="UdpStreamManager-136"><a href="#UdpStreamManager-136"><span class="linenos">136</span></a><span class="sd">        object, while client_writer is a UdpStreamWriter object.  This</span>
</span><span id="UdpStreamManager-137"><a href="#UdpStreamManager-137"><span class="linenos">137</span></a><span class="sd">        parameter can either be a plain callback function or a coroutine;</span>
</span><span id="UdpStreamManager-138"><a href="#UdpStreamManager-138"><span class="linenos">138</span></a><span class="sd">        if it is a coroutine, it will be automatically converted into a</span>
</span><span id="UdpStreamManager-139"><a href="#UdpStreamManager-139"><span class="linenos">139</span></a><span class="sd">        Task.</span>
</span><span id="UdpStreamManager-140"><a href="#UdpStreamManager-140"><span class="linenos">140</span></a>
</span><span id="UdpStreamManager-141"><a href="#UdpStreamManager-141"><span class="linenos">141</span></a><span class="sd">        The rest of the arguments are all the usual arguments to</span>
</span><span id="UdpStreamManager-142"><a href="#UdpStreamManager-142"><span class="linenos">142</span></a><span class="sd">        loop.create_server() except protocol_factory; most common are</span>
</span><span id="UdpStreamManager-143"><a href="#UdpStreamManager-143"><span class="linenos">143</span></a><span class="sd">        positional host and port, with various optional keyword arguments</span>
</span><span id="UdpStreamManager-144"><a href="#UdpStreamManager-144"><span class="linenos">144</span></a><span class="sd">        following.  The return value is the same as loop.create_server().</span>
</span><span id="UdpStreamManager-145"><a href="#UdpStreamManager-145"><span class="linenos">145</span></a>
</span><span id="UdpStreamManager-146"><a href="#UdpStreamManager-146"><span class="linenos">146</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="UdpStreamManager-147"><a href="#UdpStreamManager-147"><span class="linenos">147</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="UdpStreamManager-148"><a href="#UdpStreamManager-148"><span class="linenos">148</span></a><span class="sd">        UdpStreamReader).</span>
</span><span id="UdpStreamManager-149"><a href="#UdpStreamManager-149"><span class="linenos">149</span></a>
</span><span id="UdpStreamManager-150"><a href="#UdpStreamManager-150"><span class="linenos">150</span></a><span class="sd">        The return value is the same as loop.create_server(), i.e. a</span>
</span><span id="UdpStreamManager-151"><a href="#UdpStreamManager-151"><span class="linenos">151</span></a><span class="sd">        Server object which can be used to stop the service.</span>
</span><span id="UdpStreamManager-152"><a href="#UdpStreamManager-152"><span class="linenos">152</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamManager-153"><a href="#UdpStreamManager-153"><span class="linenos">153</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamManager-154"><a href="#UdpStreamManager-154"><span class="linenos">154</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="UdpStreamManager-155"><a href="#UdpStreamManager-155"><span class="linenos">155</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamManager-156"><a href="#UdpStreamManager-156"><span class="linenos">156</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="UdpStreamManager-157"><a href="#UdpStreamManager-157"><span class="linenos">157</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="UdpStreamManager-158"><a href="#UdpStreamManager-158"><span class="linenos">158</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="UdpStreamManager-159"><a href="#UdpStreamManager-159"><span class="linenos">159</span></a>
</span><span id="UdpStreamManager-160"><a href="#UdpStreamManager-160"><span class="linenos">160</span></a>        <span class="k">def</span> <span class="nf">factory</span><span class="p">():</span>
</span><span id="UdpStreamManager-161"><a href="#UdpStreamManager-161"><span class="linenos">161</span></a>            <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="UdpStreamManager-162"><a href="#UdpStreamManager-162"><span class="linenos">162</span></a>            <span class="n">reader</span> <span class="o">=</span>  <span class="n">UdpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager-163"><a href="#UdpStreamManager-163"><span class="linenos">163</span></a>            <span class="n">protocol</span> <span class="o">=</span> <span class="n">UdpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span>
</span><span id="UdpStreamManager-164"><a href="#UdpStreamManager-164"><span class="linenos">164</span></a>                                            <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager-165"><a href="#UdpStreamManager-165"><span class="linenos">165</span></a>            <span class="k">return</span> <span class="n">protocol</span>
</span><span id="UdpStreamManager-166"><a href="#UdpStreamManager-166"><span class="linenos">166</span></a>
</span><span id="UdpStreamManager-167"><a href="#UdpStreamManager-167"><span class="linenos">167</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_server</span><span class="p">(</span><span class="n">factory</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="UdpStreamManager-168"><a href="#UdpStreamManager-168"><span class="linenos">168</span></a>    
</span><span id="UdpStreamManager-169"><a href="#UdpStreamManager-169"><span class="linenos">169</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_server_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;UdpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="UdpStreamManager-170"><a href="#UdpStreamManager-170"><span class="linenos">170</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="UdpStreamManager-171"><a href="#UdpStreamManager-171"><span class="linenos">171</span></a>    
</span><span id="UdpStreamManager-172"><a href="#UdpStreamManager-172"><span class="linenos">172</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_client_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;UdpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="UdpStreamManager-173"><a href="#UdpStreamManager-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            <div id="UdpStreamManager.io_memory_management" class="classattr">
                                <div class="attr variable">
            <span class="name">io_memory_management</span><span class="annotation">: <a href="#StreamManagerIOCoreMemoryManagement">StreamManagerIOCoreMemoryManagement</a></span>

        
    </div>
    <a class="headerlink" href="#UdpStreamManager.io_memory_management"></a>
    
    

                            </div>
                            <div id="UdpStreamManager.autonomous_writer_stop_default_timeout" class="classattr">
                                <div class="attr variable">
            <span class="name">autonomous_writer_stop_default_timeout</span><span class="annotation">: Union[int, float, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#UdpStreamManager.autonomous_writer_stop_default_timeout"></a>
    
    

                            </div>
                            <div id="UdpStreamManager.output_to_client_container_type" class="classattr">
                                <div class="attr variable">
            <span class="name">output_to_client_container_type</span>

        
    </div>
    <a class="headerlink" href="#UdpStreamManager.output_to_client_container_type"></a>
    
    

                            </div>
                            <div id="UdpStreamManager.input_from_client_container_type" class="classattr">
                                <div class="attr variable">
            <span class="name">input_from_client_container_type</span>

        
    </div>
    <a class="headerlink" href="#UdpStreamManager.input_from_client_container_type"></a>
    
    

                            </div>
                            <div id="UdpStreamManager.open_connection" class="classattr">
                                        <input id="UdpStreamManager.open_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">open_connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">host</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">port</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">loop</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">limit</span><span class="o">=</span><span class="mi">10485760</span>,</span><span class="param">	<span class="n">stream_type</span><span class="p">:</span> <span class="n"><a href="#StreamType">StreamType</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#StreamType.general">StreamType.general</a></span><span class="p">:</span> <span class="mi">0</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>,</span><span class="param">	<span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwds</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamManager.open_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamManager.open_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamManager.open_connection-84"><a href="#UdpStreamManager.open_connection-84"><span class="linenos"> 84</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">open_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="UdpStreamManager.open_connection-85"><a href="#UdpStreamManager.open_connection-85"><span class="linenos"> 85</span></a>                            <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="UdpStreamManager.open_connection-86"><a href="#UdpStreamManager.open_connection-86"><span class="linenos"> 86</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="UdpStreamManager.open_connection-87"><a href="#UdpStreamManager.open_connection-87"><span class="linenos"> 87</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager.open_connection-88"><a href="#UdpStreamManager.open_connection-88"><span class="linenos"> 88</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager.open_connection-89"><a href="#UdpStreamManager.open_connection-89"><span class="linenos"> 89</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="UdpStreamManager.open_connection-90"><a href="#UdpStreamManager.open_connection-90"><span class="linenos"> 90</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;A wrapper for create_connection() returning a (reader, writer) pair.</span>
</span><span id="UdpStreamManager.open_connection-91"><a href="#UdpStreamManager.open_connection-91"><span class="linenos"> 91</span></a>
</span><span id="UdpStreamManager.open_connection-92"><a href="#UdpStreamManager.open_connection-92"><span class="linenos"> 92</span></a><span class="sd">        The reader returned is a UdpStreamReader instance; the writer is a</span>
</span><span id="UdpStreamManager.open_connection-93"><a href="#UdpStreamManager.open_connection-93"><span class="linenos"> 93</span></a><span class="sd">        UdpStreamWriter instance.</span>
</span><span id="UdpStreamManager.open_connection-94"><a href="#UdpStreamManager.open_connection-94"><span class="linenos"> 94</span></a>
</span><span id="UdpStreamManager.open_connection-95"><a href="#UdpStreamManager.open_connection-95"><span class="linenos"> 95</span></a><span class="sd">        The arguments are all the usual arguments to create_connection()</span>
</span><span id="UdpStreamManager.open_connection-96"><a href="#UdpStreamManager.open_connection-96"><span class="linenos"> 96</span></a><span class="sd">        except protocol_factory; most common are positional host and port,</span>
</span><span id="UdpStreamManager.open_connection-97"><a href="#UdpStreamManager.open_connection-97"><span class="linenos"> 97</span></a><span class="sd">        with various optional keyword arguments following.</span>
</span><span id="UdpStreamManager.open_connection-98"><a href="#UdpStreamManager.open_connection-98"><span class="linenos"> 98</span></a>
</span><span id="UdpStreamManager.open_connection-99"><a href="#UdpStreamManager.open_connection-99"><span class="linenos"> 99</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="UdpStreamManager.open_connection-100"><a href="#UdpStreamManager.open_connection-100"><span class="linenos">100</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="UdpStreamManager.open_connection-101"><a href="#UdpStreamManager.open_connection-101"><span class="linenos">101</span></a><span class="sd">        UdpStreamReader).</span>
</span><span id="UdpStreamManager.open_connection-102"><a href="#UdpStreamManager.open_connection-102"><span class="linenos">102</span></a>
</span><span id="UdpStreamManager.open_connection-103"><a href="#UdpStreamManager.open_connection-103"><span class="linenos">103</span></a><span class="sd">        (If you want to customize the UdpStreamReader and/or</span>
</span><span id="UdpStreamManager.open_connection-104"><a href="#UdpStreamManager.open_connection-104"><span class="linenos">104</span></a><span class="sd">        UdpStreamReaderProtocol classes, just copy the code -- there&#39;s</span>
</span><span id="UdpStreamManager.open_connection-105"><a href="#UdpStreamManager.open_connection-105"><span class="linenos">105</span></a><span class="sd">        really nothing special here except some convenience.)</span>
</span><span id="UdpStreamManager.open_connection-106"><a href="#UdpStreamManager.open_connection-106"><span class="linenos">106</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamManager.open_connection-107"><a href="#UdpStreamManager.open_connection-107"><span class="linenos">107</span></a>        <span class="k">if</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">gate</span> <span class="o">==</span> <span class="n">stream_type</span><span class="p">:</span>
</span><span id="UdpStreamManager.open_connection-108"><a href="#UdpStreamManager.open_connection-108"><span class="linenos">108</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong stream_type value: client can not be a &quot;gate&quot;.&#39;</span><span class="p">)</span>
</span><span id="UdpStreamManager.open_connection-109"><a href="#UdpStreamManager.open_connection-109"><span class="linenos">109</span></a>        
</span><span id="UdpStreamManager.open_connection-110"><a href="#UdpStreamManager.open_connection-110"><span class="linenos">110</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamManager.open_connection-111"><a href="#UdpStreamManager.open_connection-111"><span class="linenos">111</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="UdpStreamManager.open_connection-112"><a href="#UdpStreamManager.open_connection-112"><span class="linenos">112</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamManager.open_connection-113"><a href="#UdpStreamManager.open_connection-113"><span class="linenos">113</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="UdpStreamManager.open_connection-114"><a href="#UdpStreamManager.open_connection-114"><span class="linenos">114</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="UdpStreamManager.open_connection-115"><a href="#UdpStreamManager.open_connection-115"><span class="linenos">115</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="UdpStreamManager.open_connection-116"><a href="#UdpStreamManager.open_connection-116"><span class="linenos">116</span></a>        
</span><span id="UdpStreamManager.open_connection-117"><a href="#UdpStreamManager.open_connection-117"><span class="linenos">117</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="UdpStreamManager.open_connection-118"><a href="#UdpStreamManager.open_connection-118"><span class="linenos">118</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">UdpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager.open_connection-119"><a href="#UdpStreamManager.open_connection-119"><span class="linenos">119</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">UdpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager.open_connection-120"><a href="#UdpStreamManager.open_connection-120"><span class="linenos">120</span></a>        <span class="n">transport</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_connection</span><span class="p">(</span>
</span><span id="UdpStreamManager.open_connection-121"><a href="#UdpStreamManager.open_connection-121"><span class="linenos">121</span></a>            <span class="k">lambda</span><span class="p">:</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="UdpStreamManager.open_connection-122"><a href="#UdpStreamManager.open_connection-122"><span class="linenos">122</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">UdpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager.open_connection-123"><a href="#UdpStreamManager.open_connection-123"><span class="linenos">123</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span></pre></div>


            <div class="docstring"><p>A wrapper for create_connection() returning a (reader, writer) pair.</p>

<p>The reader returned is a UdpStreamReader instance; the writer is a
UdpStreamWriter instance.</p>

<p>The arguments are all the usual arguments to create_connection()
except protocol_factory; most common are positional host and port,
with various optional keyword arguments following.</p>

<p>Additional optional keyword arguments are loop (to set the event loop
instance to use) and limit (to set the buffer limit passed to the
UdpStreamReader).</p>

<p>(If you want to customize the UdpStreamReader and/or
UdpStreamReaderProtocol classes, just copy the code -- there's
really nothing special here except some convenience.)</p>
</div>


                            </div>
                            <div id="UdpStreamManager.start_server" class="classattr">
                                        <input id="UdpStreamManager.start_server-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">start_server</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client_connected_cb</span>,</span><span class="param">	<span class="n">host</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">port</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">loop</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">limit</span><span class="o">=</span><span class="mi">10485760</span>,</span><span class="param">	<span class="n">stream_type</span><span class="p">:</span> <span class="n"><a href="#StreamType">StreamType</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#StreamType.general">StreamType.general</a></span><span class="p">:</span> <span class="mi">0</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>,</span><span class="param">	<span class="n">gate_security_policy</span><span class="p">:</span> <span class="n"><a href="#GateSecurityPolicy">GateSecurityPolicy</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#GateSecurityPolicy.disabled">GateSecurityPolicy.disabled</a></span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">policy_managed_stream_names</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwds</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamManager.start_server-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamManager.start_server"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamManager.start_server-125"><a href="#UdpStreamManager.start_server-125"><span class="linenos">125</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">start_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="UdpStreamManager.start_server-126"><a href="#UdpStreamManager.start_server-126"><span class="linenos">126</span></a>                        <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="UdpStreamManager.start_server-127"><a href="#UdpStreamManager.start_server-127"><span class="linenos">127</span></a>                        <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="UdpStreamManager.start_server-128"><a href="#UdpStreamManager.start_server-128"><span class="linenos">128</span></a>                        <span class="n">gate_security_policy</span><span class="p">:</span> <span class="n">GateSecurityPolicy</span> <span class="o">=</span> <span class="n">GateSecurityPolicy</span><span class="o">.</span><span class="n">disabled</span><span class="p">,</span> <span class="n">policy_managed_stream_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager.start_server-129"><a href="#UdpStreamManager.start_server-129"><span class="linenos">129</span></a>                        <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager.start_server-130"><a href="#UdpStreamManager.start_server-130"><span class="linenos">130</span></a>                        <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="UdpStreamManager.start_server-131"><a href="#UdpStreamManager.start_server-131"><span class="linenos">131</span></a>                        <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="UdpStreamManager.start_server-132"><a href="#UdpStreamManager.start_server-132"><span class="linenos">132</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Start a socket server, call back for each client connected.</span>
</span><span id="UdpStreamManager.start_server-133"><a href="#UdpStreamManager.start_server-133"><span class="linenos">133</span></a>
</span><span id="UdpStreamManager.start_server-134"><a href="#UdpStreamManager.start_server-134"><span class="linenos">134</span></a><span class="sd">        The first parameter, `client_connected_cb`, takes two parameters:</span>
</span><span id="UdpStreamManager.start_server-135"><a href="#UdpStreamManager.start_server-135"><span class="linenos">135</span></a><span class="sd">        client_reader, client_writer.  client_reader is a UdpStreamReader</span>
</span><span id="UdpStreamManager.start_server-136"><a href="#UdpStreamManager.start_server-136"><span class="linenos">136</span></a><span class="sd">        object, while client_writer is a UdpStreamWriter object.  This</span>
</span><span id="UdpStreamManager.start_server-137"><a href="#UdpStreamManager.start_server-137"><span class="linenos">137</span></a><span class="sd">        parameter can either be a plain callback function or a coroutine;</span>
</span><span id="UdpStreamManager.start_server-138"><a href="#UdpStreamManager.start_server-138"><span class="linenos">138</span></a><span class="sd">        if it is a coroutine, it will be automatically converted into a</span>
</span><span id="UdpStreamManager.start_server-139"><a href="#UdpStreamManager.start_server-139"><span class="linenos">139</span></a><span class="sd">        Task.</span>
</span><span id="UdpStreamManager.start_server-140"><a href="#UdpStreamManager.start_server-140"><span class="linenos">140</span></a>
</span><span id="UdpStreamManager.start_server-141"><a href="#UdpStreamManager.start_server-141"><span class="linenos">141</span></a><span class="sd">        The rest of the arguments are all the usual arguments to</span>
</span><span id="UdpStreamManager.start_server-142"><a href="#UdpStreamManager.start_server-142"><span class="linenos">142</span></a><span class="sd">        loop.create_server() except protocol_factory; most common are</span>
</span><span id="UdpStreamManager.start_server-143"><a href="#UdpStreamManager.start_server-143"><span class="linenos">143</span></a><span class="sd">        positional host and port, with various optional keyword arguments</span>
</span><span id="UdpStreamManager.start_server-144"><a href="#UdpStreamManager.start_server-144"><span class="linenos">144</span></a><span class="sd">        following.  The return value is the same as loop.create_server().</span>
</span><span id="UdpStreamManager.start_server-145"><a href="#UdpStreamManager.start_server-145"><span class="linenos">145</span></a>
</span><span id="UdpStreamManager.start_server-146"><a href="#UdpStreamManager.start_server-146"><span class="linenos">146</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="UdpStreamManager.start_server-147"><a href="#UdpStreamManager.start_server-147"><span class="linenos">147</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="UdpStreamManager.start_server-148"><a href="#UdpStreamManager.start_server-148"><span class="linenos">148</span></a><span class="sd">        UdpStreamReader).</span>
</span><span id="UdpStreamManager.start_server-149"><a href="#UdpStreamManager.start_server-149"><span class="linenos">149</span></a>
</span><span id="UdpStreamManager.start_server-150"><a href="#UdpStreamManager.start_server-150"><span class="linenos">150</span></a><span class="sd">        The return value is the same as loop.create_server(), i.e. a</span>
</span><span id="UdpStreamManager.start_server-151"><a href="#UdpStreamManager.start_server-151"><span class="linenos">151</span></a><span class="sd">        Server object which can be used to stop the service.</span>
</span><span id="UdpStreamManager.start_server-152"><a href="#UdpStreamManager.start_server-152"><span class="linenos">152</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamManager.start_server-153"><a href="#UdpStreamManager.start_server-153"><span class="linenos">153</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamManager.start_server-154"><a href="#UdpStreamManager.start_server-154"><span class="linenos">154</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="UdpStreamManager.start_server-155"><a href="#UdpStreamManager.start_server-155"><span class="linenos">155</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamManager.start_server-156"><a href="#UdpStreamManager.start_server-156"><span class="linenos">156</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="UdpStreamManager.start_server-157"><a href="#UdpStreamManager.start_server-157"><span class="linenos">157</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="UdpStreamManager.start_server-158"><a href="#UdpStreamManager.start_server-158"><span class="linenos">158</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="UdpStreamManager.start_server-159"><a href="#UdpStreamManager.start_server-159"><span class="linenos">159</span></a>
</span><span id="UdpStreamManager.start_server-160"><a href="#UdpStreamManager.start_server-160"><span class="linenos">160</span></a>        <span class="k">def</span> <span class="nf">factory</span><span class="p">():</span>
</span><span id="UdpStreamManager.start_server-161"><a href="#UdpStreamManager.start_server-161"><span class="linenos">161</span></a>            <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="UdpStreamManager.start_server-162"><a href="#UdpStreamManager.start_server-162"><span class="linenos">162</span></a>            <span class="n">reader</span> <span class="o">=</span>  <span class="n">UdpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager.start_server-163"><a href="#UdpStreamManager.start_server-163"><span class="linenos">163</span></a>            <span class="n">protocol</span> <span class="o">=</span> <span class="n">UdpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span>
</span><span id="UdpStreamManager.start_server-164"><a href="#UdpStreamManager.start_server-164"><span class="linenos">164</span></a>                                            <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="UdpStreamManager.start_server-165"><a href="#UdpStreamManager.start_server-165"><span class="linenos">165</span></a>            <span class="k">return</span> <span class="n">protocol</span>
</span><span id="UdpStreamManager.start_server-166"><a href="#UdpStreamManager.start_server-166"><span class="linenos">166</span></a>
</span><span id="UdpStreamManager.start_server-167"><a href="#UdpStreamManager.start_server-167"><span class="linenos">167</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_server</span><span class="p">(</span><span class="n">factory</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Start a socket server, call back for each client connected.</p>

<p>The first parameter, <code>client_connected_cb</code>, takes two parameters:
client_reader, client_writer.  client_reader is a UdpStreamReader
object, while client_writer is a UdpStreamWriter object.  This
parameter can either be a plain callback function or a coroutine;
if it is a coroutine, it will be automatically converted into a
Task.</p>

<p>The rest of the arguments are all the usual arguments to
loop.create_server() except protocol_factory; most common are
positional host and port, with various optional keyword arguments
following.  The return value is the same as loop.create_server().</p>

<p>Additional optional keyword arguments are loop (to set the event loop
instance to use) and limit (to set the buffer limit passed to the
UdpStreamReader).</p>

<p>The return value is the same as loop.create_server(), i.e. a
Server object which can be used to stop the service.</p>
</div>


                            </div>
                            <div id="UdpStreamManager.try_establish_message_protocol_server_side" class="classattr">
                                        <input id="UdpStreamManager.try_establish_message_protocol_server_side-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">try_establish_message_protocol_server_side</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">reader</span><span class="p">:</span> <span class="n"><a href="#UdpStreamReader">UdpStreamReader</a></span>,</span><span class="param">	<span class="n">writer</span><span class="p">:</span> <span class="n"><a href="#UdpStreamWriter">UdpStreamWriter</a></span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="UdpStreamManager.try_establish_message_protocol_server_side-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamManager.try_establish_message_protocol_server_side"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamManager.try_establish_message_protocol_server_side-169"><a href="#UdpStreamManager.try_establish_message_protocol_server_side-169"><span class="linenos">169</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_server_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;UdpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="UdpStreamManager.try_establish_message_protocol_server_side-170"><a href="#UdpStreamManager.try_establish_message_protocol_server_side-170"><span class="linenos">170</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamManager.try_establish_message_protocol_client_side" class="classattr">
                                        <input id="UdpStreamManager.try_establish_message_protocol_client_side-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">try_establish_message_protocol_client_side</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">reader</span><span class="p">:</span> <span class="n"><a href="#UdpStreamReader">UdpStreamReader</a></span>,</span><span class="param">	<span class="n">writer</span><span class="p">:</span> <span class="n"><a href="#UdpStreamWriter">UdpStreamWriter</a></span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="UdpStreamManager.try_establish_message_protocol_client_side-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamManager.try_establish_message_protocol_client_side"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamManager.try_establish_message_protocol_client_side-172"><a href="#UdpStreamManager.try_establish_message_protocol_client_side-172"><span class="linenos">172</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_client_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;UdpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="UdpStreamManager.try_establish_message_protocol_client_side-173"><a href="#UdpStreamManager.try_establish_message_protocol_client_side-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="UdpStreamReader">
                            <input id="UdpStreamReader-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UdpStreamReader</span><wbr>(<span class="base">asyncio.streams.StreamReader</span>, <span class="base">cengal.parallel_execution.asyncio.efficient_streams.versions.v_0.efficient_streams_abstract.StreamReaderAbstract</span>):

                <label class="view-source-button" for="UdpStreamReader-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader-260"><a href="#UdpStreamReader-260"><span class="linenos">260</span></a><span class="k">class</span> <span class="nc">UdpStreamReader</span><span class="p">(</span><span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">StreamReaderAbstract</span><span class="p">):</span>
</span><span id="UdpStreamReader-261"><a href="#UdpStreamReader-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader-262"><a href="#UdpStreamReader-262"><span class="linenos">262</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="UdpStreamReader-263"><a href="#UdpStreamReader-263"><span class="linenos">263</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="UdpStreamReader-264"><a href="#UdpStreamReader-264"><span class="linenos">264</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="UdpStreamReader-265"><a href="#UdpStreamReader-265"><span class="linenos">265</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">input_from_client_container_type</span><span class="p">(</span>
</span><span id="UdpStreamReader-266"><a href="#UdpStreamReader-266"><span class="linenos">266</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="UdpStreamReader-267"><a href="#UdpStreamReader-267"><span class="linenos">267</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span> <span class="o">=</span> <span class="n">RecvBuffSizeComputer</span><span class="p">()</span>
</span><span id="UdpStreamReader-268"><a href="#UdpStreamReader-268"><span class="linenos">268</span></a>        <span class="n">cpu_info_inst</span> <span class="o">=</span> <span class="n">cpu_info</span><span class="p">()</span>
</span><span id="UdpStreamReader-269"><a href="#UdpStreamReader-269"><span class="linenos">269</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size</span>
</span><span id="UdpStreamReader-270"><a href="#UdpStreamReader-270"><span class="linenos">270</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l2_cache_size_per_virtual_core</span>
</span><span id="UdpStreamReader-271"><a href="#UdpStreamReader-271"><span class="linenos">271</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size_per_virtual_core</span>
</span><span id="UdpStreamReader-272"><a href="#UdpStreamReader-272"><span class="linenos">272</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 3145728</span>
</span><span id="UdpStreamReader-273"><a href="#UdpStreamReader-273"><span class="linenos">273</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">max_recv_buff_size</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span>
</span><span id="UdpStreamReader-274"><a href="#UdpStreamReader-274"><span class="linenos">274</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 1024</span>
</span><span id="UdpStreamReader-275"><a href="#UdpStreamReader-275"><span class="linenos">275</span></a>        <span class="c1"># print(f&#39;max_recv_buff_size: {self.recv_buff_size_computer.max_recv_buff_size}&#39;)</span>
</span><span id="UdpStreamReader-276"><a href="#UdpStreamReader-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="UdpStreamReader-277"><a href="#UdpStreamReader-277"><span class="linenos">277</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="UdpStreamReader-278"><a href="#UdpStreamReader-278"><span class="linenos">278</span></a>    
</span><span id="UdpStreamReader-279"><a href="#UdpStreamReader-279"><span class="linenos">279</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-280"><a href="#UdpStreamReader-280"><span class="linenos">280</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="UdpStreamReader-281"><a href="#UdpStreamReader-281"><span class="linenos">281</span></a>    
</span><span id="UdpStreamReader-282"><a href="#UdpStreamReader-282"><span class="linenos">282</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-283"><a href="#UdpStreamReader-283"><span class="linenos">283</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="UdpStreamReader-284"><a href="#UdpStreamReader-284"><span class="linenos">284</span></a>    
</span><span id="UdpStreamReader-285"><a href="#UdpStreamReader-285"><span class="linenos">285</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_with_counter</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-286"><a href="#UdpStreamReader-286"><span class="linenos">286</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader-287"><a href="#UdpStreamReader-287"><span class="linenos">287</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader-288"><a href="#UdpStreamReader-288"><span class="linenos">288</span></a>
</span><span id="UdpStreamReader-289"><a href="#UdpStreamReader-289"><span class="linenos">289</span></a>        <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="UdpStreamReader-290"><a href="#UdpStreamReader-290"><span class="linenos">290</span></a>        <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="UdpStreamReader-291"><a href="#UdpStreamReader-291"><span class="linenos">291</span></a>        <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="UdpStreamReader-292"><a href="#UdpStreamReader-292"><span class="linenos">292</span></a>        <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="UdpStreamReader-293"><a href="#UdpStreamReader-293"><span class="linenos">293</span></a>        <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="UdpStreamReader-294"><a href="#UdpStreamReader-294"><span class="linenos">294</span></a>        <span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="UdpStreamReader-295"><a href="#UdpStreamReader-295"><span class="linenos">295</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="UdpStreamReader-296"><a href="#UdpStreamReader-296"><span class="linenos">296</span></a>            <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_max</span><span class="p">()</span>
</span><span id="UdpStreamReader-297"><a href="#UdpStreamReader-297"><span class="linenos">297</span></a>            <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="UdpStreamReader-298"><a href="#UdpStreamReader-298"><span class="linenos">298</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="UdpStreamReader-299"><a href="#UdpStreamReader-299"><span class="linenos">299</span></a>                <span class="k">break</span>
</span><span id="UdpStreamReader-300"><a href="#UdpStreamReader-300"><span class="linenos">300</span></a>            <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="UdpStreamReader-301"><a href="#UdpStreamReader-301"><span class="linenos">301</span></a>        <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">),</span> <span class="n">counter</span>
</span><span id="UdpStreamReader-302"><a href="#UdpStreamReader-302"><span class="linenos">302</span></a>
</span><span id="UdpStreamReader-303"><a href="#UdpStreamReader-303"><span class="linenos">303</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-304"><a href="#UdpStreamReader-304"><span class="linenos">304</span></a>        <span class="n">info</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;UdpStreamReader&#39;</span><span class="p">]</span>
</span><span id="UdpStreamReader-305"><a href="#UdpStreamReader-305"><span class="linenos">305</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="UdpStreamReader-306"><a href="#UdpStreamReader-306"><span class="linenos">306</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span><span class="si">}</span><span class="s1"> bytes&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-307"><a href="#UdpStreamReader-307"><span class="linenos">307</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader-308"><a href="#UdpStreamReader-308"><span class="linenos">308</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;eof&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-309"><a href="#UdpStreamReader-309"><span class="linenos">309</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span> <span class="o">!=</span> <span class="n">DEFAULT_LIMIT</span><span class="p">:</span>
</span><span id="UdpStreamReader-310"><a href="#UdpStreamReader-310"><span class="linenos">310</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;limit=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-311"><a href="#UdpStreamReader-311"><span class="linenos">311</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_waiter</span><span class="p">:</span>
</span><span id="UdpStreamReader-312"><a href="#UdpStreamReader-312"><span class="linenos">312</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;waiter=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiter</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-313"><a href="#UdpStreamReader-313"><span class="linenos">313</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span><span class="p">:</span>
</span><span id="UdpStreamReader-314"><a href="#UdpStreamReader-314"><span class="linenos">314</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;exception=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_exception</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-315"><a href="#UdpStreamReader-315"><span class="linenos">315</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">:</span>
</span><span id="UdpStreamReader-316"><a href="#UdpStreamReader-316"><span class="linenos">316</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;transport=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-317"><a href="#UdpStreamReader-317"><span class="linenos">317</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span><span class="p">:</span>
</span><span id="UdpStreamReader-318"><a href="#UdpStreamReader-318"><span class="linenos">318</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;paused&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-319"><a href="#UdpStreamReader-319"><span class="linenos">319</span></a>        <span class="k">return</span> <span class="s1">&#39;&lt;</span><span class="si">{}</span><span class="s1">&gt;&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">info</span><span class="p">))</span>
</span><span id="UdpStreamReader-320"><a href="#UdpStreamReader-320"><span class="linenos">320</span></a>
</span><span id="UdpStreamReader-321"><a href="#UdpStreamReader-321"><span class="linenos">321</span></a>    <span class="k">def</span> <span class="nf">_maybe_resume_transport</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-322"><a href="#UdpStreamReader-322"><span class="linenos">322</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">,</span> <span class="p">(</span>
</span><span id="UdpStreamReader-323"><a href="#UdpStreamReader-323"><span class="linenos">323</span></a>            <span class="n">proactor_events</span><span class="o">.</span><span class="n">_ProactorDatagramTransport</span><span class="p">,</span>
</span><span id="UdpStreamReader-324"><a href="#UdpStreamReader-324"><span class="linenos">324</span></a>            <span class="n">selector_events</span><span class="o">.</span><span class="n">_SelectorTransport</span><span class="p">,</span>
</span><span id="UdpStreamReader-325"><a href="#UdpStreamReader-325"><span class="linenos">325</span></a>            <span class="n">unix_events</span><span class="o">.</span><span class="n">_UnixReadPipeTransport</span>
</span><span id="UdpStreamReader-326"><a href="#UdpStreamReader-326"><span class="linenos">326</span></a>            <span class="p">)):</span>
</span><span id="UdpStreamReader-327"><a href="#UdpStreamReader-327"><span class="linenos">327</span></a>            <span class="c1"># if hasattr(self._transport, &#39;max_size&#39;):</span>
</span><span id="UdpStreamReader-328"><a href="#UdpStreamReader-328"><span class="linenos">328</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="UdpStreamReader-329"><a href="#UdpStreamReader-329"><span class="linenos">329</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">max_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">recv_buff_size</span>
</span><span id="UdpStreamReader-330"><a href="#UdpStreamReader-330"><span class="linenos">330</span></a>                <span class="c1"># print(f&#39;max_size: {self._transport.max_size}&#39;)</span>
</span><span id="UdpStreamReader-331"><a href="#UdpStreamReader-331"><span class="linenos">331</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="UdpStreamReader-332"><a href="#UdpStreamReader-332"><span class="linenos">332</span></a>                <span class="k">pass</span>
</span><span id="UdpStreamReader-333"><a href="#UdpStreamReader-333"><span class="linenos">333</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader-334"><a href="#UdpStreamReader-334"><span class="linenos">334</span></a>            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-335"><a href="#UdpStreamReader-335"><span class="linenos">335</span></a>        
</span><span id="UdpStreamReader-336"><a href="#UdpStreamReader-336"><span class="linenos">336</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> \
</span><span id="UdpStreamReader-337"><a href="#UdpStreamReader-337"><span class="linenos">337</span></a>            <span class="ow">and</span> <span class="p">(</span>
</span><span id="UdpStreamReader-338"><a href="#UdpStreamReader-338"><span class="linenos">338</span></a>                <span class="p">((</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">))</span> \
</span><span id="UdpStreamReader-339"><a href="#UdpStreamReader-339"><span class="linenos">339</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">))</span> \
</span><span id="UdpStreamReader-340"><a href="#UdpStreamReader-340"><span class="linenos">340</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">))</span> \
</span><span id="UdpStreamReader-341"><a href="#UdpStreamReader-341"><span class="linenos">341</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="p">))</span> \
</span><span id="UdpStreamReader-342"><a href="#UdpStreamReader-342"><span class="linenos">342</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">))</span>
</span><span id="UdpStreamReader-343"><a href="#UdpStreamReader-343"><span class="linenos">343</span></a>            <span class="p">):</span>
</span><span id="UdpStreamReader-344"><a href="#UdpStreamReader-344"><span class="linenos">344</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="UdpStreamReader-345"><a href="#UdpStreamReader-345"><span class="linenos">345</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span><span id="UdpStreamReader-346"><a href="#UdpStreamReader-346"><span class="linenos">346</span></a>
</span><span id="UdpStreamReader-347"><a href="#UdpStreamReader-347"><span class="linenos">347</span></a>    <span class="k">def</span> <span class="nf">at_eof</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-348"><a href="#UdpStreamReader-348"><span class="linenos">348</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Return True if the buffer is empty and &#39;feed_eof&#39; was called.&quot;&quot;&quot;</span>
</span><span id="UdpStreamReader-349"><a href="#UdpStreamReader-349"><span class="linenos">349</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="UdpStreamReader-350"><a href="#UdpStreamReader-350"><span class="linenos">350</span></a>
</span><span id="UdpStreamReader-351"><a href="#UdpStreamReader-351"><span class="linenos">351</span></a>    <span class="k">def</span> <span class="nf">feed_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamReader-352"><a href="#UdpStreamReader-352"><span class="linenos">352</span></a>        <span class="k">assert</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">,</span> <span class="s1">&#39;feed_data after feed_eof&#39;</span>
</span><span id="UdpStreamReader-353"><a href="#UdpStreamReader-353"><span class="linenos">353</span></a>
</span><span id="UdpStreamReader-354"><a href="#UdpStreamReader-354"><span class="linenos">354</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
</span><span id="UdpStreamReader-355"><a href="#UdpStreamReader-355"><span class="linenos">355</span></a>            <span class="k">return</span>
</span><span id="UdpStreamReader-356"><a href="#UdpStreamReader-356"><span class="linenos">356</span></a>
</span><span id="UdpStreamReader-357"><a href="#UdpStreamReader-357"><span class="linenos">357</span></a>        <span class="n">data_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamReader-358"><a href="#UdpStreamReader-358"><span class="linenos">358</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">data_len</span><span class="p">)</span>
</span><span id="UdpStreamReader-359"><a href="#UdpStreamReader-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamReader-360"><a href="#UdpStreamReader-360"><span class="linenos">360</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_wakeup_waiter</span><span class="p">()</span>
</span><span id="UdpStreamReader-361"><a href="#UdpStreamReader-361"><span class="linenos">361</span></a>
</span><span id="UdpStreamReader-362"><a href="#UdpStreamReader-362"><span class="linenos">362</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="UdpStreamReader-363"><a href="#UdpStreamReader-363"><span class="linenos">363</span></a>                <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> 
</span><span id="UdpStreamReader-364"><a href="#UdpStreamReader-364"><span class="linenos">364</span></a>                <span class="ow">and</span> <span class="p">(</span>
</span><span id="UdpStreamReader-365"><a href="#UdpStreamReader-365"><span class="linenos">365</span></a>                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="UdpStreamReader-366"><a href="#UdpStreamReader-366"><span class="linenos">366</span></a>                    <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">)))</span>
</span><span id="UdpStreamReader-367"><a href="#UdpStreamReader-367"><span class="linenos">367</span></a>                <span class="p">)):</span>
</span><span id="UdpStreamReader-368"><a href="#UdpStreamReader-368"><span class="linenos">368</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="UdpStreamReader-369"><a href="#UdpStreamReader-369"><span class="linenos">369</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="UdpStreamReader-370"><a href="#UdpStreamReader-370"><span class="linenos">370</span></a>            <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="UdpStreamReader-371"><a href="#UdpStreamReader-371"><span class="linenos">371</span></a>                <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="UdpStreamReader-372"><a href="#UdpStreamReader-372"><span class="linenos">372</span></a>                <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="UdpStreamReader-373"><a href="#UdpStreamReader-373"><span class="linenos">373</span></a>                <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="UdpStreamReader-374"><a href="#UdpStreamReader-374"><span class="linenos">374</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="UdpStreamReader-375"><a href="#UdpStreamReader-375"><span class="linenos">375</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader-376"><a href="#UdpStreamReader-376"><span class="linenos">376</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="UdpStreamReader-377"><a href="#UdpStreamReader-377"><span class="linenos">377</span></a>
</span><span id="UdpStreamReader-378"><a href="#UdpStreamReader-378"><span class="linenos">378</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readline</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-379"><a href="#UdpStreamReader-379"><span class="linenos">379</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read chunk of data from the stream until newline (b&#39;\n&#39;) is found.</span>
</span><span id="UdpStreamReader-380"><a href="#UdpStreamReader-380"><span class="linenos">380</span></a>
</span><span id="UdpStreamReader-381"><a href="#UdpStreamReader-381"><span class="linenos">381</span></a><span class="sd">        On success, return chunk that ends with newline. If only partial</span>
</span><span id="UdpStreamReader-382"><a href="#UdpStreamReader-382"><span class="linenos">382</span></a><span class="sd">        line can be read due to EOF, return incomplete line without</span>
</span><span id="UdpStreamReader-383"><a href="#UdpStreamReader-383"><span class="linenos">383</span></a><span class="sd">        terminating newline. When EOF was reached while no bytes read, empty</span>
</span><span id="UdpStreamReader-384"><a href="#UdpStreamReader-384"><span class="linenos">384</span></a><span class="sd">        bytes object is returned.</span>
</span><span id="UdpStreamReader-385"><a href="#UdpStreamReader-385"><span class="linenos">385</span></a>
</span><span id="UdpStreamReader-386"><a href="#UdpStreamReader-386"><span class="linenos">386</span></a><span class="sd">        If limit is reached, ValueError will be raised. In that case, if</span>
</span><span id="UdpStreamReader-387"><a href="#UdpStreamReader-387"><span class="linenos">387</span></a><span class="sd">        newline was found, complete line including newline will be removed</span>
</span><span id="UdpStreamReader-388"><a href="#UdpStreamReader-388"><span class="linenos">388</span></a><span class="sd">        from internal buffer. Else, internal buffer will be cleared. Limit is</span>
</span><span id="UdpStreamReader-389"><a href="#UdpStreamReader-389"><span class="linenos">389</span></a><span class="sd">        compared against part of the line without newline.</span>
</span><span id="UdpStreamReader-390"><a href="#UdpStreamReader-390"><span class="linenos">390</span></a>
</span><span id="UdpStreamReader-391"><a href="#UdpStreamReader-391"><span class="linenos">391</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="UdpStreamReader-392"><a href="#UdpStreamReader-392"><span class="linenos">392</span></a><span class="sd">        needed.</span>
</span><span id="UdpStreamReader-393"><a href="#UdpStreamReader-393"><span class="linenos">393</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader-394"><a href="#UdpStreamReader-394"><span class="linenos">394</span></a>        <span class="n">sep</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="UdpStreamReader-395"><a href="#UdpStreamReader-395"><span class="linenos">395</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="UdpStreamReader-396"><a href="#UdpStreamReader-396"><span class="linenos">396</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="UdpStreamReader-397"><a href="#UdpStreamReader-397"><span class="linenos">397</span></a>            <span class="n">line</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readuntil</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="UdpStreamReader-398"><a href="#UdpStreamReader-398"><span class="linenos">398</span></a>        <span class="k">except</span> <span class="n">IncompleteReadError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="UdpStreamReader-399"><a href="#UdpStreamReader-399"><span class="linenos">399</span></a>            <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">partial</span>
</span><span id="UdpStreamReader-400"><a href="#UdpStreamReader-400"><span class="linenos">400</span></a>        <span class="k">except</span> <span class="n">LimitOverrunError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="UdpStreamReader-401"><a href="#UdpStreamReader-401"><span class="linenos">401</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">sep</span><span class="p">,</span> <span class="n">e</span><span class="o">.</span><span class="n">consumed</span><span class="p">):</span>
</span><span id="UdpStreamReader-402"><a href="#UdpStreamReader-402"><span class="linenos">402</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">consumed</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="UdpStreamReader-403"><a href="#UdpStreamReader-403"><span class="linenos">403</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader-404"><a href="#UdpStreamReader-404"><span class="linenos">404</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="UdpStreamReader-405"><a href="#UdpStreamReader-405"><span class="linenos">405</span></a>            
</span><span id="UdpStreamReader-406"><a href="#UdpStreamReader-406"><span class="linenos">406</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader-407"><a href="#UdpStreamReader-407"><span class="linenos">407</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="UdpStreamReader-408"><a href="#UdpStreamReader-408"><span class="linenos">408</span></a>        <span class="k">return</span> <span class="n">line</span>
</span><span id="UdpStreamReader-409"><a href="#UdpStreamReader-409"><span class="linenos">409</span></a>
</span><span id="UdpStreamReader-410"><a href="#UdpStreamReader-410"><span class="linenos">410</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readuntil</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">separator</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="UdpStreamReader-411"><a href="#UdpStreamReader-411"><span class="linenos">411</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read data from the stream until ``separator`` is found.</span>
</span><span id="UdpStreamReader-412"><a href="#UdpStreamReader-412"><span class="linenos">412</span></a>
</span><span id="UdpStreamReader-413"><a href="#UdpStreamReader-413"><span class="linenos">413</span></a><span class="sd">        On success, the data and separator will be removed from the</span>
</span><span id="UdpStreamReader-414"><a href="#UdpStreamReader-414"><span class="linenos">414</span></a><span class="sd">        internal buffer (consumed). Returned data will include the</span>
</span><span id="UdpStreamReader-415"><a href="#UdpStreamReader-415"><span class="linenos">415</span></a><span class="sd">        separator at the end.</span>
</span><span id="UdpStreamReader-416"><a href="#UdpStreamReader-416"><span class="linenos">416</span></a>
</span><span id="UdpStreamReader-417"><a href="#UdpStreamReader-417"><span class="linenos">417</span></a><span class="sd">        Configured stream limit is used to check result. Limit sets the</span>
</span><span id="UdpStreamReader-418"><a href="#UdpStreamReader-418"><span class="linenos">418</span></a><span class="sd">        maximal length of data that can be returned, not counting the</span>
</span><span id="UdpStreamReader-419"><a href="#UdpStreamReader-419"><span class="linenos">419</span></a><span class="sd">        separator.</span>
</span><span id="UdpStreamReader-420"><a href="#UdpStreamReader-420"><span class="linenos">420</span></a>
</span><span id="UdpStreamReader-421"><a href="#UdpStreamReader-421"><span class="linenos">421</span></a><span class="sd">        If an EOF occurs and the complete separator is still not found,</span>
</span><span id="UdpStreamReader-422"><a href="#UdpStreamReader-422"><span class="linenos">422</span></a><span class="sd">        an IncompleteReadError exception will be raised, and the internal</span>
</span><span id="UdpStreamReader-423"><a href="#UdpStreamReader-423"><span class="linenos">423</span></a><span class="sd">        buffer will be reset.  The IncompleteReadError.partial attribute</span>
</span><span id="UdpStreamReader-424"><a href="#UdpStreamReader-424"><span class="linenos">424</span></a><span class="sd">        may contain the separator partially.</span>
</span><span id="UdpStreamReader-425"><a href="#UdpStreamReader-425"><span class="linenos">425</span></a>
</span><span id="UdpStreamReader-426"><a href="#UdpStreamReader-426"><span class="linenos">426</span></a><span class="sd">        If the data cannot be read because of over limit, a</span>
</span><span id="UdpStreamReader-427"><a href="#UdpStreamReader-427"><span class="linenos">427</span></a><span class="sd">        LimitOverrunError exception  will be raised, and the data</span>
</span><span id="UdpStreamReader-428"><a href="#UdpStreamReader-428"><span class="linenos">428</span></a><span class="sd">        will be left in the internal buffer, so it can be read again.</span>
</span><span id="UdpStreamReader-429"><a href="#UdpStreamReader-429"><span class="linenos">429</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader-430"><a href="#UdpStreamReader-430"><span class="linenos">430</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">separator</span><span class="p">)</span>
</span><span id="UdpStreamReader-431"><a href="#UdpStreamReader-431"><span class="linenos">431</span></a>        <span class="k">if</span> <span class="n">seplen</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-432"><a href="#UdpStreamReader-432"><span class="linenos">432</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;Separator should be at least one-byte string&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-433"><a href="#UdpStreamReader-433"><span class="linenos">433</span></a>
</span><span id="UdpStreamReader-434"><a href="#UdpStreamReader-434"><span class="linenos">434</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader-435"><a href="#UdpStreamReader-435"><span class="linenos">435</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader-436"><a href="#UdpStreamReader-436"><span class="linenos">436</span></a>
</span><span id="UdpStreamReader-437"><a href="#UdpStreamReader-437"><span class="linenos">437</span></a>        <span class="c1"># Consume whole buffer except last bytes, which length is</span>
</span><span id="UdpStreamReader-438"><a href="#UdpStreamReader-438"><span class="linenos">438</span></a>        <span class="c1"># one less than seplen. Let&#39;s check corner cases with</span>
</span><span id="UdpStreamReader-439"><a href="#UdpStreamReader-439"><span class="linenos">439</span></a>        <span class="c1"># separator=&#39;SEPARATOR&#39;:</span>
</span><span id="UdpStreamReader-440"><a href="#UdpStreamReader-440"><span class="linenos">440</span></a>        <span class="c1"># * we have received almost complete separator (without last</span>
</span><span id="UdpStreamReader-441"><a href="#UdpStreamReader-441"><span class="linenos">441</span></a>        <span class="c1">#   byte). i.e buffer=&#39;some textSEPARATO&#39;. In this case we</span>
</span><span id="UdpStreamReader-442"><a href="#UdpStreamReader-442"><span class="linenos">442</span></a>        <span class="c1">#   can safely consume len(separator) - 1 bytes.</span>
</span><span id="UdpStreamReader-443"><a href="#UdpStreamReader-443"><span class="linenos">443</span></a>        <span class="c1"># * last byte of buffer is first byte of separator, i.e.</span>
</span><span id="UdpStreamReader-444"><a href="#UdpStreamReader-444"><span class="linenos">444</span></a>        <span class="c1">#   buffer=&#39;abcdefghijklmnopqrS&#39;. We may safely consume</span>
</span><span id="UdpStreamReader-445"><a href="#UdpStreamReader-445"><span class="linenos">445</span></a>        <span class="c1">#   everything except that last byte, but this require to</span>
</span><span id="UdpStreamReader-446"><a href="#UdpStreamReader-446"><span class="linenos">446</span></a>        <span class="c1">#   analyze bytes of buffer that match partial separator.</span>
</span><span id="UdpStreamReader-447"><a href="#UdpStreamReader-447"><span class="linenos">447</span></a>        <span class="c1">#   This is slow and/or require FSM. For this case our</span>
</span><span id="UdpStreamReader-448"><a href="#UdpStreamReader-448"><span class="linenos">448</span></a>        <span class="c1">#   implementation is not optimal, since require rescanning</span>
</span><span id="UdpStreamReader-449"><a href="#UdpStreamReader-449"><span class="linenos">449</span></a>        <span class="c1">#   of data that is known to not belong to separator. In</span>
</span><span id="UdpStreamReader-450"><a href="#UdpStreamReader-450"><span class="linenos">450</span></a>        <span class="c1">#   real world, separator will not be so long to notice</span>
</span><span id="UdpStreamReader-451"><a href="#UdpStreamReader-451"><span class="linenos">451</span></a>        <span class="c1">#   performance problems. Even when reading MIME-encoded</span>
</span><span id="UdpStreamReader-452"><a href="#UdpStreamReader-452"><span class="linenos">452</span></a>        <span class="c1">#   messages :)</span>
</span><span id="UdpStreamReader-453"><a href="#UdpStreamReader-453"><span class="linenos">453</span></a>
</span><span id="UdpStreamReader-454"><a href="#UdpStreamReader-454"><span class="linenos">454</span></a>        <span class="c1"># `offset` is the number of bytes from the beginning of the buffer</span>
</span><span id="UdpStreamReader-455"><a href="#UdpStreamReader-455"><span class="linenos">455</span></a>        <span class="c1"># where there is no occurrence of `separator`.</span>
</span><span id="UdpStreamReader-456"><a href="#UdpStreamReader-456"><span class="linenos">456</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="UdpStreamReader-457"><a href="#UdpStreamReader-457"><span class="linenos">457</span></a>
</span><span id="UdpStreamReader-458"><a href="#UdpStreamReader-458"><span class="linenos">458</span></a>        <span class="c1"># Loop until we find `separator` in the buffer, exceed the buffer size,</span>
</span><span id="UdpStreamReader-459"><a href="#UdpStreamReader-459"><span class="linenos">459</span></a>        <span class="c1"># or an EOF has happened.</span>
</span><span id="UdpStreamReader-460"><a href="#UdpStreamReader-460"><span class="linenos">460</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="UdpStreamReader-461"><a href="#UdpStreamReader-461"><span class="linenos">461</span></a>            <span class="n">buflen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="UdpStreamReader-462"><a href="#UdpStreamReader-462"><span class="linenos">462</span></a>
</span><span id="UdpStreamReader-463"><a href="#UdpStreamReader-463"><span class="linenos">463</span></a>            <span class="c1"># Check if we now have enough data in the buffer for `separator` to</span>
</span><span id="UdpStreamReader-464"><a href="#UdpStreamReader-464"><span class="linenos">464</span></a>            <span class="c1"># fit.</span>
</span><span id="UdpStreamReader-465"><a href="#UdpStreamReader-465"><span class="linenos">465</span></a>            <span class="k">if</span> <span class="n">buflen</span> <span class="o">-</span> <span class="n">offset</span> <span class="o">&gt;=</span> <span class="n">seplen</span><span class="p">:</span>
</span><span id="UdpStreamReader-466"><a href="#UdpStreamReader-466"><span class="linenos">466</span></a>                <span class="n">isep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">separator</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span>
</span><span id="UdpStreamReader-467"><a href="#UdpStreamReader-467"><span class="linenos">467</span></a>
</span><span id="UdpStreamReader-468"><a href="#UdpStreamReader-468"><span class="linenos">468</span></a>                <span class="k">if</span> <span class="n">isep</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
</span><span id="UdpStreamReader-469"><a href="#UdpStreamReader-469"><span class="linenos">469</span></a>                    <span class="c1"># `separator` is in the buffer. `isep` will be used later</span>
</span><span id="UdpStreamReader-470"><a href="#UdpStreamReader-470"><span class="linenos">470</span></a>                    <span class="c1"># to retrieve the data.</span>
</span><span id="UdpStreamReader-471"><a href="#UdpStreamReader-471"><span class="linenos">471</span></a>                    <span class="k">break</span>
</span><span id="UdpStreamReader-472"><a href="#UdpStreamReader-472"><span class="linenos">472</span></a>
</span><span id="UdpStreamReader-473"><a href="#UdpStreamReader-473"><span class="linenos">473</span></a>                <span class="c1"># see upper comment for explanation.</span>
</span><span id="UdpStreamReader-474"><a href="#UdpStreamReader-474"><span class="linenos">474</span></a>                <span class="n">offset</span> <span class="o">=</span> <span class="n">buflen</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">-</span> <span class="n">seplen</span>
</span><span id="UdpStreamReader-475"><a href="#UdpStreamReader-475"><span class="linenos">475</span></a>                <span class="k">if</span> <span class="n">offset</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="UdpStreamReader-476"><a href="#UdpStreamReader-476"><span class="linenos">476</span></a>                    <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="UdpStreamReader-477"><a href="#UdpStreamReader-477"><span class="linenos">477</span></a>                        <span class="s1">&#39;Separator is not found, and chunk exceed the limit&#39;</span><span class="p">,</span>
</span><span id="UdpStreamReader-478"><a href="#UdpStreamReader-478"><span class="linenos">478</span></a>                        <span class="n">offset</span><span class="p">)</span>
</span><span id="UdpStreamReader-479"><a href="#UdpStreamReader-479"><span class="linenos">479</span></a>
</span><span id="UdpStreamReader-480"><a href="#UdpStreamReader-480"><span class="linenos">480</span></a>            <span class="c1"># Complete message (with full separator) may be present in buffer</span>
</span><span id="UdpStreamReader-481"><a href="#UdpStreamReader-481"><span class="linenos">481</span></a>            <span class="c1"># even when EOF flag is set. This may happen when the last chunk</span>
</span><span id="UdpStreamReader-482"><a href="#UdpStreamReader-482"><span class="linenos">482</span></a>            <span class="c1"># adds data which makes separator be found. That&#39;s why we check for</span>
</span><span id="UdpStreamReader-483"><a href="#UdpStreamReader-483"><span class="linenos">483</span></a>            <span class="c1"># EOF *ater* inspecting the buffer.</span>
</span><span id="UdpStreamReader-484"><a href="#UdpStreamReader-484"><span class="linenos">484</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader-485"><a href="#UdpStreamReader-485"><span class="linenos">485</span></a>                <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader-486"><a href="#UdpStreamReader-486"><span class="linenos">486</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="UdpStreamReader-487"><a href="#UdpStreamReader-487"><span class="linenos">487</span></a>
</span><span id="UdpStreamReader-488"><a href="#UdpStreamReader-488"><span class="linenos">488</span></a>            <span class="c1"># _wait_for_data() will resume reading if stream was paused.</span>
</span><span id="UdpStreamReader-489"><a href="#UdpStreamReader-489"><span class="linenos">489</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readuntil&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-490"><a href="#UdpStreamReader-490"><span class="linenos">490</span></a>
</span><span id="UdpStreamReader-491"><a href="#UdpStreamReader-491"><span class="linenos">491</span></a>        <span class="k">if</span> <span class="n">isep</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="UdpStreamReader-492"><a href="#UdpStreamReader-492"><span class="linenos">492</span></a>            <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="UdpStreamReader-493"><a href="#UdpStreamReader-493"><span class="linenos">493</span></a>                <span class="s1">&#39;Separator is found, but chunk is longer than limit&#39;</span><span class="p">,</span> <span class="n">isep</span><span class="p">)</span>
</span><span id="UdpStreamReader-494"><a href="#UdpStreamReader-494"><span class="linenos">494</span></a>
</span><span id="UdpStreamReader-495"><a href="#UdpStreamReader-495"><span class="linenos">495</span></a>        <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">isep</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="UdpStreamReader-496"><a href="#UdpStreamReader-496"><span class="linenos">496</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader-497"><a href="#UdpStreamReader-497"><span class="linenos">497</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
</span><span id="UdpStreamReader-498"><a href="#UdpStreamReader-498"><span class="linenos">498</span></a>
</span><span id="UdpStreamReader-499"><a href="#UdpStreamReader-499"><span class="linenos">499</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="UdpStreamReader-500"><a href="#UdpStreamReader-500"><span class="linenos">500</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="UdpStreamReader-501"><a href="#UdpStreamReader-501"><span class="linenos">501</span></a>
</span><span id="UdpStreamReader-502"><a href="#UdpStreamReader-502"><span class="linenos">502</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="UdpStreamReader-503"><a href="#UdpStreamReader-503"><span class="linenos">503</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="UdpStreamReader-504"><a href="#UdpStreamReader-504"><span class="linenos">504</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="UdpStreamReader-505"><a href="#UdpStreamReader-505"><span class="linenos">505</span></a>
</span><span id="UdpStreamReader-506"><a href="#UdpStreamReader-506"><span class="linenos">506</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="UdpStreamReader-507"><a href="#UdpStreamReader-507"><span class="linenos">507</span></a>
</span><span id="UdpStreamReader-508"><a href="#UdpStreamReader-508"><span class="linenos">508</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="UdpStreamReader-509"><a href="#UdpStreamReader-509"><span class="linenos">509</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="UdpStreamReader-510"><a href="#UdpStreamReader-510"><span class="linenos">510</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="UdpStreamReader-511"><a href="#UdpStreamReader-511"><span class="linenos">511</span></a><span class="sd">        object.</span>
</span><span id="UdpStreamReader-512"><a href="#UdpStreamReader-512"><span class="linenos">512</span></a>
</span><span id="UdpStreamReader-513"><a href="#UdpStreamReader-513"><span class="linenos">513</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="UdpStreamReader-514"><a href="#UdpStreamReader-514"><span class="linenos">514</span></a><span class="sd">        creation.</span>
</span><span id="UdpStreamReader-515"><a href="#UdpStreamReader-515"><span class="linenos">515</span></a>
</span><span id="UdpStreamReader-516"><a href="#UdpStreamReader-516"><span class="linenos">516</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="UdpStreamReader-517"><a href="#UdpStreamReader-517"><span class="linenos">517</span></a><span class="sd">        needed.</span>
</span><span id="UdpStreamReader-518"><a href="#UdpStreamReader-518"><span class="linenos">518</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader-519"><a href="#UdpStreamReader-519"><span class="linenos">519</span></a>
</span><span id="UdpStreamReader-520"><a href="#UdpStreamReader-520"><span class="linenos">520</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader-521"><a href="#UdpStreamReader-521"><span class="linenos">521</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader-522"><a href="#UdpStreamReader-522"><span class="linenos">522</span></a>
</span><span id="UdpStreamReader-523"><a href="#UdpStreamReader-523"><span class="linenos">523</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-524"><a href="#UdpStreamReader-524"><span class="linenos">524</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="UdpStreamReader-525"><a href="#UdpStreamReader-525"><span class="linenos">525</span></a>
</span><span id="UdpStreamReader-526"><a href="#UdpStreamReader-526"><span class="linenos">526</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-527"><a href="#UdpStreamReader-527"><span class="linenos">527</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="UdpStreamReader-528"><a href="#UdpStreamReader-528"><span class="linenos">528</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="UdpStreamReader-529"><a href="#UdpStreamReader-529"><span class="linenos">529</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="UdpStreamReader-530"><a href="#UdpStreamReader-530"><span class="linenos">530</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="UdpStreamReader-531"><a href="#UdpStreamReader-531"><span class="linenos">531</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="UdpStreamReader-532"><a href="#UdpStreamReader-532"><span class="linenos">532</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="UdpStreamReader-533"><a href="#UdpStreamReader-533"><span class="linenos">533</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="UdpStreamReader-534"><a href="#UdpStreamReader-534"><span class="linenos">534</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="UdpStreamReader-535"><a href="#UdpStreamReader-535"><span class="linenos">535</span></a>                    <span class="k">break</span>
</span><span id="UdpStreamReader-536"><a href="#UdpStreamReader-536"><span class="linenos">536</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="UdpStreamReader-537"><a href="#UdpStreamReader-537"><span class="linenos">537</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="UdpStreamReader-538"><a href="#UdpStreamReader-538"><span class="linenos">538</span></a>
</span><span id="UdpStreamReader-539"><a href="#UdpStreamReader-539"><span class="linenos">539</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader-540"><a href="#UdpStreamReader-540"><span class="linenos">540</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-541"><a href="#UdpStreamReader-541"><span class="linenos">541</span></a>
</span><span id="UdpStreamReader-542"><a href="#UdpStreamReader-542"><span class="linenos">542</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="UdpStreamReader-543"><a href="#UdpStreamReader-543"><span class="linenos">543</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="UdpStreamReader-544"><a href="#UdpStreamReader-544"><span class="linenos">544</span></a>
</span><span id="UdpStreamReader-545"><a href="#UdpStreamReader-545"><span class="linenos">545</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader-546"><a href="#UdpStreamReader-546"><span class="linenos">546</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="UdpStreamReader-547"><a href="#UdpStreamReader-547"><span class="linenos">547</span></a>
</span><span id="UdpStreamReader-548"><a href="#UdpStreamReader-548"><span class="linenos">548</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="UdpStreamReader-549"><a href="#UdpStreamReader-549"><span class="linenos">549</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="UdpStreamReader-550"><a href="#UdpStreamReader-550"><span class="linenos">550</span></a>
</span><span id="UdpStreamReader-551"><a href="#UdpStreamReader-551"><span class="linenos">551</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="UdpStreamReader-552"><a href="#UdpStreamReader-552"><span class="linenos">552</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="UdpStreamReader-553"><a href="#UdpStreamReader-553"><span class="linenos">553</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="UdpStreamReader-554"><a href="#UdpStreamReader-554"><span class="linenos">554</span></a>
</span><span id="UdpStreamReader-555"><a href="#UdpStreamReader-555"><span class="linenos">555</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="UdpStreamReader-556"><a href="#UdpStreamReader-556"><span class="linenos">556</span></a>
</span><span id="UdpStreamReader-557"><a href="#UdpStreamReader-557"><span class="linenos">557</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="UdpStreamReader-558"><a href="#UdpStreamReader-558"><span class="linenos">558</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="UdpStreamReader-559"><a href="#UdpStreamReader-559"><span class="linenos">559</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="UdpStreamReader-560"><a href="#UdpStreamReader-560"><span class="linenos">560</span></a><span class="sd">        object.</span>
</span><span id="UdpStreamReader-561"><a href="#UdpStreamReader-561"><span class="linenos">561</span></a>
</span><span id="UdpStreamReader-562"><a href="#UdpStreamReader-562"><span class="linenos">562</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="UdpStreamReader-563"><a href="#UdpStreamReader-563"><span class="linenos">563</span></a><span class="sd">        creation.</span>
</span><span id="UdpStreamReader-564"><a href="#UdpStreamReader-564"><span class="linenos">564</span></a>
</span><span id="UdpStreamReader-565"><a href="#UdpStreamReader-565"><span class="linenos">565</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="UdpStreamReader-566"><a href="#UdpStreamReader-566"><span class="linenos">566</span></a><span class="sd">        needed.</span>
</span><span id="UdpStreamReader-567"><a href="#UdpStreamReader-567"><span class="linenos">567</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader-568"><a href="#UdpStreamReader-568"><span class="linenos">568</span></a>
</span><span id="UdpStreamReader-569"><a href="#UdpStreamReader-569"><span class="linenos">569</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader-570"><a href="#UdpStreamReader-570"><span class="linenos">570</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader-571"><a href="#UdpStreamReader-571"><span class="linenos">571</span></a>
</span><span id="UdpStreamReader-572"><a href="#UdpStreamReader-572"><span class="linenos">572</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-573"><a href="#UdpStreamReader-573"><span class="linenos">573</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="UdpStreamReader-574"><a href="#UdpStreamReader-574"><span class="linenos">574</span></a>
</span><span id="UdpStreamReader-575"><a href="#UdpStreamReader-575"><span class="linenos">575</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-576"><a href="#UdpStreamReader-576"><span class="linenos">576</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="UdpStreamReader-577"><a href="#UdpStreamReader-577"><span class="linenos">577</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="UdpStreamReader-578"><a href="#UdpStreamReader-578"><span class="linenos">578</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="UdpStreamReader-579"><a href="#UdpStreamReader-579"><span class="linenos">579</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="UdpStreamReader-580"><a href="#UdpStreamReader-580"><span class="linenos">580</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="UdpStreamReader-581"><a href="#UdpStreamReader-581"><span class="linenos">581</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="UdpStreamReader-582"><a href="#UdpStreamReader-582"><span class="linenos">582</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="UdpStreamReader-583"><a href="#UdpStreamReader-583"><span class="linenos">583</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="UdpStreamReader-584"><a href="#UdpStreamReader-584"><span class="linenos">584</span></a>                    <span class="k">break</span>
</span><span id="UdpStreamReader-585"><a href="#UdpStreamReader-585"><span class="linenos">585</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="UdpStreamReader-586"><a href="#UdpStreamReader-586"><span class="linenos">586</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="UdpStreamReader-587"><a href="#UdpStreamReader-587"><span class="linenos">587</span></a>
</span><span id="UdpStreamReader-588"><a href="#UdpStreamReader-588"><span class="linenos">588</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader-589"><a href="#UdpStreamReader-589"><span class="linenos">589</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-590"><a href="#UdpStreamReader-590"><span class="linenos">590</span></a>
</span><span id="UdpStreamReader-591"><a href="#UdpStreamReader-591"><span class="linenos">591</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="UdpStreamReader-592"><a href="#UdpStreamReader-592"><span class="linenos">592</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data_nearly</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader-593"><a href="#UdpStreamReader-593"><span class="linenos">593</span></a>
</span><span id="UdpStreamReader-594"><a href="#UdpStreamReader-594"><span class="linenos">594</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader-595"><a href="#UdpStreamReader-595"><span class="linenos">595</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="UdpStreamReader-596"><a href="#UdpStreamReader-596"><span class="linenos">596</span></a>
</span><span id="UdpStreamReader-597"><a href="#UdpStreamReader-597"><span class="linenos">597</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="UdpStreamReader-598"><a href="#UdpStreamReader-598"><span class="linenos">598</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read exactly `n` bytes.</span>
</span><span id="UdpStreamReader-599"><a href="#UdpStreamReader-599"><span class="linenos">599</span></a>
</span><span id="UdpStreamReader-600"><a href="#UdpStreamReader-600"><span class="linenos">600</span></a><span class="sd">        Raise an IncompleteReadError if EOF is reached before `n` bytes can be</span>
</span><span id="UdpStreamReader-601"><a href="#UdpStreamReader-601"><span class="linenos">601</span></a><span class="sd">        read. The IncompleteReadError.partial attribute of the exception will</span>
</span><span id="UdpStreamReader-602"><a href="#UdpStreamReader-602"><span class="linenos">602</span></a><span class="sd">        contain the partial read bytes.</span>
</span><span id="UdpStreamReader-603"><a href="#UdpStreamReader-603"><span class="linenos">603</span></a>
</span><span id="UdpStreamReader-604"><a href="#UdpStreamReader-604"><span class="linenos">604</span></a><span class="sd">        if n is zero, return empty bytes object.</span>
</span><span id="UdpStreamReader-605"><a href="#UdpStreamReader-605"><span class="linenos">605</span></a>
</span><span id="UdpStreamReader-606"><a href="#UdpStreamReader-606"><span class="linenos">606</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="UdpStreamReader-607"><a href="#UdpStreamReader-607"><span class="linenos">607</span></a><span class="sd">        creation.</span>
</span><span id="UdpStreamReader-608"><a href="#UdpStreamReader-608"><span class="linenos">608</span></a>
</span><span id="UdpStreamReader-609"><a href="#UdpStreamReader-609"><span class="linenos">609</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="UdpStreamReader-610"><a href="#UdpStreamReader-610"><span class="linenos">610</span></a><span class="sd">        needed.</span>
</span><span id="UdpStreamReader-611"><a href="#UdpStreamReader-611"><span class="linenos">611</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader-612"><a href="#UdpStreamReader-612"><span class="linenos">612</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-613"><a href="#UdpStreamReader-613"><span class="linenos">613</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-614"><a href="#UdpStreamReader-614"><span class="linenos">614</span></a>
</span><span id="UdpStreamReader-615"><a href="#UdpStreamReader-615"><span class="linenos">615</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader-616"><a href="#UdpStreamReader-616"><span class="linenos">616</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader-617"><a href="#UdpStreamReader-617"><span class="linenos">617</span></a>
</span><span id="UdpStreamReader-618"><a href="#UdpStreamReader-618"><span class="linenos">618</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-619"><a href="#UdpStreamReader-619"><span class="linenos">619</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="UdpStreamReader-620"><a href="#UdpStreamReader-620"><span class="linenos">620</span></a>
</span><span id="UdpStreamReader-621"><a href="#UdpStreamReader-621"><span class="linenos">621</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="UdpStreamReader-622"><a href="#UdpStreamReader-622"><span class="linenos">622</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader-623"><a href="#UdpStreamReader-623"><span class="linenos">623</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader-624"><a href="#UdpStreamReader-624"><span class="linenos">624</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader-625"><a href="#UdpStreamReader-625"><span class="linenos">625</span></a>
</span><span id="UdpStreamReader-626"><a href="#UdpStreamReader-626"><span class="linenos">626</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-627"><a href="#UdpStreamReader-627"><span class="linenos">627</span></a>
</span><span id="UdpStreamReader-628"><a href="#UdpStreamReader-628"><span class="linenos">628</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="UdpStreamReader-629"><a href="#UdpStreamReader-629"><span class="linenos">629</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader-630"><a href="#UdpStreamReader-630"><span class="linenos">630</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader-631"><a href="#UdpStreamReader-631"><span class="linenos">631</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader-632"><a href="#UdpStreamReader-632"><span class="linenos">632</span></a>
</span><span id="UdpStreamReader-633"><a href="#UdpStreamReader-633"><span class="linenos">633</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader-634"><a href="#UdpStreamReader-634"><span class="linenos">634</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="UdpStreamReader-635"><a href="#UdpStreamReader-635"><span class="linenos">635</span></a>    
</span><span id="UdpStreamReader-636"><a href="#UdpStreamReader-636"><span class="linenos">636</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readonly_exactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="UdpStreamReader-637"><a href="#UdpStreamReader-637"><span class="linenos">637</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-638"><a href="#UdpStreamReader-638"><span class="linenos">638</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-639"><a href="#UdpStreamReader-639"><span class="linenos">639</span></a>
</span><span id="UdpStreamReader-640"><a href="#UdpStreamReader-640"><span class="linenos">640</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader-641"><a href="#UdpStreamReader-641"><span class="linenos">641</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader-642"><a href="#UdpStreamReader-642"><span class="linenos">642</span></a>
</span><span id="UdpStreamReader-643"><a href="#UdpStreamReader-643"><span class="linenos">643</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader-644"><a href="#UdpStreamReader-644"><span class="linenos">644</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="UdpStreamReader-645"><a href="#UdpStreamReader-645"><span class="linenos">645</span></a>
</span><span id="UdpStreamReader-646"><a href="#UdpStreamReader-646"><span class="linenos">646</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="UdpStreamReader-647"><a href="#UdpStreamReader-647"><span class="linenos">647</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader-648"><a href="#UdpStreamReader-648"><span class="linenos">648</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader-649"><a href="#UdpStreamReader-649"><span class="linenos">649</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader-650"><a href="#UdpStreamReader-650"><span class="linenos">650</span></a>
</span><span id="UdpStreamReader-651"><a href="#UdpStreamReader-651"><span class="linenos">651</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-652"><a href="#UdpStreamReader-652"><span class="linenos">652</span></a>
</span><span id="UdpStreamReader-653"><a href="#UdpStreamReader-653"><span class="linenos">653</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="UdpStreamReader-654"><a href="#UdpStreamReader-654"><span class="linenos">654</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader-655"><a href="#UdpStreamReader-655"><span class="linenos">655</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader-656"><a href="#UdpStreamReader-656"><span class="linenos">656</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader-657"><a href="#UdpStreamReader-657"><span class="linenos">657</span></a>
</span><span id="UdpStreamReader-658"><a href="#UdpStreamReader-658"><span class="linenos">658</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader-659"><a href="#UdpStreamReader-659"><span class="linenos">659</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="UdpStreamReader-660"><a href="#UdpStreamReader-660"><span class="linenos">660</span></a>    
</span><span id="UdpStreamReader-661"><a href="#UdpStreamReader-661"><span class="linenos">661</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_message</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-662"><a href="#UdpStreamReader-662"><span class="linenos">662</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span><span class="p">)</span>
</span><span id="UdpStreamReader-663"><a href="#UdpStreamReader-663"><span class="linenos">663</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-664"><a href="#UdpStreamReader-664"><span class="linenos">664</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="n">message_len</span><span class="p">)</span>
</span><span id="UdpStreamReader-665"><a href="#UdpStreamReader-665"><span class="linenos">665</span></a>    
</span><span id="UdpStreamReader-666"><a href="#UdpStreamReader-666"><span class="linenos">666</span></a>    <span class="k">def</span> <span class="nf">message_awailable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="UdpStreamReader-667"><a href="#UdpStreamReader-667"><span class="linenos">667</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span>
</span><span id="UdpStreamReader-668"><a href="#UdpStreamReader-668"><span class="linenos">668</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">message_size_len</span><span class="p">:</span>
</span><span id="UdpStreamReader-669"><a href="#UdpStreamReader-669"><span class="linenos">669</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="UdpStreamReader-670"><a href="#UdpStreamReader-670"><span class="linenos">670</span></a>
</span><span id="UdpStreamReader-671"><a href="#UdpStreamReader-671"><span class="linenos">671</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="UdpStreamReader-672"><a href="#UdpStreamReader-672"><span class="linenos">672</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader-673"><a href="#UdpStreamReader-673"><span class="linenos">673</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="p">(</span><span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_len</span><span class="p">):</span>
</span><span id="UdpStreamReader-674"><a href="#UdpStreamReader-674"><span class="linenos">674</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="UdpStreamReader-675"><a href="#UdpStreamReader-675"><span class="linenos">675</span></a>        
</span><span id="UdpStreamReader-676"><a href="#UdpStreamReader-676"><span class="linenos">676</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="UdpStreamReader-677"><a href="#UdpStreamReader-677"><span class="linenos">677</span></a>    
</span><span id="UdpStreamReader-678"><a href="#UdpStreamReader-678"><span class="linenos">678</span></a>    <span class="k">def</span> <span class="nf">transport_pause_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-679"><a href="#UdpStreamReader-679"><span class="linenos">679</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="UdpStreamReader-680"><a href="#UdpStreamReader-680"><span class="linenos">680</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="UdpStreamReader-681"><a href="#UdpStreamReader-681"><span class="linenos">681</span></a>        <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="UdpStreamReader-682"><a href="#UdpStreamReader-682"><span class="linenos">682</span></a>            <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="UdpStreamReader-683"><a href="#UdpStreamReader-683"><span class="linenos">683</span></a>            <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="UdpStreamReader-684"><a href="#UdpStreamReader-684"><span class="linenos">684</span></a>            <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="UdpStreamReader-685"><a href="#UdpStreamReader-685"><span class="linenos">685</span></a>            <span class="k">pass</span>
</span><span id="UdpStreamReader-686"><a href="#UdpStreamReader-686"><span class="linenos">686</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader-687"><a href="#UdpStreamReader-687"><span class="linenos">687</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="UdpStreamReader-688"><a href="#UdpStreamReader-688"><span class="linenos">688</span></a>    
</span><span id="UdpStreamReader-689"><a href="#UdpStreamReader-689"><span class="linenos">689</span></a>    <span class="k">def</span> <span class="nf">transport_resume_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader-690"><a href="#UdpStreamReader-690"><span class="linenos">690</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="UdpStreamReader-691"><a href="#UdpStreamReader-691"><span class="linenos">691</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="UdpStreamReader.__init__" class="classattr">
                                        <input id="UdpStreamReader.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">UdpStreamReader</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">manager</span><span class="p">:</span> <span class="n"><a href="#UdpStreamManager">UdpStreamManager</a></span>,</span><span class="param">	<span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">asyncio</span><span class="o">.</span><span class="n">efficient_streams</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">efficient_streams_base_internal</span><span class="o">.</span><span class="n">MessageProtocolSettings</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="UdpStreamReader.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.__init__-261"><a href="#UdpStreamReader.__init__-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader.__init__-262"><a href="#UdpStreamReader.__init__-262"><span class="linenos">262</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="UdpStreamReader.__init__-263"><a href="#UdpStreamReader.__init__-263"><span class="linenos">263</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="UdpStreamReader.__init__-264"><a href="#UdpStreamReader.__init__-264"><span class="linenos">264</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="UdpStreamReader.__init__-265"><a href="#UdpStreamReader.__init__-265"><span class="linenos">265</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">input_from_client_container_type</span><span class="p">(</span>
</span><span id="UdpStreamReader.__init__-266"><a href="#UdpStreamReader.__init__-266"><span class="linenos">266</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="UdpStreamReader.__init__-267"><a href="#UdpStreamReader.__init__-267"><span class="linenos">267</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span> <span class="o">=</span> <span class="n">RecvBuffSizeComputer</span><span class="p">()</span>
</span><span id="UdpStreamReader.__init__-268"><a href="#UdpStreamReader.__init__-268"><span class="linenos">268</span></a>        <span class="n">cpu_info_inst</span> <span class="o">=</span> <span class="n">cpu_info</span><span class="p">()</span>
</span><span id="UdpStreamReader.__init__-269"><a href="#UdpStreamReader.__init__-269"><span class="linenos">269</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size</span>
</span><span id="UdpStreamReader.__init__-270"><a href="#UdpStreamReader.__init__-270"><span class="linenos">270</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l2_cache_size_per_virtual_core</span>
</span><span id="UdpStreamReader.__init__-271"><a href="#UdpStreamReader.__init__-271"><span class="linenos">271</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size_per_virtual_core</span>
</span><span id="UdpStreamReader.__init__-272"><a href="#UdpStreamReader.__init__-272"><span class="linenos">272</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 3145728</span>
</span><span id="UdpStreamReader.__init__-273"><a href="#UdpStreamReader.__init__-273"><span class="linenos">273</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">max_recv_buff_size</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span>
</span><span id="UdpStreamReader.__init__-274"><a href="#UdpStreamReader.__init__-274"><span class="linenos">274</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 1024</span>
</span><span id="UdpStreamReader.__init__-275"><a href="#UdpStreamReader.__init__-275"><span class="linenos">275</span></a>        <span class="c1"># print(f&#39;max_recv_buff_size: {self.recv_buff_size_computer.max_recv_buff_size}&#39;)</span>
</span><span id="UdpStreamReader.__init__-276"><a href="#UdpStreamReader.__init__-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="UdpStreamReader.__init__-277"><a href="#UdpStreamReader.__init__-277"><span class="linenos">277</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.recv_buff_size_computer" class="classattr">
                                <div class="attr variable">
            <span class="name">recv_buff_size_computer</span>

        
    </div>
    <a class="headerlink" href="#UdpStreamReader.recv_buff_size_computer"></a>
    
    

                            </div>
                            <div id="UdpStreamReader.limit_by_limit" class="classattr">
                                <div class="attr variable">
            <span class="name">limit_by_limit</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#UdpStreamReader.limit_by_limit"></a>
    
    

                            </div>
                            <div id="UdpStreamReader.limit_by_global_in__data_size_limit" class="classattr">
                                <div class="attr variable">
            <span class="name">limit_by_global_in__data_size_limit</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#UdpStreamReader.limit_by_global_in__data_size_limit"></a>
    
    

                            </div>
                            <div id="UdpStreamReader.read_max" class="classattr">
                                        <input id="UdpStreamReader.read_max-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_max</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.read_max-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.read_max"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.read_max-279"><a href="#UdpStreamReader.read_max-279"><span class="linenos">279</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader.read_max-280"><a href="#UdpStreamReader.read_max-280"><span class="linenos">280</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.read_nearly_max" class="classattr">
                                        <input id="UdpStreamReader.read_nearly_max-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_nearly_max</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.read_nearly_max-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.read_nearly_max"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.read_nearly_max-282"><a href="#UdpStreamReader.read_nearly_max-282"><span class="linenos">282</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader.read_nearly_max-283"><a href="#UdpStreamReader.read_nearly_max-283"><span class="linenos">283</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.read_with_counter" class="classattr">
                                        <input id="UdpStreamReader.read_with_counter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_with_counter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.read_with_counter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.read_with_counter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.read_with_counter-285"><a href="#UdpStreamReader.read_with_counter-285"><span class="linenos">285</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_with_counter</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader.read_with_counter-286"><a href="#UdpStreamReader.read_with_counter-286"><span class="linenos">286</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_with_counter-287"><a href="#UdpStreamReader.read_with_counter-287"><span class="linenos">287</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader.read_with_counter-288"><a href="#UdpStreamReader.read_with_counter-288"><span class="linenos">288</span></a>
</span><span id="UdpStreamReader.read_with_counter-289"><a href="#UdpStreamReader.read_with_counter-289"><span class="linenos">289</span></a>        <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="UdpStreamReader.read_with_counter-290"><a href="#UdpStreamReader.read_with_counter-290"><span class="linenos">290</span></a>        <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="UdpStreamReader.read_with_counter-291"><a href="#UdpStreamReader.read_with_counter-291"><span class="linenos">291</span></a>        <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="UdpStreamReader.read_with_counter-292"><a href="#UdpStreamReader.read_with_counter-292"><span class="linenos">292</span></a>        <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="UdpStreamReader.read_with_counter-293"><a href="#UdpStreamReader.read_with_counter-293"><span class="linenos">293</span></a>        <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="UdpStreamReader.read_with_counter-294"><a href="#UdpStreamReader.read_with_counter-294"><span class="linenos">294</span></a>        <span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="UdpStreamReader.read_with_counter-295"><a href="#UdpStreamReader.read_with_counter-295"><span class="linenos">295</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_with_counter-296"><a href="#UdpStreamReader.read_with_counter-296"><span class="linenos">296</span></a>            <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_max</span><span class="p">()</span>
</span><span id="UdpStreamReader.read_with_counter-297"><a href="#UdpStreamReader.read_with_counter-297"><span class="linenos">297</span></a>            <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="UdpStreamReader.read_with_counter-298"><a href="#UdpStreamReader.read_with_counter-298"><span class="linenos">298</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_with_counter-299"><a href="#UdpStreamReader.read_with_counter-299"><span class="linenos">299</span></a>                <span class="k">break</span>
</span><span id="UdpStreamReader.read_with_counter-300"><a href="#UdpStreamReader.read_with_counter-300"><span class="linenos">300</span></a>            <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="UdpStreamReader.read_with_counter-301"><a href="#UdpStreamReader.read_with_counter-301"><span class="linenos">301</span></a>        <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">),</span> <span class="n">counter</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.at_eof" class="classattr">
                                        <input id="UdpStreamReader.at_eof-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">at_eof</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.at_eof-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.at_eof"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.at_eof-347"><a href="#UdpStreamReader.at_eof-347"><span class="linenos">347</span></a>    <span class="k">def</span> <span class="nf">at_eof</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader.at_eof-348"><a href="#UdpStreamReader.at_eof-348"><span class="linenos">348</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Return True if the buffer is empty and &#39;feed_eof&#39; was called.&quot;&quot;&quot;</span>
</span><span id="UdpStreamReader.at_eof-349"><a href="#UdpStreamReader.at_eof-349"><span class="linenos">349</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Return True if the buffer is empty and 'feed_eof' was called.</p>
</div>


                            </div>
                            <div id="UdpStreamReader.feed_data" class="classattr">
                                        <input id="UdpStreamReader.feed_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">feed_data</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.feed_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.feed_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.feed_data-351"><a href="#UdpStreamReader.feed_data-351"><span class="linenos">351</span></a>    <span class="k">def</span> <span class="nf">feed_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamReader.feed_data-352"><a href="#UdpStreamReader.feed_data-352"><span class="linenos">352</span></a>        <span class="k">assert</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">,</span> <span class="s1">&#39;feed_data after feed_eof&#39;</span>
</span><span id="UdpStreamReader.feed_data-353"><a href="#UdpStreamReader.feed_data-353"><span class="linenos">353</span></a>
</span><span id="UdpStreamReader.feed_data-354"><a href="#UdpStreamReader.feed_data-354"><span class="linenos">354</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
</span><span id="UdpStreamReader.feed_data-355"><a href="#UdpStreamReader.feed_data-355"><span class="linenos">355</span></a>            <span class="k">return</span>
</span><span id="UdpStreamReader.feed_data-356"><a href="#UdpStreamReader.feed_data-356"><span class="linenos">356</span></a>
</span><span id="UdpStreamReader.feed_data-357"><a href="#UdpStreamReader.feed_data-357"><span class="linenos">357</span></a>        <span class="n">data_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamReader.feed_data-358"><a href="#UdpStreamReader.feed_data-358"><span class="linenos">358</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">data_len</span><span class="p">)</span>
</span><span id="UdpStreamReader.feed_data-359"><a href="#UdpStreamReader.feed_data-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamReader.feed_data-360"><a href="#UdpStreamReader.feed_data-360"><span class="linenos">360</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_wakeup_waiter</span><span class="p">()</span>
</span><span id="UdpStreamReader.feed_data-361"><a href="#UdpStreamReader.feed_data-361"><span class="linenos">361</span></a>
</span><span id="UdpStreamReader.feed_data-362"><a href="#UdpStreamReader.feed_data-362"><span class="linenos">362</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="UdpStreamReader.feed_data-363"><a href="#UdpStreamReader.feed_data-363"><span class="linenos">363</span></a>                <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> 
</span><span id="UdpStreamReader.feed_data-364"><a href="#UdpStreamReader.feed_data-364"><span class="linenos">364</span></a>                <span class="ow">and</span> <span class="p">(</span>
</span><span id="UdpStreamReader.feed_data-365"><a href="#UdpStreamReader.feed_data-365"><span class="linenos">365</span></a>                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="UdpStreamReader.feed_data-366"><a href="#UdpStreamReader.feed_data-366"><span class="linenos">366</span></a>                    <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">)))</span>
</span><span id="UdpStreamReader.feed_data-367"><a href="#UdpStreamReader.feed_data-367"><span class="linenos">367</span></a>                <span class="p">)):</span>
</span><span id="UdpStreamReader.feed_data-368"><a href="#UdpStreamReader.feed_data-368"><span class="linenos">368</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="UdpStreamReader.feed_data-369"><a href="#UdpStreamReader.feed_data-369"><span class="linenos">369</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="UdpStreamReader.feed_data-370"><a href="#UdpStreamReader.feed_data-370"><span class="linenos">370</span></a>            <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="UdpStreamReader.feed_data-371"><a href="#UdpStreamReader.feed_data-371"><span class="linenos">371</span></a>                <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="UdpStreamReader.feed_data-372"><a href="#UdpStreamReader.feed_data-372"><span class="linenos">372</span></a>                <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="UdpStreamReader.feed_data-373"><a href="#UdpStreamReader.feed_data-373"><span class="linenos">373</span></a>                <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="UdpStreamReader.feed_data-374"><a href="#UdpStreamReader.feed_data-374"><span class="linenos">374</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="UdpStreamReader.feed_data-375"><a href="#UdpStreamReader.feed_data-375"><span class="linenos">375</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader.feed_data-376"><a href="#UdpStreamReader.feed_data-376"><span class="linenos">376</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.readline" class="classattr">
                                        <input id="UdpStreamReader.readline-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">readline</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.readline-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.readline"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.readline-378"><a href="#UdpStreamReader.readline-378"><span class="linenos">378</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readline</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader.readline-379"><a href="#UdpStreamReader.readline-379"><span class="linenos">379</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read chunk of data from the stream until newline (b&#39;\n&#39;) is found.</span>
</span><span id="UdpStreamReader.readline-380"><a href="#UdpStreamReader.readline-380"><span class="linenos">380</span></a>
</span><span id="UdpStreamReader.readline-381"><a href="#UdpStreamReader.readline-381"><span class="linenos">381</span></a><span class="sd">        On success, return chunk that ends with newline. If only partial</span>
</span><span id="UdpStreamReader.readline-382"><a href="#UdpStreamReader.readline-382"><span class="linenos">382</span></a><span class="sd">        line can be read due to EOF, return incomplete line without</span>
</span><span id="UdpStreamReader.readline-383"><a href="#UdpStreamReader.readline-383"><span class="linenos">383</span></a><span class="sd">        terminating newline. When EOF was reached while no bytes read, empty</span>
</span><span id="UdpStreamReader.readline-384"><a href="#UdpStreamReader.readline-384"><span class="linenos">384</span></a><span class="sd">        bytes object is returned.</span>
</span><span id="UdpStreamReader.readline-385"><a href="#UdpStreamReader.readline-385"><span class="linenos">385</span></a>
</span><span id="UdpStreamReader.readline-386"><a href="#UdpStreamReader.readline-386"><span class="linenos">386</span></a><span class="sd">        If limit is reached, ValueError will be raised. In that case, if</span>
</span><span id="UdpStreamReader.readline-387"><a href="#UdpStreamReader.readline-387"><span class="linenos">387</span></a><span class="sd">        newline was found, complete line including newline will be removed</span>
</span><span id="UdpStreamReader.readline-388"><a href="#UdpStreamReader.readline-388"><span class="linenos">388</span></a><span class="sd">        from internal buffer. Else, internal buffer will be cleared. Limit is</span>
</span><span id="UdpStreamReader.readline-389"><a href="#UdpStreamReader.readline-389"><span class="linenos">389</span></a><span class="sd">        compared against part of the line without newline.</span>
</span><span id="UdpStreamReader.readline-390"><a href="#UdpStreamReader.readline-390"><span class="linenos">390</span></a>
</span><span id="UdpStreamReader.readline-391"><a href="#UdpStreamReader.readline-391"><span class="linenos">391</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="UdpStreamReader.readline-392"><a href="#UdpStreamReader.readline-392"><span class="linenos">392</span></a><span class="sd">        needed.</span>
</span><span id="UdpStreamReader.readline-393"><a href="#UdpStreamReader.readline-393"><span class="linenos">393</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader.readline-394"><a href="#UdpStreamReader.readline-394"><span class="linenos">394</span></a>        <span class="n">sep</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="UdpStreamReader.readline-395"><a href="#UdpStreamReader.readline-395"><span class="linenos">395</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="UdpStreamReader.readline-396"><a href="#UdpStreamReader.readline-396"><span class="linenos">396</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="UdpStreamReader.readline-397"><a href="#UdpStreamReader.readline-397"><span class="linenos">397</span></a>            <span class="n">line</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readuntil</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="UdpStreamReader.readline-398"><a href="#UdpStreamReader.readline-398"><span class="linenos">398</span></a>        <span class="k">except</span> <span class="n">IncompleteReadError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="UdpStreamReader.readline-399"><a href="#UdpStreamReader.readline-399"><span class="linenos">399</span></a>            <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">partial</span>
</span><span id="UdpStreamReader.readline-400"><a href="#UdpStreamReader.readline-400"><span class="linenos">400</span></a>        <span class="k">except</span> <span class="n">LimitOverrunError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="UdpStreamReader.readline-401"><a href="#UdpStreamReader.readline-401"><span class="linenos">401</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">sep</span><span class="p">,</span> <span class="n">e</span><span class="o">.</span><span class="n">consumed</span><span class="p">):</span>
</span><span id="UdpStreamReader.readline-402"><a href="#UdpStreamReader.readline-402"><span class="linenos">402</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">consumed</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="UdpStreamReader.readline-403"><a href="#UdpStreamReader.readline-403"><span class="linenos">403</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader.readline-404"><a href="#UdpStreamReader.readline-404"><span class="linenos">404</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="UdpStreamReader.readline-405"><a href="#UdpStreamReader.readline-405"><span class="linenos">405</span></a>            
</span><span id="UdpStreamReader.readline-406"><a href="#UdpStreamReader.readline-406"><span class="linenos">406</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader.readline-407"><a href="#UdpStreamReader.readline-407"><span class="linenos">407</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="UdpStreamReader.readline-408"><a href="#UdpStreamReader.readline-408"><span class="linenos">408</span></a>        <span class="k">return</span> <span class="n">line</span>
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
                            <div id="UdpStreamReader.readuntil" class="classattr">
                                        <input id="UdpStreamReader.readuntil-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">readuntil</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">separator</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.readuntil-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.readuntil"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.readuntil-410"><a href="#UdpStreamReader.readuntil-410"><span class="linenos">410</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readuntil</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">separator</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="UdpStreamReader.readuntil-411"><a href="#UdpStreamReader.readuntil-411"><span class="linenos">411</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read data from the stream until ``separator`` is found.</span>
</span><span id="UdpStreamReader.readuntil-412"><a href="#UdpStreamReader.readuntil-412"><span class="linenos">412</span></a>
</span><span id="UdpStreamReader.readuntil-413"><a href="#UdpStreamReader.readuntil-413"><span class="linenos">413</span></a><span class="sd">        On success, the data and separator will be removed from the</span>
</span><span id="UdpStreamReader.readuntil-414"><a href="#UdpStreamReader.readuntil-414"><span class="linenos">414</span></a><span class="sd">        internal buffer (consumed). Returned data will include the</span>
</span><span id="UdpStreamReader.readuntil-415"><a href="#UdpStreamReader.readuntil-415"><span class="linenos">415</span></a><span class="sd">        separator at the end.</span>
</span><span id="UdpStreamReader.readuntil-416"><a href="#UdpStreamReader.readuntil-416"><span class="linenos">416</span></a>
</span><span id="UdpStreamReader.readuntil-417"><a href="#UdpStreamReader.readuntil-417"><span class="linenos">417</span></a><span class="sd">        Configured stream limit is used to check result. Limit sets the</span>
</span><span id="UdpStreamReader.readuntil-418"><a href="#UdpStreamReader.readuntil-418"><span class="linenos">418</span></a><span class="sd">        maximal length of data that can be returned, not counting the</span>
</span><span id="UdpStreamReader.readuntil-419"><a href="#UdpStreamReader.readuntil-419"><span class="linenos">419</span></a><span class="sd">        separator.</span>
</span><span id="UdpStreamReader.readuntil-420"><a href="#UdpStreamReader.readuntil-420"><span class="linenos">420</span></a>
</span><span id="UdpStreamReader.readuntil-421"><a href="#UdpStreamReader.readuntil-421"><span class="linenos">421</span></a><span class="sd">        If an EOF occurs and the complete separator is still not found,</span>
</span><span id="UdpStreamReader.readuntil-422"><a href="#UdpStreamReader.readuntil-422"><span class="linenos">422</span></a><span class="sd">        an IncompleteReadError exception will be raised, and the internal</span>
</span><span id="UdpStreamReader.readuntil-423"><a href="#UdpStreamReader.readuntil-423"><span class="linenos">423</span></a><span class="sd">        buffer will be reset.  The IncompleteReadError.partial attribute</span>
</span><span id="UdpStreamReader.readuntil-424"><a href="#UdpStreamReader.readuntil-424"><span class="linenos">424</span></a><span class="sd">        may contain the separator partially.</span>
</span><span id="UdpStreamReader.readuntil-425"><a href="#UdpStreamReader.readuntil-425"><span class="linenos">425</span></a>
</span><span id="UdpStreamReader.readuntil-426"><a href="#UdpStreamReader.readuntil-426"><span class="linenos">426</span></a><span class="sd">        If the data cannot be read because of over limit, a</span>
</span><span id="UdpStreamReader.readuntil-427"><a href="#UdpStreamReader.readuntil-427"><span class="linenos">427</span></a><span class="sd">        LimitOverrunError exception  will be raised, and the data</span>
</span><span id="UdpStreamReader.readuntil-428"><a href="#UdpStreamReader.readuntil-428"><span class="linenos">428</span></a><span class="sd">        will be left in the internal buffer, so it can be read again.</span>
</span><span id="UdpStreamReader.readuntil-429"><a href="#UdpStreamReader.readuntil-429"><span class="linenos">429</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader.readuntil-430"><a href="#UdpStreamReader.readuntil-430"><span class="linenos">430</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">separator</span><span class="p">)</span>
</span><span id="UdpStreamReader.readuntil-431"><a href="#UdpStreamReader.readuntil-431"><span class="linenos">431</span></a>        <span class="k">if</span> <span class="n">seplen</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.readuntil-432"><a href="#UdpStreamReader.readuntil-432"><span class="linenos">432</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;Separator should be at least one-byte string&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.readuntil-433"><a href="#UdpStreamReader.readuntil-433"><span class="linenos">433</span></a>
</span><span id="UdpStreamReader.readuntil-434"><a href="#UdpStreamReader.readuntil-434"><span class="linenos">434</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader.readuntil-435"><a href="#UdpStreamReader.readuntil-435"><span class="linenos">435</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader.readuntil-436"><a href="#UdpStreamReader.readuntil-436"><span class="linenos">436</span></a>
</span><span id="UdpStreamReader.readuntil-437"><a href="#UdpStreamReader.readuntil-437"><span class="linenos">437</span></a>        <span class="c1"># Consume whole buffer except last bytes, which length is</span>
</span><span id="UdpStreamReader.readuntil-438"><a href="#UdpStreamReader.readuntil-438"><span class="linenos">438</span></a>        <span class="c1"># one less than seplen. Let&#39;s check corner cases with</span>
</span><span id="UdpStreamReader.readuntil-439"><a href="#UdpStreamReader.readuntil-439"><span class="linenos">439</span></a>        <span class="c1"># separator=&#39;SEPARATOR&#39;:</span>
</span><span id="UdpStreamReader.readuntil-440"><a href="#UdpStreamReader.readuntil-440"><span class="linenos">440</span></a>        <span class="c1"># * we have received almost complete separator (without last</span>
</span><span id="UdpStreamReader.readuntil-441"><a href="#UdpStreamReader.readuntil-441"><span class="linenos">441</span></a>        <span class="c1">#   byte). i.e buffer=&#39;some textSEPARATO&#39;. In this case we</span>
</span><span id="UdpStreamReader.readuntil-442"><a href="#UdpStreamReader.readuntil-442"><span class="linenos">442</span></a>        <span class="c1">#   can safely consume len(separator) - 1 bytes.</span>
</span><span id="UdpStreamReader.readuntil-443"><a href="#UdpStreamReader.readuntil-443"><span class="linenos">443</span></a>        <span class="c1"># * last byte of buffer is first byte of separator, i.e.</span>
</span><span id="UdpStreamReader.readuntil-444"><a href="#UdpStreamReader.readuntil-444"><span class="linenos">444</span></a>        <span class="c1">#   buffer=&#39;abcdefghijklmnopqrS&#39;. We may safely consume</span>
</span><span id="UdpStreamReader.readuntil-445"><a href="#UdpStreamReader.readuntil-445"><span class="linenos">445</span></a>        <span class="c1">#   everything except that last byte, but this require to</span>
</span><span id="UdpStreamReader.readuntil-446"><a href="#UdpStreamReader.readuntil-446"><span class="linenos">446</span></a>        <span class="c1">#   analyze bytes of buffer that match partial separator.</span>
</span><span id="UdpStreamReader.readuntil-447"><a href="#UdpStreamReader.readuntil-447"><span class="linenos">447</span></a>        <span class="c1">#   This is slow and/or require FSM. For this case our</span>
</span><span id="UdpStreamReader.readuntil-448"><a href="#UdpStreamReader.readuntil-448"><span class="linenos">448</span></a>        <span class="c1">#   implementation is not optimal, since require rescanning</span>
</span><span id="UdpStreamReader.readuntil-449"><a href="#UdpStreamReader.readuntil-449"><span class="linenos">449</span></a>        <span class="c1">#   of data that is known to not belong to separator. In</span>
</span><span id="UdpStreamReader.readuntil-450"><a href="#UdpStreamReader.readuntil-450"><span class="linenos">450</span></a>        <span class="c1">#   real world, separator will not be so long to notice</span>
</span><span id="UdpStreamReader.readuntil-451"><a href="#UdpStreamReader.readuntil-451"><span class="linenos">451</span></a>        <span class="c1">#   performance problems. Even when reading MIME-encoded</span>
</span><span id="UdpStreamReader.readuntil-452"><a href="#UdpStreamReader.readuntil-452"><span class="linenos">452</span></a>        <span class="c1">#   messages :)</span>
</span><span id="UdpStreamReader.readuntil-453"><a href="#UdpStreamReader.readuntil-453"><span class="linenos">453</span></a>
</span><span id="UdpStreamReader.readuntil-454"><a href="#UdpStreamReader.readuntil-454"><span class="linenos">454</span></a>        <span class="c1"># `offset` is the number of bytes from the beginning of the buffer</span>
</span><span id="UdpStreamReader.readuntil-455"><a href="#UdpStreamReader.readuntil-455"><span class="linenos">455</span></a>        <span class="c1"># where there is no occurrence of `separator`.</span>
</span><span id="UdpStreamReader.readuntil-456"><a href="#UdpStreamReader.readuntil-456"><span class="linenos">456</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="UdpStreamReader.readuntil-457"><a href="#UdpStreamReader.readuntil-457"><span class="linenos">457</span></a>
</span><span id="UdpStreamReader.readuntil-458"><a href="#UdpStreamReader.readuntil-458"><span class="linenos">458</span></a>        <span class="c1"># Loop until we find `separator` in the buffer, exceed the buffer size,</span>
</span><span id="UdpStreamReader.readuntil-459"><a href="#UdpStreamReader.readuntil-459"><span class="linenos">459</span></a>        <span class="c1"># or an EOF has happened.</span>
</span><span id="UdpStreamReader.readuntil-460"><a href="#UdpStreamReader.readuntil-460"><span class="linenos">460</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="UdpStreamReader.readuntil-461"><a href="#UdpStreamReader.readuntil-461"><span class="linenos">461</span></a>            <span class="n">buflen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="UdpStreamReader.readuntil-462"><a href="#UdpStreamReader.readuntil-462"><span class="linenos">462</span></a>
</span><span id="UdpStreamReader.readuntil-463"><a href="#UdpStreamReader.readuntil-463"><span class="linenos">463</span></a>            <span class="c1"># Check if we now have enough data in the buffer for `separator` to</span>
</span><span id="UdpStreamReader.readuntil-464"><a href="#UdpStreamReader.readuntil-464"><span class="linenos">464</span></a>            <span class="c1"># fit.</span>
</span><span id="UdpStreamReader.readuntil-465"><a href="#UdpStreamReader.readuntil-465"><span class="linenos">465</span></a>            <span class="k">if</span> <span class="n">buflen</span> <span class="o">-</span> <span class="n">offset</span> <span class="o">&gt;=</span> <span class="n">seplen</span><span class="p">:</span>
</span><span id="UdpStreamReader.readuntil-466"><a href="#UdpStreamReader.readuntil-466"><span class="linenos">466</span></a>                <span class="n">isep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">separator</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span>
</span><span id="UdpStreamReader.readuntil-467"><a href="#UdpStreamReader.readuntil-467"><span class="linenos">467</span></a>
</span><span id="UdpStreamReader.readuntil-468"><a href="#UdpStreamReader.readuntil-468"><span class="linenos">468</span></a>                <span class="k">if</span> <span class="n">isep</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
</span><span id="UdpStreamReader.readuntil-469"><a href="#UdpStreamReader.readuntil-469"><span class="linenos">469</span></a>                    <span class="c1"># `separator` is in the buffer. `isep` will be used later</span>
</span><span id="UdpStreamReader.readuntil-470"><a href="#UdpStreamReader.readuntil-470"><span class="linenos">470</span></a>                    <span class="c1"># to retrieve the data.</span>
</span><span id="UdpStreamReader.readuntil-471"><a href="#UdpStreamReader.readuntil-471"><span class="linenos">471</span></a>                    <span class="k">break</span>
</span><span id="UdpStreamReader.readuntil-472"><a href="#UdpStreamReader.readuntil-472"><span class="linenos">472</span></a>
</span><span id="UdpStreamReader.readuntil-473"><a href="#UdpStreamReader.readuntil-473"><span class="linenos">473</span></a>                <span class="c1"># see upper comment for explanation.</span>
</span><span id="UdpStreamReader.readuntil-474"><a href="#UdpStreamReader.readuntil-474"><span class="linenos">474</span></a>                <span class="n">offset</span> <span class="o">=</span> <span class="n">buflen</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">-</span> <span class="n">seplen</span>
</span><span id="UdpStreamReader.readuntil-475"><a href="#UdpStreamReader.readuntil-475"><span class="linenos">475</span></a>                <span class="k">if</span> <span class="n">offset</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="UdpStreamReader.readuntil-476"><a href="#UdpStreamReader.readuntil-476"><span class="linenos">476</span></a>                    <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="UdpStreamReader.readuntil-477"><a href="#UdpStreamReader.readuntil-477"><span class="linenos">477</span></a>                        <span class="s1">&#39;Separator is not found, and chunk exceed the limit&#39;</span><span class="p">,</span>
</span><span id="UdpStreamReader.readuntil-478"><a href="#UdpStreamReader.readuntil-478"><span class="linenos">478</span></a>                        <span class="n">offset</span><span class="p">)</span>
</span><span id="UdpStreamReader.readuntil-479"><a href="#UdpStreamReader.readuntil-479"><span class="linenos">479</span></a>
</span><span id="UdpStreamReader.readuntil-480"><a href="#UdpStreamReader.readuntil-480"><span class="linenos">480</span></a>            <span class="c1"># Complete message (with full separator) may be present in buffer</span>
</span><span id="UdpStreamReader.readuntil-481"><a href="#UdpStreamReader.readuntil-481"><span class="linenos">481</span></a>            <span class="c1"># even when EOF flag is set. This may happen when the last chunk</span>
</span><span id="UdpStreamReader.readuntil-482"><a href="#UdpStreamReader.readuntil-482"><span class="linenos">482</span></a>            <span class="c1"># adds data which makes separator be found. That&#39;s why we check for</span>
</span><span id="UdpStreamReader.readuntil-483"><a href="#UdpStreamReader.readuntil-483"><span class="linenos">483</span></a>            <span class="c1"># EOF *ater* inspecting the buffer.</span>
</span><span id="UdpStreamReader.readuntil-484"><a href="#UdpStreamReader.readuntil-484"><span class="linenos">484</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader.readuntil-485"><a href="#UdpStreamReader.readuntil-485"><span class="linenos">485</span></a>                <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader.readuntil-486"><a href="#UdpStreamReader.readuntil-486"><span class="linenos">486</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="UdpStreamReader.readuntil-487"><a href="#UdpStreamReader.readuntil-487"><span class="linenos">487</span></a>
</span><span id="UdpStreamReader.readuntil-488"><a href="#UdpStreamReader.readuntil-488"><span class="linenos">488</span></a>            <span class="c1"># _wait_for_data() will resume reading if stream was paused.</span>
</span><span id="UdpStreamReader.readuntil-489"><a href="#UdpStreamReader.readuntil-489"><span class="linenos">489</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readuntil&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.readuntil-490"><a href="#UdpStreamReader.readuntil-490"><span class="linenos">490</span></a>
</span><span id="UdpStreamReader.readuntil-491"><a href="#UdpStreamReader.readuntil-491"><span class="linenos">491</span></a>        <span class="k">if</span> <span class="n">isep</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="UdpStreamReader.readuntil-492"><a href="#UdpStreamReader.readuntil-492"><span class="linenos">492</span></a>            <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="UdpStreamReader.readuntil-493"><a href="#UdpStreamReader.readuntil-493"><span class="linenos">493</span></a>                <span class="s1">&#39;Separator is found, but chunk is longer than limit&#39;</span><span class="p">,</span> <span class="n">isep</span><span class="p">)</span>
</span><span id="UdpStreamReader.readuntil-494"><a href="#UdpStreamReader.readuntil-494"><span class="linenos">494</span></a>
</span><span id="UdpStreamReader.readuntil-495"><a href="#UdpStreamReader.readuntil-495"><span class="linenos">495</span></a>        <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">isep</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="UdpStreamReader.readuntil-496"><a href="#UdpStreamReader.readuntil-496"><span class="linenos">496</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader.readuntil-497"><a href="#UdpStreamReader.readuntil-497"><span class="linenos">497</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
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
                            <div id="UdpStreamReader.read" class="classattr">
                                        <input id="UdpStreamReader.read-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">n</span><span class="o">=-</span><span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.read-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.read"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.read-499"><a href="#UdpStreamReader.read-499"><span class="linenos">499</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="UdpStreamReader.read-500"><a href="#UdpStreamReader.read-500"><span class="linenos">500</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="UdpStreamReader.read-501"><a href="#UdpStreamReader.read-501"><span class="linenos">501</span></a>
</span><span id="UdpStreamReader.read-502"><a href="#UdpStreamReader.read-502"><span class="linenos">502</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="UdpStreamReader.read-503"><a href="#UdpStreamReader.read-503"><span class="linenos">503</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="UdpStreamReader.read-504"><a href="#UdpStreamReader.read-504"><span class="linenos">504</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="UdpStreamReader.read-505"><a href="#UdpStreamReader.read-505"><span class="linenos">505</span></a>
</span><span id="UdpStreamReader.read-506"><a href="#UdpStreamReader.read-506"><span class="linenos">506</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="UdpStreamReader.read-507"><a href="#UdpStreamReader.read-507"><span class="linenos">507</span></a>
</span><span id="UdpStreamReader.read-508"><a href="#UdpStreamReader.read-508"><span class="linenos">508</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="UdpStreamReader.read-509"><a href="#UdpStreamReader.read-509"><span class="linenos">509</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="UdpStreamReader.read-510"><a href="#UdpStreamReader.read-510"><span class="linenos">510</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="UdpStreamReader.read-511"><a href="#UdpStreamReader.read-511"><span class="linenos">511</span></a><span class="sd">        object.</span>
</span><span id="UdpStreamReader.read-512"><a href="#UdpStreamReader.read-512"><span class="linenos">512</span></a>
</span><span id="UdpStreamReader.read-513"><a href="#UdpStreamReader.read-513"><span class="linenos">513</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="UdpStreamReader.read-514"><a href="#UdpStreamReader.read-514"><span class="linenos">514</span></a><span class="sd">        creation.</span>
</span><span id="UdpStreamReader.read-515"><a href="#UdpStreamReader.read-515"><span class="linenos">515</span></a>
</span><span id="UdpStreamReader.read-516"><a href="#UdpStreamReader.read-516"><span class="linenos">516</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="UdpStreamReader.read-517"><a href="#UdpStreamReader.read-517"><span class="linenos">517</span></a><span class="sd">        needed.</span>
</span><span id="UdpStreamReader.read-518"><a href="#UdpStreamReader.read-518"><span class="linenos">518</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader.read-519"><a href="#UdpStreamReader.read-519"><span class="linenos">519</span></a>
</span><span id="UdpStreamReader.read-520"><a href="#UdpStreamReader.read-520"><span class="linenos">520</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader.read-521"><a href="#UdpStreamReader.read-521"><span class="linenos">521</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader.read-522"><a href="#UdpStreamReader.read-522"><span class="linenos">522</span></a>
</span><span id="UdpStreamReader.read-523"><a href="#UdpStreamReader.read-523"><span class="linenos">523</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.read-524"><a href="#UdpStreamReader.read-524"><span class="linenos">524</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="UdpStreamReader.read-525"><a href="#UdpStreamReader.read-525"><span class="linenos">525</span></a>
</span><span id="UdpStreamReader.read-526"><a href="#UdpStreamReader.read-526"><span class="linenos">526</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.read-527"><a href="#UdpStreamReader.read-527"><span class="linenos">527</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="UdpStreamReader.read-528"><a href="#UdpStreamReader.read-528"><span class="linenos">528</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="UdpStreamReader.read-529"><a href="#UdpStreamReader.read-529"><span class="linenos">529</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="UdpStreamReader.read-530"><a href="#UdpStreamReader.read-530"><span class="linenos">530</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="UdpStreamReader.read-531"><a href="#UdpStreamReader.read-531"><span class="linenos">531</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="UdpStreamReader.read-532"><a href="#UdpStreamReader.read-532"><span class="linenos">532</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="UdpStreamReader.read-533"><a href="#UdpStreamReader.read-533"><span class="linenos">533</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="UdpStreamReader.read-534"><a href="#UdpStreamReader.read-534"><span class="linenos">534</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="UdpStreamReader.read-535"><a href="#UdpStreamReader.read-535"><span class="linenos">535</span></a>                    <span class="k">break</span>
</span><span id="UdpStreamReader.read-536"><a href="#UdpStreamReader.read-536"><span class="linenos">536</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="UdpStreamReader.read-537"><a href="#UdpStreamReader.read-537"><span class="linenos">537</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="UdpStreamReader.read-538"><a href="#UdpStreamReader.read-538"><span class="linenos">538</span></a>
</span><span id="UdpStreamReader.read-539"><a href="#UdpStreamReader.read-539"><span class="linenos">539</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader.read-540"><a href="#UdpStreamReader.read-540"><span class="linenos">540</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.read-541"><a href="#UdpStreamReader.read-541"><span class="linenos">541</span></a>
</span><span id="UdpStreamReader.read-542"><a href="#UdpStreamReader.read-542"><span class="linenos">542</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="UdpStreamReader.read-543"><a href="#UdpStreamReader.read-543"><span class="linenos">543</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="UdpStreamReader.read-544"><a href="#UdpStreamReader.read-544"><span class="linenos">544</span></a>
</span><span id="UdpStreamReader.read-545"><a href="#UdpStreamReader.read-545"><span class="linenos">545</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader.read-546"><a href="#UdpStreamReader.read-546"><span class="linenos">546</span></a>        <span class="k">return</span> <span class="n">data</span>
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
                            <div id="UdpStreamReader.read_nearly" class="classattr">
                                        <input id="UdpStreamReader.read_nearly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_nearly</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">n</span><span class="o">=-</span><span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.read_nearly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.read_nearly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.read_nearly-548"><a href="#UdpStreamReader.read_nearly-548"><span class="linenos">548</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="UdpStreamReader.read_nearly-549"><a href="#UdpStreamReader.read_nearly-549"><span class="linenos">549</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="UdpStreamReader.read_nearly-550"><a href="#UdpStreamReader.read_nearly-550"><span class="linenos">550</span></a>
</span><span id="UdpStreamReader.read_nearly-551"><a href="#UdpStreamReader.read_nearly-551"><span class="linenos">551</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="UdpStreamReader.read_nearly-552"><a href="#UdpStreamReader.read_nearly-552"><span class="linenos">552</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="UdpStreamReader.read_nearly-553"><a href="#UdpStreamReader.read_nearly-553"><span class="linenos">553</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="UdpStreamReader.read_nearly-554"><a href="#UdpStreamReader.read_nearly-554"><span class="linenos">554</span></a>
</span><span id="UdpStreamReader.read_nearly-555"><a href="#UdpStreamReader.read_nearly-555"><span class="linenos">555</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="UdpStreamReader.read_nearly-556"><a href="#UdpStreamReader.read_nearly-556"><span class="linenos">556</span></a>
</span><span id="UdpStreamReader.read_nearly-557"><a href="#UdpStreamReader.read_nearly-557"><span class="linenos">557</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="UdpStreamReader.read_nearly-558"><a href="#UdpStreamReader.read_nearly-558"><span class="linenos">558</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="UdpStreamReader.read_nearly-559"><a href="#UdpStreamReader.read_nearly-559"><span class="linenos">559</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="UdpStreamReader.read_nearly-560"><a href="#UdpStreamReader.read_nearly-560"><span class="linenos">560</span></a><span class="sd">        object.</span>
</span><span id="UdpStreamReader.read_nearly-561"><a href="#UdpStreamReader.read_nearly-561"><span class="linenos">561</span></a>
</span><span id="UdpStreamReader.read_nearly-562"><a href="#UdpStreamReader.read_nearly-562"><span class="linenos">562</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="UdpStreamReader.read_nearly-563"><a href="#UdpStreamReader.read_nearly-563"><span class="linenos">563</span></a><span class="sd">        creation.</span>
</span><span id="UdpStreamReader.read_nearly-564"><a href="#UdpStreamReader.read_nearly-564"><span class="linenos">564</span></a>
</span><span id="UdpStreamReader.read_nearly-565"><a href="#UdpStreamReader.read_nearly-565"><span class="linenos">565</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="UdpStreamReader.read_nearly-566"><a href="#UdpStreamReader.read_nearly-566"><span class="linenos">566</span></a><span class="sd">        needed.</span>
</span><span id="UdpStreamReader.read_nearly-567"><a href="#UdpStreamReader.read_nearly-567"><span class="linenos">567</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader.read_nearly-568"><a href="#UdpStreamReader.read_nearly-568"><span class="linenos">568</span></a>
</span><span id="UdpStreamReader.read_nearly-569"><a href="#UdpStreamReader.read_nearly-569"><span class="linenos">569</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_nearly-570"><a href="#UdpStreamReader.read_nearly-570"><span class="linenos">570</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader.read_nearly-571"><a href="#UdpStreamReader.read_nearly-571"><span class="linenos">571</span></a>
</span><span id="UdpStreamReader.read_nearly-572"><a href="#UdpStreamReader.read_nearly-572"><span class="linenos">572</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_nearly-573"><a href="#UdpStreamReader.read_nearly-573"><span class="linenos">573</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="UdpStreamReader.read_nearly-574"><a href="#UdpStreamReader.read_nearly-574"><span class="linenos">574</span></a>
</span><span id="UdpStreamReader.read_nearly-575"><a href="#UdpStreamReader.read_nearly-575"><span class="linenos">575</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_nearly-576"><a href="#UdpStreamReader.read_nearly-576"><span class="linenos">576</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="UdpStreamReader.read_nearly-577"><a href="#UdpStreamReader.read_nearly-577"><span class="linenos">577</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="UdpStreamReader.read_nearly-578"><a href="#UdpStreamReader.read_nearly-578"><span class="linenos">578</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="UdpStreamReader.read_nearly-579"><a href="#UdpStreamReader.read_nearly-579"><span class="linenos">579</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="UdpStreamReader.read_nearly-580"><a href="#UdpStreamReader.read_nearly-580"><span class="linenos">580</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="UdpStreamReader.read_nearly-581"><a href="#UdpStreamReader.read_nearly-581"><span class="linenos">581</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_nearly-582"><a href="#UdpStreamReader.read_nearly-582"><span class="linenos">582</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="UdpStreamReader.read_nearly-583"><a href="#UdpStreamReader.read_nearly-583"><span class="linenos">583</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_nearly-584"><a href="#UdpStreamReader.read_nearly-584"><span class="linenos">584</span></a>                    <span class="k">break</span>
</span><span id="UdpStreamReader.read_nearly-585"><a href="#UdpStreamReader.read_nearly-585"><span class="linenos">585</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="UdpStreamReader.read_nearly-586"><a href="#UdpStreamReader.read_nearly-586"><span class="linenos">586</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="UdpStreamReader.read_nearly-587"><a href="#UdpStreamReader.read_nearly-587"><span class="linenos">587</span></a>
</span><span id="UdpStreamReader.read_nearly-588"><a href="#UdpStreamReader.read_nearly-588"><span class="linenos">588</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader.read_nearly-589"><a href="#UdpStreamReader.read_nearly-589"><span class="linenos">589</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.read_nearly-590"><a href="#UdpStreamReader.read_nearly-590"><span class="linenos">590</span></a>
</span><span id="UdpStreamReader.read_nearly-591"><a href="#UdpStreamReader.read_nearly-591"><span class="linenos">591</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="UdpStreamReader.read_nearly-592"><a href="#UdpStreamReader.read_nearly-592"><span class="linenos">592</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data_nearly</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader.read_nearly-593"><a href="#UdpStreamReader.read_nearly-593"><span class="linenos">593</span></a>
</span><span id="UdpStreamReader.read_nearly-594"><a href="#UdpStreamReader.read_nearly-594"><span class="linenos">594</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader.read_nearly-595"><a href="#UdpStreamReader.read_nearly-595"><span class="linenos">595</span></a>        <span class="k">return</span> <span class="n">data</span>
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
                            <div id="UdpStreamReader.readexactly" class="classattr">
                                        <input id="UdpStreamReader.readexactly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">readexactly</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">n</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.readexactly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.readexactly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.readexactly-597"><a href="#UdpStreamReader.readexactly-597"><span class="linenos">597</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="UdpStreamReader.readexactly-598"><a href="#UdpStreamReader.readexactly-598"><span class="linenos">598</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read exactly `n` bytes.</span>
</span><span id="UdpStreamReader.readexactly-599"><a href="#UdpStreamReader.readexactly-599"><span class="linenos">599</span></a>
</span><span id="UdpStreamReader.readexactly-600"><a href="#UdpStreamReader.readexactly-600"><span class="linenos">600</span></a><span class="sd">        Raise an IncompleteReadError if EOF is reached before `n` bytes can be</span>
</span><span id="UdpStreamReader.readexactly-601"><a href="#UdpStreamReader.readexactly-601"><span class="linenos">601</span></a><span class="sd">        read. The IncompleteReadError.partial attribute of the exception will</span>
</span><span id="UdpStreamReader.readexactly-602"><a href="#UdpStreamReader.readexactly-602"><span class="linenos">602</span></a><span class="sd">        contain the partial read bytes.</span>
</span><span id="UdpStreamReader.readexactly-603"><a href="#UdpStreamReader.readexactly-603"><span class="linenos">603</span></a>
</span><span id="UdpStreamReader.readexactly-604"><a href="#UdpStreamReader.readexactly-604"><span class="linenos">604</span></a><span class="sd">        if n is zero, return empty bytes object.</span>
</span><span id="UdpStreamReader.readexactly-605"><a href="#UdpStreamReader.readexactly-605"><span class="linenos">605</span></a>
</span><span id="UdpStreamReader.readexactly-606"><a href="#UdpStreamReader.readexactly-606"><span class="linenos">606</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="UdpStreamReader.readexactly-607"><a href="#UdpStreamReader.readexactly-607"><span class="linenos">607</span></a><span class="sd">        creation.</span>
</span><span id="UdpStreamReader.readexactly-608"><a href="#UdpStreamReader.readexactly-608"><span class="linenos">608</span></a>
</span><span id="UdpStreamReader.readexactly-609"><a href="#UdpStreamReader.readexactly-609"><span class="linenos">609</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="UdpStreamReader.readexactly-610"><a href="#UdpStreamReader.readexactly-610"><span class="linenos">610</span></a><span class="sd">        needed.</span>
</span><span id="UdpStreamReader.readexactly-611"><a href="#UdpStreamReader.readexactly-611"><span class="linenos">611</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamReader.readexactly-612"><a href="#UdpStreamReader.readexactly-612"><span class="linenos">612</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.readexactly-613"><a href="#UdpStreamReader.readexactly-613"><span class="linenos">613</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.readexactly-614"><a href="#UdpStreamReader.readexactly-614"><span class="linenos">614</span></a>
</span><span id="UdpStreamReader.readexactly-615"><a href="#UdpStreamReader.readexactly-615"><span class="linenos">615</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader.readexactly-616"><a href="#UdpStreamReader.readexactly-616"><span class="linenos">616</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader.readexactly-617"><a href="#UdpStreamReader.readexactly-617"><span class="linenos">617</span></a>
</span><span id="UdpStreamReader.readexactly-618"><a href="#UdpStreamReader.readexactly-618"><span class="linenos">618</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.readexactly-619"><a href="#UdpStreamReader.readexactly-619"><span class="linenos">619</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="UdpStreamReader.readexactly-620"><a href="#UdpStreamReader.readexactly-620"><span class="linenos">620</span></a>
</span><span id="UdpStreamReader.readexactly-621"><a href="#UdpStreamReader.readexactly-621"><span class="linenos">621</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="UdpStreamReader.readexactly-622"><a href="#UdpStreamReader.readexactly-622"><span class="linenos">622</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader.readexactly-623"><a href="#UdpStreamReader.readexactly-623"><span class="linenos">623</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader.readexactly-624"><a href="#UdpStreamReader.readexactly-624"><span class="linenos">624</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader.readexactly-625"><a href="#UdpStreamReader.readexactly-625"><span class="linenos">625</span></a>
</span><span id="UdpStreamReader.readexactly-626"><a href="#UdpStreamReader.readexactly-626"><span class="linenos">626</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.readexactly-627"><a href="#UdpStreamReader.readexactly-627"><span class="linenos">627</span></a>
</span><span id="UdpStreamReader.readexactly-628"><a href="#UdpStreamReader.readexactly-628"><span class="linenos">628</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="UdpStreamReader.readexactly-629"><a href="#UdpStreamReader.readexactly-629"><span class="linenos">629</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader.readexactly-630"><a href="#UdpStreamReader.readexactly-630"><span class="linenos">630</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader.readexactly-631"><a href="#UdpStreamReader.readexactly-631"><span class="linenos">631</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader.readexactly-632"><a href="#UdpStreamReader.readexactly-632"><span class="linenos">632</span></a>
</span><span id="UdpStreamReader.readexactly-633"><a href="#UdpStreamReader.readexactly-633"><span class="linenos">633</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader.readexactly-634"><a href="#UdpStreamReader.readexactly-634"><span class="linenos">634</span></a>        <span class="k">return</span> <span class="n">data</span>
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
                            <div id="UdpStreamReader.readonly_exactly" class="classattr">
                                        <input id="UdpStreamReader.readonly_exactly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">readonly_exactly</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">n</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.readonly_exactly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.readonly_exactly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.readonly_exactly-636"><a href="#UdpStreamReader.readonly_exactly-636"><span class="linenos">636</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readonly_exactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="UdpStreamReader.readonly_exactly-637"><a href="#UdpStreamReader.readonly_exactly-637"><span class="linenos">637</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.readonly_exactly-638"><a href="#UdpStreamReader.readonly_exactly-638"><span class="linenos">638</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.readonly_exactly-639"><a href="#UdpStreamReader.readonly_exactly-639"><span class="linenos">639</span></a>
</span><span id="UdpStreamReader.readonly_exactly-640"><a href="#UdpStreamReader.readonly_exactly-640"><span class="linenos">640</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReader.readonly_exactly-641"><a href="#UdpStreamReader.readonly_exactly-641"><span class="linenos">641</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="UdpStreamReader.readonly_exactly-642"><a href="#UdpStreamReader.readonly_exactly-642"><span class="linenos">642</span></a>
</span><span id="UdpStreamReader.readonly_exactly-643"><a href="#UdpStreamReader.readonly_exactly-643"><span class="linenos">643</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="UdpStreamReader.readonly_exactly-644"><a href="#UdpStreamReader.readonly_exactly-644"><span class="linenos">644</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="UdpStreamReader.readonly_exactly-645"><a href="#UdpStreamReader.readonly_exactly-645"><span class="linenos">645</span></a>
</span><span id="UdpStreamReader.readonly_exactly-646"><a href="#UdpStreamReader.readonly_exactly-646"><span class="linenos">646</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="UdpStreamReader.readonly_exactly-647"><a href="#UdpStreamReader.readonly_exactly-647"><span class="linenos">647</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="UdpStreamReader.readonly_exactly-648"><a href="#UdpStreamReader.readonly_exactly-648"><span class="linenos">648</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader.readonly_exactly-649"><a href="#UdpStreamReader.readonly_exactly-649"><span class="linenos">649</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader.readonly_exactly-650"><a href="#UdpStreamReader.readonly_exactly-650"><span class="linenos">650</span></a>
</span><span id="UdpStreamReader.readonly_exactly-651"><a href="#UdpStreamReader.readonly_exactly-651"><span class="linenos">651</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.readonly_exactly-652"><a href="#UdpStreamReader.readonly_exactly-652"><span class="linenos">652</span></a>
</span><span id="UdpStreamReader.readonly_exactly-653"><a href="#UdpStreamReader.readonly_exactly-653"><span class="linenos">653</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="UdpStreamReader.readonly_exactly-654"><a href="#UdpStreamReader.readonly_exactly-654"><span class="linenos">654</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="UdpStreamReader.readonly_exactly-655"><a href="#UdpStreamReader.readonly_exactly-655"><span class="linenos">655</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader.readonly_exactly-656"><a href="#UdpStreamReader.readonly_exactly-656"><span class="linenos">656</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="UdpStreamReader.readonly_exactly-657"><a href="#UdpStreamReader.readonly_exactly-657"><span class="linenos">657</span></a>
</span><span id="UdpStreamReader.readonly_exactly-658"><a href="#UdpStreamReader.readonly_exactly-658"><span class="linenos">658</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="UdpStreamReader.readonly_exactly-659"><a href="#UdpStreamReader.readonly_exactly-659"><span class="linenos">659</span></a>        <span class="k">return</span> <span class="n">data</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.read_message" class="classattr">
                                        <input id="UdpStreamReader.read_message-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.read_message-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.read_message"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.read_message-661"><a href="#UdpStreamReader.read_message-661"><span class="linenos">661</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_message</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader.read_message-662"><a href="#UdpStreamReader.read_message-662"><span class="linenos">662</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span><span class="p">)</span>
</span><span id="UdpStreamReader.read_message-663"><a href="#UdpStreamReader.read_message-663"><span class="linenos">663</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.read_message-664"><a href="#UdpStreamReader.read_message-664"><span class="linenos">664</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="n">message_len</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.message_awailable" class="classattr">
                                        <input id="UdpStreamReader.message_awailable-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">message_awailable</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="UdpStreamReader.message_awailable-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.message_awailable"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.message_awailable-666"><a href="#UdpStreamReader.message_awailable-666"><span class="linenos">666</span></a>    <span class="k">def</span> <span class="nf">message_awailable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="UdpStreamReader.message_awailable-667"><a href="#UdpStreamReader.message_awailable-667"><span class="linenos">667</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span>
</span><span id="UdpStreamReader.message_awailable-668"><a href="#UdpStreamReader.message_awailable-668"><span class="linenos">668</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">message_size_len</span><span class="p">:</span>
</span><span id="UdpStreamReader.message_awailable-669"><a href="#UdpStreamReader.message_awailable-669"><span class="linenos">669</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="UdpStreamReader.message_awailable-670"><a href="#UdpStreamReader.message_awailable-670"><span class="linenos">670</span></a>
</span><span id="UdpStreamReader.message_awailable-671"><a href="#UdpStreamReader.message_awailable-671"><span class="linenos">671</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="UdpStreamReader.message_awailable-672"><a href="#UdpStreamReader.message_awailable-672"><span class="linenos">672</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReader.message_awailable-673"><a href="#UdpStreamReader.message_awailable-673"><span class="linenos">673</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="p">(</span><span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_len</span><span class="p">):</span>
</span><span id="UdpStreamReader.message_awailable-674"><a href="#UdpStreamReader.message_awailable-674"><span class="linenos">674</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="UdpStreamReader.message_awailable-675"><a href="#UdpStreamReader.message_awailable-675"><span class="linenos">675</span></a>        
</span><span id="UdpStreamReader.message_awailable-676"><a href="#UdpStreamReader.message_awailable-676"><span class="linenos">676</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.transport_pause_reading" class="classattr">
                                        <input id="UdpStreamReader.transport_pause_reading-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">transport_pause_reading</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.transport_pause_reading-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.transport_pause_reading"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.transport_pause_reading-678"><a href="#UdpStreamReader.transport_pause_reading-678"><span class="linenos">678</span></a>    <span class="k">def</span> <span class="nf">transport_pause_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader.transport_pause_reading-679"><a href="#UdpStreamReader.transport_pause_reading-679"><span class="linenos">679</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="UdpStreamReader.transport_pause_reading-680"><a href="#UdpStreamReader.transport_pause_reading-680"><span class="linenos">680</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="UdpStreamReader.transport_pause_reading-681"><a href="#UdpStreamReader.transport_pause_reading-681"><span class="linenos">681</span></a>        <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="UdpStreamReader.transport_pause_reading-682"><a href="#UdpStreamReader.transport_pause_reading-682"><span class="linenos">682</span></a>            <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="UdpStreamReader.transport_pause_reading-683"><a href="#UdpStreamReader.transport_pause_reading-683"><span class="linenos">683</span></a>            <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="UdpStreamReader.transport_pause_reading-684"><a href="#UdpStreamReader.transport_pause_reading-684"><span class="linenos">684</span></a>            <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="UdpStreamReader.transport_pause_reading-685"><a href="#UdpStreamReader.transport_pause_reading-685"><span class="linenos">685</span></a>            <span class="k">pass</span>
</span><span id="UdpStreamReader.transport_pause_reading-686"><a href="#UdpStreamReader.transport_pause_reading-686"><span class="linenos">686</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamReader.transport_pause_reading-687"><a href="#UdpStreamReader.transport_pause_reading-687"><span class="linenos">687</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReader.transport_resume_reading" class="classattr">
                                        <input id="UdpStreamReader.transport_resume_reading-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">transport_resume_reading</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReader.transport_resume_reading-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReader.transport_resume_reading"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReader.transport_resume_reading-689"><a href="#UdpStreamReader.transport_resume_reading-689"><span class="linenos">689</span></a>    <span class="k">def</span> <span class="nf">transport_resume_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamReader.transport_resume_reading-690"><a href="#UdpStreamReader.transport_resume_reading-690"><span class="linenos">690</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="UdpStreamReader.transport_resume_reading-691"><a href="#UdpStreamReader.transport_resume_reading-691"><span class="linenos">691</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>asyncio.streams.StreamReader</dt>
                                <dd id="UdpStreamReader.exception" class="function">exception</dd>
                <dd id="UdpStreamReader.set_exception" class="function">set_exception</dd>
                <dd id="UdpStreamReader.set_transport" class="function">set_transport</dd>
                <dd id="UdpStreamReader.feed_eof" class="function">feed_eof</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="UdpStreamReaderProtocol">
                            <input id="UdpStreamReaderProtocol-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UdpStreamReaderProtocol</span><wbr>(<span class="base">asyncio.streams.StreamReaderProtocol</span>, <span class="base">cengal.parallel_execution.asyncio.efficient_streams.versions.v_0.efficient_streams_abstract.StreamReaderProtocolAbstract</span>):

                <label class="view-source-button" for="UdpStreamReaderProtocol-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReaderProtocol"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReaderProtocol-694"><a href="#UdpStreamReaderProtocol-694"><span class="linenos">694</span></a><span class="k">class</span> <span class="nc">UdpStreamReaderProtocol</span><span class="p">(</span><span class="n">OriginalStreamReaderProtocol</span><span class="p">,</span> <span class="n">StreamReaderProtocolAbstract</span><span class="p">):</span>
</span><span id="UdpStreamReaderProtocol-695"><a href="#UdpStreamReaderProtocol-695"><span class="linenos">695</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol-696"><a href="#UdpStreamReaderProtocol-696"><span class="linenos">696</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="UdpStreamReaderProtocol-697"><a href="#UdpStreamReaderProtocol-697"><span class="linenos">697</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="UdpStreamReaderProtocol-698"><a href="#UdpStreamReaderProtocol-698"><span class="linenos">698</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol-699"><a href="#UdpStreamReaderProtocol-699"><span class="linenos">699</span></a>
</span><span id="UdpStreamReaderProtocol-700"><a href="#UdpStreamReaderProtocol-700"><span class="linenos">700</span></a>    <span class="k">def</span> <span class="nf">connection_made</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="UdpStreamReaderProtocol-701"><a href="#UdpStreamReaderProtocol-701"><span class="linenos">701</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reject_connection</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol-702"><a href="#UdpStreamReaderProtocol-702"><span class="linenos">702</span></a>            <span class="n">context</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="UdpStreamReaderProtocol-703"><a href="#UdpStreamReaderProtocol-703"><span class="linenos">703</span></a>                <span class="s1">&#39;message&#39;</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;An open stream was garbage collected prior to &#39;</span>
</span><span id="UdpStreamReaderProtocol-704"><a href="#UdpStreamReaderProtocol-704"><span class="linenos">704</span></a>                            <span class="s1">&#39;establishing network connection; &#39;</span>
</span><span id="UdpStreamReaderProtocol-705"><a href="#UdpStreamReaderProtocol-705"><span class="linenos">705</span></a>                            <span class="s1">&#39;call &quot;stream.close()&quot; explicitly.&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol-706"><a href="#UdpStreamReaderProtocol-706"><span class="linenos">706</span></a>            <span class="p">}</span>
</span><span id="UdpStreamReaderProtocol-707"><a href="#UdpStreamReaderProtocol-707"><span class="linenos">707</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol-708"><a href="#UdpStreamReaderProtocol-708"><span class="linenos">708</span></a>                <span class="n">context</span><span class="p">[</span><span class="s1">&#39;source_traceback&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span>
</span><span id="UdpStreamReaderProtocol-709"><a href="#UdpStreamReaderProtocol-709"><span class="linenos">709</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">call_exception_handler</span><span class="p">(</span><span class="n">context</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol-710"><a href="#UdpStreamReaderProtocol-710"><span class="linenos">710</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">abort</span><span class="p">()</span>
</span><span id="UdpStreamReaderProtocol-711"><a href="#UdpStreamReaderProtocol-711"><span class="linenos">711</span></a>            <span class="k">return</span>
</span><span id="UdpStreamReaderProtocol-712"><a href="#UdpStreamReaderProtocol-712"><span class="linenos">712</span></a>        
</span><span id="UdpStreamReaderProtocol-713"><a href="#UdpStreamReaderProtocol-713"><span class="linenos">713</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="n">transport</span>
</span><span id="UdpStreamReaderProtocol-714"><a href="#UdpStreamReaderProtocol-714"><span class="linenos">714</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_reader</span>
</span><span id="UdpStreamReaderProtocol-715"><a href="#UdpStreamReaderProtocol-715"><span class="linenos">715</span></a>        <span class="k">if</span> <span class="n">reader</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol-716"><a href="#UdpStreamReaderProtocol-716"><span class="linenos">716</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">set_transport</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol-717"><a href="#UdpStreamReaderProtocol-717"><span class="linenos">717</span></a>
</span><span id="UdpStreamReaderProtocol-718"><a href="#UdpStreamReaderProtocol-718"><span class="linenos">718</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_over_ssl</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">get_extra_info</span><span class="p">(</span><span class="s1">&#39;sslcontext&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</span><span id="UdpStreamReaderProtocol-719"><a href="#UdpStreamReaderProtocol-719"><span class="linenos">719</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol-720"><a href="#UdpStreamReaderProtocol-720"><span class="linenos">720</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span> <span class="o">=</span> <span class="n">UdpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span>
</span><span id="UdpStreamReaderProtocol-721"><a href="#UdpStreamReaderProtocol-721"><span class="linenos">721</span></a>                                               <span class="n">reader</span><span class="p">,</span>
</span><span id="UdpStreamReaderProtocol-722"><a href="#UdpStreamReaderProtocol-722"><span class="linenos">722</span></a>                                               <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol-723"><a href="#UdpStreamReaderProtocol-723"><span class="linenos">723</span></a>            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span><span class="p">(</span><span class="n">reader</span><span class="p">,</span>
</span><span id="UdpStreamReaderProtocol-724"><a href="#UdpStreamReaderProtocol-724"><span class="linenos">724</span></a>                                            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol-725"><a href="#UdpStreamReaderProtocol-725"><span class="linenos">725</span></a>            <span class="k">if</span> <span class="n">coroutines</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">res</span><span class="p">):</span>
</span><span id="UdpStreamReaderProtocol-726"><a href="#UdpStreamReaderProtocol-726"><span class="linenos">726</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">res</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol-727"><a href="#UdpStreamReaderProtocol-727"><span class="linenos">727</span></a>            
</span><span id="UdpStreamReaderProtocol-728"><a href="#UdpStreamReaderProtocol-728"><span class="linenos">728</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_strong_reader</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


            <div class="docstring"><p>Helper class to adapt between Protocol and StreamReader.</p>

<p>(This is a helper class instead of making StreamReader itself a
Protocol subclass, because the StreamReader has other potential
uses, and to prevent the user of the StreamReader to accidentally
call inappropriate methods of the protocol.)</p>
</div>


                            <div id="UdpStreamReaderProtocol.__init__" class="classattr">
                                        <input id="UdpStreamReaderProtocol.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">UdpStreamReaderProtocol</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">manager</span><span class="p">:</span> <span class="n"><a href="#UdpStreamManager">UdpStreamManager</a></span>,</span><span class="param">	<span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">asyncio</span><span class="o">.</span><span class="n">efficient_streams</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">efficient_streams_base_internal</span><span class="o">.</span><span class="n">MessageProtocolSettings</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="UdpStreamReaderProtocol.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReaderProtocol.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReaderProtocol.__init__-695"><a href="#UdpStreamReaderProtocol.__init__-695"><span class="linenos">695</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol.__init__-696"><a href="#UdpStreamReaderProtocol.__init__-696"><span class="linenos">696</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="UdpStreamReaderProtocol.__init__-697"><a href="#UdpStreamReaderProtocol.__init__-697"><span class="linenos">697</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="UdpStreamReaderProtocol.__init__-698"><a href="#UdpStreamReaderProtocol.__init__-698"><span class="linenos">698</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamReaderProtocol.connection_made" class="classattr">
                                        <input id="UdpStreamReaderProtocol.connection_made-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">connection_made</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">transport</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamReaderProtocol.connection_made-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamReaderProtocol.connection_made"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamReaderProtocol.connection_made-700"><a href="#UdpStreamReaderProtocol.connection_made-700"><span class="linenos">700</span></a>    <span class="k">def</span> <span class="nf">connection_made</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="UdpStreamReaderProtocol.connection_made-701"><a href="#UdpStreamReaderProtocol.connection_made-701"><span class="linenos">701</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reject_connection</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol.connection_made-702"><a href="#UdpStreamReaderProtocol.connection_made-702"><span class="linenos">702</span></a>            <span class="n">context</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="UdpStreamReaderProtocol.connection_made-703"><a href="#UdpStreamReaderProtocol.connection_made-703"><span class="linenos">703</span></a>                <span class="s1">&#39;message&#39;</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;An open stream was garbage collected prior to &#39;</span>
</span><span id="UdpStreamReaderProtocol.connection_made-704"><a href="#UdpStreamReaderProtocol.connection_made-704"><span class="linenos">704</span></a>                            <span class="s1">&#39;establishing network connection; &#39;</span>
</span><span id="UdpStreamReaderProtocol.connection_made-705"><a href="#UdpStreamReaderProtocol.connection_made-705"><span class="linenos">705</span></a>                            <span class="s1">&#39;call &quot;stream.close()&quot; explicitly.&#39;</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol.connection_made-706"><a href="#UdpStreamReaderProtocol.connection_made-706"><span class="linenos">706</span></a>            <span class="p">}</span>
</span><span id="UdpStreamReaderProtocol.connection_made-707"><a href="#UdpStreamReaderProtocol.connection_made-707"><span class="linenos">707</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol.connection_made-708"><a href="#UdpStreamReaderProtocol.connection_made-708"><span class="linenos">708</span></a>                <span class="n">context</span><span class="p">[</span><span class="s1">&#39;source_traceback&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span>
</span><span id="UdpStreamReaderProtocol.connection_made-709"><a href="#UdpStreamReaderProtocol.connection_made-709"><span class="linenos">709</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">call_exception_handler</span><span class="p">(</span><span class="n">context</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol.connection_made-710"><a href="#UdpStreamReaderProtocol.connection_made-710"><span class="linenos">710</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">abort</span><span class="p">()</span>
</span><span id="UdpStreamReaderProtocol.connection_made-711"><a href="#UdpStreamReaderProtocol.connection_made-711"><span class="linenos">711</span></a>            <span class="k">return</span>
</span><span id="UdpStreamReaderProtocol.connection_made-712"><a href="#UdpStreamReaderProtocol.connection_made-712"><span class="linenos">712</span></a>        
</span><span id="UdpStreamReaderProtocol.connection_made-713"><a href="#UdpStreamReaderProtocol.connection_made-713"><span class="linenos">713</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="n">transport</span>
</span><span id="UdpStreamReaderProtocol.connection_made-714"><a href="#UdpStreamReaderProtocol.connection_made-714"><span class="linenos">714</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_reader</span>
</span><span id="UdpStreamReaderProtocol.connection_made-715"><a href="#UdpStreamReaderProtocol.connection_made-715"><span class="linenos">715</span></a>        <span class="k">if</span> <span class="n">reader</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol.connection_made-716"><a href="#UdpStreamReaderProtocol.connection_made-716"><span class="linenos">716</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">set_transport</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol.connection_made-717"><a href="#UdpStreamReaderProtocol.connection_made-717"><span class="linenos">717</span></a>
</span><span id="UdpStreamReaderProtocol.connection_made-718"><a href="#UdpStreamReaderProtocol.connection_made-718"><span class="linenos">718</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_over_ssl</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">get_extra_info</span><span class="p">(</span><span class="s1">&#39;sslcontext&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</span><span id="UdpStreamReaderProtocol.connection_made-719"><a href="#UdpStreamReaderProtocol.connection_made-719"><span class="linenos">719</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamReaderProtocol.connection_made-720"><a href="#UdpStreamReaderProtocol.connection_made-720"><span class="linenos">720</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span> <span class="o">=</span> <span class="n">UdpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span>
</span><span id="UdpStreamReaderProtocol.connection_made-721"><a href="#UdpStreamReaderProtocol.connection_made-721"><span class="linenos">721</span></a>                                               <span class="n">reader</span><span class="p">,</span>
</span><span id="UdpStreamReaderProtocol.connection_made-722"><a href="#UdpStreamReaderProtocol.connection_made-722"><span class="linenos">722</span></a>                                               <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol.connection_made-723"><a href="#UdpStreamReaderProtocol.connection_made-723"><span class="linenos">723</span></a>            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span><span class="p">(</span><span class="n">reader</span><span class="p">,</span>
</span><span id="UdpStreamReaderProtocol.connection_made-724"><a href="#UdpStreamReaderProtocol.connection_made-724"><span class="linenos">724</span></a>                                            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol.connection_made-725"><a href="#UdpStreamReaderProtocol.connection_made-725"><span class="linenos">725</span></a>            <span class="k">if</span> <span class="n">coroutines</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">res</span><span class="p">):</span>
</span><span id="UdpStreamReaderProtocol.connection_made-726"><a href="#UdpStreamReaderProtocol.connection_made-726"><span class="linenos">726</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">res</span><span class="p">)</span>
</span><span id="UdpStreamReaderProtocol.connection_made-727"><a href="#UdpStreamReaderProtocol.connection_made-727"><span class="linenos">727</span></a>            
</span><span id="UdpStreamReaderProtocol.connection_made-728"><a href="#UdpStreamReaderProtocol.connection_made-728"><span class="linenos">728</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_strong_reader</span> <span class="o">=</span> <span class="kc">None</span>
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
                                <dd id="UdpStreamReaderProtocol.connection_lost" class="function">connection_lost</dd>
                <dd id="UdpStreamReaderProtocol.data_received" class="function">data_received</dd>
                <dd id="UdpStreamReaderProtocol.eof_received" class="function">eof_received</dd>

            </div>
            <div><dt>asyncio.streams.FlowControlMixin</dt>
                                <dd id="UdpStreamReaderProtocol.pause_writing" class="function">pause_writing</dd>
                <dd id="UdpStreamReaderProtocol.resume_writing" class="function">resume_writing</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="UdpStreamWriter">
                            <input id="UdpStreamWriter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UdpStreamWriter</span><wbr>(<span class="base">asyncio.streams.StreamWriter</span>, <span class="base">cengal.parallel_execution.asyncio.efficient_streams.versions.v_0.efficient_streams_abstract.StreamWriterAbstract</span>):

                <label class="view-source-button" for="UdpStreamWriter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter-731"><a href="#UdpStreamWriter-731"><span class="linenos">731</span></a><span class="k">class</span> <span class="nc">UdpStreamWriter</span><span class="p">(</span><span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="n">StreamWriterAbstract</span><span class="p">):</span>
</span><span id="UdpStreamWriter-732"><a href="#UdpStreamWriter-732"><span class="linenos">732</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamWriter-733"><a href="#UdpStreamWriter-733"><span class="linenos">733</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="UdpStreamWriter-734"><a href="#UdpStreamWriter-734"><span class="linenos">734</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_stream_manager</span>
</span><span id="UdpStreamWriter-735"><a href="#UdpStreamWriter-735"><span class="linenos">735</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">output_to_client_container_type</span><span class="p">(</span>
</span><span id="UdpStreamWriter-736"><a href="#UdpStreamWriter-736"><span class="linenos">736</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_out__data_full_size</span><span class="p">)</span>
</span><span id="UdpStreamWriter-737"><a href="#UdpStreamWriter-737"><span class="linenos">737</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="p">:</span> <span class="n">ValueExistence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span>
</span><span id="UdpStreamWriter-738"><a href="#UdpStreamWriter-738"><span class="linenos">738</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">:</span> <span class="n">Task</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="UdpStreamWriter-739"><a href="#UdpStreamWriter-739"><span class="linenos">739</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="UdpStreamWriter-740"><a href="#UdpStreamWriter-740"><span class="linenos">740</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Future</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="UdpStreamWriter-741"><a href="#UdpStreamWriter-741"><span class="linenos">741</span></a>    
</span><span id="UdpStreamWriter-742"><a href="#UdpStreamWriter-742"><span class="linenos">742</span></a>    <span class="k">def</span> <span class="nf">optimized_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter-743"><a href="#UdpStreamWriter-743"><span class="linenos">743</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamWriter-744"><a href="#UdpStreamWriter-744"><span class="linenos">744</span></a>        <span class="c1"># self.write(data)</span>
</span><span id="UdpStreamWriter-745"><a href="#UdpStreamWriter-745"><span class="linenos">745</span></a>
</span><span id="UdpStreamWriter-746"><a href="#UdpStreamWriter-746"><span class="linenos">746</span></a>    <span class="k">def</span> <span class="nf">owrite</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter-747"><a href="#UdpStreamWriter-747"><span class="linenos">747</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamWriter-748"><a href="#UdpStreamWriter-748"><span class="linenos">748</span></a>
</span><span id="UdpStreamWriter-749"><a href="#UdpStreamWriter-749"><span class="linenos">749</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">partial_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-750"><a href="#UdpStreamWriter-750"><span class="linenos">750</span></a>        <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="UdpStreamWriter-751"><a href="#UdpStreamWriter-751"><span class="linenos">751</span></a>        <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="UdpStreamWriter-752"><a href="#UdpStreamWriter-752"><span class="linenos">752</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="UdpStreamWriter-753"><a href="#UdpStreamWriter-753"><span class="linenos">753</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="UdpStreamWriter-754"><a href="#UdpStreamWriter-754"><span class="linenos">754</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="UdpStreamWriter-755"><a href="#UdpStreamWriter-755"><span class="linenos">755</span></a>
</span><span id="UdpStreamWriter-756"><a href="#UdpStreamWriter-756"><span class="linenos">756</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-757"><a href="#UdpStreamWriter-757"><span class="linenos">757</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_drain</span><span class="p">()</span>
</span><span id="UdpStreamWriter-758"><a href="#UdpStreamWriter-758"><span class="linenos">758</span></a>
</span><span id="UdpStreamWriter-759"><a href="#UdpStreamWriter-759"><span class="linenos">759</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">full_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-760"><a href="#UdpStreamWriter-760"><span class="linenos">760</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">pdrain</span><span class="p">()</span>
</span><span id="UdpStreamWriter-761"><a href="#UdpStreamWriter-761"><span class="linenos">761</span></a>        <span class="n">rest_of_the_data_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="UdpStreamWriter-762"><a href="#UdpStreamWriter-762"><span class="linenos">762</span></a>        <span class="k">if</span> <span class="n">rest_of_the_data_size</span><span class="p">:</span>
</span><span id="UdpStreamWriter-763"><a href="#UdpStreamWriter-763"><span class="linenos">763</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">rest_of_the_data_size</span><span class="p">)</span>
</span><span id="UdpStreamWriter-764"><a href="#UdpStreamWriter-764"><span class="linenos">764</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="UdpStreamWriter-765"><a href="#UdpStreamWriter-765"><span class="linenos">765</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="UdpStreamWriter-766"><a href="#UdpStreamWriter-766"><span class="linenos">766</span></a>
</span><span id="UdpStreamWriter-767"><a href="#UdpStreamWriter-767"><span class="linenos">767</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">fdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-768"><a href="#UdpStreamWriter-768"><span class="linenos">768</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="UdpStreamWriter-769"><a href="#UdpStreamWriter-769"><span class="linenos">769</span></a>    
</span><span id="UdpStreamWriter-770"><a href="#UdpStreamWriter-770"><span class="linenos">770</span></a>    <span class="k">def</span> <span class="nf">_release_autonomous_writer_waiters</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-771"><a href="#UdpStreamWriter-771"><span class="linenos">771</span></a>        <span class="n">current_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="UdpStreamWriter-772"><a href="#UdpStreamWriter-772"><span class="linenos">772</span></a>        <span class="n">autonomous_writer_drain_enough_futures_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span>
</span><span id="UdpStreamWriter-773"><a href="#UdpStreamWriter-773"><span class="linenos">773</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">autonomous_writer_drain_enough_futures_buff</span><span class="p">)()</span>
</span><span id="UdpStreamWriter-774"><a href="#UdpStreamWriter-774"><span class="linenos">774</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">autonomous_writer_drain_enough_futures_buff</span><span class="p">:</span>
</span><span id="UdpStreamWriter-775"><a href="#UdpStreamWriter-775"><span class="linenos">775</span></a>            <span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="UdpStreamWriter-776"><a href="#UdpStreamWriter-776"><span class="linenos">776</span></a>            <span class="k">if</span> <span class="n">current_size</span> <span class="o">&lt;</span> <span class="n">lower_water_size</span><span class="p">:</span>
</span><span id="UdpStreamWriter-777"><a href="#UdpStreamWriter-777"><span class="linenos">777</span></a>                <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">done</span><span class="p">())</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="UdpStreamWriter-778"><a href="#UdpStreamWriter-778"><span class="linenos">778</span></a>                    <span class="n">future</span><span class="o">.</span><span class="n">set_result</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="UdpStreamWriter-779"><a href="#UdpStreamWriter-779"><span class="linenos">779</span></a>
</span><span id="UdpStreamWriter-780"><a href="#UdpStreamWriter-780"><span class="linenos">780</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">done</span><span class="p">())</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="UdpStreamWriter-781"><a href="#UdpStreamWriter-781"><span class="linenos">781</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
</span><span id="UdpStreamWriter-782"><a href="#UdpStreamWriter-782"><span class="linenos">782</span></a>    
</span><span id="UdpStreamWriter-783"><a href="#UdpStreamWriter-783"><span class="linenos">783</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">_autonomous_writer_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-784"><a href="#UdpStreamWriter-784"><span class="linenos">784</span></a>        <span class="n">ty</span> <span class="o">=</span> <span class="n">TimedYield</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="UdpStreamWriter-785"><a href="#UdpStreamWriter-785"><span class="linenos">785</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span>
</span><span id="UdpStreamWriter-786"><a href="#UdpStreamWriter-786"><span class="linenos">786</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="UdpStreamWriter-787"><a href="#UdpStreamWriter-787"><span class="linenos">787</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_release_autonomous_writer_waiters</span><span class="p">()</span>
</span><span id="UdpStreamWriter-788"><a href="#UdpStreamWriter-788"><span class="linenos">788</span></a>            <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="UdpStreamWriter-789"><a href="#UdpStreamWriter-789"><span class="linenos">789</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="UdpStreamWriter-790"><a href="#UdpStreamWriter-790"><span class="linenos">790</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="UdpStreamWriter-791"><a href="#UdpStreamWriter-791"><span class="linenos">791</span></a>                <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="UdpStreamWriter-792"><a href="#UdpStreamWriter-792"><span class="linenos">792</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_release_autonomous_writer_waiters</span><span class="p">()</span>
</span><span id="UdpStreamWriter-793"><a href="#UdpStreamWriter-793"><span class="linenos">793</span></a>            
</span><span id="UdpStreamWriter-794"><a href="#UdpStreamWriter-794"><span class="linenos">794</span></a>            <span class="k">await</span> <span class="n">ty</span><span class="p">()</span>
</span><span id="UdpStreamWriter-795"><a href="#UdpStreamWriter-795"><span class="linenos">795</span></a>    
</span><span id="UdpStreamWriter-796"><a href="#UdpStreamWriter-796"><span class="linenos">796</span></a>    <span class="k">def</span> <span class="nf">start_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-797"><a href="#UdpStreamWriter-797"><span class="linenos">797</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_impl</span><span class="p">)</span>
</span><span id="UdpStreamWriter-798"><a href="#UdpStreamWriter-798"><span class="linenos">798</span></a>    
</span><span id="UdpStreamWriter-799"><a href="#UdpStreamWriter-799"><span class="linenos">799</span></a>    <span class="k">def</span> <span class="nf">start_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-800"><a href="#UdpStreamWriter-800"><span class="linenos">800</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span><span id="UdpStreamWriter-801"><a href="#UdpStreamWriter-801"><span class="linenos">801</span></a>    
</span><span id="UdpStreamWriter-802"><a href="#UdpStreamWriter-802"><span class="linenos">802</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="UdpStreamWriter-803"><a href="#UdpStreamWriter-803"><span class="linenos">803</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="UdpStreamWriter-804"><a href="#UdpStreamWriter-804"><span class="linenos">804</span></a>
</span><span id="UdpStreamWriter-805"><a href="#UdpStreamWriter-805"><span class="linenos">805</span></a><span class="sd">        Args:</span>
</span><span id="UdpStreamWriter-806"><a href="#UdpStreamWriter-806"><span class="linenos">806</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="UdpStreamWriter-807"><a href="#UdpStreamWriter-807"><span class="linenos">807</span></a>
</span><span id="UdpStreamWriter-808"><a href="#UdpStreamWriter-808"><span class="linenos">808</span></a><span class="sd">        Returns:</span>
</span><span id="UdpStreamWriter-809"><a href="#UdpStreamWriter-809"><span class="linenos">809</span></a><span class="sd">            _type_: _description_</span>
</span><span id="UdpStreamWriter-810"><a href="#UdpStreamWriter-810"><span class="linenos">810</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamWriter-811"><a href="#UdpStreamWriter-811"><span class="linenos">811</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="UdpStreamWriter-812"><a href="#UdpStreamWriter-812"><span class="linenos">812</span></a>        <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamWriter-813"><a href="#UdpStreamWriter-813"><span class="linenos">813</span></a>            <span class="n">timeout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span>
</span><span id="UdpStreamWriter-814"><a href="#UdpStreamWriter-814"><span class="linenos">814</span></a>        
</span><span id="UdpStreamWriter-815"><a href="#UdpStreamWriter-815"><span class="linenos">815</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">):</span>
</span><span id="UdpStreamWriter-816"><a href="#UdpStreamWriter-816"><span class="linenos">816</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="UdpStreamWriter-817"><a href="#UdpStreamWriter-817"><span class="linenos">817</span></a>            <span class="k">if</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="UdpStreamWriter-818"><a href="#UdpStreamWriter-818"><span class="linenos">818</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">wait_for</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>
</span><span id="UdpStreamWriter-819"><a href="#UdpStreamWriter-819"><span class="linenos">819</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamWriter-820"><a href="#UdpStreamWriter-820"><span class="linenos">820</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span>
</span><span id="UdpStreamWriter-821"><a href="#UdpStreamWriter-821"><span class="linenos">821</span></a>            
</span><span id="UdpStreamWriter-822"><a href="#UdpStreamWriter-822"><span class="linenos">822</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="UdpStreamWriter-823"><a href="#UdpStreamWriter-823"><span class="linenos">823</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="UdpStreamWriter-824"><a href="#UdpStreamWriter-824"><span class="linenos">824</span></a>        
</span><span id="UdpStreamWriter-825"><a href="#UdpStreamWriter-825"><span class="linenos">825</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="UdpStreamWriter-826"><a href="#UdpStreamWriter-826"><span class="linenos">826</span></a>    
</span><span id="UdpStreamWriter-827"><a href="#UdpStreamWriter-827"><span class="linenos">827</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="UdpStreamWriter-828"><a href="#UdpStreamWriter-828"><span class="linenos">828</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="UdpStreamWriter-829"><a href="#UdpStreamWriter-829"><span class="linenos">829</span></a>
</span><span id="UdpStreamWriter-830"><a href="#UdpStreamWriter-830"><span class="linenos">830</span></a><span class="sd">        Args:</span>
</span><span id="UdpStreamWriter-831"><a href="#UdpStreamWriter-831"><span class="linenos">831</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="UdpStreamWriter-832"><a href="#UdpStreamWriter-832"><span class="linenos">832</span></a>
</span><span id="UdpStreamWriter-833"><a href="#UdpStreamWriter-833"><span class="linenos">833</span></a><span class="sd">        Returns:</span>
</span><span id="UdpStreamWriter-834"><a href="#UdpStreamWriter-834"><span class="linenos">834</span></a><span class="sd">            _type_: _description_</span>
</span><span id="UdpStreamWriter-835"><a href="#UdpStreamWriter-835"><span class="linenos">835</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamWriter-836"><a href="#UdpStreamWriter-836"><span class="linenos">836</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
</span><span id="UdpStreamWriter-837"><a href="#UdpStreamWriter-837"><span class="linenos">837</span></a>    
</span><span id="UdpStreamWriter-838"><a href="#UdpStreamWriter-838"><span class="linenos">838</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lower_water_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="UdpStreamWriter-839"><a href="#UdpStreamWriter-839"><span class="linenos">839</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamWriter-840"><a href="#UdpStreamWriter-840"><span class="linenos">840</span></a>            <span class="n">lower_water_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span> <span class="o">*</span> <span class="mi">3</span>
</span><span id="UdpStreamWriter-841"><a href="#UdpStreamWriter-841"><span class="linenos">841</span></a>            <span class="c1"># print(f&#39;lower_water_size: {lower_water_size}&#39;)</span>
</span><span id="UdpStreamWriter-842"><a href="#UdpStreamWriter-842"><span class="linenos">842</span></a>            <span class="c1"># lower_water_size = cpu_info().l3_cache_size</span>
</span><span id="UdpStreamWriter-843"><a href="#UdpStreamWriter-843"><span class="linenos">843</span></a>        
</span><span id="UdpStreamWriter-844"><a href="#UdpStreamWriter-844"><span class="linenos">844</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="UdpStreamWriter-845"><a href="#UdpStreamWriter-845"><span class="linenos">845</span></a>            <span class="n">future</span><span class="p">:</span> <span class="n">Future</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="UdpStreamWriter-846"><a href="#UdpStreamWriter-846"><span class="linenos">846</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span><span class="p">))</span>
</span><span id="UdpStreamWriter-847"><a href="#UdpStreamWriter-847"><span class="linenos">847</span></a>            <span class="k">await</span> <span class="n">future</span>
</span><span id="UdpStreamWriter-848"><a href="#UdpStreamWriter-848"><span class="linenos">848</span></a>    
</span><span id="UdpStreamWriter-849"><a href="#UdpStreamWriter-849"><span class="linenos">849</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aw_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter-850"><a href="#UdpStreamWriter-850"><span class="linenos">850</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_drain_enough</span><span class="p">()</span>
</span><span id="UdpStreamWriter-851"><a href="#UdpStreamWriter-851"><span class="linenos">851</span></a>    
</span><span id="UdpStreamWriter-852"><a href="#UdpStreamWriter-852"><span class="linenos">852</span></a>    <span class="k">def</span> <span class="nf">optimized_write_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter-853"><a href="#UdpStreamWriter-853"><span class="linenos">853</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamWriter-854"><a href="#UdpStreamWriter-854"><span class="linenos">854</span></a>    
</span><span id="UdpStreamWriter-855"><a href="#UdpStreamWriter-855"><span class="linenos">855</span></a>    <span class="k">def</span> <span class="nf">owrite_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter-856"><a href="#UdpStreamWriter-856"><span class="linenos">856</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamWriter-857"><a href="#UdpStreamWriter-857"><span class="linenos">857</span></a>    
</span><span id="UdpStreamWriter-858"><a href="#UdpStreamWriter-858"><span class="linenos">858</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">send_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter-859"><a href="#UdpStreamWriter-859"><span class="linenos">859</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamWriter-860"><a href="#UdpStreamWriter-860"><span class="linenos">860</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">fdrain</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Wraps a Transport.</p>

<p>This exposes write(), writelines(), [can_]write_eof(),
get_extra_info() and close().  It adds drain() which returns an
optional Future on which you can wait for flow control.  It also
adds a transport property which references the Transport
directly.</p>
</div>


                            <div id="UdpStreamWriter.__init__" class="classattr">
                                        <input id="UdpStreamWriter.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">UdpStreamWriter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="UdpStreamWriter.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.__init__-732"><a href="#UdpStreamWriter.__init__-732"><span class="linenos">732</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamWriter.__init__-733"><a href="#UdpStreamWriter.__init__-733"><span class="linenos">733</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="UdpStreamWriter.__init__-734"><a href="#UdpStreamWriter.__init__-734"><span class="linenos">734</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="p">:</span> <span class="n">UdpStreamManager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_stream_manager</span>
</span><span id="UdpStreamWriter.__init__-735"><a href="#UdpStreamWriter.__init__-735"><span class="linenos">735</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">output_to_client_container_type</span><span class="p">(</span>
</span><span id="UdpStreamWriter.__init__-736"><a href="#UdpStreamWriter.__init__-736"><span class="linenos">736</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_out__data_full_size</span><span class="p">)</span>
</span><span id="UdpStreamWriter.__init__-737"><a href="#UdpStreamWriter.__init__-737"><span class="linenos">737</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="p">:</span> <span class="n">ValueExistence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span>
</span><span id="UdpStreamWriter.__init__-738"><a href="#UdpStreamWriter.__init__-738"><span class="linenos">738</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">:</span> <span class="n">Task</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="UdpStreamWriter.__init__-739"><a href="#UdpStreamWriter.__init__-739"><span class="linenos">739</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="UdpStreamWriter.__init__-740"><a href="#UdpStreamWriter.__init__-740"><span class="linenos">740</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Future</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.socket_write_fixed_buffer_size" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_write_fixed_buffer_size</span><span class="annotation">: cengal.code_flow_control.smart_values.versions.v_2.smart_values.ValueExistence</span>

        
    </div>
    <a class="headerlink" href="#UdpStreamWriter.socket_write_fixed_buffer_size"></a>
    
    

                            </div>
                            <div id="UdpStreamWriter.optimized_write" class="classattr">
                                        <input id="UdpStreamWriter.optimized_write-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">optimized_write</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.optimized_write-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.optimized_write"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.optimized_write-742"><a href="#UdpStreamWriter.optimized_write-742"><span class="linenos">742</span></a>    <span class="k">def</span> <span class="nf">optimized_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter.optimized_write-743"><a href="#UdpStreamWriter.optimized_write-743"><span class="linenos">743</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamWriter.optimized_write-744"><a href="#UdpStreamWriter.optimized_write-744"><span class="linenos">744</span></a>        <span class="c1"># self.write(data)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.owrite" class="classattr">
                                        <input id="UdpStreamWriter.owrite-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">owrite</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.owrite-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.owrite"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.owrite-746"><a href="#UdpStreamWriter.owrite-746"><span class="linenos">746</span></a>    <span class="k">def</span> <span class="nf">owrite</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter.owrite-747"><a href="#UdpStreamWriter.owrite-747"><span class="linenos">747</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.partial_drain" class="classattr">
                                        <input id="UdpStreamWriter.partial_drain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">partial_drain</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.partial_drain-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.partial_drain"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.partial_drain-749"><a href="#UdpStreamWriter.partial_drain-749"><span class="linenos">749</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">partial_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter.partial_drain-750"><a href="#UdpStreamWriter.partial_drain-750"><span class="linenos">750</span></a>        <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="UdpStreamWriter.partial_drain-751"><a href="#UdpStreamWriter.partial_drain-751"><span class="linenos">751</span></a>        <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="UdpStreamWriter.partial_drain-752"><a href="#UdpStreamWriter.partial_drain-752"><span class="linenos">752</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="UdpStreamWriter.partial_drain-753"><a href="#UdpStreamWriter.partial_drain-753"><span class="linenos">753</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="UdpStreamWriter.partial_drain-754"><a href="#UdpStreamWriter.partial_drain-754"><span class="linenos">754</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.pdrain" class="classattr">
                                        <input id="UdpStreamWriter.pdrain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">pdrain</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.pdrain-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.pdrain"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.pdrain-756"><a href="#UdpStreamWriter.pdrain-756"><span class="linenos">756</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter.pdrain-757"><a href="#UdpStreamWriter.pdrain-757"><span class="linenos">757</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_drain</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.full_drain" class="classattr">
                                        <input id="UdpStreamWriter.full_drain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">full_drain</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.full_drain-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.full_drain"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.full_drain-759"><a href="#UdpStreamWriter.full_drain-759"><span class="linenos">759</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">full_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter.full_drain-760"><a href="#UdpStreamWriter.full_drain-760"><span class="linenos">760</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">pdrain</span><span class="p">()</span>
</span><span id="UdpStreamWriter.full_drain-761"><a href="#UdpStreamWriter.full_drain-761"><span class="linenos">761</span></a>        <span class="n">rest_of_the_data_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="UdpStreamWriter.full_drain-762"><a href="#UdpStreamWriter.full_drain-762"><span class="linenos">762</span></a>        <span class="k">if</span> <span class="n">rest_of_the_data_size</span><span class="p">:</span>
</span><span id="UdpStreamWriter.full_drain-763"><a href="#UdpStreamWriter.full_drain-763"><span class="linenos">763</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">rest_of_the_data_size</span><span class="p">)</span>
</span><span id="UdpStreamWriter.full_drain-764"><a href="#UdpStreamWriter.full_drain-764"><span class="linenos">764</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="UdpStreamWriter.full_drain-765"><a href="#UdpStreamWriter.full_drain-765"><span class="linenos">765</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.fdrain" class="classattr">
                                        <input id="UdpStreamWriter.fdrain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">fdrain</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.fdrain-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.fdrain"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.fdrain-767"><a href="#UdpStreamWriter.fdrain-767"><span class="linenos">767</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">fdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter.fdrain-768"><a href="#UdpStreamWriter.fdrain-768"><span class="linenos">768</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.start_autonomous_writer" class="classattr">
                                        <input id="UdpStreamWriter.start_autonomous_writer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start_autonomous_writer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.start_autonomous_writer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.start_autonomous_writer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.start_autonomous_writer-796"><a href="#UdpStreamWriter.start_autonomous_writer-796"><span class="linenos">796</span></a>    <span class="k">def</span> <span class="nf">start_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter.start_autonomous_writer-797"><a href="#UdpStreamWriter.start_autonomous_writer-797"><span class="linenos">797</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.start_aw" class="classattr">
                                        <input id="UdpStreamWriter.start_aw-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start_aw</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.start_aw-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.start_aw"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.start_aw-799"><a href="#UdpStreamWriter.start_aw-799"><span class="linenos">799</span></a>    <span class="k">def</span> <span class="nf">start_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter.start_aw-800"><a href="#UdpStreamWriter.start_aw-800"><span class="linenos">800</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.stop_autonomous_writer" class="classattr">
                                        <input id="UdpStreamWriter.stop_autonomous_writer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">stop_autonomous_writer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.stop_autonomous_writer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.stop_autonomous_writer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.stop_autonomous_writer-802"><a href="#UdpStreamWriter.stop_autonomous_writer-802"><span class="linenos">802</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-803"><a href="#UdpStreamWriter.stop_autonomous_writer-803"><span class="linenos">803</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-804"><a href="#UdpStreamWriter.stop_autonomous_writer-804"><span class="linenos">804</span></a>
</span><span id="UdpStreamWriter.stop_autonomous_writer-805"><a href="#UdpStreamWriter.stop_autonomous_writer-805"><span class="linenos">805</span></a><span class="sd">        Args:</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-806"><a href="#UdpStreamWriter.stop_autonomous_writer-806"><span class="linenos">806</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-807"><a href="#UdpStreamWriter.stop_autonomous_writer-807"><span class="linenos">807</span></a>
</span><span id="UdpStreamWriter.stop_autonomous_writer-808"><a href="#UdpStreamWriter.stop_autonomous_writer-808"><span class="linenos">808</span></a><span class="sd">        Returns:</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-809"><a href="#UdpStreamWriter.stop_autonomous_writer-809"><span class="linenos">809</span></a><span class="sd">            _type_: _description_</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-810"><a href="#UdpStreamWriter.stop_autonomous_writer-810"><span class="linenos">810</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-811"><a href="#UdpStreamWriter.stop_autonomous_writer-811"><span class="linenos">811</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-812"><a href="#UdpStreamWriter.stop_autonomous_writer-812"><span class="linenos">812</span></a>        <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-813"><a href="#UdpStreamWriter.stop_autonomous_writer-813"><span class="linenos">813</span></a>            <span class="n">timeout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-814"><a href="#UdpStreamWriter.stop_autonomous_writer-814"><span class="linenos">814</span></a>        
</span><span id="UdpStreamWriter.stop_autonomous_writer-815"><a href="#UdpStreamWriter.stop_autonomous_writer-815"><span class="linenos">815</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">):</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-816"><a href="#UdpStreamWriter.stop_autonomous_writer-816"><span class="linenos">816</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-817"><a href="#UdpStreamWriter.stop_autonomous_writer-817"><span class="linenos">817</span></a>            <span class="k">if</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-818"><a href="#UdpStreamWriter.stop_autonomous_writer-818"><span class="linenos">818</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">wait_for</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-819"><a href="#UdpStreamWriter.stop_autonomous_writer-819"><span class="linenos">819</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-820"><a href="#UdpStreamWriter.stop_autonomous_writer-820"><span class="linenos">820</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-821"><a href="#UdpStreamWriter.stop_autonomous_writer-821"><span class="linenos">821</span></a>            
</span><span id="UdpStreamWriter.stop_autonomous_writer-822"><a href="#UdpStreamWriter.stop_autonomous_writer-822"><span class="linenos">822</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-823"><a href="#UdpStreamWriter.stop_autonomous_writer-823"><span class="linenos">823</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="UdpStreamWriter.stop_autonomous_writer-824"><a href="#UdpStreamWriter.stop_autonomous_writer-824"><span class="linenos">824</span></a>        
</span><span id="UdpStreamWriter.stop_autonomous_writer-825"><a href="#UdpStreamWriter.stop_autonomous_writer-825"><span class="linenos">825</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>_summary_</p>

<p>Args:
    timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</p>

<p>Returns:
    _type_: _description_</p>
</div>


                            </div>
                            <div id="UdpStreamWriter.stop_aw" class="classattr">
                                        <input id="UdpStreamWriter.stop_aw-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">stop_aw</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.stop_aw-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.stop_aw"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.stop_aw-827"><a href="#UdpStreamWriter.stop_aw-827"><span class="linenos">827</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="UdpStreamWriter.stop_aw-828"><a href="#UdpStreamWriter.stop_aw-828"><span class="linenos">828</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="UdpStreamWriter.stop_aw-829"><a href="#UdpStreamWriter.stop_aw-829"><span class="linenos">829</span></a>
</span><span id="UdpStreamWriter.stop_aw-830"><a href="#UdpStreamWriter.stop_aw-830"><span class="linenos">830</span></a><span class="sd">        Args:</span>
</span><span id="UdpStreamWriter.stop_aw-831"><a href="#UdpStreamWriter.stop_aw-831"><span class="linenos">831</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="UdpStreamWriter.stop_aw-832"><a href="#UdpStreamWriter.stop_aw-832"><span class="linenos">832</span></a>
</span><span id="UdpStreamWriter.stop_aw-833"><a href="#UdpStreamWriter.stop_aw-833"><span class="linenos">833</span></a><span class="sd">        Returns:</span>
</span><span id="UdpStreamWriter.stop_aw-834"><a href="#UdpStreamWriter.stop_aw-834"><span class="linenos">834</span></a><span class="sd">            _type_: _description_</span>
</span><span id="UdpStreamWriter.stop_aw-835"><a href="#UdpStreamWriter.stop_aw-835"><span class="linenos">835</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="UdpStreamWriter.stop_aw-836"><a href="#UdpStreamWriter.stop_aw-836"><span class="linenos">836</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>_summary_</p>

<p>Args:
    timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</p>

<p>Returns:
    _type_: _description_</p>
</div>


                            </div>
                            <div id="UdpStreamWriter.autonomous_writer_drain_enough" class="classattr">
                                        <input id="UdpStreamWriter.autonomous_writer_drain_enough-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">autonomous_writer_drain_enough</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">lower_water_size</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.autonomous_writer_drain_enough-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.autonomous_writer_drain_enough"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.autonomous_writer_drain_enough-838"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-838"><span class="linenos">838</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lower_water_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-839"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-839"><span class="linenos">839</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-840"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-840"><span class="linenos">840</span></a>            <span class="n">lower_water_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span> <span class="o">*</span> <span class="mi">3</span>
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-841"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-841"><span class="linenos">841</span></a>            <span class="c1"># print(f&#39;lower_water_size: {lower_water_size}&#39;)</span>
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-842"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-842"><span class="linenos">842</span></a>            <span class="c1"># lower_water_size = cpu_info().l3_cache_size</span>
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-843"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-843"><span class="linenos">843</span></a>        
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-844"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-844"><span class="linenos">844</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-845"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-845"><span class="linenos">845</span></a>            <span class="n">future</span><span class="p">:</span> <span class="n">Future</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-846"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-846"><span class="linenos">846</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span><span class="p">))</span>
</span><span id="UdpStreamWriter.autonomous_writer_drain_enough-847"><a href="#UdpStreamWriter.autonomous_writer_drain_enough-847"><span class="linenos">847</span></a>            <span class="k">await</span> <span class="n">future</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.aw_drain_enough" class="classattr">
                                        <input id="UdpStreamWriter.aw_drain_enough-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aw_drain_enough</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.aw_drain_enough-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.aw_drain_enough"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.aw_drain_enough-849"><a href="#UdpStreamWriter.aw_drain_enough-849"><span class="linenos">849</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aw_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UdpStreamWriter.aw_drain_enough-850"><a href="#UdpStreamWriter.aw_drain_enough-850"><span class="linenos">850</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_drain_enough</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.optimized_write_message" class="classattr">
                                        <input id="UdpStreamWriter.optimized_write_message-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">optimized_write_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.optimized_write_message-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.optimized_write_message"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.optimized_write_message-852"><a href="#UdpStreamWriter.optimized_write_message-852"><span class="linenos">852</span></a>    <span class="k">def</span> <span class="nf">optimized_write_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter.optimized_write_message-853"><a href="#UdpStreamWriter.optimized_write_message-853"><span class="linenos">853</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">_message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.owrite_message" class="classattr">
                                        <input id="UdpStreamWriter.owrite_message-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">owrite_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.owrite_message-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.owrite_message"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.owrite_message-855"><a href="#UdpStreamWriter.owrite_message-855"><span class="linenos">855</span></a>    <span class="k">def</span> <span class="nf">owrite_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter.owrite_message-856"><a href="#UdpStreamWriter.owrite_message-856"><span class="linenos">856</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UdpStreamWriter.send_message" class="classattr">
                                        <input id="UdpStreamWriter.send_message-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">send_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="UdpStreamWriter.send_message-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UdpStreamWriter.send_message"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UdpStreamWriter.send_message-858"><a href="#UdpStreamWriter.send_message-858"><span class="linenos">858</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">send_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="UdpStreamWriter.send_message-859"><a href="#UdpStreamWriter.send_message-859"><span class="linenos">859</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="UdpStreamWriter.send_message-860"><a href="#UdpStreamWriter.send_message-860"><span class="linenos">860</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">fdrain</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>asyncio.streams.StreamWriter</dt>
                                <dd id="UdpStreamWriter.transport" class="variable">transport</dd>
                <dd id="UdpStreamWriter.write" class="function">write</dd>
                <dd id="UdpStreamWriter.writelines" class="function">writelines</dd>
                <dd id="UdpStreamWriter.write_eof" class="function">write_eof</dd>
                <dd id="UdpStreamWriter.can_write_eof" class="function">can_write_eof</dd>
                <dd id="UdpStreamWriter.close" class="function">close</dd>
                <dd id="UdpStreamWriter.is_closing" class="function">is_closing</dd>
                <dd id="UdpStreamWriter.wait_closed" class="function">wait_closed</dd>
                <dd id="UdpStreamWriter.get_extra_info" class="function">get_extra_info</dd>
                <dd id="UdpStreamWriter.drain" class="function">drain</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>