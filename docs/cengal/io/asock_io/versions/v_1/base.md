---
title: base
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.io<wbr>.asock_io<wbr>.versions<wbr>.v_1<wbr>.base    </h1>

                
                        <input id="mod-base-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-base-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="kn">import</span> <span class="nn">errno</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">import</span> <span class="nn">socket</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="kn">from</span> <span class="nn">cengal.base.classes</span> <span class="kn">import</span> <span class="n">BaseClassSettings</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values.versions.v_0</span> <span class="kn">import</span> <span class="n">ResultExistence</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">from</span> <span class="nn">cengal.data_containers.dynamic_list_of_pieces</span> <span class="kn">import</span> \
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>    <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">cengal.data_containers.fast_fifo</span> <span class="kn">import</span> <span class="n">FIFODequeWithLengthControl</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">from</span> <span class="nn">cengal.hardware.info.cpu.versions.v_0</span> <span class="kn">import</span> <span class="n">l2_cache_per_core</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">from</span> <span class="nn">.abstract</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">from</span> <span class="nn">.recv_buff_size_computer</span> <span class="kn">import</span> <span class="n">RecvBuffSizeComputer</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="sd">Module Docstring</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">SET_OF_CONNECTION_ERRORS</span> <span class="o">=</span> <span class="p">{</span><span class="n">errno</span><span class="o">.</span><span class="n">ECONNRESET</span><span class="p">,</span> <span class="n">errno</span><span class="o">.</span><span class="n">ECONNREFUSED</span><span class="p">,</span> <span class="n">errno</span><span class="o">.</span><span class="n">ECONNABORTED</span><span class="p">,</span> <span class="n">errno</span><span class="o">.</span><span class="n">EPIPE</span><span class="p">,</span> <span class="n">errno</span><span class="o">.</span><span class="n">ESHUTDOWN</span><span class="p">}</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">INET_TYPE_CONNECTIONS</span> <span class="o">=</span> <span class="p">{</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">AF_INET6</span><span class="p">}</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="ne">BlockingIOError</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="k">class</span> <span class="nc">BlockingIOError</span><span class="p">(</span><span class="ne">OSError</span><span class="p">):</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>        <span class="k">pass</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="ne">InterruptedError</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="k">class</span> <span class="nc">InterruptedError</span><span class="p">(</span><span class="ne">OSError</span><span class="p">):</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="k">pass</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="ne">ConnectionError</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="k">class</span> <span class="nc">ConnectionError</span><span class="p">(</span><span class="ne">OSError</span><span class="p">):</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="k">pass</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="ne">BrokenPipeError</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="k">class</span> <span class="nc">BrokenPipeError</span><span class="p">(</span><span class="ne">ConnectionError</span><span class="p">):</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="k">pass</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="ne">ConnectionAbortedError</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="k">class</span> <span class="nc">ConnectionAbortedError</span><span class="p">(</span><span class="ne">ConnectionError</span><span class="p">):</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="k">pass</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="ne">ConnectionRefusedError</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>    <span class="k">class</span> <span class="nc">ConnectionRefusedError</span><span class="p">(</span><span class="ne">ConnectionError</span><span class="p">):</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="k">pass</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    <span class="ne">ConnectionResetError</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="k">class</span> <span class="nc">ConnectionResetError</span><span class="p">(</span><span class="ne">ConnectionError</span><span class="p">):</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="k">pass</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="k">class</span> <span class="nc">InternalNotCriticalError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>    <span class="k">pass</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a><span class="n">MESSAGE_SIZE_LEN</span> <span class="o">=</span> <span class="mi">8</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a><span class="n">SERVER_ANSWER__KEYWORD_ACCEPTED</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;OK&#39;</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a><span class="k">class</span> <span class="nc">SimpleNetworkError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="k">pass</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a><span class="k">class</span> <span class="nc">ConnectionSettings</span><span class="p">(</span><span class="n">BaseClassSettings</span><span class="p">):</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>                 <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>                 <span class="n">non_socket_connection_settings</span><span class="p">:</span> <span class="n">NonSocketConnectionSettings</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="sd">        :param connection_type: ConnectionType()</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a><span class="sd">        :param socket_address: &#39;./main.server.AF_UNIX.socket&#39;, (&#39;localhost&#39;, 8080), (&#39;::&#39;, 50007, 0, 0), , ect.</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a><span class="sd">        :param keyword: b&#39;sdlkfj s894 saf 84ewksdhf sdf&#39;. Can be None for a Super Server</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a><span class="sd">        :param socket_family: AF_INET (the default), AF_INET6, AF_UNIX, AF_CAN or AF_RDS</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="sd">        :param socket_type: SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a><span class="sd">        :param socket_protocol: in the case where the address family is AF_CAN the protocol should be one of CAN_RAW or</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="sd">            CAN_BCM</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="sd">        :param socket_fileno: If fileno is specified, the other arguments are ignored, causing the socket with the</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a><span class="sd">            specified file descriptor to return</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="n">keyword</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">non_socket_connection_settings</span> <span class="o">=</span> <span class="n">non_socket_connection_settings</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_clients_with_empty_output_fifo</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a><span class="k">class</span> <span class="nc">IOCoreMemoryManagement</span><span class="p">:</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global__data_size_limit</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">2</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">3</span><span class="p">)</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_size_limit</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">512</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_full_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__deletable_data_full_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_size_limit</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">512</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_full_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__deletable_data_full_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="nf">link_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">):</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global__data_size_limit</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__data_size_limit</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__data_full_size</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__deletable_data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__deletable_data_full_size</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__data_size_limit</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__data_full_size</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__deletable_data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__deletable_data_full_size</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a><span class="k">class</span> <span class="nc">ASockIOCoreMemoryManagement</span><span class="p">(</span><span class="n">IOCoreMemoryManagement</span><span class="p">):</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ASockIOCoreMemoryManagement</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_read_fixed_buffer_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>                                                             <span class="nb">int</span><span class="p">(</span><span class="n">l2_cache_per_core</span><span class="p">()</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span> <span class="ow">or</span> <span class="mi">1024</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="c1"># 1024**2 is the fastest fixed read buffer on my CPU.</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="c1"># Also ingeneral, it should be the half of the CPU cache per core (UPD: I don&#39;t remember why. Maybe to save other memory to instructions when we are dealing with big amount of connections).</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>        <span class="c1">#</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>        <span class="c1"># My CPU is Intel Core i5 3570:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="c1"># Architecture	x86-64</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="c1"># Threads	4 threads</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="c1"># L2 cache	1 MB</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="c1"># L2 cache per core	0.25 MB/core</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="c1"># L3 cache	6 MB</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="c1"># L3 cache per core	1.5 MB/core</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">link_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">):</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ASockIOCoreMemoryManagement</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">link_to</span><span class="p">(</span><span class="n">parent</span><span class="p">)</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">socket_read_fixed_buffer_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">socket_read_fixed_buffer_size</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>            <span class="k">pass</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a><span class="k">class</span> <span class="nc">Connection</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>                 <span class="n">connection_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>                 <span class="n">connection_settings</span><span class="p">:</span> <span class="n">ConnectionSettings</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>                 <span class="n">connection__conn_addr</span><span class="p">:</span> <span class="nb">tuple</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>                 <span class="n">global_memory_management</span><span class="p">:</span> <span class="n">ASockIOCoreMemoryManagement</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>                 <span class="p">):</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="sd">        :param connection_id: ID for this connection</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a><span class="sd">        :param connection__conn_addr: tuple(conn, addr) where conn is a socket, addr is an address</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a><span class="sd">        :param global_memory_management: global memory management obj</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span> <span class="o">=</span> <span class="n">connection_settings</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="k">if</span> <span class="n">connection__conn_addr</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">conn</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">addr</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">conn</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">connection__conn_addr</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">addr</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">connection__conn_addr</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span> <span class="o">=</span> <span class="n">RecvBuffSizeComputer</span><span class="p">()</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># socket should be closed immediately. For example because of IO error.</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ready_to_be_closed</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># socket should be closed, after all messages had been sent to client.</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ready_for_deletion</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># connection should be deleted immediately. For example because of unexpected</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="c1">#   keyword.</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_nbytes</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_message_nbytes</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raw_input_from_client</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span><span class="p">(</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_message_length</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># length of current input message (or None, if size waw not read yet)</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            <span class="n">external_data_full_size</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_output_memoryview</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="n">external_data_full_size</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_out__data_full_size</span><span class="p">)</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">this_is_raw_connection</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connected_expected_client_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connected_expected_client</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">has_inline_processor</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>    <span class="k">def</span> <span class="nf">calc_new_recv_buff_size</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">last_recv_amount</span><span class="p">):</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">last_recv_amount</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raw_input_from_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>    <span class="k">def</span> <span class="nf">add_data_to_output_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="k">pass</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="nf">add_data_to_input_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>        <span class="k">pass</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a><span class="k">class</span> <span class="nc">InlineProcessor</span><span class="p">(</span><span class="n">InlineWorkerBase</span><span class="p">):</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;client_id&#39;</span><span class="p">,</span> <span class="s1">&#39;keyword&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_family&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_type&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_proto&#39;</span><span class="p">,</span> <span class="s1">&#39;addr_info&#39;</span><span class="p">,</span> <span class="s1">&#39;host_names&#39;</span><span class="p">,</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>                 <span class="s1">&#39;is_in_raw_mode&#39;</span><span class="p">,</span> <span class="s1">&#39;__set__is_in_raw_mode&#39;</span><span class="p">,</span> <span class="s1">&#39;__set__mark_socket_as_should_be_closed_immediately&#39;</span><span class="p">,</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>                 <span class="s1">&#39;__set__mark_socket_as_ready_to_be_closed&#39;</span><span class="p">,</span> <span class="s1">&#39;__external_parameters_set_trigger&#39;</span><span class="p">,</span> <span class="s1">&#39;output_messages&#39;</span><span class="p">,</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>                 <span class="s1">&#39;__hold__client_id&#39;</span><span class="p">)</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">socket_family</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_type</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_proto</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>                 <span class="n">addr_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">host_names</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a><span class="sd">        :param keyword: client keyword. You may check for a known keywords to act appropriately</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a><span class="sd">        :param socket_family:</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a><span class="sd">        :param socket_type:</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a><span class="sd">        :param socket_proto:</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a><span class="sd">        :param addr_info: result of socket.getaddrinfo() call</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a><span class="sd">        :param host_names: result of socket.gethostbyaddr() call</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">InlineProcessor</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="n">keyword</span><span class="p">,</span> <span class="n">socket_family</span><span class="p">,</span> <span class="n">socket_type</span><span class="p">,</span> <span class="n">socket_proto</span><span class="p">,</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                                              <span class="n">addr_info</span><span class="p">,</span> <span class="n">host_names</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">)</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span> <span class="o">=</span> <span class="n">external_parameters_set_trigger</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>    <span class="k">def</span> <span class="nf">set__is_in_raw_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_in_raw_mode</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span> <span class="o">=</span> <span class="n">is_in_raw_mode</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_should_be_closed_immediately</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span> <span class="o">=</span> <span class="n">mark_socket_as</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_ready_to_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span> <span class="o">=</span> <span class="n">mark_socket_as</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_proto</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span><span class="p">,</span> \
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_in_raw_mode</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span><span class="p">,</span> \
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span><span class="p">,</span> \
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_messages</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_proto</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span><span class="p">,</span> \
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_in_raw_mode</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span><span class="p">,</span> \
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span><span class="p">,</span> \
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_messages</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="k">class</span> <span class="nc">Client</span><span class="p">:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_settings</span><span class="p">:</span> <span class="n">ConnectionSettings</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection_id</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot; Dasdfd safd</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a><span class="sd">        :param client_id: ID of the expected client</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a><span class="sd">        :param connection_id: ID of the connection</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a><span class="sd">        :param connection_settings: useful ConnectionSettings parameters are {connection_type, keyword} - for a client,</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a><span class="sd">            and all - for the super server.</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="c1"># self.__connection = None  # Нельзя! Потому что в этом случае, объект клиента станет несериализуемым</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__connection</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Можно! Сделаем сериализуемым через переопределение магических методов</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span> <span class="o">=</span> <span class="n">connection_settings</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_client_connection</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_connection_without_handshake</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">this_is_unknown_client</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">obj_for_inline_processing</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>        <span class="c1"># data_for_pickling = (</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>        <span class="c1">#     self.id,</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>        <span class="c1">#     self.connection_id,</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>        <span class="c1">#     self.connection_settings,</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        <span class="c1">#     self.will_use_raw_client_connection,</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="c1">#     self.will_use_raw_connection_without_handshake,</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>        <span class="c1">#     self.this_is_unknown_client,</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        <span class="c1">#     self.obj_for_inline_processing</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="c1"># )</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        <span class="c1"># return data_for_pickling</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> \
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span><span class="p">,</span> \
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span><span class="p">,</span> \
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_client_connection</span><span class="p">,</span> \
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_connection_without_handshake</span><span class="p">,</span> \
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">this_is_unknown_client</span><span class="p">,</span> \
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">obj_for_inline_processing</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data_after_unpickling</span><span class="p">):</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_client_connection</span><span class="p">,</span> \
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_connection_without_handshake</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">this_is_unknown_client</span><span class="p">,</span> \
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">obj_for_inline_processing</span> <span class="o">=</span> <span class="n">data_after_unpickling</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__connection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a><span class="k">class</span> <span class="nc">CheckIsRawConnection</span><span class="p">:</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asock_io_core</span><span class="p">:</span> <span class="s1">&#39;ASockIOCore&#39;</span><span class="p">,</span> <span class="n">connection_info</span><span class="p">:</span> <span class="n">Connection</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a><span class="sd">        :param asock_io_core:</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a><span class="sd">        :param connection_info:</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a><span class="sd">        :return: &quot;True&quot; if it is RAW connection for Unknow Client. &quot;False&quot; otherwise.</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>            <span class="k">if</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">conn</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">family</span> <span class="ow">in</span> <span class="p">{</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">AF_INET6</span><span class="p">}:</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>                <span class="k">if</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">addr</span><span class="o">.</span><span class="n">result</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">asock_io_core</span><span class="o">.</span><span class="n">set_of_gate_addresses</span><span class="p">:</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>                    <span class="c1"># If connected not from local IP address</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>            <span class="k">pass</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            </section>
                <section id="SET_OF_CONNECTION_ERRORS">
                    <div class="attr variable">
            <span class="name">SET_OF_CONNECTION_ERRORS</span>        =
<span class="default_value">{32, 103, 104, 108, 111}</span>

        
    </div>
    <a class="headerlink" href="#SET_OF_CONNECTION_ERRORS"></a>
    
    

                </section>
                <section id="INET_TYPE_CONNECTIONS">
                    <div class="attr variable">
            <span class="name">INET_TYPE_CONNECTIONS</span>        =
<span class="default_value">{&lt;AddressFamily.AF_INET: 2&gt;, &lt;AddressFamily.AF_INET6: 10&gt;}</span>

        
    </div>
    <a class="headerlink" href="#INET_TYPE_CONNECTIONS"></a>
    
    

                </section>
                <section id="InternalNotCriticalError">
                            <input id="InternalNotCriticalError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">InternalNotCriticalError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="InternalNotCriticalError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InternalNotCriticalError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InternalNotCriticalError-96"><a href="#InternalNotCriticalError-96"><span class="linenos">96</span></a><span class="k">class</span> <span class="nc">InternalNotCriticalError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="InternalNotCriticalError-97"><a href="#InternalNotCriticalError-97"><span class="linenos">97</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="InternalNotCriticalError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="InternalNotCriticalError.with_traceback" class="function">with_traceback</dd>
                <dd id="InternalNotCriticalError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="MESSAGE_SIZE_LEN">
                    <div class="attr variable">
            <span class="name">MESSAGE_SIZE_LEN</span>        =
<span class="default_value">8</span>

        
    </div>
    <a class="headerlink" href="#MESSAGE_SIZE_LEN"></a>
    
    

                </section>
                <section id="SERVER_ANSWER__KEYWORD_ACCEPTED">
                    <div class="attr variable">
            <span class="name">SERVER_ANSWER__KEYWORD_ACCEPTED</span>        =
<span class="default_value">b&#39;OK&#39;</span>

        
    </div>
    <a class="headerlink" href="#SERVER_ANSWER__KEYWORD_ACCEPTED"></a>
    
    

                </section>
                <section id="SimpleNetworkError">
                            <input id="SimpleNetworkError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SimpleNetworkError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="SimpleNetworkError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SimpleNetworkError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SimpleNetworkError-104"><a href="#SimpleNetworkError-104"><span class="linenos">104</span></a><span class="k">class</span> <span class="nc">SimpleNetworkError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="SimpleNetworkError-105"><a href="#SimpleNetworkError-105"><span class="linenos">105</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="SimpleNetworkError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="SimpleNetworkError.with_traceback" class="function">with_traceback</dd>
                <dd id="SimpleNetworkError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ConnectionSettings">
                            <input id="ConnectionSettings-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ConnectionSettings</span><wbr>(<span class="base">cengal.base.classes.versions.v_0.classes.BaseClassSettings</span>):

                <label class="view-source-button" for="ConnectionSettings-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionSettings"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionSettings-108"><a href="#ConnectionSettings-108"><span class="linenos">108</span></a><span class="k">class</span> <span class="nc">ConnectionSettings</span><span class="p">(</span><span class="n">BaseClassSettings</span><span class="p">):</span>
</span><span id="ConnectionSettings-109"><a href="#ConnectionSettings-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="ConnectionSettings-110"><a href="#ConnectionSettings-110"><span class="linenos">110</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="ConnectionSettings-111"><a href="#ConnectionSettings-111"><span class="linenos">111</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionSettings-112"><a href="#ConnectionSettings-112"><span class="linenos">112</span></a>                 <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionSettings-113"><a href="#ConnectionSettings-113"><span class="linenos">113</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="ConnectionSettings-114"><a href="#ConnectionSettings-114"><span class="linenos">114</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="ConnectionSettings-115"><a href="#ConnectionSettings-115"><span class="linenos">115</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="ConnectionSettings-116"><a href="#ConnectionSettings-116"><span class="linenos">116</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionSettings-117"><a href="#ConnectionSettings-117"><span class="linenos">117</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="ConnectionSettings-118"><a href="#ConnectionSettings-118"><span class="linenos">118</span></a>                 <span class="n">non_socket_connection_settings</span><span class="p">:</span> <span class="n">NonSocketConnectionSettings</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ConnectionSettings-119"><a href="#ConnectionSettings-119"><span class="linenos">119</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ConnectionSettings-120"><a href="#ConnectionSettings-120"><span class="linenos">120</span></a><span class="sd">        :param connection_type: ConnectionType()</span>
</span><span id="ConnectionSettings-121"><a href="#ConnectionSettings-121"><span class="linenos">121</span></a><span class="sd">        :param socket_address: &#39;./main.server.AF_UNIX.socket&#39;, (&#39;localhost&#39;, 8080), (&#39;::&#39;, 50007, 0, 0), , ect.</span>
</span><span id="ConnectionSettings-122"><a href="#ConnectionSettings-122"><span class="linenos">122</span></a><span class="sd">        :param keyword: b&#39;sdlkfj s894 saf 84ewksdhf sdf&#39;. Can be None for a Super Server</span>
</span><span id="ConnectionSettings-123"><a href="#ConnectionSettings-123"><span class="linenos">123</span></a><span class="sd">        :param socket_family: AF_INET (the default), AF_INET6, AF_UNIX, AF_CAN or AF_RDS</span>
</span><span id="ConnectionSettings-124"><a href="#ConnectionSettings-124"><span class="linenos">124</span></a><span class="sd">        :param socket_type: SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants</span>
</span><span id="ConnectionSettings-125"><a href="#ConnectionSettings-125"><span class="linenos">125</span></a><span class="sd">        :param socket_protocol: in the case where the address family is AF_CAN the protocol should be one of CAN_RAW or</span>
</span><span id="ConnectionSettings-126"><a href="#ConnectionSettings-126"><span class="linenos">126</span></a><span class="sd">            CAN_BCM</span>
</span><span id="ConnectionSettings-127"><a href="#ConnectionSettings-127"><span class="linenos">127</span></a><span class="sd">        :param socket_fileno: If fileno is specified, the other arguments are ignored, causing the socket with the</span>
</span><span id="ConnectionSettings-128"><a href="#ConnectionSettings-128"><span class="linenos">128</span></a><span class="sd">            specified file descriptor to return</span>
</span><span id="ConnectionSettings-129"><a href="#ConnectionSettings-129"><span class="linenos">129</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="ConnectionSettings-130"><a href="#ConnectionSettings-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="ConnectionSettings-131"><a href="#ConnectionSettings-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="n">keyword</span>
</span><span id="ConnectionSettings-132"><a href="#ConnectionSettings-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="ConnectionSettings-133"><a href="#ConnectionSettings-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="ConnectionSettings-134"><a href="#ConnectionSettings-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="ConnectionSettings-135"><a href="#ConnectionSettings-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="ConnectionSettings-136"><a href="#ConnectionSettings-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="ConnectionSettings-137"><a href="#ConnectionSettings-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span><span id="ConnectionSettings-138"><a href="#ConnectionSettings-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">non_socket_connection_settings</span> <span class="o">=</span> <span class="n">non_socket_connection_settings</span>
</span><span id="ConnectionSettings-139"><a href="#ConnectionSettings-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_clients_with_empty_output_fifo</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="ConnectionSettings.__init__" class="classattr">
                                        <input id="ConnectionSettings.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ConnectionSettings</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">connection_type</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">io</span><span class="o">.</span><span class="n">asock_io</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_1</span><span class="o">.</span><span class="n">abstract</span><span class="o">.</span><span class="n">ConnectionType</span>,</span><span class="param">	<span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">socket_family</span><span class="o">=&lt;</span><span class="n">AddressFamily</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">:</span> <span class="mi">2</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">socket_type</span><span class="o">=&lt;</span><span class="n">SocketKind</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span>,</span><span class="param">	<span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">backlog</span><span class="o">=</span><span class="mi">0</span>,</span><span class="param">	<span class="n">non_socket_connection_settings</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">io</span><span class="o">.</span><span class="n">asock_io</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_1</span><span class="o">.</span><span class="n">abstract</span><span class="o">.</span><span class="n">NonSocketConnectionSettings</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ConnectionSettings.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionSettings.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionSettings.__init__-109"><a href="#ConnectionSettings.__init__-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-110"><a href="#ConnectionSettings.__init__-110"><span class="linenos">110</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-111"><a href="#ConnectionSettings.__init__-111"><span class="linenos">111</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-112"><a href="#ConnectionSettings.__init__-112"><span class="linenos">112</span></a>                 <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-113"><a href="#ConnectionSettings.__init__-113"><span class="linenos">113</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-114"><a href="#ConnectionSettings.__init__-114"><span class="linenos">114</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-115"><a href="#ConnectionSettings.__init__-115"><span class="linenos">115</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-116"><a href="#ConnectionSettings.__init__-116"><span class="linenos">116</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-117"><a href="#ConnectionSettings.__init__-117"><span class="linenos">117</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="ConnectionSettings.__init__-118"><a href="#ConnectionSettings.__init__-118"><span class="linenos">118</span></a>                 <span class="n">non_socket_connection_settings</span><span class="p">:</span> <span class="n">NonSocketConnectionSettings</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ConnectionSettings.__init__-119"><a href="#ConnectionSettings.__init__-119"><span class="linenos">119</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ConnectionSettings.__init__-120"><a href="#ConnectionSettings.__init__-120"><span class="linenos">120</span></a><span class="sd">        :param connection_type: ConnectionType()</span>
</span><span id="ConnectionSettings.__init__-121"><a href="#ConnectionSettings.__init__-121"><span class="linenos">121</span></a><span class="sd">        :param socket_address: &#39;./main.server.AF_UNIX.socket&#39;, (&#39;localhost&#39;, 8080), (&#39;::&#39;, 50007, 0, 0), , ect.</span>
</span><span id="ConnectionSettings.__init__-122"><a href="#ConnectionSettings.__init__-122"><span class="linenos">122</span></a><span class="sd">        :param keyword: b&#39;sdlkfj s894 saf 84ewksdhf sdf&#39;. Can be None for a Super Server</span>
</span><span id="ConnectionSettings.__init__-123"><a href="#ConnectionSettings.__init__-123"><span class="linenos">123</span></a><span class="sd">        :param socket_family: AF_INET (the default), AF_INET6, AF_UNIX, AF_CAN or AF_RDS</span>
</span><span id="ConnectionSettings.__init__-124"><a href="#ConnectionSettings.__init__-124"><span class="linenos">124</span></a><span class="sd">        :param socket_type: SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants</span>
</span><span id="ConnectionSettings.__init__-125"><a href="#ConnectionSettings.__init__-125"><span class="linenos">125</span></a><span class="sd">        :param socket_protocol: in the case where the address family is AF_CAN the protocol should be one of CAN_RAW or</span>
</span><span id="ConnectionSettings.__init__-126"><a href="#ConnectionSettings.__init__-126"><span class="linenos">126</span></a><span class="sd">            CAN_BCM</span>
</span><span id="ConnectionSettings.__init__-127"><a href="#ConnectionSettings.__init__-127"><span class="linenos">127</span></a><span class="sd">        :param socket_fileno: If fileno is specified, the other arguments are ignored, causing the socket with the</span>
</span><span id="ConnectionSettings.__init__-128"><a href="#ConnectionSettings.__init__-128"><span class="linenos">128</span></a><span class="sd">            specified file descriptor to return</span>
</span><span id="ConnectionSettings.__init__-129"><a href="#ConnectionSettings.__init__-129"><span class="linenos">129</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="ConnectionSettings.__init__-130"><a href="#ConnectionSettings.__init__-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="ConnectionSettings.__init__-131"><a href="#ConnectionSettings.__init__-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="n">keyword</span>
</span><span id="ConnectionSettings.__init__-132"><a href="#ConnectionSettings.__init__-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="ConnectionSettings.__init__-133"><a href="#ConnectionSettings.__init__-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="ConnectionSettings.__init__-134"><a href="#ConnectionSettings.__init__-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="ConnectionSettings.__init__-135"><a href="#ConnectionSettings.__init__-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="ConnectionSettings.__init__-136"><a href="#ConnectionSettings.__init__-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="ConnectionSettings.__init__-137"><a href="#ConnectionSettings.__init__-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span><span id="ConnectionSettings.__init__-138"><a href="#ConnectionSettings.__init__-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">non_socket_connection_settings</span> <span class="o">=</span> <span class="n">non_socket_connection_settings</span>
</span><span id="ConnectionSettings.__init__-139"><a href="#ConnectionSettings.__init__-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_clients_with_empty_output_fifo</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>:param connection_type: ConnectionType()
:param socket_address: './main.server.AF_UNIX.socket', ('localhost', 8080), ('::', 50007, 0, 0), , ect.
:param keyword: b'sdlkfj s894 saf 84ewksdhf sdf'. Can be None for a Super Server
:param socket_family: AF_INET (the default), AF_INET6, AF_UNIX, AF_CAN or AF_RDS
:param socket_type: SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants
:param socket_protocol: in the case where the address family is AF_CAN the protocol should be one of CAN_RAW or
    CAN_BCM
:param socket_fileno: If fileno is specified, the other arguments are ignored, causing the socket with the
    specified file descriptor to return</p>
</div>


                            </div>
                            <div id="ConnectionSettings.connection_type" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_type</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.connection_type"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.keyword" class="classattr">
                                <div class="attr variable">
            <span class="name">keyword</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.keyword"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.socket_address" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_address</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.socket_address"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.socket_family" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_family</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.socket_family"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.socket_type" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_type</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.socket_type"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.socket_protocol" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_protocol</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.socket_protocol"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.socket_fileno" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_fileno</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.socket_fileno"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.backlog" class="classattr">
                                <div class="attr variable">
            <span class="name">backlog</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.backlog"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.non_socket_connection_settings" class="classattr">
                                <div class="attr variable">
            <span class="name">non_socket_connection_settings</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.non_socket_connection_settings"></a>
    
    

                            </div>
                            <div id="ConnectionSettings.expected_clients_with_empty_output_fifo" class="classattr">
                                <div class="attr variable">
            <span class="name">expected_clients_with_empty_output_fifo</span>

        
    </div>
    <a class="headerlink" href="#ConnectionSettings.expected_clients_with_empty_output_fifo"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.base.classes.versions.v_0.classes.BaseClassSettings</dt>
                                <dd id="ConnectionSettings.check" class="function">check</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IOCoreMemoryManagement">
                            <input id="IOCoreMemoryManagement-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IOCoreMemoryManagement</span>:

                <label class="view-source-button" for="IOCoreMemoryManagement-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOCoreMemoryManagement-142"><a href="#IOCoreMemoryManagement-142"><span class="linenos">142</span></a><span class="k">class</span> <span class="nc">IOCoreMemoryManagement</span><span class="p">:</span>
</span><span id="IOCoreMemoryManagement-143"><a href="#IOCoreMemoryManagement-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IOCoreMemoryManagement-144"><a href="#IOCoreMemoryManagement-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global__data_size_limit</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">2</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">3</span><span class="p">)</span>
</span><span id="IOCoreMemoryManagement-145"><a href="#IOCoreMemoryManagement-145"><span class="linenos">145</span></a>
</span><span id="IOCoreMemoryManagement-146"><a href="#IOCoreMemoryManagement-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_size_limit</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">512</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="IOCoreMemoryManagement-147"><a href="#IOCoreMemoryManagement-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_full_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="IOCoreMemoryManagement-148"><a href="#IOCoreMemoryManagement-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__deletable_data_full_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="IOCoreMemoryManagement-149"><a href="#IOCoreMemoryManagement-149"><span class="linenos">149</span></a>
</span><span id="IOCoreMemoryManagement-150"><a href="#IOCoreMemoryManagement-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_size_limit</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">512</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="IOCoreMemoryManagement-151"><a href="#IOCoreMemoryManagement-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_full_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="IOCoreMemoryManagement-152"><a href="#IOCoreMemoryManagement-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__deletable_data_full_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="IOCoreMemoryManagement-153"><a href="#IOCoreMemoryManagement-153"><span class="linenos">153</span></a>
</span><span id="IOCoreMemoryManagement-154"><a href="#IOCoreMemoryManagement-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">link_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">):</span>
</span><span id="IOCoreMemoryManagement-155"><a href="#IOCoreMemoryManagement-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global__data_size_limit</span>
</span><span id="IOCoreMemoryManagement-156"><a href="#IOCoreMemoryManagement-156"><span class="linenos">156</span></a>
</span><span id="IOCoreMemoryManagement-157"><a href="#IOCoreMemoryManagement-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__data_size_limit</span>
</span><span id="IOCoreMemoryManagement-158"><a href="#IOCoreMemoryManagement-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__data_full_size</span>
</span><span id="IOCoreMemoryManagement-159"><a href="#IOCoreMemoryManagement-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__deletable_data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__deletable_data_full_size</span>
</span><span id="IOCoreMemoryManagement-160"><a href="#IOCoreMemoryManagement-160"><span class="linenos">160</span></a>
</span><span id="IOCoreMemoryManagement-161"><a href="#IOCoreMemoryManagement-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__data_size_limit</span>
</span><span id="IOCoreMemoryManagement-162"><a href="#IOCoreMemoryManagement-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__data_full_size</span>
</span><span id="IOCoreMemoryManagement-163"><a href="#IOCoreMemoryManagement-163"><span class="linenos">163</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__deletable_data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__deletable_data_full_size</span>
</span></pre></div>


    

                            <div id="IOCoreMemoryManagement.global__data_size_limit" class="classattr">
                                <div class="attr variable">
            <span class="name">global__data_size_limit</span>

        
    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement.global__data_size_limit"></a>
    
    

                            </div>
                            <div id="IOCoreMemoryManagement.global_in__data_size_limit" class="classattr">
                                <div class="attr variable">
            <span class="name">global_in__data_size_limit</span>

        
    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement.global_in__data_size_limit"></a>
    
    

                            </div>
                            <div id="IOCoreMemoryManagement.global_in__data_full_size" class="classattr">
                                <div class="attr variable">
            <span class="name">global_in__data_full_size</span>

        
    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement.global_in__data_full_size"></a>
    
    

                            </div>
                            <div id="IOCoreMemoryManagement.global_in__deletable_data_full_size" class="classattr">
                                <div class="attr variable">
            <span class="name">global_in__deletable_data_full_size</span>

        
    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement.global_in__deletable_data_full_size"></a>
    
    

                            </div>
                            <div id="IOCoreMemoryManagement.global_out__data_size_limit" class="classattr">
                                <div class="attr variable">
            <span class="name">global_out__data_size_limit</span>

        
    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement.global_out__data_size_limit"></a>
    
    

                            </div>
                            <div id="IOCoreMemoryManagement.global_out__data_full_size" class="classattr">
                                <div class="attr variable">
            <span class="name">global_out__data_full_size</span>

        
    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement.global_out__data_full_size"></a>
    
    

                            </div>
                            <div id="IOCoreMemoryManagement.global_out__deletable_data_full_size" class="classattr">
                                <div class="attr variable">
            <span class="name">global_out__deletable_data_full_size</span>

        
    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement.global_out__deletable_data_full_size"></a>
    
    

                            </div>
                            <div id="IOCoreMemoryManagement.link_to" class="classattr">
                                        <input id="IOCoreMemoryManagement.link_to-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">link_to</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">parent</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOCoreMemoryManagement.link_to-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOCoreMemoryManagement.link_to"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOCoreMemoryManagement.link_to-154"><a href="#IOCoreMemoryManagement.link_to-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">link_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">):</span>
</span><span id="IOCoreMemoryManagement.link_to-155"><a href="#IOCoreMemoryManagement.link_to-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global__data_size_limit</span>
</span><span id="IOCoreMemoryManagement.link_to-156"><a href="#IOCoreMemoryManagement.link_to-156"><span class="linenos">156</span></a>
</span><span id="IOCoreMemoryManagement.link_to-157"><a href="#IOCoreMemoryManagement.link_to-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__data_size_limit</span>
</span><span id="IOCoreMemoryManagement.link_to-158"><a href="#IOCoreMemoryManagement.link_to-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__data_full_size</span>
</span><span id="IOCoreMemoryManagement.link_to-159"><a href="#IOCoreMemoryManagement.link_to-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_in__deletable_data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_in__deletable_data_full_size</span>
</span><span id="IOCoreMemoryManagement.link_to-160"><a href="#IOCoreMemoryManagement.link_to-160"><span class="linenos">160</span></a>
</span><span id="IOCoreMemoryManagement.link_to-161"><a href="#IOCoreMemoryManagement.link_to-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_size_limit</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__data_size_limit</span>
</span><span id="IOCoreMemoryManagement.link_to-162"><a href="#IOCoreMemoryManagement.link_to-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__data_full_size</span>
</span><span id="IOCoreMemoryManagement.link_to-163"><a href="#IOCoreMemoryManagement.link_to-163"><span class="linenos">163</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">global_out__deletable_data_full_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">global_out__deletable_data_full_size</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="ASockIOCoreMemoryManagement">
                            <input id="ASockIOCoreMemoryManagement-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ASockIOCoreMemoryManagement</span><wbr>(<span class="base"><a href="#IOCoreMemoryManagement">IOCoreMemoryManagement</a></span>):

                <label class="view-source-button" for="ASockIOCoreMemoryManagement-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ASockIOCoreMemoryManagement"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ASockIOCoreMemoryManagement-166"><a href="#ASockIOCoreMemoryManagement-166"><span class="linenos">166</span></a><span class="k">class</span> <span class="nc">ASockIOCoreMemoryManagement</span><span class="p">(</span><span class="n">IOCoreMemoryManagement</span><span class="p">):</span>
</span><span id="ASockIOCoreMemoryManagement-167"><a href="#ASockIOCoreMemoryManagement-167"><span class="linenos">167</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ASockIOCoreMemoryManagement-168"><a href="#ASockIOCoreMemoryManagement-168"><span class="linenos">168</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ASockIOCoreMemoryManagement</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="ASockIOCoreMemoryManagement-169"><a href="#ASockIOCoreMemoryManagement-169"><span class="linenos">169</span></a>
</span><span id="ASockIOCoreMemoryManagement-170"><a href="#ASockIOCoreMemoryManagement-170"><span class="linenos">170</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_read_fixed_buffer_size</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span>
</span><span id="ASockIOCoreMemoryManagement-171"><a href="#ASockIOCoreMemoryManagement-171"><span class="linenos">171</span></a>                                                             <span class="nb">int</span><span class="p">(</span><span class="n">l2_cache_per_core</span><span class="p">()</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span> <span class="ow">or</span> <span class="mi">1024</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="ASockIOCoreMemoryManagement-172"><a href="#ASockIOCoreMemoryManagement-172"><span class="linenos">172</span></a>        <span class="c1"># 1024**2 is the fastest fixed read buffer on my CPU.</span>
</span><span id="ASockIOCoreMemoryManagement-173"><a href="#ASockIOCoreMemoryManagement-173"><span class="linenos">173</span></a>        <span class="c1"># Also ingeneral, it should be the half of the CPU cache per core (UPD: I don&#39;t remember why. Maybe to save other memory to instructions when we are dealing with big amount of connections).</span>
</span><span id="ASockIOCoreMemoryManagement-174"><a href="#ASockIOCoreMemoryManagement-174"><span class="linenos">174</span></a>        <span class="c1">#</span>
</span><span id="ASockIOCoreMemoryManagement-175"><a href="#ASockIOCoreMemoryManagement-175"><span class="linenos">175</span></a>        <span class="c1"># My CPU is Intel Core i5 3570:</span>
</span><span id="ASockIOCoreMemoryManagement-176"><a href="#ASockIOCoreMemoryManagement-176"><span class="linenos">176</span></a>        <span class="c1"># Architecture	x86-64</span>
</span><span id="ASockIOCoreMemoryManagement-177"><a href="#ASockIOCoreMemoryManagement-177"><span class="linenos">177</span></a>        <span class="c1"># Threads	4 threads</span>
</span><span id="ASockIOCoreMemoryManagement-178"><a href="#ASockIOCoreMemoryManagement-178"><span class="linenos">178</span></a>        <span class="c1"># L2 cache	1 MB</span>
</span><span id="ASockIOCoreMemoryManagement-179"><a href="#ASockIOCoreMemoryManagement-179"><span class="linenos">179</span></a>        <span class="c1"># L2 cache per core	0.25 MB/core</span>
</span><span id="ASockIOCoreMemoryManagement-180"><a href="#ASockIOCoreMemoryManagement-180"><span class="linenos">180</span></a>        <span class="c1"># L3 cache	6 MB</span>
</span><span id="ASockIOCoreMemoryManagement-181"><a href="#ASockIOCoreMemoryManagement-181"><span class="linenos">181</span></a>        <span class="c1"># L3 cache per core	1.5 MB/core</span>
</span><span id="ASockIOCoreMemoryManagement-182"><a href="#ASockIOCoreMemoryManagement-182"><span class="linenos">182</span></a>
</span><span id="ASockIOCoreMemoryManagement-183"><a href="#ASockIOCoreMemoryManagement-183"><span class="linenos">183</span></a>    <span class="k">def</span> <span class="nf">link_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">):</span>
</span><span id="ASockIOCoreMemoryManagement-184"><a href="#ASockIOCoreMemoryManagement-184"><span class="linenos">184</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ASockIOCoreMemoryManagement</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">link_to</span><span class="p">(</span><span class="n">parent</span><span class="p">)</span>
</span><span id="ASockIOCoreMemoryManagement-185"><a href="#ASockIOCoreMemoryManagement-185"><span class="linenos">185</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ASockIOCoreMemoryManagement-186"><a href="#ASockIOCoreMemoryManagement-186"><span class="linenos">186</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">socket_read_fixed_buffer_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">socket_read_fixed_buffer_size</span>
</span><span id="ASockIOCoreMemoryManagement-187"><a href="#ASockIOCoreMemoryManagement-187"><span class="linenos">187</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ASockIOCoreMemoryManagement-188"><a href="#ASockIOCoreMemoryManagement-188"><span class="linenos">188</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            <div id="ASockIOCoreMemoryManagement.socket_read_fixed_buffer_size" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_read_fixed_buffer_size</span>

        
    </div>
    <a class="headerlink" href="#ASockIOCoreMemoryManagement.socket_read_fixed_buffer_size"></a>
    
    

                            </div>
                            <div id="ASockIOCoreMemoryManagement.link_to" class="classattr">
                                        <input id="ASockIOCoreMemoryManagement.link_to-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">link_to</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">parent</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ASockIOCoreMemoryManagement.link_to-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ASockIOCoreMemoryManagement.link_to"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ASockIOCoreMemoryManagement.link_to-183"><a href="#ASockIOCoreMemoryManagement.link_to-183"><span class="linenos">183</span></a>    <span class="k">def</span> <span class="nf">link_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">):</span>
</span><span id="ASockIOCoreMemoryManagement.link_to-184"><a href="#ASockIOCoreMemoryManagement.link_to-184"><span class="linenos">184</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ASockIOCoreMemoryManagement</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">link_to</span><span class="p">(</span><span class="n">parent</span><span class="p">)</span>
</span><span id="ASockIOCoreMemoryManagement.link_to-185"><a href="#ASockIOCoreMemoryManagement.link_to-185"><span class="linenos">185</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ASockIOCoreMemoryManagement.link_to-186"><a href="#ASockIOCoreMemoryManagement.link_to-186"><span class="linenos">186</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">socket_read_fixed_buffer_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">socket_read_fixed_buffer_size</span>
</span><span id="ASockIOCoreMemoryManagement.link_to-187"><a href="#ASockIOCoreMemoryManagement.link_to-187"><span class="linenos">187</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ASockIOCoreMemoryManagement.link_to-188"><a href="#ASockIOCoreMemoryManagement.link_to-188"><span class="linenos">188</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#IOCoreMemoryManagement">IOCoreMemoryManagement</a></dt>
                                <dd id="ASockIOCoreMemoryManagement.global__data_size_limit" class="variable"><a href="#IOCoreMemoryManagement.global__data_size_limit">global__data_size_limit</a></dd>
                <dd id="ASockIOCoreMemoryManagement.global_in__data_size_limit" class="variable"><a href="#IOCoreMemoryManagement.global_in__data_size_limit">global_in__data_size_limit</a></dd>
                <dd id="ASockIOCoreMemoryManagement.global_in__data_full_size" class="variable"><a href="#IOCoreMemoryManagement.global_in__data_full_size">global_in__data_full_size</a></dd>
                <dd id="ASockIOCoreMemoryManagement.global_in__deletable_data_full_size" class="variable"><a href="#IOCoreMemoryManagement.global_in__deletable_data_full_size">global_in__deletable_data_full_size</a></dd>
                <dd id="ASockIOCoreMemoryManagement.global_out__data_size_limit" class="variable"><a href="#IOCoreMemoryManagement.global_out__data_size_limit">global_out__data_size_limit</a></dd>
                <dd id="ASockIOCoreMemoryManagement.global_out__data_full_size" class="variable"><a href="#IOCoreMemoryManagement.global_out__data_full_size">global_out__data_full_size</a></dd>
                <dd id="ASockIOCoreMemoryManagement.global_out__deletable_data_full_size" class="variable"><a href="#IOCoreMemoryManagement.global_out__deletable_data_full_size">global_out__deletable_data_full_size</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Connection">
                            <input id="Connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Connection</span>:

                <label class="view-source-button" for="Connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection-191"><a href="#Connection-191"><span class="linenos">191</span></a><span class="k">class</span> <span class="nc">Connection</span><span class="p">:</span>
</span><span id="Connection-192"><a href="#Connection-192"><span class="linenos">192</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="Connection-193"><a href="#Connection-193"><span class="linenos">193</span></a>                 <span class="n">connection_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="Connection-194"><a href="#Connection-194"><span class="linenos">194</span></a>                 <span class="n">connection_settings</span><span class="p">:</span> <span class="n">ConnectionSettings</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="Connection-195"><a href="#Connection-195"><span class="linenos">195</span></a>                 <span class="n">connection__conn_addr</span><span class="p">:</span> <span class="nb">tuple</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="Connection-196"><a href="#Connection-196"><span class="linenos">196</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="Connection-197"><a href="#Connection-197"><span class="linenos">197</span></a>                 <span class="n">global_memory_management</span><span class="p">:</span> <span class="n">ASockIOCoreMemoryManagement</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection-198"><a href="#Connection-198"><span class="linenos">198</span></a>                 <span class="p">):</span>
</span><span id="Connection-199"><a href="#Connection-199"><span class="linenos">199</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection-200"><a href="#Connection-200"><span class="linenos">200</span></a>
</span><span id="Connection-201"><a href="#Connection-201"><span class="linenos">201</span></a><span class="sd">        :param connection_id: ID for this connection</span>
</span><span id="Connection-202"><a href="#Connection-202"><span class="linenos">202</span></a><span class="sd">        :param connection__conn_addr: tuple(conn, addr) where conn is a socket, addr is an address</span>
</span><span id="Connection-203"><a href="#Connection-203"><span class="linenos">203</span></a><span class="sd">        :param global_memory_management: global memory management obj</span>
</span><span id="Connection-204"><a href="#Connection-204"><span class="linenos">204</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection-205"><a href="#Connection-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="Connection-206"><a href="#Connection-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span> <span class="o">=</span> <span class="n">connection_settings</span>
</span><span id="Connection-207"><a href="#Connection-207"><span class="linenos">207</span></a>        <span class="k">if</span> <span class="n">connection__conn_addr</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Connection-208"><a href="#Connection-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">conn</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Connection-209"><a href="#Connection-209"><span class="linenos">209</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">addr</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Connection-210"><a href="#Connection-210"><span class="linenos">210</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Connection-211"><a href="#Connection-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">conn</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">connection__conn_addr</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="Connection-212"><a href="#Connection-212"><span class="linenos">212</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">addr</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">connection__conn_addr</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="Connection-213"><a href="#Connection-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="Connection-214"><a href="#Connection-214"><span class="linenos">214</span></a>
</span><span id="Connection-215"><a href="#Connection-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection-216"><a href="#Connection-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection-217"><a href="#Connection-217"><span class="linenos">217</span></a>
</span><span id="Connection-218"><a href="#Connection-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span> <span class="o">=</span> <span class="n">RecvBuffSizeComputer</span><span class="p">()</span>
</span><span id="Connection-219"><a href="#Connection-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection-220"><a href="#Connection-220"><span class="linenos">220</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="Connection-221"><a href="#Connection-221"><span class="linenos">221</span></a>
</span><span id="Connection-222"><a href="#Connection-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># socket should be closed immediately. For example because of IO error.</span>
</span><span id="Connection-223"><a href="#Connection-223"><span class="linenos">223</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ready_to_be_closed</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># socket should be closed, after all messages had been sent to client.</span>
</span><span id="Connection-224"><a href="#Connection-224"><span class="linenos">224</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ready_for_deletion</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># connection should be deleted immediately. For example because of unexpected</span>
</span><span id="Connection-225"><a href="#Connection-225"><span class="linenos">225</span></a>        <span class="c1">#   keyword.</span>
</span><span id="Connection-226"><a href="#Connection-226"><span class="linenos">226</span></a>
</span><span id="Connection-227"><a href="#Connection-227"><span class="linenos">227</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection-228"><a href="#Connection-228"><span class="linenos">228</span></a>
</span><span id="Connection-229"><a href="#Connection-229"><span class="linenos">229</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection-230"><a href="#Connection-230"><span class="linenos">230</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection-231"><a href="#Connection-231"><span class="linenos">231</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_nbytes</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection-232"><a href="#Connection-232"><span class="linenos">232</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection-233"><a href="#Connection-233"><span class="linenos">233</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_message_nbytes</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection-234"><a href="#Connection-234"><span class="linenos">234</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raw_input_from_client</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span><span class="p">(</span>
</span><span id="Connection-235"><a href="#Connection-235"><span class="linenos">235</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="Connection-236"><a href="#Connection-236"><span class="linenos">236</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_message_length</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># length of current input message (or None, if size waw not read yet)</span>
</span><span id="Connection-237"><a href="#Connection-237"><span class="linenos">237</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span>
</span><span id="Connection-238"><a href="#Connection-238"><span class="linenos">238</span></a>            <span class="n">external_data_full_size</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="Connection-239"><a href="#Connection-239"><span class="linenos">239</span></a>
</span><span id="Connection-240"><a href="#Connection-240"><span class="linenos">240</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_output_memoryview</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection-241"><a href="#Connection-241"><span class="linenos">241</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span>
</span><span id="Connection-242"><a href="#Connection-242"><span class="linenos">242</span></a>            <span class="n">external_data_full_size</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_out__data_full_size</span><span class="p">)</span>
</span><span id="Connection-243"><a href="#Connection-243"><span class="linenos">243</span></a>
</span><span id="Connection-244"><a href="#Connection-244"><span class="linenos">244</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">this_is_raw_connection</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Connection-245"><a href="#Connection-245"><span class="linenos">245</span></a>
</span><span id="Connection-246"><a href="#Connection-246"><span class="linenos">246</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connected_expected_client_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection-247"><a href="#Connection-247"><span class="linenos">247</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connected_expected_client</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection-248"><a href="#Connection-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">has_inline_processor</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Connection-249"><a href="#Connection-249"><span class="linenos">249</span></a>
</span><span id="Connection-250"><a href="#Connection-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">calc_new_recv_buff_size</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">last_recv_amount</span><span class="p">):</span>
</span><span id="Connection-251"><a href="#Connection-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">last_recv_amount</span><span class="p">)</span>
</span><span id="Connection-252"><a href="#Connection-252"><span class="linenos">252</span></a>
</span><span id="Connection-253"><a href="#Connection-253"><span class="linenos">253</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Connection-254"><a href="#Connection-254"><span class="linenos">254</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raw_input_from_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="Connection-255"><a href="#Connection-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="Connection-256"><a href="#Connection-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="Connection-257"><a href="#Connection-257"><span class="linenos">257</span></a>
</span><span id="Connection-258"><a href="#Connection-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="nf">add_data_to_output_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="Connection-259"><a href="#Connection-259"><span class="linenos">259</span></a>        <span class="k">pass</span>
</span><span id="Connection-260"><a href="#Connection-260"><span class="linenos">260</span></a>
</span><span id="Connection-261"><a href="#Connection-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="nf">add_data_to_input_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="Connection-262"><a href="#Connection-262"><span class="linenos">262</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            <div id="Connection.__init__" class="classattr">
                                        <input id="Connection.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">connection_id</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">connection_settings</span><span class="p">:</span> <span class="n"><a href="#ConnectionSettings">ConnectionSettings</a></span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">connection__conn_addr</span><span class="p">:</span> <span class="nb">tuple</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">connection_state</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">io</span><span class="o">.</span><span class="n">asock_io</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_1</span><span class="o">.</span><span class="n">abstract</span><span class="o">.</span><span class="n">ConnectionState</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">global_memory_management</span><span class="p">:</span> <span class="n"><a href="#ASockIOCoreMemoryManagement">ASockIOCoreMemoryManagement</a></span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="Connection.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Connection.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.__init__-192"><a href="#Connection.__init__-192"><span class="linenos">192</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="Connection.__init__-193"><a href="#Connection.__init__-193"><span class="linenos">193</span></a>                 <span class="n">connection_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="Connection.__init__-194"><a href="#Connection.__init__-194"><span class="linenos">194</span></a>                 <span class="n">connection_settings</span><span class="p">:</span> <span class="n">ConnectionSettings</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="Connection.__init__-195"><a href="#Connection.__init__-195"><span class="linenos">195</span></a>                 <span class="n">connection__conn_addr</span><span class="p">:</span> <span class="nb">tuple</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="Connection.__init__-196"><a href="#Connection.__init__-196"><span class="linenos">196</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="Connection.__init__-197"><a href="#Connection.__init__-197"><span class="linenos">197</span></a>                 <span class="n">global_memory_management</span><span class="p">:</span> <span class="n">ASockIOCoreMemoryManagement</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection.__init__-198"><a href="#Connection.__init__-198"><span class="linenos">198</span></a>                 <span class="p">):</span>
</span><span id="Connection.__init__-199"><a href="#Connection.__init__-199"><span class="linenos">199</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection.__init__-200"><a href="#Connection.__init__-200"><span class="linenos">200</span></a>
</span><span id="Connection.__init__-201"><a href="#Connection.__init__-201"><span class="linenos">201</span></a><span class="sd">        :param connection_id: ID for this connection</span>
</span><span id="Connection.__init__-202"><a href="#Connection.__init__-202"><span class="linenos">202</span></a><span class="sd">        :param connection__conn_addr: tuple(conn, addr) where conn is a socket, addr is an address</span>
</span><span id="Connection.__init__-203"><a href="#Connection.__init__-203"><span class="linenos">203</span></a><span class="sd">        :param global_memory_management: global memory management obj</span>
</span><span id="Connection.__init__-204"><a href="#Connection.__init__-204"><span class="linenos">204</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection.__init__-205"><a href="#Connection.__init__-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="Connection.__init__-206"><a href="#Connection.__init__-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span> <span class="o">=</span> <span class="n">connection_settings</span>
</span><span id="Connection.__init__-207"><a href="#Connection.__init__-207"><span class="linenos">207</span></a>        <span class="k">if</span> <span class="n">connection__conn_addr</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Connection.__init__-208"><a href="#Connection.__init__-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">conn</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Connection.__init__-209"><a href="#Connection.__init__-209"><span class="linenos">209</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">addr</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Connection.__init__-210"><a href="#Connection.__init__-210"><span class="linenos">210</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Connection.__init__-211"><a href="#Connection.__init__-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">conn</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">connection__conn_addr</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="Connection.__init__-212"><a href="#Connection.__init__-212"><span class="linenos">212</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">addr</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">connection__conn_addr</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="Connection.__init__-213"><a href="#Connection.__init__-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="Connection.__init__-214"><a href="#Connection.__init__-214"><span class="linenos">214</span></a>
</span><span id="Connection.__init__-215"><a href="#Connection.__init__-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection.__init__-216"><a href="#Connection.__init__-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection.__init__-217"><a href="#Connection.__init__-217"><span class="linenos">217</span></a>
</span><span id="Connection.__init__-218"><a href="#Connection.__init__-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span> <span class="o">=</span> <span class="n">RecvBuffSizeComputer</span><span class="p">()</span>
</span><span id="Connection.__init__-219"><a href="#Connection.__init__-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection.__init__-220"><a href="#Connection.__init__-220"><span class="linenos">220</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="Connection.__init__-221"><a href="#Connection.__init__-221"><span class="linenos">221</span></a>
</span><span id="Connection.__init__-222"><a href="#Connection.__init__-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># socket should be closed immediately. For example because of IO error.</span>
</span><span id="Connection.__init__-223"><a href="#Connection.__init__-223"><span class="linenos">223</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ready_to_be_closed</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># socket should be closed, after all messages had been sent to client.</span>
</span><span id="Connection.__init__-224"><a href="#Connection.__init__-224"><span class="linenos">224</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ready_for_deletion</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># connection should be deleted immediately. For example because of unexpected</span>
</span><span id="Connection.__init__-225"><a href="#Connection.__init__-225"><span class="linenos">225</span></a>        <span class="c1">#   keyword.</span>
</span><span id="Connection.__init__-226"><a href="#Connection.__init__-226"><span class="linenos">226</span></a>
</span><span id="Connection.__init__-227"><a href="#Connection.__init__-227"><span class="linenos">227</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection.__init__-228"><a href="#Connection.__init__-228"><span class="linenos">228</span></a>
</span><span id="Connection.__init__-229"><a href="#Connection.__init__-229"><span class="linenos">229</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection.__init__-230"><a href="#Connection.__init__-230"><span class="linenos">230</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection.__init__-231"><a href="#Connection.__init__-231"><span class="linenos">231</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_nbytes</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection.__init__-232"><a href="#Connection.__init__-232"><span class="linenos">232</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection.__init__-233"><a href="#Connection.__init__-233"><span class="linenos">233</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_input_memoryview_message_nbytes</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Connection.__init__-234"><a href="#Connection.__init__-234"><span class="linenos">234</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raw_input_from_client</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span><span class="p">(</span>
</span><span id="Connection.__init__-235"><a href="#Connection.__init__-235"><span class="linenos">235</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="Connection.__init__-236"><a href="#Connection.__init__-236"><span class="linenos">236</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_message_length</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># length of current input message (or None, if size waw not read yet)</span>
</span><span id="Connection.__init__-237"><a href="#Connection.__init__-237"><span class="linenos">237</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span>
</span><span id="Connection.__init__-238"><a href="#Connection.__init__-238"><span class="linenos">238</span></a>            <span class="n">external_data_full_size</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="Connection.__init__-239"><a href="#Connection.__init__-239"><span class="linenos">239</span></a>
</span><span id="Connection.__init__-240"><a href="#Connection.__init__-240"><span class="linenos">240</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_output_memoryview</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection.__init__-241"><a href="#Connection.__init__-241"><span class="linenos">241</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span>
</span><span id="Connection.__init__-242"><a href="#Connection.__init__-242"><span class="linenos">242</span></a>            <span class="n">external_data_full_size</span><span class="o">=</span><span class="n">global_memory_management</span><span class="o">.</span><span class="n">global_out__data_full_size</span><span class="p">)</span>
</span><span id="Connection.__init__-243"><a href="#Connection.__init__-243"><span class="linenos">243</span></a>
</span><span id="Connection.__init__-244"><a href="#Connection.__init__-244"><span class="linenos">244</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">this_is_raw_connection</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Connection.__init__-245"><a href="#Connection.__init__-245"><span class="linenos">245</span></a>
</span><span id="Connection.__init__-246"><a href="#Connection.__init__-246"><span class="linenos">246</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connected_expected_client_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection.__init__-247"><a href="#Connection.__init__-247"><span class="linenos">247</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connected_expected_client</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Connection.__init__-248"><a href="#Connection.__init__-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">has_inline_processor</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


            <div class="docstring"><p>:param connection_id: ID for this connection
:param connection__conn_addr: tuple(conn, addr) where conn is a socket, addr is an address
:param global_memory_management: global memory management obj</p>
</div>


                            </div>
                            <div id="Connection.id" class="classattr">
                                <div class="attr variable">
            <span class="name">id</span>

        
    </div>
    <a class="headerlink" href="#Connection.id"></a>
    
    

                            </div>
                            <div id="Connection.connection_settings" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_settings</span>

        
    </div>
    <a class="headerlink" href="#Connection.connection_settings"></a>
    
    

                            </div>
                            <div id="Connection.connection_state" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_state</span>

        
    </div>
    <a class="headerlink" href="#Connection.connection_state"></a>
    
    

                            </div>
                            <div id="Connection.addr_info" class="classattr">
                                <div class="attr variable">
            <span class="name">addr_info</span>

        
    </div>
    <a class="headerlink" href="#Connection.addr_info"></a>
    
    

                            </div>
                            <div id="Connection.host_names" class="classattr">
                                <div class="attr variable">
            <span class="name">host_names</span>

        
    </div>
    <a class="headerlink" href="#Connection.host_names"></a>
    
    

                            </div>
                            <div id="Connection.recv_buff_size_computer" class="classattr">
                                <div class="attr variable">
            <span class="name">recv_buff_size_computer</span>

        
    </div>
    <a class="headerlink" href="#Connection.recv_buff_size_computer"></a>
    
    

                            </div>
                            <div id="Connection.recv_buff_size" class="classattr">
                                <div class="attr variable">
            <span class="name">recv_buff_size</span>

        
    </div>
    <a class="headerlink" href="#Connection.recv_buff_size"></a>
    
    

                            </div>
                            <div id="Connection.should_be_closed" class="classattr">
                                <div class="attr variable">
            <span class="name">should_be_closed</span>

        
    </div>
    <a class="headerlink" href="#Connection.should_be_closed"></a>
    
    

                            </div>
                            <div id="Connection.ready_to_be_closed" class="classattr">
                                <div class="attr variable">
            <span class="name">ready_to_be_closed</span>

        
    </div>
    <a class="headerlink" href="#Connection.ready_to_be_closed"></a>
    
    

                            </div>
                            <div id="Connection.ready_for_deletion" class="classattr">
                                <div class="attr variable">
            <span class="name">ready_for_deletion</span>

        
    </div>
    <a class="headerlink" href="#Connection.ready_for_deletion"></a>
    
    

                            </div>
                            <div id="Connection.keyword" class="classattr">
                                <div class="attr variable">
            <span class="name">keyword</span>

        
    </div>
    <a class="headerlink" href="#Connection.keyword"></a>
    
    

                            </div>
                            <div id="Connection.current_input_memoryview" class="classattr">
                                <div class="attr variable">
            <span class="name">current_input_memoryview</span>

        
    </div>
    <a class="headerlink" href="#Connection.current_input_memoryview"></a>
    
    

                            </div>
                            <div id="Connection.current_input_memoryview_offset" class="classattr">
                                <div class="attr variable">
            <span class="name">current_input_memoryview_offset</span>

        
    </div>
    <a class="headerlink" href="#Connection.current_input_memoryview_offset"></a>
    
    

                            </div>
                            <div id="Connection.current_input_memoryview_nbytes" class="classattr">
                                <div class="attr variable">
            <span class="name">current_input_memoryview_nbytes</span>

        
    </div>
    <a class="headerlink" href="#Connection.current_input_memoryview_nbytes"></a>
    
    

                            </div>
                            <div id="Connection.current_input_memoryview_diff" class="classattr">
                                <div class="attr variable">
            <span class="name">current_input_memoryview_diff</span>

        
    </div>
    <a class="headerlink" href="#Connection.current_input_memoryview_diff"></a>
    
    

                            </div>
                            <div id="Connection.current_input_memoryview_message_nbytes" class="classattr">
                                <div class="attr variable">
            <span class="name">current_input_memoryview_message_nbytes</span>

        
    </div>
    <a class="headerlink" href="#Connection.current_input_memoryview_message_nbytes"></a>
    
    

                            </div>
                            <div id="Connection.raw_input_from_client" class="classattr">
                                <div class="attr variable">
            <span class="name">raw_input_from_client</span>

        
    </div>
    <a class="headerlink" href="#Connection.raw_input_from_client"></a>
    
    

                            </div>
                            <div id="Connection.current_message_length" class="classattr">
                                <div class="attr variable">
            <span class="name">current_message_length</span>

        
    </div>
    <a class="headerlink" href="#Connection.current_message_length"></a>
    
    

                            </div>
                            <div id="Connection.input_from_client" class="classattr">
                                <div class="attr variable">
            <span class="name">input_from_client</span>

        
    </div>
    <a class="headerlink" href="#Connection.input_from_client"></a>
    
    

                            </div>
                            <div id="Connection.current_output_memoryview" class="classattr">
                                <div class="attr variable">
            <span class="name">current_output_memoryview</span>

        
    </div>
    <a class="headerlink" href="#Connection.current_output_memoryview"></a>
    
    

                            </div>
                            <div id="Connection.output_to_client" class="classattr">
                                <div class="attr variable">
            <span class="name">output_to_client</span>

        
    </div>
    <a class="headerlink" href="#Connection.output_to_client"></a>
    
    

                            </div>
                            <div id="Connection.this_is_raw_connection" class="classattr">
                                <div class="attr variable">
            <span class="name">this_is_raw_connection</span>

        
    </div>
    <a class="headerlink" href="#Connection.this_is_raw_connection"></a>
    
    

                            </div>
                            <div id="Connection.connected_expected_client_id" class="classattr">
                                <div class="attr variable">
            <span class="name">connected_expected_client_id</span>

        
    </div>
    <a class="headerlink" href="#Connection.connected_expected_client_id"></a>
    
    

                            </div>
                            <div id="Connection.connected_expected_client" class="classattr">
                                <div class="attr variable">
            <span class="name">connected_expected_client</span>

        
    </div>
    <a class="headerlink" href="#Connection.connected_expected_client"></a>
    
    

                            </div>
                            <div id="Connection.has_inline_processor" class="classattr">
                                <div class="attr variable">
            <span class="name">has_inline_processor</span>

        
    </div>
    <a class="headerlink" href="#Connection.has_inline_processor"></a>
    
    

                            </div>
                            <div id="Connection.calc_new_recv_buff_size" class="classattr">
                                        <input id="Connection.calc_new_recv_buff_size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">calc_new_recv_buff_size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">last_recv_amount</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Connection.calc_new_recv_buff_size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Connection.calc_new_recv_buff_size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.calc_new_recv_buff_size-250"><a href="#Connection.calc_new_recv_buff_size-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">calc_new_recv_buff_size</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">last_recv_amount</span><span class="p">):</span>
</span><span id="Connection.calc_new_recv_buff_size-251"><a href="#Connection.calc_new_recv_buff_size-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">last_recv_amount</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Connection.remove" class="classattr">
                                        <input id="Connection.remove-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Connection.remove-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Connection.remove"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.remove-253"><a href="#Connection.remove-253"><span class="linenos">253</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Connection.remove-254"><a href="#Connection.remove-254"><span class="linenos">254</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raw_input_from_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="Connection.remove-255"><a href="#Connection.remove-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="Connection.remove-256"><a href="#Connection.remove-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="Connection.add_data_to_output_buffer" class="classattr">
                                        <input id="Connection.add_data_to_output_buffer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_data_to_output_buffer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Connection.add_data_to_output_buffer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Connection.add_data_to_output_buffer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.add_data_to_output_buffer-258"><a href="#Connection.add_data_to_output_buffer-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="nf">add_data_to_output_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="Connection.add_data_to_output_buffer-259"><a href="#Connection.add_data_to_output_buffer-259"><span class="linenos">259</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="Connection.add_data_to_input_buffer" class="classattr">
                                        <input id="Connection.add_data_to_input_buffer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_data_to_input_buffer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Connection.add_data_to_input_buffer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Connection.add_data_to_input_buffer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.add_data_to_input_buffer-261"><a href="#Connection.add_data_to_input_buffer-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="nf">add_data_to_input_buffer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="Connection.add_data_to_input_buffer-262"><a href="#Connection.add_data_to_input_buffer-262"><span class="linenos">262</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="InlineProcessor">
                            <input id="InlineProcessor-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">InlineProcessor</span><wbr>(<span class="base">cengal.io.asock_io.versions.v_1.abstract.InlineWorkerBase</span>):

                <label class="view-source-button" for="InlineProcessor-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineProcessor"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineProcessor-265"><a href="#InlineProcessor-265"><span class="linenos">265</span></a><span class="k">class</span> <span class="nc">InlineProcessor</span><span class="p">(</span><span class="n">InlineWorkerBase</span><span class="p">):</span>
</span><span id="InlineProcessor-266"><a href="#InlineProcessor-266"><span class="linenos">266</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;client_id&#39;</span><span class="p">,</span> <span class="s1">&#39;keyword&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_family&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_type&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_proto&#39;</span><span class="p">,</span> <span class="s1">&#39;addr_info&#39;</span><span class="p">,</span> <span class="s1">&#39;host_names&#39;</span><span class="p">,</span>
</span><span id="InlineProcessor-267"><a href="#InlineProcessor-267"><span class="linenos">267</span></a>                 <span class="s1">&#39;is_in_raw_mode&#39;</span><span class="p">,</span> <span class="s1">&#39;__set__is_in_raw_mode&#39;</span><span class="p">,</span> <span class="s1">&#39;__set__mark_socket_as_should_be_closed_immediately&#39;</span><span class="p">,</span>
</span><span id="InlineProcessor-268"><a href="#InlineProcessor-268"><span class="linenos">268</span></a>                 <span class="s1">&#39;__set__mark_socket_as_ready_to_be_closed&#39;</span><span class="p">,</span> <span class="s1">&#39;__external_parameters_set_trigger&#39;</span><span class="p">,</span> <span class="s1">&#39;output_messages&#39;</span><span class="p">,</span>
</span><span id="InlineProcessor-269"><a href="#InlineProcessor-269"><span class="linenos">269</span></a>                 <span class="s1">&#39;__hold__client_id&#39;</span><span class="p">)</span>
</span><span id="InlineProcessor-270"><a href="#InlineProcessor-270"><span class="linenos">270</span></a>
</span><span id="InlineProcessor-271"><a href="#InlineProcessor-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">socket_family</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_type</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_proto</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="InlineProcessor-272"><a href="#InlineProcessor-272"><span class="linenos">272</span></a>                 <span class="n">addr_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">host_names</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="InlineProcessor-273"><a href="#InlineProcessor-273"><span class="linenos">273</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineProcessor-274"><a href="#InlineProcessor-274"><span class="linenos">274</span></a>
</span><span id="InlineProcessor-275"><a href="#InlineProcessor-275"><span class="linenos">275</span></a><span class="sd">        :param keyword: client keyword. You may check for a known keywords to act appropriately</span>
</span><span id="InlineProcessor-276"><a href="#InlineProcessor-276"><span class="linenos">276</span></a><span class="sd">        :param socket_family:</span>
</span><span id="InlineProcessor-277"><a href="#InlineProcessor-277"><span class="linenos">277</span></a><span class="sd">        :param socket_type:</span>
</span><span id="InlineProcessor-278"><a href="#InlineProcessor-278"><span class="linenos">278</span></a><span class="sd">        :param socket_proto:</span>
</span><span id="InlineProcessor-279"><a href="#InlineProcessor-279"><span class="linenos">279</span></a><span class="sd">        :param addr_info: result of socket.getaddrinfo() call</span>
</span><span id="InlineProcessor-280"><a href="#InlineProcessor-280"><span class="linenos">280</span></a><span class="sd">        :param host_names: result of socket.gethostbyaddr() call</span>
</span><span id="InlineProcessor-281"><a href="#InlineProcessor-281"><span class="linenos">281</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineProcessor-282"><a href="#InlineProcessor-282"><span class="linenos">282</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">InlineProcessor</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="n">keyword</span><span class="p">,</span> <span class="n">socket_family</span><span class="p">,</span> <span class="n">socket_type</span><span class="p">,</span> <span class="n">socket_proto</span><span class="p">,</span>
</span><span id="InlineProcessor-283"><a href="#InlineProcessor-283"><span class="linenos">283</span></a>                                              <span class="n">addr_info</span><span class="p">,</span> <span class="n">host_names</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">)</span>
</span><span id="InlineProcessor-284"><a href="#InlineProcessor-284"><span class="linenos">284</span></a>
</span><span id="InlineProcessor-285"><a href="#InlineProcessor-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="InlineProcessor-286"><a href="#InlineProcessor-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="InlineProcessor-287"><a href="#InlineProcessor-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="InlineProcessor-288"><a href="#InlineProcessor-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="InlineProcessor-289"><a href="#InlineProcessor-289"><span class="linenos">289</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span> <span class="o">=</span> <span class="n">external_parameters_set_trigger</span>
</span><span id="InlineProcessor-290"><a href="#InlineProcessor-290"><span class="linenos">290</span></a>
</span><span id="InlineProcessor-291"><a href="#InlineProcessor-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="nf">set__is_in_raw_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_in_raw_mode</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineProcessor-292"><a href="#InlineProcessor-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span> <span class="o">=</span> <span class="n">is_in_raw_mode</span>
</span><span id="InlineProcessor-293"><a href="#InlineProcessor-293"><span class="linenos">293</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span><span id="InlineProcessor-294"><a href="#InlineProcessor-294"><span class="linenos">294</span></a>
</span><span id="InlineProcessor-295"><a href="#InlineProcessor-295"><span class="linenos">295</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_should_be_closed_immediately</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineProcessor-296"><a href="#InlineProcessor-296"><span class="linenos">296</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span> <span class="o">=</span> <span class="n">mark_socket_as</span>
</span><span id="InlineProcessor-297"><a href="#InlineProcessor-297"><span class="linenos">297</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span><span id="InlineProcessor-298"><a href="#InlineProcessor-298"><span class="linenos">298</span></a>
</span><span id="InlineProcessor-299"><a href="#InlineProcessor-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_ready_to_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineProcessor-300"><a href="#InlineProcessor-300"><span class="linenos">300</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span> <span class="o">=</span> <span class="n">mark_socket_as</span>
</span><span id="InlineProcessor-301"><a href="#InlineProcessor-301"><span class="linenos">301</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span><span id="InlineProcessor-302"><a href="#InlineProcessor-302"><span class="linenos">302</span></a>
</span><span id="InlineProcessor-303"><a href="#InlineProcessor-303"><span class="linenos">303</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="InlineProcessor-304"><a href="#InlineProcessor-304"><span class="linenos">304</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_proto</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span><span class="p">,</span> \
</span><span id="InlineProcessor-305"><a href="#InlineProcessor-305"><span class="linenos">305</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_in_raw_mode</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span><span class="p">,</span> \
</span><span id="InlineProcessor-306"><a href="#InlineProcessor-306"><span class="linenos">306</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span><span class="p">,</span> \
</span><span id="InlineProcessor-307"><a href="#InlineProcessor-307"><span class="linenos">307</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_messages</span>
</span><span id="InlineProcessor-308"><a href="#InlineProcessor-308"><span class="linenos">308</span></a>
</span><span id="InlineProcessor-309"><a href="#InlineProcessor-309"><span class="linenos">309</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="InlineProcessor-310"><a href="#InlineProcessor-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_proto</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span><span class="p">,</span> \
</span><span id="InlineProcessor-311"><a href="#InlineProcessor-311"><span class="linenos">311</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_in_raw_mode</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span><span class="p">,</span> \
</span><span id="InlineProcessor-312"><a href="#InlineProcessor-312"><span class="linenos">312</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span><span class="p">,</span> \
</span><span id="InlineProcessor-313"><a href="#InlineProcessor-313"><span class="linenos">313</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">output_messages</span> <span class="o">=</span> <span class="n">state</span>
</span></pre></div>


    

                            <div id="InlineProcessor.__init__" class="classattr">
                                        <input id="InlineProcessor.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">InlineProcessor</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">client_id</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">socket_family</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">socket_type</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">socket_proto</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">addr_info</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">host_names</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">external_parameters_set_trigger</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="InlineProcessor.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineProcessor.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineProcessor.__init__-271"><a href="#InlineProcessor.__init__-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">socket_family</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_type</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_proto</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="InlineProcessor.__init__-272"><a href="#InlineProcessor.__init__-272"><span class="linenos">272</span></a>                 <span class="n">addr_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">host_names</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="InlineProcessor.__init__-273"><a href="#InlineProcessor.__init__-273"><span class="linenos">273</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineProcessor.__init__-274"><a href="#InlineProcessor.__init__-274"><span class="linenos">274</span></a>
</span><span id="InlineProcessor.__init__-275"><a href="#InlineProcessor.__init__-275"><span class="linenos">275</span></a><span class="sd">        :param keyword: client keyword. You may check for a known keywords to act appropriately</span>
</span><span id="InlineProcessor.__init__-276"><a href="#InlineProcessor.__init__-276"><span class="linenos">276</span></a><span class="sd">        :param socket_family:</span>
</span><span id="InlineProcessor.__init__-277"><a href="#InlineProcessor.__init__-277"><span class="linenos">277</span></a><span class="sd">        :param socket_type:</span>
</span><span id="InlineProcessor.__init__-278"><a href="#InlineProcessor.__init__-278"><span class="linenos">278</span></a><span class="sd">        :param socket_proto:</span>
</span><span id="InlineProcessor.__init__-279"><a href="#InlineProcessor.__init__-279"><span class="linenos">279</span></a><span class="sd">        :param addr_info: result of socket.getaddrinfo() call</span>
</span><span id="InlineProcessor.__init__-280"><a href="#InlineProcessor.__init__-280"><span class="linenos">280</span></a><span class="sd">        :param host_names: result of socket.gethostbyaddr() call</span>
</span><span id="InlineProcessor.__init__-281"><a href="#InlineProcessor.__init__-281"><span class="linenos">281</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineProcessor.__init__-282"><a href="#InlineProcessor.__init__-282"><span class="linenos">282</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">InlineProcessor</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="n">keyword</span><span class="p">,</span> <span class="n">socket_family</span><span class="p">,</span> <span class="n">socket_type</span><span class="p">,</span> <span class="n">socket_proto</span><span class="p">,</span>
</span><span id="InlineProcessor.__init__-283"><a href="#InlineProcessor.__init__-283"><span class="linenos">283</span></a>                                              <span class="n">addr_info</span><span class="p">,</span> <span class="n">host_names</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">)</span>
</span><span id="InlineProcessor.__init__-284"><a href="#InlineProcessor.__init__-284"><span class="linenos">284</span></a>
</span><span id="InlineProcessor.__init__-285"><a href="#InlineProcessor.__init__-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="InlineProcessor.__init__-286"><a href="#InlineProcessor.__init__-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="InlineProcessor.__init__-287"><a href="#InlineProcessor.__init__-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="InlineProcessor.__init__-288"><a href="#InlineProcessor.__init__-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="InlineProcessor.__init__-289"><a href="#InlineProcessor.__init__-289"><span class="linenos">289</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span> <span class="o">=</span> <span class="n">external_parameters_set_trigger</span>
</span></pre></div>


            <div class="docstring"><p>:param keyword: client keyword. You may check for a known keywords to act appropriately
:param socket_family:
:param socket_type:
:param socket_proto:
:param addr_info: result of socket.getaddrinfo() call
:param host_names: result of socket.gethostbyaddr() call</p>
</div>


                            </div>
                            <div id="InlineProcessor.set__is_in_raw_mode" class="classattr">
                                        <input id="InlineProcessor.set__is_in_raw_mode-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set__is_in_raw_mode</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">is_in_raw_mode</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineProcessor.set__is_in_raw_mode-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineProcessor.set__is_in_raw_mode"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineProcessor.set__is_in_raw_mode-291"><a href="#InlineProcessor.set__is_in_raw_mode-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="nf">set__is_in_raw_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_in_raw_mode</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineProcessor.set__is_in_raw_mode-292"><a href="#InlineProcessor.set__is_in_raw_mode-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__is_in_raw_mode</span> <span class="o">=</span> <span class="n">is_in_raw_mode</span>
</span><span id="InlineProcessor.set__is_in_raw_mode-293"><a href="#InlineProcessor.set__is_in_raw_mode-293"><span class="linenos">293</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="InlineProcessor.mark__socket_as_should_be_closed_immediately" class="classattr">
                                        <input id="InlineProcessor.mark__socket_as_should_be_closed_immediately-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mark__socket_as_should_be_closed_immediately</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineProcessor.mark__socket_as_should_be_closed_immediately-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineProcessor.mark__socket_as_should_be_closed_immediately"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineProcessor.mark__socket_as_should_be_closed_immediately-295"><a href="#InlineProcessor.mark__socket_as_should_be_closed_immediately-295"><span class="linenos">295</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_should_be_closed_immediately</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineProcessor.mark__socket_as_should_be_closed_immediately-296"><a href="#InlineProcessor.mark__socket_as_should_be_closed_immediately-296"><span class="linenos">296</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_should_be_closed_immediately</span> <span class="o">=</span> <span class="n">mark_socket_as</span>
</span><span id="InlineProcessor.mark__socket_as_should_be_closed_immediately-297"><a href="#InlineProcessor.mark__socket_as_should_be_closed_immediately-297"><span class="linenos">297</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="InlineProcessor.mark__socket_as_ready_to_be_closed" class="classattr">
                                        <input id="InlineProcessor.mark__socket_as_ready_to_be_closed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mark__socket_as_ready_to_be_closed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineProcessor.mark__socket_as_ready_to_be_closed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineProcessor.mark__socket_as_ready_to_be_closed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineProcessor.mark__socket_as_ready_to_be_closed-299"><a href="#InlineProcessor.mark__socket_as_ready_to_be_closed-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_ready_to_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineProcessor.mark__socket_as_ready_to_be_closed-300"><a href="#InlineProcessor.mark__socket_as_ready_to_be_closed-300"><span class="linenos">300</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__set__mark_socket_as_ready_to_be_closed</span> <span class="o">=</span> <span class="n">mark_socket_as</span>
</span><span id="InlineProcessor.mark__socket_as_ready_to_be_closed-301"><a href="#InlineProcessor.mark__socket_as_ready_to_be_closed-301"><span class="linenos">301</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__external_parameters_set_trigger</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__hold__client_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="InlineProcessor.client_id" class="classattr">
                                <div class="attr variable">
            <span class="name">client_id</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.client_id"></a>
    
    

                            </div>
                            <div id="InlineProcessor.keyword" class="classattr">
                                <div class="attr variable">
            <span class="name">keyword</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.keyword"></a>
    
    

                            </div>
                            <div id="InlineProcessor.socket_family" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_family</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.socket_family"></a>
    
    

                            </div>
                            <div id="InlineProcessor.socket_type" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_type</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.socket_type"></a>
    
    

                            </div>
                            <div id="InlineProcessor.socket_proto" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_proto</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.socket_proto"></a>
    
    

                            </div>
                            <div id="InlineProcessor.addr_info" class="classattr">
                                <div class="attr variable">
            <span class="name">addr_info</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.addr_info"></a>
    
    

                            </div>
                            <div id="InlineProcessor.host_names" class="classattr">
                                <div class="attr variable">
            <span class="name">host_names</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.host_names"></a>
    
    

                            </div>
                            <div id="InlineProcessor.is_in_raw_mode" class="classattr">
                                <div class="attr variable">
            <span class="name">is_in_raw_mode</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.is_in_raw_mode"></a>
    
    

                            </div>
                            <div id="InlineProcessor.output_messages" class="classattr">
                                <div class="attr variable">
            <span class="name">output_messages</span>

        
    </div>
    <a class="headerlink" href="#InlineProcessor.output_messages"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.io.asock_io.versions.v_1.abstract.InlineWorkerBase</dt>
                                <dd id="InlineProcessor.on__data_received" class="function">on__data_received</dd>
                <dd id="InlineProcessor.on__output_buffers_are_empty" class="function">on__output_buffers_are_empty</dd>
                <dd id="InlineProcessor.on__connection_lost" class="function">on__connection_lost</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Client">
                            <input id="Client-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Client</span>:

                <label class="view-source-button" for="Client-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Client"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Client-316"><a href="#Client-316"><span class="linenos">316</span></a><span class="k">class</span> <span class="nc">Client</span><span class="p">:</span>
</span><span id="Client-317"><a href="#Client-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_settings</span><span class="p">:</span> <span class="n">ConnectionSettings</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection_id</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="Client-318"><a href="#Client-318"><span class="linenos">318</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot; Dasdfd safd</span>
</span><span id="Client-319"><a href="#Client-319"><span class="linenos">319</span></a>
</span><span id="Client-320"><a href="#Client-320"><span class="linenos">320</span></a><span class="sd">        :param client_id: ID of the expected client</span>
</span><span id="Client-321"><a href="#Client-321"><span class="linenos">321</span></a><span class="sd">        :param connection_id: ID of the connection</span>
</span><span id="Client-322"><a href="#Client-322"><span class="linenos">322</span></a><span class="sd">        :param connection_settings: useful ConnectionSettings parameters are {connection_type, keyword} - for a client,</span>
</span><span id="Client-323"><a href="#Client-323"><span class="linenos">323</span></a><span class="sd">            and all - for the super server.</span>
</span><span id="Client-324"><a href="#Client-324"><span class="linenos">324</span></a>
</span><span id="Client-325"><a href="#Client-325"><span class="linenos">325</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Client-326"><a href="#Client-326"><span class="linenos">326</span></a>
</span><span id="Client-327"><a href="#Client-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="Client-328"><a href="#Client-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="Client-329"><a href="#Client-329"><span class="linenos">329</span></a>        <span class="c1"># self.__connection = None  # Нельзя! Потому что в этом случае, объект клиента станет несериализуемым</span>
</span><span id="Client-330"><a href="#Client-330"><span class="linenos">330</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__connection</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Можно! Сделаем сериализуемым через переопределение магических методов</span>
</span><span id="Client-331"><a href="#Client-331"><span class="linenos">331</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span> <span class="o">=</span> <span class="n">connection_settings</span>
</span><span id="Client-332"><a href="#Client-332"><span class="linenos">332</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span><span id="Client-333"><a href="#Client-333"><span class="linenos">333</span></a>
</span><span id="Client-334"><a href="#Client-334"><span class="linenos">334</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_client_connection</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Client-335"><a href="#Client-335"><span class="linenos">335</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_connection_without_handshake</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Client-336"><a href="#Client-336"><span class="linenos">336</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">this_is_unknown_client</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Client-337"><a href="#Client-337"><span class="linenos">337</span></a>
</span><span id="Client-338"><a href="#Client-338"><span class="linenos">338</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">obj_for_inline_processing</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Client-339"><a href="#Client-339"><span class="linenos">339</span></a>
</span><span id="Client-340"><a href="#Client-340"><span class="linenos">340</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Client-341"><a href="#Client-341"><span class="linenos">341</span></a>        <span class="c1"># data_for_pickling = (</span>
</span><span id="Client-342"><a href="#Client-342"><span class="linenos">342</span></a>        <span class="c1">#     self.id,</span>
</span><span id="Client-343"><a href="#Client-343"><span class="linenos">343</span></a>        <span class="c1">#     self.connection_id,</span>
</span><span id="Client-344"><a href="#Client-344"><span class="linenos">344</span></a>        <span class="c1">#     self.connection_settings,</span>
</span><span id="Client-345"><a href="#Client-345"><span class="linenos">345</span></a>        <span class="c1">#     self.will_use_raw_client_connection,</span>
</span><span id="Client-346"><a href="#Client-346"><span class="linenos">346</span></a>        <span class="c1">#     self.will_use_raw_connection_without_handshake,</span>
</span><span id="Client-347"><a href="#Client-347"><span class="linenos">347</span></a>        <span class="c1">#     self.this_is_unknown_client,</span>
</span><span id="Client-348"><a href="#Client-348"><span class="linenos">348</span></a>        <span class="c1">#     self.obj_for_inline_processing</span>
</span><span id="Client-349"><a href="#Client-349"><span class="linenos">349</span></a>        <span class="c1"># )</span>
</span><span id="Client-350"><a href="#Client-350"><span class="linenos">350</span></a>        <span class="c1"># return data_for_pickling</span>
</span><span id="Client-351"><a href="#Client-351"><span class="linenos">351</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> \
</span><span id="Client-352"><a href="#Client-352"><span class="linenos">352</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span><span class="p">,</span> \
</span><span id="Client-353"><a href="#Client-353"><span class="linenos">353</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span><span class="p">,</span> \
</span><span id="Client-354"><a href="#Client-354"><span class="linenos">354</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_client_connection</span><span class="p">,</span> \
</span><span id="Client-355"><a href="#Client-355"><span class="linenos">355</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_connection_without_handshake</span><span class="p">,</span> \
</span><span id="Client-356"><a href="#Client-356"><span class="linenos">356</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">this_is_unknown_client</span><span class="p">,</span> \
</span><span id="Client-357"><a href="#Client-357"><span class="linenos">357</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">obj_for_inline_processing</span>
</span><span id="Client-358"><a href="#Client-358"><span class="linenos">358</span></a>
</span><span id="Client-359"><a href="#Client-359"><span class="linenos">359</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data_after_unpickling</span><span class="p">):</span>
</span><span id="Client-360"><a href="#Client-360"><span class="linenos">360</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_client_connection</span><span class="p">,</span> \
</span><span id="Client-361"><a href="#Client-361"><span class="linenos">361</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_connection_without_handshake</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">this_is_unknown_client</span><span class="p">,</span> \
</span><span id="Client-362"><a href="#Client-362"><span class="linenos">362</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">obj_for_inline_processing</span> <span class="o">=</span> <span class="n">data_after_unpickling</span>
</span><span id="Client-363"><a href="#Client-363"><span class="linenos">363</span></a>
</span><span id="Client-364"><a href="#Client-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__connection</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            <div id="Client.__init__" class="classattr">
                                        <input id="Client.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Client</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">connection_settings</span><span class="p">:</span> <span class="n"><a href="#ConnectionSettings">ConnectionSettings</a></span>,</span><span class="param">	<span class="n">client_id</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">connection_id</span><span class="o">=</span><span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="Client.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Client.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Client.__init__-317"><a href="#Client.__init__-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_settings</span><span class="p">:</span> <span class="n">ConnectionSettings</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection_id</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="Client.__init__-318"><a href="#Client.__init__-318"><span class="linenos">318</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot; Dasdfd safd</span>
</span><span id="Client.__init__-319"><a href="#Client.__init__-319"><span class="linenos">319</span></a>
</span><span id="Client.__init__-320"><a href="#Client.__init__-320"><span class="linenos">320</span></a><span class="sd">        :param client_id: ID of the expected client</span>
</span><span id="Client.__init__-321"><a href="#Client.__init__-321"><span class="linenos">321</span></a><span class="sd">        :param connection_id: ID of the connection</span>
</span><span id="Client.__init__-322"><a href="#Client.__init__-322"><span class="linenos">322</span></a><span class="sd">        :param connection_settings: useful ConnectionSettings parameters are {connection_type, keyword} - for a client,</span>
</span><span id="Client.__init__-323"><a href="#Client.__init__-323"><span class="linenos">323</span></a><span class="sd">            and all - for the super server.</span>
</span><span id="Client.__init__-324"><a href="#Client.__init__-324"><span class="linenos">324</span></a>
</span><span id="Client.__init__-325"><a href="#Client.__init__-325"><span class="linenos">325</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Client.__init__-326"><a href="#Client.__init__-326"><span class="linenos">326</span></a>
</span><span id="Client.__init__-327"><a href="#Client.__init__-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="Client.__init__-328"><a href="#Client.__init__-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="Client.__init__-329"><a href="#Client.__init__-329"><span class="linenos">329</span></a>        <span class="c1"># self.__connection = None  # Нельзя! Потому что в этом случае, объект клиента станет несериализуемым</span>
</span><span id="Client.__init__-330"><a href="#Client.__init__-330"><span class="linenos">330</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__connection</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Можно! Сделаем сериализуемым через переопределение магических методов</span>
</span><span id="Client.__init__-331"><a href="#Client.__init__-331"><span class="linenos">331</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span> <span class="o">=</span> <span class="n">connection_settings</span>
</span><span id="Client.__init__-332"><a href="#Client.__init__-332"><span class="linenos">332</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span><span id="Client.__init__-333"><a href="#Client.__init__-333"><span class="linenos">333</span></a>
</span><span id="Client.__init__-334"><a href="#Client.__init__-334"><span class="linenos">334</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_client_connection</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Client.__init__-335"><a href="#Client.__init__-335"><span class="linenos">335</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">will_use_raw_connection_without_handshake</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Client.__init__-336"><a href="#Client.__init__-336"><span class="linenos">336</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">this_is_unknown_client</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Client.__init__-337"><a href="#Client.__init__-337"><span class="linenos">337</span></a>
</span><span id="Client.__init__-338"><a href="#Client.__init__-338"><span class="linenos">338</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">obj_for_inline_processing</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


            <div class="docstring"><p>Dasdfd safd</p>

<p>:param client_id: ID of the expected client
:param connection_id: ID of the connection
:param connection_settings: useful ConnectionSettings parameters are {connection_type, keyword} - for a client,
    and all - for the super server.</p>
</div>


                            </div>
                            <div id="Client.id" class="classattr">
                                <div class="attr variable">
            <span class="name">id</span>

        
    </div>
    <a class="headerlink" href="#Client.id"></a>
    
    

                            </div>
                            <div id="Client.connection_id" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_id</span>

        
    </div>
    <a class="headerlink" href="#Client.connection_id"></a>
    
    

                            </div>
                            <div id="Client.connection_settings" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_settings</span>

        
    </div>
    <a class="headerlink" href="#Client.connection_settings"></a>
    
    

                            </div>
                            <div id="Client.will_use_raw_client_connection" class="classattr">
                                <div class="attr variable">
            <span class="name">will_use_raw_client_connection</span>

        
    </div>
    <a class="headerlink" href="#Client.will_use_raw_client_connection"></a>
    
    

                            </div>
                            <div id="Client.will_use_raw_connection_without_handshake" class="classattr">
                                <div class="attr variable">
            <span class="name">will_use_raw_connection_without_handshake</span>

        
    </div>
    <a class="headerlink" href="#Client.will_use_raw_connection_without_handshake"></a>
    
    

                            </div>
                            <div id="Client.this_is_unknown_client" class="classattr">
                                <div class="attr variable">
            <span class="name">this_is_unknown_client</span>

        
    </div>
    <a class="headerlink" href="#Client.this_is_unknown_client"></a>
    
    

                            </div>
                            <div id="Client.obj_for_inline_processing" class="classattr">
                                <div class="attr variable">
            <span class="name">obj_for_inline_processing</span>

        
    </div>
    <a class="headerlink" href="#Client.obj_for_inline_processing"></a>
    
    

                            </div>
                </section>
                <section id="CheckIsRawConnection">
                            <input id="CheckIsRawConnection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CheckIsRawConnection</span>:

                <label class="view-source-button" for="CheckIsRawConnection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CheckIsRawConnection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CheckIsRawConnection-367"><a href="#CheckIsRawConnection-367"><span class="linenos">367</span></a><span class="k">class</span> <span class="nc">CheckIsRawConnection</span><span class="p">:</span>
</span><span id="CheckIsRawConnection-368"><a href="#CheckIsRawConnection-368"><span class="linenos">368</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asock_io_core</span><span class="p">:</span> <span class="s1">&#39;ASockIOCore&#39;</span><span class="p">,</span> <span class="n">connection_info</span><span class="p">:</span> <span class="n">Connection</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="CheckIsRawConnection-369"><a href="#CheckIsRawConnection-369"><span class="linenos">369</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="CheckIsRawConnection-370"><a href="#CheckIsRawConnection-370"><span class="linenos">370</span></a><span class="sd">        :param asock_io_core:</span>
</span><span id="CheckIsRawConnection-371"><a href="#CheckIsRawConnection-371"><span class="linenos">371</span></a><span class="sd">        :param connection_info:</span>
</span><span id="CheckIsRawConnection-372"><a href="#CheckIsRawConnection-372"><span class="linenos">372</span></a><span class="sd">        :return: &quot;True&quot; if it is RAW connection for Unknow Client. &quot;False&quot; otherwise.</span>
</span><span id="CheckIsRawConnection-373"><a href="#CheckIsRawConnection-373"><span class="linenos">373</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="CheckIsRawConnection-374"><a href="#CheckIsRawConnection-374"><span class="linenos">374</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="CheckIsRawConnection-375"><a href="#CheckIsRawConnection-375"><span class="linenos">375</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="CheckIsRawConnection-376"><a href="#CheckIsRawConnection-376"><span class="linenos">376</span></a>            <span class="k">if</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">conn</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">family</span> <span class="ow">in</span> <span class="p">{</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">AF_INET6</span><span class="p">}:</span>
</span><span id="CheckIsRawConnection-377"><a href="#CheckIsRawConnection-377"><span class="linenos">377</span></a>                <span class="k">if</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">addr</span><span class="o">.</span><span class="n">result</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">asock_io_core</span><span class="o">.</span><span class="n">set_of_gate_addresses</span><span class="p">:</span>
</span><span id="CheckIsRawConnection-378"><a href="#CheckIsRawConnection-378"><span class="linenos">378</span></a>                    <span class="c1"># If connected not from local IP address</span>
</span><span id="CheckIsRawConnection-379"><a href="#CheckIsRawConnection-379"><span class="linenos">379</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="CheckIsRawConnection-380"><a href="#CheckIsRawConnection-380"><span class="linenos">380</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="CheckIsRawConnection-381"><a href="#CheckIsRawConnection-381"><span class="linenos">381</span></a>            <span class="k">pass</span>
</span><span id="CheckIsRawConnection-382"><a href="#CheckIsRawConnection-382"><span class="linenos">382</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>