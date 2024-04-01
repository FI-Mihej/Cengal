---
title: abstract
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.io<wbr>.asock_io<wbr>.versions<wbr>.v_1<wbr>.abstract    </h1>

                
                        <input id="mod-abstract-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-abstract-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="kn">import</span> <span class="nn">socket</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">import</span> <span class="nn">errno</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="kn">import</span> <span class="nn">copy</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="kn">import</span> <span class="nn">enum</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="kn">from</span> <span class="nn">contextlib</span> <span class="kn">import</span> <span class="n">contextmanager</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">deque</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Iterable</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="sd">Module Docstring</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.1&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="k">class</span> <span class="nc">LoopIsAlreadyBegun</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="sd">    You can not run NetIOUserApi.start() if it was already started (and still running).</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="k">pass</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="k">class</span> <span class="nc">WrongConnectionType</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="sd">    You cannot run NetIOUserApi.make_connection() for ConnectionType.active_accepted connection. This kind of</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="sd">    connections are made only from (and by) inside of IO loop and logic itself.</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="k">pass</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="k">class</span> <span class="nc">CanNotMakeConnection</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="sd">    Currently not used. If there will be some exception on connect() call - it will be raised without any changes.</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="k">pass</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="c1"># class ConnectionType(enum.Enum):</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="c1">#     passive = 0  # passive socket (bind())</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="c1">#     active_accepted = 1  # active accepted socket (accept())</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="c1">#     active_connected = 2  # active connected socket (connect())</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="c1">#</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="c1">#</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="c1"># class ConnectionState(enum.Enum):</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="c1">#     not_connected_yet = 0  # socket is not in connection process</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="c1">#     waiting_for_connection = 1  # socket is in connection process (async connection is delayed)</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="c1">#     connected = 2  # socket is successfully connected</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a><span class="c1">#     worker_fault = 3  # there was unhandled exception from one of the WorkerBase callbacks</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="c1">#     io_fault = 4  # there was some IO trouble</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="c1">#     waiting_for_disconnection = 5  # connection was marked as &quot;should be closed&quot; but was not closed yet</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="c1">#     disconnected = 6  # socket is closed</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="k">class</span> <span class="nc">NonSocketConnectionSettings</span><span class="p">:</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="k">pass</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="c1"># class ConnectionDirectionRole:</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="c1">#     server = 0</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="c1">#     client = 1</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="k">class</span> <span class="nc">ConnectionType</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="n">passive</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># passive socket (bind())</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="n">active_accepted</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># active accepted socket (accept())</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>    <span class="n">active_connected</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># active connected socket (connect())</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="k">class</span> <span class="nc">ConnectionState</span><span class="p">:</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    <span class="n">not_connected_yet</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># socket is not in connection process</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="n">waiting_for_connection</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># socket is in connection process (async connection is delayed)</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="n">connected</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># socket is successfully connected</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="n">worker_fault</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># there was unhandled exception from one of the WorkerBase callbacks</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="n">io_fault</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># there was some IO trouble</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="n">waiting_for_disconnection</span> <span class="o">=</span> <span class="mi">5</span>  <span class="c1"># connection was marked as &quot;should be closed&quot; but was not closed yet</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="n">disconnected</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># socket is closed</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a><span class="k">class</span> <span class="nc">ConnectionInfo</span><span class="p">:</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>                 <span class="n">worker_obj</span><span class="p">,</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a><span class="sd">        :param worker_obj: constructed worker object (see WorkerBase for more info). If this is a passive</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a><span class="sd">            connection - it (worker_obj) will be inherited by the descendant active_accepted connections</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="sd">            by copy.copy() call (see WorkerBase.__copy__() method for more info)</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a><span class="sd">        :param connection_type: see ConnectionType() description</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a><span class="sd">        :param socket_address:  see socket.bind()/socket.connect() docs</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a><span class="sd">        :param socket_family: see socket.socket() docs</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="sd">        :param socket_type: see socket.socket() docs</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a><span class="sd">        :param socket_protocol: see socket.socket() docs</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="sd">        :param socket_fileno: see socket.socket() docs</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="sd">        :param backlog: see socket.listen() docs</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">worker_obj</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a><span class="k">class</span> <span class="nc">Connection</span><span class="p">:</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a><span class="sd">    Connection class. Usually created by IO loop or by IO API. But you can also create it by yourself</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>                 <span class="n">connection_id</span><span class="p">,</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>                 <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span><span class="p">,</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>                 <span class="n">connection_and_address_pair</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">,</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span><span class="p">,</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>                 <span class="n">connection_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>                 <span class="p">):</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a><span class="sd">        :param connection_id: unique connection identificator (unique within the IO object). You may use some random</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a><span class="sd">            GUID if you are creating connection by your self.</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a><span class="sd">        :param connection_and_address_pair: (conn, address) tuple where conn is connected socket (or it can be socket</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a><span class="sd">            is in the process of connection. But only if it was made by IO loop.).</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a><span class="sd">        :param connection_state: see ConnectionState for more information</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a><span class="sd">        :param connection_name: name of the connection (if it was provided)</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_info</span> <span class="o">=</span> <span class="n">connection_info</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">conn</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">address</span> <span class="o">=</span> <span class="n">connection_and_address_pair</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_name</span> <span class="o">=</span> <span class="n">connection_name</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">worker_obj</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>  <span class="c1"># already read data</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="p">)</span>  <span class="c1"># this data should be written</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_write_call</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">add_must_be_written_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="sd">        Use this method to add data to output buffers</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a><span class="sd">        :param data: some new output data to be send through this connection</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="sd">        :return:</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a><span class="k">class</span> <span class="nc">NetIOUserApi</span><span class="p">:</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a><span class="sd">    You may rely and use freely use methods of this base class from inside your program or from inside your worker</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a><span class="sd">    (WorkerBase).</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_connections</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">passive_connections</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_id</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_name</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_fileno</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a><span class="sd">        Will start IO loop</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a><span class="sd">        :param destroy_on_finish: if True - destroy() will be called from inside of this method</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a><span class="sd">        :return:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a><span class="sd">        Will initiate IO loop stop process</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a><span class="sd">        :return:</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>    <span class="k">def</span> <span class="nf">make_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span><span class="o">-&gt;</span><span class="n">Connection</span><span class="p">:</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="sd">        Will create connection from given connection_info object. Than connection will be established. Immediate or</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a><span class="sd">        delayed - depends on the connection type:</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a><span class="sd">        - ConnectionType.passive - immediate;</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a><span class="sd">        - ConnectionType.active_connected - delayed.</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a><span class="sd">        In both cases WorkerBase.on_connect will be called immediately after connection will be successfully</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a><span class="sd">        established (IF it will be successfully established).</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a><span class="sd">        :param name: name of the connection. If you&#39;ll provide it - you will be able to find this connection in</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a><span class="sd">            NetIOUserApi.connection_by_name dictionary by it&#39;s name.</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a><span class="sd">        :return:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a><span class="sd">        Will register already established connection. You need to use this method for example if you have already</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a><span class="sd">        connected socket</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a><span class="sd">        :param connection:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a><span class="sd">        :return:</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a><span class="sd">        Will close and remove connection</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a><span class="sd">        :param connection:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a><span class="sd">        :return:</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>    <span class="k">def</span> <span class="nf">check_is_connection_need_to_sent_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a><span class="sd">        Will check connection to output data presence. It is automatically called after EACH WorkerBase callback call</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a><span class="sd">        by the IO loop. But if you are filling other connection&#39;s output buffer - you&#39;ll need to make this call for that</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a><span class="sd">        connection by your self.</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a><span class="sd">        :param connection:</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a><span class="sd">        :return:</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a><span class="k">class</span> <span class="nc">NetIOCallbacks</span><span class="p">:</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a><span class="sd">    Callbacks from this class will be called from inside (and by) IOMethodBase loop.</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="nf">on_accept_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="nf">on_connected</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>    <span class="k">def</span> <span class="nf">on_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>    <span class="k">def</span> <span class="nf">on_close</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a><span class="k">class</span> <span class="nc">NetIOBase</span><span class="p">(</span><span class="n">NetIOUserApi</span><span class="p">,</span> <span class="n">NetIOCallbacks</span><span class="p">):</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a><span class="sd">    Base class for any IO implementation (Linux, BSD, Windows, cross platform, etc.).</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a><span class="sd">        :param transport: class of the desired IOMethod. Instance (object) will be created by NetIOBase itself</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">method</span> <span class="o">=</span> <span class="n">transport</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a><span class="k">class</span> <span class="nc">WorkerBase</span><span class="p">:</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a><span class="sd">    Base class for all workers.</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a><span class="sd">    on_* callbacks will be called by the IO loop.</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a><span class="sd">    General info:</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a><span class="sd">    You can read input data from self.connection at any time (see &quot;Caution&quot; section of __init__ doc string) from any</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a><span class="sd">    callback.</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a><span class="sd">    You can write output data (to be send) to self.connection at any time (see &quot;Caution&quot;) from any callback.</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api</span><span class="p">:</span> <span class="n">NetIOUserApi</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a><span class="sd">        Caution:</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a><span class="sd">        Please do not rely on self.api and self.connection inside of your __init__ constructor: it is guaranteed that</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a><span class="sd">        they will be set before any callback call, but not at the construction process.</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a><span class="sd">        :param api: link to the constructed network io object</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a><span class="sd">        :param connection: link to the constructed connection object</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">api</span> <span class="o">=</span> <span class="n">api</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection</span> <span class="o">=</span> <span class="n">connection</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>    <span class="k">def</span> <span class="nf">on_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a><span class="sd">        Will be called after connection successfully established</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="sd">        :return:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        <span class="k">pass</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a><span class="sd">        Will be called if there is some NEW data in the connection input buffer</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a><span class="sd">        :return:</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="k">pass</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>    <span class="k">def</span> <span class="nf">on_no_more_data_to_write</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a><span class="sd">        Will be called after all data is sent.</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a><span class="sd">        Normally it will be called once (one single shot after each portion of out data is sent).</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a><span class="sd">        If you&#39;ll set self.connection.force_write_call to True state - this callback may be called continuously</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a><span class="sd">        (but not guaranteed: it depends of used IOMethod implementation)</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a><span class="sd">        :return:</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="k">pass</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>    <span class="k">def</span> <span class="nf">on_connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a><span class="sd">        Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a><span class="sd">        At this time, self.connection.connection_state is already set to ConnectionState.disconnected.</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a><span class="sd">        :return:</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>        <span class="k">pass</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a><span class="sd">        This method SHOULD be implemented. It should create a new instance and copy some global (shared) data from</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a><span class="sd">        current object to that new instance. It will be called when new peer is connected to existing passive connection</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a><span class="sd">        So this is the way you may use to give all new connection some links to some global data by worker object of</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a><span class="sd">        the passive connection replication process.</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a><span class="sd">        :return:</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a><span class="k">class</span> <span class="nc">InlineWorkerBase</span><span class="p">:</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;client_id&#39;</span><span class="p">,</span> <span class="s1">&#39;keyword&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_family&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_type&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_proto&#39;</span><span class="p">,</span> <span class="s1">&#39;addr_info&#39;</span><span class="p">,</span> <span class="s1">&#39;host_names&#39;</span><span class="p">,</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>                 <span class="s1">&#39;is_in_raw_mode&#39;</span><span class="p">,</span> <span class="s1">&#39;__set__is_in_raw_mode&#39;</span><span class="p">,</span> <span class="s1">&#39;__set__mark_socket_as_should_be_closed_immediately&#39;</span><span class="p">,</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>                 <span class="s1">&#39;__set__mark_socket_as_ready_to_be_closed&#39;</span><span class="p">,</span> <span class="s1">&#39;__external_parameters_set_trigger&#39;</span><span class="p">,</span> <span class="s1">&#39;output_messages&#39;</span><span class="p">,</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>                 <span class="s1">&#39;__hold__client_id&#39;</span><span class="p">)</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">socket_family</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_type</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_proto</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>                 <span class="n">addr_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">host_names</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a><span class="sd">        :param keyword: client keyword. You may check for a known keywords to act appropriately</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a><span class="sd">        :param socket_family:</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a><span class="sd">        :param socket_type:</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a><span class="sd">        :param socket_proto:</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a><span class="sd">        :param addr_info: result of socket.getaddrinfo() call</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a><span class="sd">        :param host_names: result of socket.gethostbyaddr() call</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="n">keyword</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_proto</span> <span class="o">=</span> <span class="n">socket_proto</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span> <span class="o">=</span> <span class="n">addr_info</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span> <span class="o">=</span> <span class="n">host_names</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_in_raw_mode</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="c1"># self.output_messages = FIFODequeWithLengthControl()</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_messages</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="c1"># self.output_messages = list()</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>    <span class="k">def</span> <span class="nf">on__data_received</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a><span class="sd">        Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a><span class="sd">        Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a><span class="sd">        be logged</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a><span class="sd">        :param data: piece of input data if connection is in RAW-mode and full message otherwise.</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        <span class="k">pass</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>    <span class="k">def</span> <span class="nf">on__output_buffers_are_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a><span class="sd">        Will be called immediately when all output data was send.</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a><span class="sd">        Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a><span class="sd">        Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a><span class="sd">        be logged</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="k">pass</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>    <span class="k">def</span> <span class="nf">on__connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a><span class="sd">        Will be called after connection was closed. Current Inline Processor object will be destroyed after this call.</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a><span class="sd">        Situation with unhandled exception will be logged.</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>        <span class="k">pass</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>    <span class="k">def</span> <span class="nf">set__is_in_raw_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_in_raw_mode</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_should_be_closed_immediately</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_ready_to_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a><span class="nd">@contextmanager</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a><span class="k">def</span> <span class="nf">net_io</span><span class="p">(</span><span class="n">net_io_obj</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a><span class="sd">    Context manager.</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a><span class="sd">    Usage:</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a><span class="sd">    main_io = NetIOBase()</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a><span class="sd">    with(net_io(main_io)) as io:</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a><span class="sd">        print(&#39;Preparing connections&#39;)</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a><span class="sd">        connection1 = io.make_connection(...)</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a><span class="sd">        connection2 = io.make_connection(...)</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a><span class="sd">        k = c + 12</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a><span class="sd">        ...</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a><span class="sd">        connectionN = io.make_connection(...)</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a><span class="sd">        print(&#39;Starting IO loop&#39;)</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a><span class="sd">    print(&#39;IO loop was finished properly&#39;)</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a><span class="sd">    :param net_io_obj: constructed IO instance (object)</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a><span class="sd">    :return:</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="k">yield</span> <span class="n">net_io_obj</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>        <span class="n">net_io_obj</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="n">net_io_obj</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a><span class="k">class</span> <span class="nc">IOLoopBase</span><span class="p">:</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a><span class="sd">    Base class for all IOMethod implementation (select, epoll, overlapped io, kqueue, etc.)</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a><span class="sd">    All his methods are called by the NetIOBase instance.</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>        <span class="k">pass</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>    <span class="k">def</span> <span class="nf">loop_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a><span class="sd">        Single IO loop iteration.</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a><span class="sd">        This method holds all IOMethod logic.</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a><span class="sd">        :param timeout: float or int. If timeout is negative, the call will block until there is an event.</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a><span class="sd">        :return:</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a><span class="sd">        Initiates destruction process</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a><span class="sd">        :return:</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>    <span class="k">def</span> <span class="nf">set__can_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to read&quot; checks for socket</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a><span class="sd">        :return:</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>    <span class="k">def</span> <span class="nf">set__need_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to write&quot; checks for socket</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a><span class="sd">        :return:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>    <span class="k">def</span> <span class="nf">set__should_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a><span class="sd">        Mark socket as &quot;should be closed&quot;</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a><span class="sd">        :return:</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a><span class="sd">        Will add socket to the internal connections list</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a><span class="sd">        :return:</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a><span class="sd">        Will remove socket from the internal connections list</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a><span class="sd">        :return:</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            </section>
                <section id="LoopIsAlreadyBegun">
                            <input id="LoopIsAlreadyBegun-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LoopIsAlreadyBegun</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="LoopIsAlreadyBegun-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopIsAlreadyBegun"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopIsAlreadyBegun-44"><a href="#LoopIsAlreadyBegun-44"><span class="linenos">44</span></a><span class="k">class</span> <span class="nc">LoopIsAlreadyBegun</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="LoopIsAlreadyBegun-45"><a href="#LoopIsAlreadyBegun-45"><span class="linenos">45</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="LoopIsAlreadyBegun-46"><a href="#LoopIsAlreadyBegun-46"><span class="linenos">46</span></a><span class="sd">    You can not run NetIOUserApi.start() if it was already started (and still running).</span>
</span><span id="LoopIsAlreadyBegun-47"><a href="#LoopIsAlreadyBegun-47"><span class="linenos">47</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="LoopIsAlreadyBegun-48"><a href="#LoopIsAlreadyBegun-48"><span class="linenos">48</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>You can not run <a href="#NetIOUserApi.start">NetIOUserApi.start()</a> if it was already started (and still running).</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="LoopIsAlreadyBegun.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="LoopIsAlreadyBegun.with_traceback" class="function">with_traceback</dd>
                <dd id="LoopIsAlreadyBegun.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="WrongConnectionType">
                            <input id="WrongConnectionType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">WrongConnectionType</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="WrongConnectionType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WrongConnectionType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WrongConnectionType-51"><a href="#WrongConnectionType-51"><span class="linenos">51</span></a><span class="k">class</span> <span class="nc">WrongConnectionType</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="WrongConnectionType-52"><a href="#WrongConnectionType-52"><span class="linenos">52</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WrongConnectionType-53"><a href="#WrongConnectionType-53"><span class="linenos">53</span></a><span class="sd">    You cannot run NetIOUserApi.make_connection() for ConnectionType.active_accepted connection. This kind of</span>
</span><span id="WrongConnectionType-54"><a href="#WrongConnectionType-54"><span class="linenos">54</span></a><span class="sd">    connections are made only from (and by) inside of IO loop and logic itself.</span>
</span><span id="WrongConnectionType-55"><a href="#WrongConnectionType-55"><span class="linenos">55</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="WrongConnectionType-56"><a href="#WrongConnectionType-56"><span class="linenos">56</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>You cannot run <a href="#NetIOUserApi.make_connection">NetIOUserApi.make_connection()</a> for <a href="#ConnectionType.active_accepted">ConnectionType.active_accepted</a> connection. This kind of
connections are made only from (and by) inside of IO loop and logic itself.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="WrongConnectionType.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="WrongConnectionType.with_traceback" class="function">with_traceback</dd>
                <dd id="WrongConnectionType.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CanNotMakeConnection">
                            <input id="CanNotMakeConnection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CanNotMakeConnection</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="CanNotMakeConnection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CanNotMakeConnection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CanNotMakeConnection-59"><a href="#CanNotMakeConnection-59"><span class="linenos">59</span></a><span class="k">class</span> <span class="nc">CanNotMakeConnection</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="CanNotMakeConnection-60"><a href="#CanNotMakeConnection-60"><span class="linenos">60</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="CanNotMakeConnection-61"><a href="#CanNotMakeConnection-61"><span class="linenos">61</span></a><span class="sd">    Currently not used. If there will be some exception on connect() call - it will be raised without any changes.</span>
</span><span id="CanNotMakeConnection-62"><a href="#CanNotMakeConnection-62"><span class="linenos">62</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="CanNotMakeConnection-63"><a href="#CanNotMakeConnection-63"><span class="linenos">63</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Currently not used. If there will be some exception on connect() call - it will be raised without any changes.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="CanNotMakeConnection.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="CanNotMakeConnection.with_traceback" class="function">with_traceback</dd>
                <dd id="CanNotMakeConnection.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="NonSocketConnectionSettings">
                            <input id="NonSocketConnectionSettings-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">NonSocketConnectionSettings</span>:

                <label class="view-source-button" for="NonSocketConnectionSettings-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NonSocketConnectionSettings"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NonSocketConnectionSettings-82"><a href="#NonSocketConnectionSettings-82"><span class="linenos">82</span></a><span class="k">class</span> <span class="nc">NonSocketConnectionSettings</span><span class="p">:</span>
</span><span id="NonSocketConnectionSettings-83"><a href="#NonSocketConnectionSettings-83"><span class="linenos">83</span></a>    <span class="k">pass</span>
</span></pre></div>


    

                </section>
                <section id="ConnectionType">
                            <input id="ConnectionType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ConnectionType</span>:

                <label class="view-source-button" for="ConnectionType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionType-91"><a href="#ConnectionType-91"><span class="linenos">91</span></a><span class="k">class</span> <span class="nc">ConnectionType</span><span class="p">:</span>
</span><span id="ConnectionType-92"><a href="#ConnectionType-92"><span class="linenos">92</span></a>    <span class="n">passive</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># passive socket (bind())</span>
</span><span id="ConnectionType-93"><a href="#ConnectionType-93"><span class="linenos">93</span></a>    <span class="n">active_accepted</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># active accepted socket (accept())</span>
</span><span id="ConnectionType-94"><a href="#ConnectionType-94"><span class="linenos">94</span></a>    <span class="n">active_connected</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># active connected socket (connect())</span>
</span></pre></div>


    

                            <div id="ConnectionType.passive" class="classattr">
                                <div class="attr variable">
            <span class="name">passive</span>        =
<span class="default_value">0</span>

        
    </div>
    <a class="headerlink" href="#ConnectionType.passive"></a>
    
    

                            </div>
                            <div id="ConnectionType.active_accepted" class="classattr">
                                <div class="attr variable">
            <span class="name">active_accepted</span>        =
<span class="default_value">1</span>

        
    </div>
    <a class="headerlink" href="#ConnectionType.active_accepted"></a>
    
    

                            </div>
                            <div id="ConnectionType.active_connected" class="classattr">
                                <div class="attr variable">
            <span class="name">active_connected</span>        =
<span class="default_value">2</span>

        
    </div>
    <a class="headerlink" href="#ConnectionType.active_connected"></a>
    
    

                            </div>
                </section>
                <section id="ConnectionState">
                            <input id="ConnectionState-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ConnectionState</span>:

                <label class="view-source-button" for="ConnectionState-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionState"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionState-97"><a href="#ConnectionState-97"><span class="linenos"> 97</span></a><span class="k">class</span> <span class="nc">ConnectionState</span><span class="p">:</span>
</span><span id="ConnectionState-98"><a href="#ConnectionState-98"><span class="linenos"> 98</span></a>    <span class="n">not_connected_yet</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># socket is not in connection process</span>
</span><span id="ConnectionState-99"><a href="#ConnectionState-99"><span class="linenos"> 99</span></a>    <span class="n">waiting_for_connection</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># socket is in connection process (async connection is delayed)</span>
</span><span id="ConnectionState-100"><a href="#ConnectionState-100"><span class="linenos">100</span></a>    <span class="n">connected</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># socket is successfully connected</span>
</span><span id="ConnectionState-101"><a href="#ConnectionState-101"><span class="linenos">101</span></a>    <span class="n">worker_fault</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># there was unhandled exception from one of the WorkerBase callbacks</span>
</span><span id="ConnectionState-102"><a href="#ConnectionState-102"><span class="linenos">102</span></a>    <span class="n">io_fault</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># there was some IO trouble</span>
</span><span id="ConnectionState-103"><a href="#ConnectionState-103"><span class="linenos">103</span></a>    <span class="n">waiting_for_disconnection</span> <span class="o">=</span> <span class="mi">5</span>  <span class="c1"># connection was marked as &quot;should be closed&quot; but was not closed yet</span>
</span><span id="ConnectionState-104"><a href="#ConnectionState-104"><span class="linenos">104</span></a>    <span class="n">disconnected</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># socket is closed</span>
</span></pre></div>


    

                            <div id="ConnectionState.not_connected_yet" class="classattr">
                                <div class="attr variable">
            <span class="name">not_connected_yet</span>        =
<span class="default_value">0</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.not_connected_yet"></a>
    
    

                            </div>
                            <div id="ConnectionState.waiting_for_connection" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_for_connection</span>        =
<span class="default_value">1</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.waiting_for_connection"></a>
    
    

                            </div>
                            <div id="ConnectionState.connected" class="classattr">
                                <div class="attr variable">
            <span class="name">connected</span>        =
<span class="default_value">2</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.connected"></a>
    
    

                            </div>
                            <div id="ConnectionState.worker_fault" class="classattr">
                                <div class="attr variable">
            <span class="name">worker_fault</span>        =
<span class="default_value">3</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.worker_fault"></a>
    
    

                            </div>
                            <div id="ConnectionState.io_fault" class="classattr">
                                <div class="attr variable">
            <span class="name">io_fault</span>        =
<span class="default_value">4</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.io_fault"></a>
    
    

                            </div>
                            <div id="ConnectionState.waiting_for_disconnection" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_for_disconnection</span>        =
<span class="default_value">5</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.waiting_for_disconnection"></a>
    
    

                            </div>
                            <div id="ConnectionState.disconnected" class="classattr">
                                <div class="attr variable">
            <span class="name">disconnected</span>        =
<span class="default_value">6</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.disconnected"></a>
    
    

                            </div>
                </section>
                <section id="ConnectionInfo">
                            <input id="ConnectionInfo-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ConnectionInfo</span>:

                <label class="view-source-button" for="ConnectionInfo-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionInfo"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionInfo-107"><a href="#ConnectionInfo-107"><span class="linenos">107</span></a><span class="k">class</span> <span class="nc">ConnectionInfo</span><span class="p">:</span>
</span><span id="ConnectionInfo-108"><a href="#ConnectionInfo-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="ConnectionInfo-109"><a href="#ConnectionInfo-109"><span class="linenos">109</span></a>                 <span class="n">worker_obj</span><span class="p">,</span>
</span><span id="ConnectionInfo-110"><a href="#ConnectionInfo-110"><span class="linenos">110</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="ConnectionInfo-111"><a href="#ConnectionInfo-111"><span class="linenos">111</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionInfo-112"><a href="#ConnectionInfo-112"><span class="linenos">112</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="ConnectionInfo-113"><a href="#ConnectionInfo-113"><span class="linenos">113</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="ConnectionInfo-114"><a href="#ConnectionInfo-114"><span class="linenos">114</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="ConnectionInfo-115"><a href="#ConnectionInfo-115"><span class="linenos">115</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionInfo-116"><a href="#ConnectionInfo-116"><span class="linenos">116</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
</span><span id="ConnectionInfo-117"><a href="#ConnectionInfo-117"><span class="linenos">117</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ConnectionInfo-118"><a href="#ConnectionInfo-118"><span class="linenos">118</span></a><span class="sd">        :param worker_obj: constructed worker object (see WorkerBase for more info). If this is a passive</span>
</span><span id="ConnectionInfo-119"><a href="#ConnectionInfo-119"><span class="linenos">119</span></a><span class="sd">            connection - it (worker_obj) will be inherited by the descendant active_accepted connections</span>
</span><span id="ConnectionInfo-120"><a href="#ConnectionInfo-120"><span class="linenos">120</span></a><span class="sd">            by copy.copy() call (see WorkerBase.__copy__() method for more info)</span>
</span><span id="ConnectionInfo-121"><a href="#ConnectionInfo-121"><span class="linenos">121</span></a><span class="sd">        :param connection_type: see ConnectionType() description</span>
</span><span id="ConnectionInfo-122"><a href="#ConnectionInfo-122"><span class="linenos">122</span></a><span class="sd">        :param socket_address:  see socket.bind()/socket.connect() docs</span>
</span><span id="ConnectionInfo-123"><a href="#ConnectionInfo-123"><span class="linenos">123</span></a><span class="sd">        :param socket_family: see socket.socket() docs</span>
</span><span id="ConnectionInfo-124"><a href="#ConnectionInfo-124"><span class="linenos">124</span></a><span class="sd">        :param socket_type: see socket.socket() docs</span>
</span><span id="ConnectionInfo-125"><a href="#ConnectionInfo-125"><span class="linenos">125</span></a><span class="sd">        :param socket_protocol: see socket.socket() docs</span>
</span><span id="ConnectionInfo-126"><a href="#ConnectionInfo-126"><span class="linenos">126</span></a><span class="sd">        :param socket_fileno: see socket.socket() docs</span>
</span><span id="ConnectionInfo-127"><a href="#ConnectionInfo-127"><span class="linenos">127</span></a><span class="sd">        :param backlog: see socket.listen() docs</span>
</span><span id="ConnectionInfo-128"><a href="#ConnectionInfo-128"><span class="linenos">128</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="ConnectionInfo-129"><a href="#ConnectionInfo-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">worker_obj</span>
</span><span id="ConnectionInfo-130"><a href="#ConnectionInfo-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="ConnectionInfo-131"><a href="#ConnectionInfo-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="ConnectionInfo-132"><a href="#ConnectionInfo-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="ConnectionInfo-133"><a href="#ConnectionInfo-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="ConnectionInfo-134"><a href="#ConnectionInfo-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="ConnectionInfo-135"><a href="#ConnectionInfo-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="ConnectionInfo-136"><a href="#ConnectionInfo-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span></pre></div>


    

                            <div id="ConnectionInfo.__init__" class="classattr">
                                        <input id="ConnectionInfo.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ConnectionInfo</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">worker_obj</span>,</span><span class="param">	<span class="n">connection_type</span><span class="p">:</span> <span class="n"><a href="#ConnectionType">ConnectionType</a></span>,</span><span class="param">	<span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">socket_family</span><span class="o">=&lt;</span><span class="n">AddressFamily</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">:</span> <span class="mi">2</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">socket_type</span><span class="o">=&lt;</span><span class="n">SocketKind</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span>,</span><span class="param">	<span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">backlog</span><span class="o">=</span><span class="mi">0</span></span>)</span>

                <label class="view-source-button" for="ConnectionInfo.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionInfo.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionInfo.__init__-108"><a href="#ConnectionInfo.__init__-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-109"><a href="#ConnectionInfo.__init__-109"><span class="linenos">109</span></a>                 <span class="n">worker_obj</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-110"><a href="#ConnectionInfo.__init__-110"><span class="linenos">110</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-111"><a href="#ConnectionInfo.__init__-111"><span class="linenos">111</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-112"><a href="#ConnectionInfo.__init__-112"><span class="linenos">112</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-113"><a href="#ConnectionInfo.__init__-113"><span class="linenos">113</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-114"><a href="#ConnectionInfo.__init__-114"><span class="linenos">114</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-115"><a href="#ConnectionInfo.__init__-115"><span class="linenos">115</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-116"><a href="#ConnectionInfo.__init__-116"><span class="linenos">116</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
</span><span id="ConnectionInfo.__init__-117"><a href="#ConnectionInfo.__init__-117"><span class="linenos">117</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ConnectionInfo.__init__-118"><a href="#ConnectionInfo.__init__-118"><span class="linenos">118</span></a><span class="sd">        :param worker_obj: constructed worker object (see WorkerBase for more info). If this is a passive</span>
</span><span id="ConnectionInfo.__init__-119"><a href="#ConnectionInfo.__init__-119"><span class="linenos">119</span></a><span class="sd">            connection - it (worker_obj) will be inherited by the descendant active_accepted connections</span>
</span><span id="ConnectionInfo.__init__-120"><a href="#ConnectionInfo.__init__-120"><span class="linenos">120</span></a><span class="sd">            by copy.copy() call (see WorkerBase.__copy__() method for more info)</span>
</span><span id="ConnectionInfo.__init__-121"><a href="#ConnectionInfo.__init__-121"><span class="linenos">121</span></a><span class="sd">        :param connection_type: see ConnectionType() description</span>
</span><span id="ConnectionInfo.__init__-122"><a href="#ConnectionInfo.__init__-122"><span class="linenos">122</span></a><span class="sd">        :param socket_address:  see socket.bind()/socket.connect() docs</span>
</span><span id="ConnectionInfo.__init__-123"><a href="#ConnectionInfo.__init__-123"><span class="linenos">123</span></a><span class="sd">        :param socket_family: see socket.socket() docs</span>
</span><span id="ConnectionInfo.__init__-124"><a href="#ConnectionInfo.__init__-124"><span class="linenos">124</span></a><span class="sd">        :param socket_type: see socket.socket() docs</span>
</span><span id="ConnectionInfo.__init__-125"><a href="#ConnectionInfo.__init__-125"><span class="linenos">125</span></a><span class="sd">        :param socket_protocol: see socket.socket() docs</span>
</span><span id="ConnectionInfo.__init__-126"><a href="#ConnectionInfo.__init__-126"><span class="linenos">126</span></a><span class="sd">        :param socket_fileno: see socket.socket() docs</span>
</span><span id="ConnectionInfo.__init__-127"><a href="#ConnectionInfo.__init__-127"><span class="linenos">127</span></a><span class="sd">        :param backlog: see socket.listen() docs</span>
</span><span id="ConnectionInfo.__init__-128"><a href="#ConnectionInfo.__init__-128"><span class="linenos">128</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="ConnectionInfo.__init__-129"><a href="#ConnectionInfo.__init__-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">worker_obj</span>
</span><span id="ConnectionInfo.__init__-130"><a href="#ConnectionInfo.__init__-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="ConnectionInfo.__init__-131"><a href="#ConnectionInfo.__init__-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="ConnectionInfo.__init__-132"><a href="#ConnectionInfo.__init__-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="ConnectionInfo.__init__-133"><a href="#ConnectionInfo.__init__-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="ConnectionInfo.__init__-134"><a href="#ConnectionInfo.__init__-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="ConnectionInfo.__init__-135"><a href="#ConnectionInfo.__init__-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="ConnectionInfo.__init__-136"><a href="#ConnectionInfo.__init__-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span></pre></div>


            <div class="docstring"><p>:param worker_obj: constructed worker object (see WorkerBase for more info). If this is a passive
    connection - it (worker_obj) will be inherited by the descendant active_accepted connections
    by copy.copy() call (see WorkerBase.__copy__() method for more info)
:param connection_type: see ConnectionType() description
:param socket_address:  see socket.bind()/socket.connect() docs
:param socket_family: see socket.socket() docs
:param socket_type: see socket.socket() docs
:param socket_protocol: see socket.socket() docs
:param socket_fileno: see socket.socket() docs
:param backlog: see socket.listen() docs</p>
</div>


                            </div>
                            <div id="ConnectionInfo.worker_obj" class="classattr">
                                <div class="attr variable">
            <span class="name">worker_obj</span>

        
    </div>
    <a class="headerlink" href="#ConnectionInfo.worker_obj"></a>
    
    

                            </div>
                            <div id="ConnectionInfo.connection_type" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_type</span>

        
    </div>
    <a class="headerlink" href="#ConnectionInfo.connection_type"></a>
    
    

                            </div>
                            <div id="ConnectionInfo.socket_address" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_address</span>

        
    </div>
    <a class="headerlink" href="#ConnectionInfo.socket_address"></a>
    
    

                            </div>
                            <div id="ConnectionInfo.socket_family" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_family</span>

        
    </div>
    <a class="headerlink" href="#ConnectionInfo.socket_family"></a>
    
    

                            </div>
                            <div id="ConnectionInfo.socket_type" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_type</span>

        
    </div>
    <a class="headerlink" href="#ConnectionInfo.socket_type"></a>
    
    

                            </div>
                            <div id="ConnectionInfo.socket_protocol" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_protocol</span>

        
    </div>
    <a class="headerlink" href="#ConnectionInfo.socket_protocol"></a>
    
    

                            </div>
                            <div id="ConnectionInfo.socket_fileno" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_fileno</span>

        
    </div>
    <a class="headerlink" href="#ConnectionInfo.socket_fileno"></a>
    
    

                            </div>
                            <div id="ConnectionInfo.backlog" class="classattr">
                                <div class="attr variable">
            <span class="name">backlog</span>

        
    </div>
    <a class="headerlink" href="#ConnectionInfo.backlog"></a>
    
    

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
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection-139"><a href="#Connection-139"><span class="linenos">139</span></a><span class="k">class</span> <span class="nc">Connection</span><span class="p">:</span>
</span><span id="Connection-140"><a href="#Connection-140"><span class="linenos">140</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection-141"><a href="#Connection-141"><span class="linenos">141</span></a><span class="sd">    Connection class. Usually created by IO loop or by IO API. But you can also create it by yourself</span>
</span><span id="Connection-142"><a href="#Connection-142"><span class="linenos">142</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="Connection-143"><a href="#Connection-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="Connection-144"><a href="#Connection-144"><span class="linenos">144</span></a>                 <span class="n">connection_id</span><span class="p">,</span>
</span><span id="Connection-145"><a href="#Connection-145"><span class="linenos">145</span></a>                 <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span><span class="p">,</span>
</span><span id="Connection-146"><a href="#Connection-146"><span class="linenos">146</span></a>                 <span class="n">connection_and_address_pair</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">,</span>
</span><span id="Connection-147"><a href="#Connection-147"><span class="linenos">147</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span><span class="p">,</span>
</span><span id="Connection-148"><a href="#Connection-148"><span class="linenos">148</span></a>                 <span class="n">connection_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="Connection-149"><a href="#Connection-149"><span class="linenos">149</span></a>                 <span class="p">):</span>
</span><span id="Connection-150"><a href="#Connection-150"><span class="linenos">150</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection-151"><a href="#Connection-151"><span class="linenos">151</span></a><span class="sd">        :param connection_id: unique connection identificator (unique within the IO object). You may use some random</span>
</span><span id="Connection-152"><a href="#Connection-152"><span class="linenos">152</span></a><span class="sd">            GUID if you are creating connection by your self.</span>
</span><span id="Connection-153"><a href="#Connection-153"><span class="linenos">153</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="Connection-154"><a href="#Connection-154"><span class="linenos">154</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="Connection-155"><a href="#Connection-155"><span class="linenos">155</span></a><span class="sd">        :param connection_and_address_pair: (conn, address) tuple where conn is connected socket (or it can be socket</span>
</span><span id="Connection-156"><a href="#Connection-156"><span class="linenos">156</span></a><span class="sd">            is in the process of connection. But only if it was made by IO loop.).</span>
</span><span id="Connection-157"><a href="#Connection-157"><span class="linenos">157</span></a><span class="sd">        :param connection_state: see ConnectionState for more information</span>
</span><span id="Connection-158"><a href="#Connection-158"><span class="linenos">158</span></a><span class="sd">        :param connection_name: name of the connection (if it was provided)</span>
</span><span id="Connection-159"><a href="#Connection-159"><span class="linenos">159</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection-160"><a href="#Connection-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="Connection-161"><a href="#Connection-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_info</span> <span class="o">=</span> <span class="n">connection_info</span>
</span><span id="Connection-162"><a href="#Connection-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">conn</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">address</span> <span class="o">=</span> <span class="n">connection_and_address_pair</span>
</span><span id="Connection-163"><a href="#Connection-163"><span class="linenos">163</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="Connection-164"><a href="#Connection-164"><span class="linenos">164</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_name</span> <span class="o">=</span> <span class="n">connection_name</span>
</span><span id="Connection-165"><a href="#Connection-165"><span class="linenos">165</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">worker_obj</span>
</span><span id="Connection-166"><a href="#Connection-166"><span class="linenos">166</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>  <span class="c1"># already read data</span>
</span><span id="Connection-167"><a href="#Connection-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="p">)</span>  <span class="c1"># this data should be written</span>
</span><span id="Connection-168"><a href="#Connection-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_write_call</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Connection-169"><a href="#Connection-169"><span class="linenos">169</span></a>
</span><span id="Connection-170"><a href="#Connection-170"><span class="linenos">170</span></a>    <span class="k">def</span> <span class="nf">add_must_be_written_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="Connection-171"><a href="#Connection-171"><span class="linenos">171</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection-172"><a href="#Connection-172"><span class="linenos">172</span></a><span class="sd">        Use this method to add data to output buffers</span>
</span><span id="Connection-173"><a href="#Connection-173"><span class="linenos">173</span></a><span class="sd">        :param data: some new output data to be send through this connection</span>
</span><span id="Connection-174"><a href="#Connection-174"><span class="linenos">174</span></a><span class="sd">        :return:</span>
</span><span id="Connection-175"><a href="#Connection-175"><span class="linenos">175</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection-176"><a href="#Connection-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Connection class. Usually created by IO loop or by IO API. But you can also create it by yourself</p>
</div>


                            <div id="Connection.__init__" class="classattr">
                                        <input id="Connection.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">connection_id</span>,</span><span class="param">	<span class="n">connection_info</span><span class="p">:</span> <span class="n"><a href="#ConnectionInfo">ConnectionInfo</a></span>,</span><span class="param">	<span class="n">connection_and_address_pair</span><span class="p">:</span> <span class="nb">tuple</span>,</span><span class="param">	<span class="n">connection_state</span><span class="p">:</span> <span class="n"><a href="#ConnectionState">ConnectionState</a></span>,</span><span class="param">	<span class="n">connection_name</span><span class="o">=</span><span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="Connection.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Connection.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.__init__-143"><a href="#Connection.__init__-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="Connection.__init__-144"><a href="#Connection.__init__-144"><span class="linenos">144</span></a>                 <span class="n">connection_id</span><span class="p">,</span>
</span><span id="Connection.__init__-145"><a href="#Connection.__init__-145"><span class="linenos">145</span></a>                 <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span><span class="p">,</span>
</span><span id="Connection.__init__-146"><a href="#Connection.__init__-146"><span class="linenos">146</span></a>                 <span class="n">connection_and_address_pair</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">,</span>
</span><span id="Connection.__init__-147"><a href="#Connection.__init__-147"><span class="linenos">147</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span><span class="p">,</span>
</span><span id="Connection.__init__-148"><a href="#Connection.__init__-148"><span class="linenos">148</span></a>                 <span class="n">connection_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="Connection.__init__-149"><a href="#Connection.__init__-149"><span class="linenos">149</span></a>                 <span class="p">):</span>
</span><span id="Connection.__init__-150"><a href="#Connection.__init__-150"><span class="linenos">150</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection.__init__-151"><a href="#Connection.__init__-151"><span class="linenos">151</span></a><span class="sd">        :param connection_id: unique connection identificator (unique within the IO object). You may use some random</span>
</span><span id="Connection.__init__-152"><a href="#Connection.__init__-152"><span class="linenos">152</span></a><span class="sd">            GUID if you are creating connection by your self.</span>
</span><span id="Connection.__init__-153"><a href="#Connection.__init__-153"><span class="linenos">153</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="Connection.__init__-154"><a href="#Connection.__init__-154"><span class="linenos">154</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="Connection.__init__-155"><a href="#Connection.__init__-155"><span class="linenos">155</span></a><span class="sd">        :param connection_and_address_pair: (conn, address) tuple where conn is connected socket (or it can be socket</span>
</span><span id="Connection.__init__-156"><a href="#Connection.__init__-156"><span class="linenos">156</span></a><span class="sd">            is in the process of connection. But only if it was made by IO loop.).</span>
</span><span id="Connection.__init__-157"><a href="#Connection.__init__-157"><span class="linenos">157</span></a><span class="sd">        :param connection_state: see ConnectionState for more information</span>
</span><span id="Connection.__init__-158"><a href="#Connection.__init__-158"><span class="linenos">158</span></a><span class="sd">        :param connection_name: name of the connection (if it was provided)</span>
</span><span id="Connection.__init__-159"><a href="#Connection.__init__-159"><span class="linenos">159</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection.__init__-160"><a href="#Connection.__init__-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="Connection.__init__-161"><a href="#Connection.__init__-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_info</span> <span class="o">=</span> <span class="n">connection_info</span>
</span><span id="Connection.__init__-162"><a href="#Connection.__init__-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">conn</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">address</span> <span class="o">=</span> <span class="n">connection_and_address_pair</span>
</span><span id="Connection.__init__-163"><a href="#Connection.__init__-163"><span class="linenos">163</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="Connection.__init__-164"><a href="#Connection.__init__-164"><span class="linenos">164</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_name</span> <span class="o">=</span> <span class="n">connection_name</span>
</span><span id="Connection.__init__-165"><a href="#Connection.__init__-165"><span class="linenos">165</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">worker_obj</span>
</span><span id="Connection.__init__-166"><a href="#Connection.__init__-166"><span class="linenos">166</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>  <span class="c1"># already read data</span>
</span><span id="Connection.__init__-167"><a href="#Connection.__init__-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="p">)</span>  <span class="c1"># this data should be written</span>
</span><span id="Connection.__init__-168"><a href="#Connection.__init__-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_write_call</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


            <div class="docstring"><p>:param connection_id: unique connection identificator (unique within the IO object). You may use some random
    GUID if you are creating connection by your self.
:param connection_info: new connection will be created using information provided in connection_info object.
    See ConnectionInfo() for more information
:param connection_and_address_pair: (conn, address) tuple where conn is connected socket (or it can be socket
    is in the process of connection. But only if it was made by IO loop.).
:param connection_state: see ConnectionState for more information
:param connection_name: name of the connection (if it was provided)</p>
</div>


                            </div>
                            <div id="Connection.connection_id" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_id</span>

        
    </div>
    <a class="headerlink" href="#Connection.connection_id"></a>
    
    

                            </div>
                            <div id="Connection.connection_info" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_info</span>

        
    </div>
    <a class="headerlink" href="#Connection.connection_info"></a>
    
    

                            </div>
                            <div id="Connection.connection_state" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_state</span>

        
    </div>
    <a class="headerlink" href="#Connection.connection_state"></a>
    
    

                            </div>
                            <div id="Connection.connection_name" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_name</span>

        
    </div>
    <a class="headerlink" href="#Connection.connection_name"></a>
    
    

                            </div>
                            <div id="Connection.worker_obj" class="classattr">
                                <div class="attr variable">
            <span class="name">worker_obj</span>

        
    </div>
    <a class="headerlink" href="#Connection.worker_obj"></a>
    
    

                            </div>
                            <div id="Connection.read_data" class="classattr">
                                <div class="attr variable">
            <span class="name">read_data</span>

        
    </div>
    <a class="headerlink" href="#Connection.read_data"></a>
    
    

                            </div>
                            <div id="Connection.must_be_written_data" class="classattr">
                                <div class="attr variable">
            <span class="name">must_be_written_data</span>

        
    </div>
    <a class="headerlink" href="#Connection.must_be_written_data"></a>
    
    

                            </div>
                            <div id="Connection.force_write_call" class="classattr">
                                <div class="attr variable">
            <span class="name">force_write_call</span>

        
    </div>
    <a class="headerlink" href="#Connection.force_write_call"></a>
    
    

                            </div>
                            <div id="Connection.add_must_be_written_data" class="classattr">
                                        <input id="Connection.add_must_be_written_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_must_be_written_data</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Connection.add_must_be_written_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Connection.add_must_be_written_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.add_must_be_written_data-170"><a href="#Connection.add_must_be_written_data-170"><span class="linenos">170</span></a>    <span class="k">def</span> <span class="nf">add_must_be_written_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="Connection.add_must_be_written_data-171"><a href="#Connection.add_must_be_written_data-171"><span class="linenos">171</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection.add_must_be_written_data-172"><a href="#Connection.add_must_be_written_data-172"><span class="linenos">172</span></a><span class="sd">        Use this method to add data to output buffers</span>
</span><span id="Connection.add_must_be_written_data-173"><a href="#Connection.add_must_be_written_data-173"><span class="linenos">173</span></a><span class="sd">        :param data: some new output data to be send through this connection</span>
</span><span id="Connection.add_must_be_written_data-174"><a href="#Connection.add_must_be_written_data-174"><span class="linenos">174</span></a><span class="sd">        :return:</span>
</span><span id="Connection.add_must_be_written_data-175"><a href="#Connection.add_must_be_written_data-175"><span class="linenos">175</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection.add_must_be_written_data-176"><a href="#Connection.add_must_be_written_data-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Use this method to add data to output buffers
:param data: some new output data to be send through this connection
:return:</p>
</div>


                            </div>
                </section>
                <section id="NetIOUserApi">
                            <input id="NetIOUserApi-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">NetIOUserApi</span>:

                <label class="view-source-button" for="NetIOUserApi-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOUserApi"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi-179"><a href="#NetIOUserApi-179"><span class="linenos">179</span></a><span class="k">class</span> <span class="nc">NetIOUserApi</span><span class="p">:</span>
</span><span id="NetIOUserApi-180"><a href="#NetIOUserApi-180"><span class="linenos">180</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-181"><a href="#NetIOUserApi-181"><span class="linenos">181</span></a><span class="sd">    You may rely and use freely use methods of this base class from inside your program or from inside your worker</span>
</span><span id="NetIOUserApi-182"><a href="#NetIOUserApi-182"><span class="linenos">182</span></a><span class="sd">    (WorkerBase).</span>
</span><span id="NetIOUserApi-183"><a href="#NetIOUserApi-183"><span class="linenos">183</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-184"><a href="#NetIOUserApi-184"><span class="linenos">184</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOUserApi-185"><a href="#NetIOUserApi-185"><span class="linenos">185</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="NetIOUserApi-186"><a href="#NetIOUserApi-186"><span class="linenos">186</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_connections</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="NetIOUserApi-187"><a href="#NetIOUserApi-187"><span class="linenos">187</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">passive_connections</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="NetIOUserApi-188"><a href="#NetIOUserApi-188"><span class="linenos">188</span></a>
</span><span id="NetIOUserApi-189"><a href="#NetIOUserApi-189"><span class="linenos">189</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_id</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NetIOUserApi-190"><a href="#NetIOUserApi-190"><span class="linenos">190</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_name</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NetIOUserApi-191"><a href="#NetIOUserApi-191"><span class="linenos">191</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_fileno</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NetIOUserApi-192"><a href="#NetIOUserApi-192"><span class="linenos">192</span></a>
</span><span id="NetIOUserApi-193"><a href="#NetIOUserApi-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="NetIOUserApi-194"><a href="#NetIOUserApi-194"><span class="linenos">194</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-195"><a href="#NetIOUserApi-195"><span class="linenos">195</span></a><span class="sd">        Will start IO loop</span>
</span><span id="NetIOUserApi-196"><a href="#NetIOUserApi-196"><span class="linenos">196</span></a><span class="sd">        :param destroy_on_finish: if True - destroy() will be called from inside of this method</span>
</span><span id="NetIOUserApi-197"><a href="#NetIOUserApi-197"><span class="linenos">197</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-198"><a href="#NetIOUserApi-198"><span class="linenos">198</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-199"><a href="#NetIOUserApi-199"><span class="linenos">199</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-200"><a href="#NetIOUserApi-200"><span class="linenos">200</span></a>
</span><span id="NetIOUserApi-201"><a href="#NetIOUserApi-201"><span class="linenos">201</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOUserApi-202"><a href="#NetIOUserApi-202"><span class="linenos">202</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-203"><a href="#NetIOUserApi-203"><span class="linenos">203</span></a><span class="sd">        Will initiate IO loop stop process</span>
</span><span id="NetIOUserApi-204"><a href="#NetIOUserApi-204"><span class="linenos">204</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-205"><a href="#NetIOUserApi-205"><span class="linenos">205</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-206"><a href="#NetIOUserApi-206"><span class="linenos">206</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-207"><a href="#NetIOUserApi-207"><span class="linenos">207</span></a>
</span><span id="NetIOUserApi-208"><a href="#NetIOUserApi-208"><span class="linenos">208</span></a>    <span class="k">def</span> <span class="nf">make_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span><span class="o">-&gt;</span><span class="n">Connection</span><span class="p">:</span>
</span><span id="NetIOUserApi-209"><a href="#NetIOUserApi-209"><span class="linenos">209</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-210"><a href="#NetIOUserApi-210"><span class="linenos">210</span></a><span class="sd">        Will create connection from given connection_info object. Than connection will be established. Immediate or</span>
</span><span id="NetIOUserApi-211"><a href="#NetIOUserApi-211"><span class="linenos">211</span></a><span class="sd">        delayed - depends on the connection type:</span>
</span><span id="NetIOUserApi-212"><a href="#NetIOUserApi-212"><span class="linenos">212</span></a><span class="sd">        - ConnectionType.passive - immediate;</span>
</span><span id="NetIOUserApi-213"><a href="#NetIOUserApi-213"><span class="linenos">213</span></a><span class="sd">        - ConnectionType.active_connected - delayed.</span>
</span><span id="NetIOUserApi-214"><a href="#NetIOUserApi-214"><span class="linenos">214</span></a><span class="sd">        In both cases WorkerBase.on_connect will be called immediately after connection will be successfully</span>
</span><span id="NetIOUserApi-215"><a href="#NetIOUserApi-215"><span class="linenos">215</span></a><span class="sd">        established (IF it will be successfully established).</span>
</span><span id="NetIOUserApi-216"><a href="#NetIOUserApi-216"><span class="linenos">216</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="NetIOUserApi-217"><a href="#NetIOUserApi-217"><span class="linenos">217</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="NetIOUserApi-218"><a href="#NetIOUserApi-218"><span class="linenos">218</span></a><span class="sd">        :param name: name of the connection. If you&#39;ll provide it - you will be able to find this connection in</span>
</span><span id="NetIOUserApi-219"><a href="#NetIOUserApi-219"><span class="linenos">219</span></a><span class="sd">            NetIOUserApi.connection_by_name dictionary by it&#39;s name.</span>
</span><span id="NetIOUserApi-220"><a href="#NetIOUserApi-220"><span class="linenos">220</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-221"><a href="#NetIOUserApi-221"><span class="linenos">221</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-222"><a href="#NetIOUserApi-222"><span class="linenos">222</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-223"><a href="#NetIOUserApi-223"><span class="linenos">223</span></a>
</span><span id="NetIOUserApi-224"><a href="#NetIOUserApi-224"><span class="linenos">224</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi-225"><a href="#NetIOUserApi-225"><span class="linenos">225</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-226"><a href="#NetIOUserApi-226"><span class="linenos">226</span></a><span class="sd">        Will register already established connection. You need to use this method for example if you have already</span>
</span><span id="NetIOUserApi-227"><a href="#NetIOUserApi-227"><span class="linenos">227</span></a><span class="sd">        connected socket</span>
</span><span id="NetIOUserApi-228"><a href="#NetIOUserApi-228"><span class="linenos">228</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi-229"><a href="#NetIOUserApi-229"><span class="linenos">229</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-230"><a href="#NetIOUserApi-230"><span class="linenos">230</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-231"><a href="#NetIOUserApi-231"><span class="linenos">231</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-232"><a href="#NetIOUserApi-232"><span class="linenos">232</span></a>
</span><span id="NetIOUserApi-233"><a href="#NetIOUserApi-233"><span class="linenos">233</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi-234"><a href="#NetIOUserApi-234"><span class="linenos">234</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-235"><a href="#NetIOUserApi-235"><span class="linenos">235</span></a><span class="sd">        Will close and remove connection</span>
</span><span id="NetIOUserApi-236"><a href="#NetIOUserApi-236"><span class="linenos">236</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi-237"><a href="#NetIOUserApi-237"><span class="linenos">237</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-238"><a href="#NetIOUserApi-238"><span class="linenos">238</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-239"><a href="#NetIOUserApi-239"><span class="linenos">239</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-240"><a href="#NetIOUserApi-240"><span class="linenos">240</span></a>
</span><span id="NetIOUserApi-241"><a href="#NetIOUserApi-241"><span class="linenos">241</span></a>    <span class="k">def</span> <span class="nf">check_is_connection_need_to_sent_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi-242"><a href="#NetIOUserApi-242"><span class="linenos">242</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-243"><a href="#NetIOUserApi-243"><span class="linenos">243</span></a><span class="sd">        Will check connection to output data presence. It is automatically called after EACH WorkerBase callback call</span>
</span><span id="NetIOUserApi-244"><a href="#NetIOUserApi-244"><span class="linenos">244</span></a><span class="sd">        by the IO loop. But if you are filling other connection&#39;s output buffer - you&#39;ll need to make this call for that</span>
</span><span id="NetIOUserApi-245"><a href="#NetIOUserApi-245"><span class="linenos">245</span></a><span class="sd">        connection by your self.</span>
</span><span id="NetIOUserApi-246"><a href="#NetIOUserApi-246"><span class="linenos">246</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi-247"><a href="#NetIOUserApi-247"><span class="linenos">247</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-248"><a href="#NetIOUserApi-248"><span class="linenos">248</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-249"><a href="#NetIOUserApi-249"><span class="linenos">249</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>You may rely and use freely use methods of this base class from inside your program or from inside your worker
(WorkerBase).</p>
</div>


                            <div id="NetIOUserApi.all_connections" class="classattr">
                                <div class="attr variable">
            <span class="name">all_connections</span>

        
    </div>
    <a class="headerlink" href="#NetIOUserApi.all_connections"></a>
    
    

                            </div>
                            <div id="NetIOUserApi.passive_connections" class="classattr">
                                <div class="attr variable">
            <span class="name">passive_connections</span>

        
    </div>
    <a class="headerlink" href="#NetIOUserApi.passive_connections"></a>
    
    

                            </div>
                            <div id="NetIOUserApi.connection_by_id" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_by_id</span>

        
    </div>
    <a class="headerlink" href="#NetIOUserApi.connection_by_id"></a>
    
    

                            </div>
                            <div id="NetIOUserApi.connection_by_name" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_by_name</span>

        
    </div>
    <a class="headerlink" href="#NetIOUserApi.connection_by_name"></a>
    
    

                            </div>
                            <div id="NetIOUserApi.connection_by_fileno" class="classattr">
                                <div class="attr variable">
            <span class="name">connection_by_fileno</span>

        
    </div>
    <a class="headerlink" href="#NetIOUserApi.connection_by_fileno"></a>
    
    

                            </div>
                            <div id="NetIOUserApi.start" class="classattr">
                                        <input id="NetIOUserApi.start-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOUserApi.start-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOUserApi.start"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.start-193"><a href="#NetIOUserApi.start-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="NetIOUserApi.start-194"><a href="#NetIOUserApi.start-194"><span class="linenos">194</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.start-195"><a href="#NetIOUserApi.start-195"><span class="linenos">195</span></a><span class="sd">        Will start IO loop</span>
</span><span id="NetIOUserApi.start-196"><a href="#NetIOUserApi.start-196"><span class="linenos">196</span></a><span class="sd">        :param destroy_on_finish: if True - destroy() will be called from inside of this method</span>
</span><span id="NetIOUserApi.start-197"><a href="#NetIOUserApi.start-197"><span class="linenos">197</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.start-198"><a href="#NetIOUserApi.start-198"><span class="linenos">198</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.start-199"><a href="#NetIOUserApi.start-199"><span class="linenos">199</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will start IO loop
:param destroy_on_finish: if True - destroy() will be called from inside of this method
:return:</p>
</div>


                            </div>
                            <div id="NetIOUserApi.stop" class="classattr">
                                        <input id="NetIOUserApi.stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOUserApi.stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOUserApi.stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.stop-201"><a href="#NetIOUserApi.stop-201"><span class="linenos">201</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOUserApi.stop-202"><a href="#NetIOUserApi.stop-202"><span class="linenos">202</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.stop-203"><a href="#NetIOUserApi.stop-203"><span class="linenos">203</span></a><span class="sd">        Will initiate IO loop stop process</span>
</span><span id="NetIOUserApi.stop-204"><a href="#NetIOUserApi.stop-204"><span class="linenos">204</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.stop-205"><a href="#NetIOUserApi.stop-205"><span class="linenos">205</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.stop-206"><a href="#NetIOUserApi.stop-206"><span class="linenos">206</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will initiate IO loop stop process
:return:</p>
</div>


                            </div>
                            <div id="NetIOUserApi.make_connection" class="classattr">
                                        <input id="NetIOUserApi.make_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">make_connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection_info</span><span class="p">:</span> <span class="n"><a href="#ConnectionInfo">ConnectionInfo</a></span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">name</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">) -> <span class="n"><a href="#Connection">Connection</a></span>:</span></span>

                <label class="view-source-button" for="NetIOUserApi.make_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOUserApi.make_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.make_connection-208"><a href="#NetIOUserApi.make_connection-208"><span class="linenos">208</span></a>    <span class="k">def</span> <span class="nf">make_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span><span class="o">-&gt;</span><span class="n">Connection</span><span class="p">:</span>
</span><span id="NetIOUserApi.make_connection-209"><a href="#NetIOUserApi.make_connection-209"><span class="linenos">209</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.make_connection-210"><a href="#NetIOUserApi.make_connection-210"><span class="linenos">210</span></a><span class="sd">        Will create connection from given connection_info object. Than connection will be established. Immediate or</span>
</span><span id="NetIOUserApi.make_connection-211"><a href="#NetIOUserApi.make_connection-211"><span class="linenos">211</span></a><span class="sd">        delayed - depends on the connection type:</span>
</span><span id="NetIOUserApi.make_connection-212"><a href="#NetIOUserApi.make_connection-212"><span class="linenos">212</span></a><span class="sd">        - ConnectionType.passive - immediate;</span>
</span><span id="NetIOUserApi.make_connection-213"><a href="#NetIOUserApi.make_connection-213"><span class="linenos">213</span></a><span class="sd">        - ConnectionType.active_connected - delayed.</span>
</span><span id="NetIOUserApi.make_connection-214"><a href="#NetIOUserApi.make_connection-214"><span class="linenos">214</span></a><span class="sd">        In both cases WorkerBase.on_connect will be called immediately after connection will be successfully</span>
</span><span id="NetIOUserApi.make_connection-215"><a href="#NetIOUserApi.make_connection-215"><span class="linenos">215</span></a><span class="sd">        established (IF it will be successfully established).</span>
</span><span id="NetIOUserApi.make_connection-216"><a href="#NetIOUserApi.make_connection-216"><span class="linenos">216</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="NetIOUserApi.make_connection-217"><a href="#NetIOUserApi.make_connection-217"><span class="linenos">217</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="NetIOUserApi.make_connection-218"><a href="#NetIOUserApi.make_connection-218"><span class="linenos">218</span></a><span class="sd">        :param name: name of the connection. If you&#39;ll provide it - you will be able to find this connection in</span>
</span><span id="NetIOUserApi.make_connection-219"><a href="#NetIOUserApi.make_connection-219"><span class="linenos">219</span></a><span class="sd">            NetIOUserApi.connection_by_name dictionary by it&#39;s name.</span>
</span><span id="NetIOUserApi.make_connection-220"><a href="#NetIOUserApi.make_connection-220"><span class="linenos">220</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.make_connection-221"><a href="#NetIOUserApi.make_connection-221"><span class="linenos">221</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.make_connection-222"><a href="#NetIOUserApi.make_connection-222"><span class="linenos">222</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will create connection from given connection_info object. Than connection will be established. Immediate or
delayed - depends on the connection type:</p>

<ul>
<li><a href="#ConnectionType.passive">ConnectionType.passive</a> - immediate;</li>
<li><a href="#ConnectionType.active_connected">ConnectionType.active_connected</a> - delayed.
In both cases <a href="#WorkerBase.on_connect">WorkerBase.on_connect</a> will be called immediately after connection will be successfully
established (IF it will be successfully established).
:param connection_info: new connection will be created using information provided in connection_info object.
See ConnectionInfo() for more information
:param name: name of the connection. If you'll provide it - you will be able to find this connection in
<a href="#NetIOUserApi.connection_by_name">NetIOUserApi.connection_by_name</a> dictionary by it's name.
:return:</li>
</ul>
</div>


                            </div>
                            <div id="NetIOUserApi.add_connection" class="classattr">
                                        <input id="NetIOUserApi.add_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOUserApi.add_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOUserApi.add_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.add_connection-224"><a href="#NetIOUserApi.add_connection-224"><span class="linenos">224</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi.add_connection-225"><a href="#NetIOUserApi.add_connection-225"><span class="linenos">225</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.add_connection-226"><a href="#NetIOUserApi.add_connection-226"><span class="linenos">226</span></a><span class="sd">        Will register already established connection. You need to use this method for example if you have already</span>
</span><span id="NetIOUserApi.add_connection-227"><a href="#NetIOUserApi.add_connection-227"><span class="linenos">227</span></a><span class="sd">        connected socket</span>
</span><span id="NetIOUserApi.add_connection-228"><a href="#NetIOUserApi.add_connection-228"><span class="linenos">228</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi.add_connection-229"><a href="#NetIOUserApi.add_connection-229"><span class="linenos">229</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.add_connection-230"><a href="#NetIOUserApi.add_connection-230"><span class="linenos">230</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.add_connection-231"><a href="#NetIOUserApi.add_connection-231"><span class="linenos">231</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will register already established connection. You need to use this method for example if you have already
connected socket
:param connection:
:return:</p>
</div>


                            </div>
                            <div id="NetIOUserApi.remove_connection" class="classattr">
                                        <input id="NetIOUserApi.remove_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOUserApi.remove_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOUserApi.remove_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.remove_connection-233"><a href="#NetIOUserApi.remove_connection-233"><span class="linenos">233</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi.remove_connection-234"><a href="#NetIOUserApi.remove_connection-234"><span class="linenos">234</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.remove_connection-235"><a href="#NetIOUserApi.remove_connection-235"><span class="linenos">235</span></a><span class="sd">        Will close and remove connection</span>
</span><span id="NetIOUserApi.remove_connection-236"><a href="#NetIOUserApi.remove_connection-236"><span class="linenos">236</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi.remove_connection-237"><a href="#NetIOUserApi.remove_connection-237"><span class="linenos">237</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.remove_connection-238"><a href="#NetIOUserApi.remove_connection-238"><span class="linenos">238</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.remove_connection-239"><a href="#NetIOUserApi.remove_connection-239"><span class="linenos">239</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will close and remove connection
:param connection:
:return:</p>
</div>


                            </div>
                            <div id="NetIOUserApi.check_is_connection_need_to_sent_data" class="classattr">
                                        <input id="NetIOUserApi.check_is_connection_need_to_sent_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_is_connection_need_to_sent_data</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOUserApi.check_is_connection_need_to_sent_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOUserApi.check_is_connection_need_to_sent_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-241"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-241"><span class="linenos">241</span></a>    <span class="k">def</span> <span class="nf">check_is_connection_need_to_sent_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-242"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-242"><span class="linenos">242</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-243"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-243"><span class="linenos">243</span></a><span class="sd">        Will check connection to output data presence. It is automatically called after EACH WorkerBase callback call</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-244"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-244"><span class="linenos">244</span></a><span class="sd">        by the IO loop. But if you are filling other connection&#39;s output buffer - you&#39;ll need to make this call for that</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-245"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-245"><span class="linenos">245</span></a><span class="sd">        connection by your self.</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-246"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-246"><span class="linenos">246</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-247"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-247"><span class="linenos">247</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-248"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-248"><span class="linenos">248</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-249"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-249"><span class="linenos">249</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will check connection to output data presence. It is automatically called after EACH WorkerBase callback call
by the IO loop. But if you are filling other connection's output buffer - you'll need to make this call for that
connection by your self.
:param connection:
:return:</p>
</div>


                            </div>
                </section>
                <section id="NetIOCallbacks">
                            <input id="NetIOCallbacks-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">NetIOCallbacks</span>:

                <label class="view-source-button" for="NetIOCallbacks-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOCallbacks"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks-252"><a href="#NetIOCallbacks-252"><span class="linenos">252</span></a><span class="k">class</span> <span class="nc">NetIOCallbacks</span><span class="p">:</span>
</span><span id="NetIOCallbacks-253"><a href="#NetIOCallbacks-253"><span class="linenos">253</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOCallbacks-254"><a href="#NetIOCallbacks-254"><span class="linenos">254</span></a><span class="sd">    Callbacks from this class will be called from inside (and by) IOMethodBase loop.</span>
</span><span id="NetIOCallbacks-255"><a href="#NetIOCallbacks-255"><span class="linenos">255</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="NetIOCallbacks-256"><a href="#NetIOCallbacks-256"><span class="linenos">256</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOCallbacks-257"><a href="#NetIOCallbacks-257"><span class="linenos">257</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="NetIOCallbacks-258"><a href="#NetIOCallbacks-258"><span class="linenos">258</span></a>
</span><span id="NetIOCallbacks-259"><a href="#NetIOCallbacks-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="nf">on_accept_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-260"><a href="#NetIOCallbacks-260"><span class="linenos">260</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOCallbacks-261"><a href="#NetIOCallbacks-261"><span class="linenos">261</span></a>
</span><span id="NetIOCallbacks-262"><a href="#NetIOCallbacks-262"><span class="linenos">262</span></a>    <span class="k">def</span> <span class="nf">on_connected</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-263"><a href="#NetIOCallbacks-263"><span class="linenos">263</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOCallbacks-264"><a href="#NetIOCallbacks-264"><span class="linenos">264</span></a>
</span><span id="NetIOCallbacks-265"><a href="#NetIOCallbacks-265"><span class="linenos">265</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-266"><a href="#NetIOCallbacks-266"><span class="linenos">266</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOCallbacks-267"><a href="#NetIOCallbacks-267"><span class="linenos">267</span></a>
</span><span id="NetIOCallbacks-268"><a href="#NetIOCallbacks-268"><span class="linenos">268</span></a>    <span class="k">def</span> <span class="nf">on_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-269"><a href="#NetIOCallbacks-269"><span class="linenos">269</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOCallbacks-270"><a href="#NetIOCallbacks-270"><span class="linenos">270</span></a>
</span><span id="NetIOCallbacks-271"><a href="#NetIOCallbacks-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="nf">on_close</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-272"><a href="#NetIOCallbacks-272"><span class="linenos">272</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Callbacks from this class will be called from inside (and by) IOMethodBase loop.</p>
</div>


                            <div id="NetIOCallbacks.on_accept_connection" class="classattr">
                                        <input id="NetIOCallbacks.on_accept_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_accept_connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOCallbacks.on_accept_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOCallbacks.on_accept_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_accept_connection-259"><a href="#NetIOCallbacks.on_accept_connection-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="nf">on_accept_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_accept_connection-260"><a href="#NetIOCallbacks.on_accept_connection-260"><span class="linenos">260</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="NetIOCallbacks.on_connected" class="classattr">
                                        <input id="NetIOCallbacks.on_connected-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_connected</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOCallbacks.on_connected-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOCallbacks.on_connected"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_connected-262"><a href="#NetIOCallbacks.on_connected-262"><span class="linenos">262</span></a>    <span class="k">def</span> <span class="nf">on_connected</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_connected-263"><a href="#NetIOCallbacks.on_connected-263"><span class="linenos">263</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="NetIOCallbacks.on_read" class="classattr">
                                        <input id="NetIOCallbacks.on_read-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_read</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOCallbacks.on_read-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOCallbacks.on_read"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_read-265"><a href="#NetIOCallbacks.on_read-265"><span class="linenos">265</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_read-266"><a href="#NetIOCallbacks.on_read-266"><span class="linenos">266</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="NetIOCallbacks.on_write" class="classattr">
                                        <input id="NetIOCallbacks.on_write-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_write</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOCallbacks.on_write-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOCallbacks.on_write"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_write-268"><a href="#NetIOCallbacks.on_write-268"><span class="linenos">268</span></a>    <span class="k">def</span> <span class="nf">on_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_write-269"><a href="#NetIOCallbacks.on_write-269"><span class="linenos">269</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="NetIOCallbacks.on_close" class="classattr">
                                        <input id="NetIOCallbacks.on_close-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_close</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOCallbacks.on_close-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOCallbacks.on_close"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_close-271"><a href="#NetIOCallbacks.on_close-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="nf">on_close</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_close-272"><a href="#NetIOCallbacks.on_close-272"><span class="linenos">272</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="NetIOBase">
                            <input id="NetIOBase-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">NetIOBase</span><wbr>(<span class="base"><a href="#NetIOUserApi">NetIOUserApi</a></span>, <span class="base"><a href="#NetIOCallbacks">NetIOCallbacks</a></span>):

                <label class="view-source-button" for="NetIOBase-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOBase"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOBase-275"><a href="#NetIOBase-275"><span class="linenos">275</span></a><span class="k">class</span> <span class="nc">NetIOBase</span><span class="p">(</span><span class="n">NetIOUserApi</span><span class="p">,</span> <span class="n">NetIOCallbacks</span><span class="p">):</span>
</span><span id="NetIOBase-276"><a href="#NetIOBase-276"><span class="linenos">276</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOBase-277"><a href="#NetIOBase-277"><span class="linenos">277</span></a><span class="sd">    Base class for any IO implementation (Linux, BSD, Windows, cross platform, etc.).</span>
</span><span id="NetIOBase-278"><a href="#NetIOBase-278"><span class="linenos">278</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="NetIOBase-279"><a href="#NetIOBase-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="NetIOBase-280"><a href="#NetIOBase-280"><span class="linenos">280</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOBase-281"><a href="#NetIOBase-281"><span class="linenos">281</span></a>
</span><span id="NetIOBase-282"><a href="#NetIOBase-282"><span class="linenos">282</span></a><span class="sd">        :param transport: class of the desired IOMethod. Instance (object) will be created by NetIOBase itself</span>
</span><span id="NetIOBase-283"><a href="#NetIOBase-283"><span class="linenos">283</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOBase-284"><a href="#NetIOBase-284"><span class="linenos">284</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="NetIOBase-285"><a href="#NetIOBase-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">method</span> <span class="o">=</span> <span class="n">transport</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="NetIOBase-286"><a href="#NetIOBase-286"><span class="linenos">286</span></a>
</span><span id="NetIOBase-287"><a href="#NetIOBase-287"><span class="linenos">287</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOBase-288"><a href="#NetIOBase-288"><span class="linenos">288</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Base class for any IO implementation (Linux, BSD, Windows, cross platform, etc.).</p>
</div>


                            <div id="NetIOBase.__init__" class="classattr">
                                        <input id="NetIOBase.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">NetIOBase</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">transport</span></span>)</span>

                <label class="view-source-button" for="NetIOBase.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOBase.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOBase.__init__-279"><a href="#NetIOBase.__init__-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="NetIOBase.__init__-280"><a href="#NetIOBase.__init__-280"><span class="linenos">280</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOBase.__init__-281"><a href="#NetIOBase.__init__-281"><span class="linenos">281</span></a>
</span><span id="NetIOBase.__init__-282"><a href="#NetIOBase.__init__-282"><span class="linenos">282</span></a><span class="sd">        :param transport: class of the desired IOMethod. Instance (object) will be created by NetIOBase itself</span>
</span><span id="NetIOBase.__init__-283"><a href="#NetIOBase.__init__-283"><span class="linenos">283</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOBase.__init__-284"><a href="#NetIOBase.__init__-284"><span class="linenos">284</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="NetIOBase.__init__-285"><a href="#NetIOBase.__init__-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">method</span> <span class="o">=</span> <span class="n">transport</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>:param transport: class of the desired IOMethod. Instance (object) will be created by NetIOBase itself</p>
</div>


                            </div>
                            <div id="NetIOBase.method" class="classattr">
                                <div class="attr variable">
            <span class="name">method</span>

        
    </div>
    <a class="headerlink" href="#NetIOBase.method"></a>
    
    

                            </div>
                            <div id="NetIOBase.destroy" class="classattr">
                                        <input id="NetIOBase.destroy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">destroy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NetIOBase.destroy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NetIOBase.destroy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOBase.destroy-287"><a href="#NetIOBase.destroy-287"><span class="linenos">287</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOBase.destroy-288"><a href="#NetIOBase.destroy-288"><span class="linenos">288</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#NetIOUserApi">NetIOUserApi</a></dt>
                                <dd id="NetIOBase.all_connections" class="variable"><a href="#NetIOUserApi.all_connections">all_connections</a></dd>
                <dd id="NetIOBase.passive_connections" class="variable"><a href="#NetIOUserApi.passive_connections">passive_connections</a></dd>
                <dd id="NetIOBase.connection_by_id" class="variable"><a href="#NetIOUserApi.connection_by_id">connection_by_id</a></dd>
                <dd id="NetIOBase.connection_by_name" class="variable"><a href="#NetIOUserApi.connection_by_name">connection_by_name</a></dd>
                <dd id="NetIOBase.connection_by_fileno" class="variable"><a href="#NetIOUserApi.connection_by_fileno">connection_by_fileno</a></dd>
                <dd id="NetIOBase.start" class="function"><a href="#NetIOUserApi.start">start</a></dd>
                <dd id="NetIOBase.stop" class="function"><a href="#NetIOUserApi.stop">stop</a></dd>
                <dd id="NetIOBase.make_connection" class="function"><a href="#NetIOUserApi.make_connection">make_connection</a></dd>
                <dd id="NetIOBase.add_connection" class="function"><a href="#NetIOUserApi.add_connection">add_connection</a></dd>
                <dd id="NetIOBase.remove_connection" class="function"><a href="#NetIOUserApi.remove_connection">remove_connection</a></dd>
                <dd id="NetIOBase.check_is_connection_need_to_sent_data" class="function"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data">check_is_connection_need_to_sent_data</a></dd>

            </div>
            <div><dt><a href="#NetIOCallbacks">NetIOCallbacks</a></dt>
                                <dd id="NetIOBase.on_accept_connection" class="function"><a href="#NetIOCallbacks.on_accept_connection">on_accept_connection</a></dd>
                <dd id="NetIOBase.on_connected" class="function"><a href="#NetIOCallbacks.on_connected">on_connected</a></dd>
                <dd id="NetIOBase.on_read" class="function"><a href="#NetIOCallbacks.on_read">on_read</a></dd>
                <dd id="NetIOBase.on_write" class="function"><a href="#NetIOCallbacks.on_write">on_write</a></dd>
                <dd id="NetIOBase.on_close" class="function"><a href="#NetIOCallbacks.on_close">on_close</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="WorkerBase">
                            <input id="WorkerBase-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">WorkerBase</span>:

                <label class="view-source-button" for="WorkerBase-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WorkerBase"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase-291"><a href="#WorkerBase-291"><span class="linenos">291</span></a><span class="k">class</span> <span class="nc">WorkerBase</span><span class="p">:</span>
</span><span id="WorkerBase-292"><a href="#WorkerBase-292"><span class="linenos">292</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-293"><a href="#WorkerBase-293"><span class="linenos">293</span></a><span class="sd">    Base class for all workers.</span>
</span><span id="WorkerBase-294"><a href="#WorkerBase-294"><span class="linenos">294</span></a><span class="sd">    on_* callbacks will be called by the IO loop.</span>
</span><span id="WorkerBase-295"><a href="#WorkerBase-295"><span class="linenos">295</span></a>
</span><span id="WorkerBase-296"><a href="#WorkerBase-296"><span class="linenos">296</span></a><span class="sd">    General info:</span>
</span><span id="WorkerBase-297"><a href="#WorkerBase-297"><span class="linenos">297</span></a><span class="sd">    You can read input data from self.connection at any time (see &quot;Caution&quot; section of __init__ doc string) from any</span>
</span><span id="WorkerBase-298"><a href="#WorkerBase-298"><span class="linenos">298</span></a><span class="sd">    callback.</span>
</span><span id="WorkerBase-299"><a href="#WorkerBase-299"><span class="linenos">299</span></a><span class="sd">    You can write output data (to be send) to self.connection at any time (see &quot;Caution&quot;) from any callback.</span>
</span><span id="WorkerBase-300"><a href="#WorkerBase-300"><span class="linenos">300</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="WorkerBase-301"><a href="#WorkerBase-301"><span class="linenos">301</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api</span><span class="p">:</span> <span class="n">NetIOUserApi</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="WorkerBase-302"><a href="#WorkerBase-302"><span class="linenos">302</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-303"><a href="#WorkerBase-303"><span class="linenos">303</span></a><span class="sd">        Caution:</span>
</span><span id="WorkerBase-304"><a href="#WorkerBase-304"><span class="linenos">304</span></a><span class="sd">        Please do not rely on self.api and self.connection inside of your __init__ constructor: it is guaranteed that</span>
</span><span id="WorkerBase-305"><a href="#WorkerBase-305"><span class="linenos">305</span></a><span class="sd">        they will be set before any callback call, but not at the construction process.</span>
</span><span id="WorkerBase-306"><a href="#WorkerBase-306"><span class="linenos">306</span></a>
</span><span id="WorkerBase-307"><a href="#WorkerBase-307"><span class="linenos">307</span></a><span class="sd">        :param api: link to the constructed network io object</span>
</span><span id="WorkerBase-308"><a href="#WorkerBase-308"><span class="linenos">308</span></a><span class="sd">        :param connection: link to the constructed connection object</span>
</span><span id="WorkerBase-309"><a href="#WorkerBase-309"><span class="linenos">309</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-310"><a href="#WorkerBase-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">api</span> <span class="o">=</span> <span class="n">api</span>
</span><span id="WorkerBase-311"><a href="#WorkerBase-311"><span class="linenos">311</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection</span> <span class="o">=</span> <span class="n">connection</span>
</span><span id="WorkerBase-312"><a href="#WorkerBase-312"><span class="linenos">312</span></a>
</span><span id="WorkerBase-313"><a href="#WorkerBase-313"><span class="linenos">313</span></a>    <span class="k">def</span> <span class="nf">on_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-314"><a href="#WorkerBase-314"><span class="linenos">314</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-315"><a href="#WorkerBase-315"><span class="linenos">315</span></a><span class="sd">        Will be called after connection successfully established</span>
</span><span id="WorkerBase-316"><a href="#WorkerBase-316"><span class="linenos">316</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-317"><a href="#WorkerBase-317"><span class="linenos">317</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-318"><a href="#WorkerBase-318"><span class="linenos">318</span></a>        <span class="k">pass</span>
</span><span id="WorkerBase-319"><a href="#WorkerBase-319"><span class="linenos">319</span></a>
</span><span id="WorkerBase-320"><a href="#WorkerBase-320"><span class="linenos">320</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-321"><a href="#WorkerBase-321"><span class="linenos">321</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-322"><a href="#WorkerBase-322"><span class="linenos">322</span></a><span class="sd">        Will be called if there is some NEW data in the connection input buffer</span>
</span><span id="WorkerBase-323"><a href="#WorkerBase-323"><span class="linenos">323</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-324"><a href="#WorkerBase-324"><span class="linenos">324</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-325"><a href="#WorkerBase-325"><span class="linenos">325</span></a>        <span class="k">pass</span>
</span><span id="WorkerBase-326"><a href="#WorkerBase-326"><span class="linenos">326</span></a>
</span><span id="WorkerBase-327"><a href="#WorkerBase-327"><span class="linenos">327</span></a>    <span class="k">def</span> <span class="nf">on_no_more_data_to_write</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-328"><a href="#WorkerBase-328"><span class="linenos">328</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-329"><a href="#WorkerBase-329"><span class="linenos">329</span></a><span class="sd">        Will be called after all data is sent.</span>
</span><span id="WorkerBase-330"><a href="#WorkerBase-330"><span class="linenos">330</span></a><span class="sd">        Normally it will be called once (one single shot after each portion of out data is sent).</span>
</span><span id="WorkerBase-331"><a href="#WorkerBase-331"><span class="linenos">331</span></a><span class="sd">        If you&#39;ll set self.connection.force_write_call to True state - this callback may be called continuously</span>
</span><span id="WorkerBase-332"><a href="#WorkerBase-332"><span class="linenos">332</span></a><span class="sd">        (but not guaranteed: it depends of used IOMethod implementation)</span>
</span><span id="WorkerBase-333"><a href="#WorkerBase-333"><span class="linenos">333</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-334"><a href="#WorkerBase-334"><span class="linenos">334</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-335"><a href="#WorkerBase-335"><span class="linenos">335</span></a>        <span class="k">pass</span>
</span><span id="WorkerBase-336"><a href="#WorkerBase-336"><span class="linenos">336</span></a>
</span><span id="WorkerBase-337"><a href="#WorkerBase-337"><span class="linenos">337</span></a>    <span class="k">def</span> <span class="nf">on_connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-338"><a href="#WorkerBase-338"><span class="linenos">338</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-339"><a href="#WorkerBase-339"><span class="linenos">339</span></a><span class="sd">        Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.</span>
</span><span id="WorkerBase-340"><a href="#WorkerBase-340"><span class="linenos">340</span></a><span class="sd">        At this time, self.connection.connection_state is already set to ConnectionState.disconnected.</span>
</span><span id="WorkerBase-341"><a href="#WorkerBase-341"><span class="linenos">341</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-342"><a href="#WorkerBase-342"><span class="linenos">342</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-343"><a href="#WorkerBase-343"><span class="linenos">343</span></a>        <span class="k">pass</span>
</span><span id="WorkerBase-344"><a href="#WorkerBase-344"><span class="linenos">344</span></a>
</span><span id="WorkerBase-345"><a href="#WorkerBase-345"><span class="linenos">345</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-346"><a href="#WorkerBase-346"><span class="linenos">346</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-347"><a href="#WorkerBase-347"><span class="linenos">347</span></a><span class="sd">        This method SHOULD be implemented. It should create a new instance and copy some global (shared) data from</span>
</span><span id="WorkerBase-348"><a href="#WorkerBase-348"><span class="linenos">348</span></a><span class="sd">        current object to that new instance. It will be called when new peer is connected to existing passive connection</span>
</span><span id="WorkerBase-349"><a href="#WorkerBase-349"><span class="linenos">349</span></a><span class="sd">        So this is the way you may use to give all new connection some links to some global data by worker object of</span>
</span><span id="WorkerBase-350"><a href="#WorkerBase-350"><span class="linenos">350</span></a><span class="sd">        the passive connection replication process.</span>
</span><span id="WorkerBase-351"><a href="#WorkerBase-351"><span class="linenos">351</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-352"><a href="#WorkerBase-352"><span class="linenos">352</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-353"><a href="#WorkerBase-353"><span class="linenos">353</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Base class for all workers.
on_* callbacks will be called by the IO loop.</p>

<p>General info:
You can read input data from self.connection at any time (see "Caution" section of __init__ doc string) from any
callback.
You can write output data (to be send) to self.connection at any time (see "Caution") from any callback.</p>
</div>


                            <div id="WorkerBase.__init__" class="classattr">
                                        <input id="WorkerBase.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">WorkerBase</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">api</span><span class="p">:</span> <span class="n"><a href="#NetIOUserApi">NetIOUserApi</a></span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">connection</span><span class="p">:</span> <span class="n"><a href="#Connection">Connection</a></span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="WorkerBase.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WorkerBase.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.__init__-301"><a href="#WorkerBase.__init__-301"><span class="linenos">301</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api</span><span class="p">:</span> <span class="n">NetIOUserApi</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="WorkerBase.__init__-302"><a href="#WorkerBase.__init__-302"><span class="linenos">302</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.__init__-303"><a href="#WorkerBase.__init__-303"><span class="linenos">303</span></a><span class="sd">        Caution:</span>
</span><span id="WorkerBase.__init__-304"><a href="#WorkerBase.__init__-304"><span class="linenos">304</span></a><span class="sd">        Please do not rely on self.api and self.connection inside of your __init__ constructor: it is guaranteed that</span>
</span><span id="WorkerBase.__init__-305"><a href="#WorkerBase.__init__-305"><span class="linenos">305</span></a><span class="sd">        they will be set before any callback call, but not at the construction process.</span>
</span><span id="WorkerBase.__init__-306"><a href="#WorkerBase.__init__-306"><span class="linenos">306</span></a>
</span><span id="WorkerBase.__init__-307"><a href="#WorkerBase.__init__-307"><span class="linenos">307</span></a><span class="sd">        :param api: link to the constructed network io object</span>
</span><span id="WorkerBase.__init__-308"><a href="#WorkerBase.__init__-308"><span class="linenos">308</span></a><span class="sd">        :param connection: link to the constructed connection object</span>
</span><span id="WorkerBase.__init__-309"><a href="#WorkerBase.__init__-309"><span class="linenos">309</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.__init__-310"><a href="#WorkerBase.__init__-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">api</span> <span class="o">=</span> <span class="n">api</span>
</span><span id="WorkerBase.__init__-311"><a href="#WorkerBase.__init__-311"><span class="linenos">311</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection</span> <span class="o">=</span> <span class="n">connection</span>
</span></pre></div>


            <div class="docstring"><p>Caution:
Please do not rely on self.api and self.connection inside of your __init__ constructor: it is guaranteed that
they will be set before any callback call, but not at the construction process.</p>

<p>:param api: link to the constructed network io object
:param connection: link to the constructed connection object</p>
</div>


                            </div>
                            <div id="WorkerBase.api" class="classattr">
                                <div class="attr variable">
            <span class="name">api</span>

        
    </div>
    <a class="headerlink" href="#WorkerBase.api"></a>
    
    

                            </div>
                            <div id="WorkerBase.connection" class="classattr">
                                <div class="attr variable">
            <span class="name">connection</span>

        
    </div>
    <a class="headerlink" href="#WorkerBase.connection"></a>
    
    

                            </div>
                            <div id="WorkerBase.on_connect" class="classattr">
                                        <input id="WorkerBase.on_connect-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_connect</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="WorkerBase.on_connect-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WorkerBase.on_connect"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.on_connect-313"><a href="#WorkerBase.on_connect-313"><span class="linenos">313</span></a>    <span class="k">def</span> <span class="nf">on_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase.on_connect-314"><a href="#WorkerBase.on_connect-314"><span class="linenos">314</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_connect-315"><a href="#WorkerBase.on_connect-315"><span class="linenos">315</span></a><span class="sd">        Will be called after connection successfully established</span>
</span><span id="WorkerBase.on_connect-316"><a href="#WorkerBase.on_connect-316"><span class="linenos">316</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase.on_connect-317"><a href="#WorkerBase.on_connect-317"><span class="linenos">317</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_connect-318"><a href="#WorkerBase.on_connect-318"><span class="linenos">318</span></a>        <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Will be called after connection successfully established
:return:</p>
</div>


                            </div>
                            <div id="WorkerBase.on_read" class="classattr">
                                        <input id="WorkerBase.on_read-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_read</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="WorkerBase.on_read-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WorkerBase.on_read"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.on_read-320"><a href="#WorkerBase.on_read-320"><span class="linenos">320</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase.on_read-321"><a href="#WorkerBase.on_read-321"><span class="linenos">321</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_read-322"><a href="#WorkerBase.on_read-322"><span class="linenos">322</span></a><span class="sd">        Will be called if there is some NEW data in the connection input buffer</span>
</span><span id="WorkerBase.on_read-323"><a href="#WorkerBase.on_read-323"><span class="linenos">323</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase.on_read-324"><a href="#WorkerBase.on_read-324"><span class="linenos">324</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_read-325"><a href="#WorkerBase.on_read-325"><span class="linenos">325</span></a>        <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Will be called if there is some NEW data in the connection input buffer
:return:</p>
</div>


                            </div>
                            <div id="WorkerBase.on_no_more_data_to_write" class="classattr">
                                        <input id="WorkerBase.on_no_more_data_to_write-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_no_more_data_to_write</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="WorkerBase.on_no_more_data_to_write-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WorkerBase.on_no_more_data_to_write"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.on_no_more_data_to_write-327"><a href="#WorkerBase.on_no_more_data_to_write-327"><span class="linenos">327</span></a>    <span class="k">def</span> <span class="nf">on_no_more_data_to_write</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase.on_no_more_data_to_write-328"><a href="#WorkerBase.on_no_more_data_to_write-328"><span class="linenos">328</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_no_more_data_to_write-329"><a href="#WorkerBase.on_no_more_data_to_write-329"><span class="linenos">329</span></a><span class="sd">        Will be called after all data is sent.</span>
</span><span id="WorkerBase.on_no_more_data_to_write-330"><a href="#WorkerBase.on_no_more_data_to_write-330"><span class="linenos">330</span></a><span class="sd">        Normally it will be called once (one single shot after each portion of out data is sent).</span>
</span><span id="WorkerBase.on_no_more_data_to_write-331"><a href="#WorkerBase.on_no_more_data_to_write-331"><span class="linenos">331</span></a><span class="sd">        If you&#39;ll set self.connection.force_write_call to True state - this callback may be called continuously</span>
</span><span id="WorkerBase.on_no_more_data_to_write-332"><a href="#WorkerBase.on_no_more_data_to_write-332"><span class="linenos">332</span></a><span class="sd">        (but not guaranteed: it depends of used IOMethod implementation)</span>
</span><span id="WorkerBase.on_no_more_data_to_write-333"><a href="#WorkerBase.on_no_more_data_to_write-333"><span class="linenos">333</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase.on_no_more_data_to_write-334"><a href="#WorkerBase.on_no_more_data_to_write-334"><span class="linenos">334</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_no_more_data_to_write-335"><a href="#WorkerBase.on_no_more_data_to_write-335"><span class="linenos">335</span></a>        <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Will be called after all data is sent.
Normally it will be called once (one single shot after each portion of out data is sent).
If you'll set self.connection.force_write_call to True state - this callback may be called continuously
(but not guaranteed: it depends of used IOMethod implementation)
:return:</p>
</div>


                            </div>
                            <div id="WorkerBase.on_connection_lost" class="classattr">
                                        <input id="WorkerBase.on_connection_lost-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_connection_lost</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="WorkerBase.on_connection_lost-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WorkerBase.on_connection_lost"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.on_connection_lost-337"><a href="#WorkerBase.on_connection_lost-337"><span class="linenos">337</span></a>    <span class="k">def</span> <span class="nf">on_connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase.on_connection_lost-338"><a href="#WorkerBase.on_connection_lost-338"><span class="linenos">338</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_connection_lost-339"><a href="#WorkerBase.on_connection_lost-339"><span class="linenos">339</span></a><span class="sd">        Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.</span>
</span><span id="WorkerBase.on_connection_lost-340"><a href="#WorkerBase.on_connection_lost-340"><span class="linenos">340</span></a><span class="sd">        At this time, self.connection.connection_state is already set to ConnectionState.disconnected.</span>
</span><span id="WorkerBase.on_connection_lost-341"><a href="#WorkerBase.on_connection_lost-341"><span class="linenos">341</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase.on_connection_lost-342"><a href="#WorkerBase.on_connection_lost-342"><span class="linenos">342</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_connection_lost-343"><a href="#WorkerBase.on_connection_lost-343"><span class="linenos">343</span></a>        <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.
At this time, self.connection.connection_state is already set to <a href="#ConnectionState.disconnected">ConnectionState.disconnected</a>.
:return:</p>
</div>


                            </div>
                </section>
                <section id="InlineWorkerBase">
                            <input id="InlineWorkerBase-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">InlineWorkerBase</span>:

                <label class="view-source-button" for="InlineWorkerBase-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineWorkerBase"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineWorkerBase-356"><a href="#InlineWorkerBase-356"><span class="linenos">356</span></a><span class="k">class</span> <span class="nc">InlineWorkerBase</span><span class="p">:</span>
</span><span id="InlineWorkerBase-357"><a href="#InlineWorkerBase-357"><span class="linenos">357</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;client_id&#39;</span><span class="p">,</span> <span class="s1">&#39;keyword&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_family&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_type&#39;</span><span class="p">,</span> <span class="s1">&#39;socket_proto&#39;</span><span class="p">,</span> <span class="s1">&#39;addr_info&#39;</span><span class="p">,</span> <span class="s1">&#39;host_names&#39;</span><span class="p">,</span>
</span><span id="InlineWorkerBase-358"><a href="#InlineWorkerBase-358"><span class="linenos">358</span></a>                 <span class="s1">&#39;is_in_raw_mode&#39;</span><span class="p">,</span> <span class="s1">&#39;__set__is_in_raw_mode&#39;</span><span class="p">,</span> <span class="s1">&#39;__set__mark_socket_as_should_be_closed_immediately&#39;</span><span class="p">,</span>
</span><span id="InlineWorkerBase-359"><a href="#InlineWorkerBase-359"><span class="linenos">359</span></a>                 <span class="s1">&#39;__set__mark_socket_as_ready_to_be_closed&#39;</span><span class="p">,</span> <span class="s1">&#39;__external_parameters_set_trigger&#39;</span><span class="p">,</span> <span class="s1">&#39;output_messages&#39;</span><span class="p">,</span>
</span><span id="InlineWorkerBase-360"><a href="#InlineWorkerBase-360"><span class="linenos">360</span></a>                 <span class="s1">&#39;__hold__client_id&#39;</span><span class="p">)</span>
</span><span id="InlineWorkerBase-361"><a href="#InlineWorkerBase-361"><span class="linenos">361</span></a>
</span><span id="InlineWorkerBase-362"><a href="#InlineWorkerBase-362"><span class="linenos">362</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">socket_family</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_type</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_proto</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="InlineWorkerBase-363"><a href="#InlineWorkerBase-363"><span class="linenos">363</span></a>                 <span class="n">addr_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">host_names</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="InlineWorkerBase-364"><a href="#InlineWorkerBase-364"><span class="linenos">364</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase-365"><a href="#InlineWorkerBase-365"><span class="linenos">365</span></a>
</span><span id="InlineWorkerBase-366"><a href="#InlineWorkerBase-366"><span class="linenos">366</span></a><span class="sd">        :param keyword: client keyword. You may check for a known keywords to act appropriately</span>
</span><span id="InlineWorkerBase-367"><a href="#InlineWorkerBase-367"><span class="linenos">367</span></a><span class="sd">        :param socket_family:</span>
</span><span id="InlineWorkerBase-368"><a href="#InlineWorkerBase-368"><span class="linenos">368</span></a><span class="sd">        :param socket_type:</span>
</span><span id="InlineWorkerBase-369"><a href="#InlineWorkerBase-369"><span class="linenos">369</span></a><span class="sd">        :param socket_proto:</span>
</span><span id="InlineWorkerBase-370"><a href="#InlineWorkerBase-370"><span class="linenos">370</span></a><span class="sd">        :param addr_info: result of socket.getaddrinfo() call</span>
</span><span id="InlineWorkerBase-371"><a href="#InlineWorkerBase-371"><span class="linenos">371</span></a><span class="sd">        :param host_names: result of socket.gethostbyaddr() call</span>
</span><span id="InlineWorkerBase-372"><a href="#InlineWorkerBase-372"><span class="linenos">372</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase-373"><a href="#InlineWorkerBase-373"><span class="linenos">373</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="InlineWorkerBase-374"><a href="#InlineWorkerBase-374"><span class="linenos">374</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="n">keyword</span>
</span><span id="InlineWorkerBase-375"><a href="#InlineWorkerBase-375"><span class="linenos">375</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="InlineWorkerBase-376"><a href="#InlineWorkerBase-376"><span class="linenos">376</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="InlineWorkerBase-377"><a href="#InlineWorkerBase-377"><span class="linenos">377</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_proto</span> <span class="o">=</span> <span class="n">socket_proto</span>
</span><span id="InlineWorkerBase-378"><a href="#InlineWorkerBase-378"><span class="linenos">378</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span> <span class="o">=</span> <span class="n">addr_info</span>
</span><span id="InlineWorkerBase-379"><a href="#InlineWorkerBase-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span> <span class="o">=</span> <span class="n">host_names</span>
</span><span id="InlineWorkerBase-380"><a href="#InlineWorkerBase-380"><span class="linenos">380</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_in_raw_mode</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="InlineWorkerBase-381"><a href="#InlineWorkerBase-381"><span class="linenos">381</span></a>
</span><span id="InlineWorkerBase-382"><a href="#InlineWorkerBase-382"><span class="linenos">382</span></a>        <span class="c1"># self.output_messages = FIFODequeWithLengthControl()</span>
</span><span id="InlineWorkerBase-383"><a href="#InlineWorkerBase-383"><span class="linenos">383</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_messages</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="InlineWorkerBase-384"><a href="#InlineWorkerBase-384"><span class="linenos">384</span></a>        <span class="c1"># self.output_messages = list()</span>
</span><span id="InlineWorkerBase-385"><a href="#InlineWorkerBase-385"><span class="linenos">385</span></a>
</span><span id="InlineWorkerBase-386"><a href="#InlineWorkerBase-386"><span class="linenos">386</span></a>    <span class="k">def</span> <span class="nf">on__data_received</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="InlineWorkerBase-387"><a href="#InlineWorkerBase-387"><span class="linenos">387</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase-388"><a href="#InlineWorkerBase-388"><span class="linenos">388</span></a><span class="sd">        Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data</span>
</span><span id="InlineWorkerBase-389"><a href="#InlineWorkerBase-389"><span class="linenos">389</span></a><span class="sd">        Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will</span>
</span><span id="InlineWorkerBase-390"><a href="#InlineWorkerBase-390"><span class="linenos">390</span></a><span class="sd">        be logged</span>
</span><span id="InlineWorkerBase-391"><a href="#InlineWorkerBase-391"><span class="linenos">391</span></a><span class="sd">        :param data: piece of input data if connection is in RAW-mode and full message otherwise.</span>
</span><span id="InlineWorkerBase-392"><a href="#InlineWorkerBase-392"><span class="linenos">392</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase-393"><a href="#InlineWorkerBase-393"><span class="linenos">393</span></a>        <span class="k">pass</span>
</span><span id="InlineWorkerBase-394"><a href="#InlineWorkerBase-394"><span class="linenos">394</span></a>
</span><span id="InlineWorkerBase-395"><a href="#InlineWorkerBase-395"><span class="linenos">395</span></a>    <span class="k">def</span> <span class="nf">on__output_buffers_are_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="InlineWorkerBase-396"><a href="#InlineWorkerBase-396"><span class="linenos">396</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase-397"><a href="#InlineWorkerBase-397"><span class="linenos">397</span></a><span class="sd">        Will be called immediately when all output data was send.</span>
</span><span id="InlineWorkerBase-398"><a href="#InlineWorkerBase-398"><span class="linenos">398</span></a><span class="sd">        Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data</span>
</span><span id="InlineWorkerBase-399"><a href="#InlineWorkerBase-399"><span class="linenos">399</span></a><span class="sd">        Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will</span>
</span><span id="InlineWorkerBase-400"><a href="#InlineWorkerBase-400"><span class="linenos">400</span></a><span class="sd">        be logged</span>
</span><span id="InlineWorkerBase-401"><a href="#InlineWorkerBase-401"><span class="linenos">401</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase-402"><a href="#InlineWorkerBase-402"><span class="linenos">402</span></a>        <span class="k">pass</span>
</span><span id="InlineWorkerBase-403"><a href="#InlineWorkerBase-403"><span class="linenos">403</span></a>
</span><span id="InlineWorkerBase-404"><a href="#InlineWorkerBase-404"><span class="linenos">404</span></a>    <span class="k">def</span> <span class="nf">on__connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="InlineWorkerBase-405"><a href="#InlineWorkerBase-405"><span class="linenos">405</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase-406"><a href="#InlineWorkerBase-406"><span class="linenos">406</span></a><span class="sd">        Will be called after connection was closed. Current Inline Processor object will be destroyed after this call.</span>
</span><span id="InlineWorkerBase-407"><a href="#InlineWorkerBase-407"><span class="linenos">407</span></a><span class="sd">        Situation with unhandled exception will be logged.</span>
</span><span id="InlineWorkerBase-408"><a href="#InlineWorkerBase-408"><span class="linenos">408</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase-409"><a href="#InlineWorkerBase-409"><span class="linenos">409</span></a>        <span class="k">pass</span>
</span><span id="InlineWorkerBase-410"><a href="#InlineWorkerBase-410"><span class="linenos">410</span></a>
</span><span id="InlineWorkerBase-411"><a href="#InlineWorkerBase-411"><span class="linenos">411</span></a>    <span class="k">def</span> <span class="nf">set__is_in_raw_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_in_raw_mode</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineWorkerBase-412"><a href="#InlineWorkerBase-412"><span class="linenos">412</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="InlineWorkerBase-413"><a href="#InlineWorkerBase-413"><span class="linenos">413</span></a>
</span><span id="InlineWorkerBase-414"><a href="#InlineWorkerBase-414"><span class="linenos">414</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_should_be_closed_immediately</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineWorkerBase-415"><a href="#InlineWorkerBase-415"><span class="linenos">415</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="InlineWorkerBase-416"><a href="#InlineWorkerBase-416"><span class="linenos">416</span></a>
</span><span id="InlineWorkerBase-417"><a href="#InlineWorkerBase-417"><span class="linenos">417</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_ready_to_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineWorkerBase-418"><a href="#InlineWorkerBase-418"><span class="linenos">418</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="InlineWorkerBase-419"><a href="#InlineWorkerBase-419"><span class="linenos">419</span></a>
</span><span id="InlineWorkerBase-420"><a href="#InlineWorkerBase-420"><span class="linenos">420</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="InlineWorkerBase-421"><a href="#InlineWorkerBase-421"><span class="linenos">421</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="InlineWorkerBase-422"><a href="#InlineWorkerBase-422"><span class="linenos">422</span></a>
</span><span id="InlineWorkerBase-423"><a href="#InlineWorkerBase-423"><span class="linenos">423</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="InlineWorkerBase-424"><a href="#InlineWorkerBase-424"><span class="linenos">424</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="InlineWorkerBase.__init__" class="classattr">
                                        <input id="InlineWorkerBase.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">InlineWorkerBase</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">client_id</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">socket_family</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">socket_type</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">socket_proto</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">addr_info</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">host_names</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">external_parameters_set_trigger</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="InlineWorkerBase.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineWorkerBase.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineWorkerBase.__init__-362"><a href="#InlineWorkerBase.__init__-362"><span class="linenos">362</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">keyword</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">socket_family</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_type</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">socket_proto</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="InlineWorkerBase.__init__-363"><a href="#InlineWorkerBase.__init__-363"><span class="linenos">363</span></a>                 <span class="n">addr_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">host_names</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">external_parameters_set_trigger</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="InlineWorkerBase.__init__-364"><a href="#InlineWorkerBase.__init__-364"><span class="linenos">364</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase.__init__-365"><a href="#InlineWorkerBase.__init__-365"><span class="linenos">365</span></a>
</span><span id="InlineWorkerBase.__init__-366"><a href="#InlineWorkerBase.__init__-366"><span class="linenos">366</span></a><span class="sd">        :param keyword: client keyword. You may check for a known keywords to act appropriately</span>
</span><span id="InlineWorkerBase.__init__-367"><a href="#InlineWorkerBase.__init__-367"><span class="linenos">367</span></a><span class="sd">        :param socket_family:</span>
</span><span id="InlineWorkerBase.__init__-368"><a href="#InlineWorkerBase.__init__-368"><span class="linenos">368</span></a><span class="sd">        :param socket_type:</span>
</span><span id="InlineWorkerBase.__init__-369"><a href="#InlineWorkerBase.__init__-369"><span class="linenos">369</span></a><span class="sd">        :param socket_proto:</span>
</span><span id="InlineWorkerBase.__init__-370"><a href="#InlineWorkerBase.__init__-370"><span class="linenos">370</span></a><span class="sd">        :param addr_info: result of socket.getaddrinfo() call</span>
</span><span id="InlineWorkerBase.__init__-371"><a href="#InlineWorkerBase.__init__-371"><span class="linenos">371</span></a><span class="sd">        :param host_names: result of socket.gethostbyaddr() call</span>
</span><span id="InlineWorkerBase.__init__-372"><a href="#InlineWorkerBase.__init__-372"><span class="linenos">372</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase.__init__-373"><a href="#InlineWorkerBase.__init__-373"><span class="linenos">373</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">client_id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="InlineWorkerBase.__init__-374"><a href="#InlineWorkerBase.__init__-374"><span class="linenos">374</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">keyword</span> <span class="o">=</span> <span class="n">keyword</span>
</span><span id="InlineWorkerBase.__init__-375"><a href="#InlineWorkerBase.__init__-375"><span class="linenos">375</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="InlineWorkerBase.__init__-376"><a href="#InlineWorkerBase.__init__-376"><span class="linenos">376</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="InlineWorkerBase.__init__-377"><a href="#InlineWorkerBase.__init__-377"><span class="linenos">377</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_proto</span> <span class="o">=</span> <span class="n">socket_proto</span>
</span><span id="InlineWorkerBase.__init__-378"><a href="#InlineWorkerBase.__init__-378"><span class="linenos">378</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">addr_info</span> <span class="o">=</span> <span class="n">addr_info</span>
</span><span id="InlineWorkerBase.__init__-379"><a href="#InlineWorkerBase.__init__-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">host_names</span> <span class="o">=</span> <span class="n">host_names</span>
</span><span id="InlineWorkerBase.__init__-380"><a href="#InlineWorkerBase.__init__-380"><span class="linenos">380</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_in_raw_mode</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="InlineWorkerBase.__init__-381"><a href="#InlineWorkerBase.__init__-381"><span class="linenos">381</span></a>
</span><span id="InlineWorkerBase.__init__-382"><a href="#InlineWorkerBase.__init__-382"><span class="linenos">382</span></a>        <span class="c1"># self.output_messages = FIFODequeWithLengthControl()</span>
</span><span id="InlineWorkerBase.__init__-383"><a href="#InlineWorkerBase.__init__-383"><span class="linenos">383</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_messages</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="InlineWorkerBase.__init__-384"><a href="#InlineWorkerBase.__init__-384"><span class="linenos">384</span></a>        <span class="c1"># self.output_messages = list()</span>
</span></pre></div>


            <div class="docstring"><p>:param keyword: client keyword. You may check for a known keywords to act appropriately
:param socket_family:
:param socket_type:
:param socket_proto:
:param addr_info: result of socket.getaddrinfo() call
:param host_names: result of socket.gethostbyaddr() call</p>
</div>


                            </div>
                            <div id="InlineWorkerBase.client_id" class="classattr">
                                <div class="attr variable">
            <span class="name">client_id</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.client_id"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.keyword" class="classattr">
                                <div class="attr variable">
            <span class="name">keyword</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.keyword"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.socket_family" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_family</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.socket_family"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.socket_type" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_type</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.socket_type"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.socket_proto" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_proto</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.socket_proto"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.addr_info" class="classattr">
                                <div class="attr variable">
            <span class="name">addr_info</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.addr_info"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.host_names" class="classattr">
                                <div class="attr variable">
            <span class="name">host_names</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.host_names"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.is_in_raw_mode" class="classattr">
                                <div class="attr variable">
            <span class="name">is_in_raw_mode</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.is_in_raw_mode"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.output_messages" class="classattr">
                                <div class="attr variable">
            <span class="name">output_messages</span>

        
    </div>
    <a class="headerlink" href="#InlineWorkerBase.output_messages"></a>
    
    

                            </div>
                            <div id="InlineWorkerBase.on__data_received" class="classattr">
                                        <input id="InlineWorkerBase.on__data_received-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on__data_received</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineWorkerBase.on__data_received-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineWorkerBase.on__data_received"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineWorkerBase.on__data_received-386"><a href="#InlineWorkerBase.on__data_received-386"><span class="linenos">386</span></a>    <span class="k">def</span> <span class="nf">on__data_received</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="InlineWorkerBase.on__data_received-387"><a href="#InlineWorkerBase.on__data_received-387"><span class="linenos">387</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase.on__data_received-388"><a href="#InlineWorkerBase.on__data_received-388"><span class="linenos">388</span></a><span class="sd">        Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data</span>
</span><span id="InlineWorkerBase.on__data_received-389"><a href="#InlineWorkerBase.on__data_received-389"><span class="linenos">389</span></a><span class="sd">        Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will</span>
</span><span id="InlineWorkerBase.on__data_received-390"><a href="#InlineWorkerBase.on__data_received-390"><span class="linenos">390</span></a><span class="sd">        be logged</span>
</span><span id="InlineWorkerBase.on__data_received-391"><a href="#InlineWorkerBase.on__data_received-391"><span class="linenos">391</span></a><span class="sd">        :param data: piece of input data if connection is in RAW-mode and full message otherwise.</span>
</span><span id="InlineWorkerBase.on__data_received-392"><a href="#InlineWorkerBase.on__data_received-392"><span class="linenos">392</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase.on__data_received-393"><a href="#InlineWorkerBase.on__data_received-393"><span class="linenos">393</span></a>        <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data
Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will
be logged
:param data: piece of input data if connection is in RAW-mode and full message otherwise.</p>
</div>


                            </div>
                            <div id="InlineWorkerBase.on__output_buffers_are_empty" class="classattr">
                                        <input id="InlineWorkerBase.on__output_buffers_are_empty-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on__output_buffers_are_empty</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineWorkerBase.on__output_buffers_are_empty-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineWorkerBase.on__output_buffers_are_empty"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineWorkerBase.on__output_buffers_are_empty-395"><a href="#InlineWorkerBase.on__output_buffers_are_empty-395"><span class="linenos">395</span></a>    <span class="k">def</span> <span class="nf">on__output_buffers_are_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="InlineWorkerBase.on__output_buffers_are_empty-396"><a href="#InlineWorkerBase.on__output_buffers_are_empty-396"><span class="linenos">396</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase.on__output_buffers_are_empty-397"><a href="#InlineWorkerBase.on__output_buffers_are_empty-397"><span class="linenos">397</span></a><span class="sd">        Will be called immediately when all output data was send.</span>
</span><span id="InlineWorkerBase.on__output_buffers_are_empty-398"><a href="#InlineWorkerBase.on__output_buffers_are_empty-398"><span class="linenos">398</span></a><span class="sd">        Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data</span>
</span><span id="InlineWorkerBase.on__output_buffers_are_empty-399"><a href="#InlineWorkerBase.on__output_buffers_are_empty-399"><span class="linenos">399</span></a><span class="sd">        Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will</span>
</span><span id="InlineWorkerBase.on__output_buffers_are_empty-400"><a href="#InlineWorkerBase.on__output_buffers_are_empty-400"><span class="linenos">400</span></a><span class="sd">        be logged</span>
</span><span id="InlineWorkerBase.on__output_buffers_are_empty-401"><a href="#InlineWorkerBase.on__output_buffers_are_empty-401"><span class="linenos">401</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase.on__output_buffers_are_empty-402"><a href="#InlineWorkerBase.on__output_buffers_are_empty-402"><span class="linenos">402</span></a>        <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Will be called immediately when all output data was send.
Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data
Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will
be logged</p>
</div>


                            </div>
                            <div id="InlineWorkerBase.on__connection_lost" class="classattr">
                                        <input id="InlineWorkerBase.on__connection_lost-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on__connection_lost</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineWorkerBase.on__connection_lost-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineWorkerBase.on__connection_lost"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineWorkerBase.on__connection_lost-404"><a href="#InlineWorkerBase.on__connection_lost-404"><span class="linenos">404</span></a>    <span class="k">def</span> <span class="nf">on__connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="InlineWorkerBase.on__connection_lost-405"><a href="#InlineWorkerBase.on__connection_lost-405"><span class="linenos">405</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase.on__connection_lost-406"><a href="#InlineWorkerBase.on__connection_lost-406"><span class="linenos">406</span></a><span class="sd">        Will be called after connection was closed. Current Inline Processor object will be destroyed after this call.</span>
</span><span id="InlineWorkerBase.on__connection_lost-407"><a href="#InlineWorkerBase.on__connection_lost-407"><span class="linenos">407</span></a><span class="sd">        Situation with unhandled exception will be logged.</span>
</span><span id="InlineWorkerBase.on__connection_lost-408"><a href="#InlineWorkerBase.on__connection_lost-408"><span class="linenos">408</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="InlineWorkerBase.on__connection_lost-409"><a href="#InlineWorkerBase.on__connection_lost-409"><span class="linenos">409</span></a>        <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Will be called after connection was closed. Current Inline Processor object will be destroyed after this call.
Situation with unhandled exception will be logged.</p>
</div>


                            </div>
                            <div id="InlineWorkerBase.set__is_in_raw_mode" class="classattr">
                                        <input id="InlineWorkerBase.set__is_in_raw_mode-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set__is_in_raw_mode</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">is_in_raw_mode</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineWorkerBase.set__is_in_raw_mode-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineWorkerBase.set__is_in_raw_mode"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineWorkerBase.set__is_in_raw_mode-411"><a href="#InlineWorkerBase.set__is_in_raw_mode-411"><span class="linenos">411</span></a>    <span class="k">def</span> <span class="nf">set__is_in_raw_mode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_in_raw_mode</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineWorkerBase.set__is_in_raw_mode-412"><a href="#InlineWorkerBase.set__is_in_raw_mode-412"><span class="linenos">412</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="InlineWorkerBase.mark__socket_as_should_be_closed_immediately" class="classattr">
                                        <input id="InlineWorkerBase.mark__socket_as_should_be_closed_immediately-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mark__socket_as_should_be_closed_immediately</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineWorkerBase.mark__socket_as_should_be_closed_immediately-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineWorkerBase.mark__socket_as_should_be_closed_immediately"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineWorkerBase.mark__socket_as_should_be_closed_immediately-414"><a href="#InlineWorkerBase.mark__socket_as_should_be_closed_immediately-414"><span class="linenos">414</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_should_be_closed_immediately</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineWorkerBase.mark__socket_as_should_be_closed_immediately-415"><a href="#InlineWorkerBase.mark__socket_as_should_be_closed_immediately-415"><span class="linenos">415</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="InlineWorkerBase.mark__socket_as_ready_to_be_closed" class="classattr">
                                        <input id="InlineWorkerBase.mark__socket_as_ready_to_be_closed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mark__socket_as_ready_to_be_closed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="InlineWorkerBase.mark__socket_as_ready_to_be_closed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InlineWorkerBase.mark__socket_as_ready_to_be_closed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InlineWorkerBase.mark__socket_as_ready_to_be_closed-417"><a href="#InlineWorkerBase.mark__socket_as_ready_to_be_closed-417"><span class="linenos">417</span></a>    <span class="k">def</span> <span class="nf">mark__socket_as_ready_to_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mark_socket_as</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="InlineWorkerBase.mark__socket_as_ready_to_be_closed-418"><a href="#InlineWorkerBase.mark__socket_as_ready_to_be_closed-418"><span class="linenos">418</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="net_io">
                            <input id="net_io-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@contextmanager</div>

        <span class="def">def</span>
        <span class="name">net_io</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">net_io_obj</span><span class="p">:</span> <span class="n"><a href="#NetIOBase">NetIOBase</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="net_io-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#net_io"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="net_io-427"><a href="#net_io-427"><span class="linenos">427</span></a><span class="nd">@contextmanager</span>
</span><span id="net_io-428"><a href="#net_io-428"><span class="linenos">428</span></a><span class="k">def</span> <span class="nf">net_io</span><span class="p">(</span><span class="n">net_io_obj</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="net_io-429"><a href="#net_io-429"><span class="linenos">429</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="net_io-430"><a href="#net_io-430"><span class="linenos">430</span></a><span class="sd">    Context manager.</span>
</span><span id="net_io-431"><a href="#net_io-431"><span class="linenos">431</span></a><span class="sd">    Usage:</span>
</span><span id="net_io-432"><a href="#net_io-432"><span class="linenos">432</span></a>
</span><span id="net_io-433"><a href="#net_io-433"><span class="linenos">433</span></a><span class="sd">    main_io = NetIOBase()</span>
</span><span id="net_io-434"><a href="#net_io-434"><span class="linenos">434</span></a><span class="sd">    with(net_io(main_io)) as io:</span>
</span><span id="net_io-435"><a href="#net_io-435"><span class="linenos">435</span></a><span class="sd">        print(&#39;Preparing connections&#39;)</span>
</span><span id="net_io-436"><a href="#net_io-436"><span class="linenos">436</span></a><span class="sd">        connection1 = io.make_connection(...)</span>
</span><span id="net_io-437"><a href="#net_io-437"><span class="linenos">437</span></a><span class="sd">        connection2 = io.make_connection(...)</span>
</span><span id="net_io-438"><a href="#net_io-438"><span class="linenos">438</span></a><span class="sd">        k = c + 12</span>
</span><span id="net_io-439"><a href="#net_io-439"><span class="linenos">439</span></a><span class="sd">        ...</span>
</span><span id="net_io-440"><a href="#net_io-440"><span class="linenos">440</span></a><span class="sd">        connectionN = io.make_connection(...)</span>
</span><span id="net_io-441"><a href="#net_io-441"><span class="linenos">441</span></a><span class="sd">        print(&#39;Starting IO loop&#39;)</span>
</span><span id="net_io-442"><a href="#net_io-442"><span class="linenos">442</span></a><span class="sd">    print(&#39;IO loop was finished properly&#39;)</span>
</span><span id="net_io-443"><a href="#net_io-443"><span class="linenos">443</span></a>
</span><span id="net_io-444"><a href="#net_io-444"><span class="linenos">444</span></a>
</span><span id="net_io-445"><a href="#net_io-445"><span class="linenos">445</span></a><span class="sd">    :param net_io_obj: constructed IO instance (object)</span>
</span><span id="net_io-446"><a href="#net_io-446"><span class="linenos">446</span></a><span class="sd">    :return:</span>
</span><span id="net_io-447"><a href="#net_io-447"><span class="linenos">447</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="net_io-448"><a href="#net_io-448"><span class="linenos">448</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="net_io-449"><a href="#net_io-449"><span class="linenos">449</span></a>        <span class="k">yield</span> <span class="n">net_io_obj</span>
</span><span id="net_io-450"><a href="#net_io-450"><span class="linenos">450</span></a>        <span class="n">net_io_obj</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="net_io-451"><a href="#net_io-451"><span class="linenos">451</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="net_io-452"><a href="#net_io-452"><span class="linenos">452</span></a>        <span class="n">net_io_obj</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Context manager.
Usage:</p>

<p>main_io = NetIOBase()
with(net_io(main_io)) as io:
    print('Preparing connections')
    connection1 = io.make_connection(...)
    connection2 = io.make_connection(...)
    k = c + 12
    ...
    connectionN = io.make_connection(...)
    print('Starting IO loop')
print('IO loop was finished properly')</p>

<p>:param net_io_obj: constructed IO instance (object)
:return:</p>
</div>


                </section>
                <section id="IOLoopBase">
                            <input id="IOLoopBase-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IOLoopBase</span>:

                <label class="view-source-button" for="IOLoopBase-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase-455"><a href="#IOLoopBase-455"><span class="linenos">455</span></a><span class="k">class</span> <span class="nc">IOLoopBase</span><span class="p">:</span>
</span><span id="IOLoopBase-456"><a href="#IOLoopBase-456"><span class="linenos">456</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase-457"><a href="#IOLoopBase-457"><span class="linenos">457</span></a><span class="sd">    Base class for all IOMethod implementation (select, epoll, overlapped io, kqueue, etc.)</span>
</span><span id="IOLoopBase-458"><a href="#IOLoopBase-458"><span class="linenos">458</span></a><span class="sd">    All his methods are called by the NetIOBase instance.</span>
</span><span id="IOLoopBase-459"><a href="#IOLoopBase-459"><span class="linenos">459</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="IOLoopBase-460"><a href="#IOLoopBase-460"><span class="linenos">460</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="IOLoopBase-461"><a href="#IOLoopBase-461"><span class="linenos">461</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="IOLoopBase-462"><a href="#IOLoopBase-462"><span class="linenos">462</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IOLoopBase-463"><a href="#IOLoopBase-463"><span class="linenos">463</span></a>        <span class="k">pass</span>
</span><span id="IOLoopBase-464"><a href="#IOLoopBase-464"><span class="linenos">464</span></a>
</span><span id="IOLoopBase-465"><a href="#IOLoopBase-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="nf">loop_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="IOLoopBase-466"><a href="#IOLoopBase-466"><span class="linenos">466</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase-467"><a href="#IOLoopBase-467"><span class="linenos">467</span></a><span class="sd">        Single IO loop iteration.</span>
</span><span id="IOLoopBase-468"><a href="#IOLoopBase-468"><span class="linenos">468</span></a><span class="sd">        This method holds all IOMethod logic.</span>
</span><span id="IOLoopBase-469"><a href="#IOLoopBase-469"><span class="linenos">469</span></a><span class="sd">        :param timeout: float or int. If timeout is negative, the call will block until there is an event.</span>
</span><span id="IOLoopBase-470"><a href="#IOLoopBase-470"><span class="linenos">470</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase-471"><a href="#IOLoopBase-471"><span class="linenos">471</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase-472"><a href="#IOLoopBase-472"><span class="linenos">472</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOLoopBase-473"><a href="#IOLoopBase-473"><span class="linenos">473</span></a>
</span><span id="IOLoopBase-474"><a href="#IOLoopBase-474"><span class="linenos">474</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IOLoopBase-475"><a href="#IOLoopBase-475"><span class="linenos">475</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase-476"><a href="#IOLoopBase-476"><span class="linenos">476</span></a><span class="sd">        Initiates destruction process</span>
</span><span id="IOLoopBase-477"><a href="#IOLoopBase-477"><span class="linenos">477</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase-478"><a href="#IOLoopBase-478"><span class="linenos">478</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase-479"><a href="#IOLoopBase-479"><span class="linenos">479</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOLoopBase-480"><a href="#IOLoopBase-480"><span class="linenos">480</span></a>
</span><span id="IOLoopBase-481"><a href="#IOLoopBase-481"><span class="linenos">481</span></a>    <span class="k">def</span> <span class="nf">set__can_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IOLoopBase-482"><a href="#IOLoopBase-482"><span class="linenos">482</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase-483"><a href="#IOLoopBase-483"><span class="linenos">483</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to read&quot; checks for socket</span>
</span><span id="IOLoopBase-484"><a href="#IOLoopBase-484"><span class="linenos">484</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase-485"><a href="#IOLoopBase-485"><span class="linenos">485</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="IOLoopBase-486"><a href="#IOLoopBase-486"><span class="linenos">486</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase-487"><a href="#IOLoopBase-487"><span class="linenos">487</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase-488"><a href="#IOLoopBase-488"><span class="linenos">488</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOLoopBase-489"><a href="#IOLoopBase-489"><span class="linenos">489</span></a>
</span><span id="IOLoopBase-490"><a href="#IOLoopBase-490"><span class="linenos">490</span></a>    <span class="k">def</span> <span class="nf">set__need_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IOLoopBase-491"><a href="#IOLoopBase-491"><span class="linenos">491</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase-492"><a href="#IOLoopBase-492"><span class="linenos">492</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to write&quot; checks for socket</span>
</span><span id="IOLoopBase-493"><a href="#IOLoopBase-493"><span class="linenos">493</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase-494"><a href="#IOLoopBase-494"><span class="linenos">494</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="IOLoopBase-495"><a href="#IOLoopBase-495"><span class="linenos">495</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase-496"><a href="#IOLoopBase-496"><span class="linenos">496</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase-497"><a href="#IOLoopBase-497"><span class="linenos">497</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOLoopBase-498"><a href="#IOLoopBase-498"><span class="linenos">498</span></a>
</span><span id="IOLoopBase-499"><a href="#IOLoopBase-499"><span class="linenos">499</span></a>    <span class="k">def</span> <span class="nf">set__should_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOLoopBase-500"><a href="#IOLoopBase-500"><span class="linenos">500</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase-501"><a href="#IOLoopBase-501"><span class="linenos">501</span></a><span class="sd">        Mark socket as &quot;should be closed&quot;</span>
</span><span id="IOLoopBase-502"><a href="#IOLoopBase-502"><span class="linenos">502</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase-503"><a href="#IOLoopBase-503"><span class="linenos">503</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase-504"><a href="#IOLoopBase-504"><span class="linenos">504</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase-505"><a href="#IOLoopBase-505"><span class="linenos">505</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOLoopBase-506"><a href="#IOLoopBase-506"><span class="linenos">506</span></a>
</span><span id="IOLoopBase-507"><a href="#IOLoopBase-507"><span class="linenos">507</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOLoopBase-508"><a href="#IOLoopBase-508"><span class="linenos">508</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase-509"><a href="#IOLoopBase-509"><span class="linenos">509</span></a><span class="sd">        Will add socket to the internal connections list</span>
</span><span id="IOLoopBase-510"><a href="#IOLoopBase-510"><span class="linenos">510</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase-511"><a href="#IOLoopBase-511"><span class="linenos">511</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase-512"><a href="#IOLoopBase-512"><span class="linenos">512</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase-513"><a href="#IOLoopBase-513"><span class="linenos">513</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOLoopBase-514"><a href="#IOLoopBase-514"><span class="linenos">514</span></a>
</span><span id="IOLoopBase-515"><a href="#IOLoopBase-515"><span class="linenos">515</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOLoopBase-516"><a href="#IOLoopBase-516"><span class="linenos">516</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase-517"><a href="#IOLoopBase-517"><span class="linenos">517</span></a><span class="sd">        Will remove socket from the internal connections list</span>
</span><span id="IOLoopBase-518"><a href="#IOLoopBase-518"><span class="linenos">518</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase-519"><a href="#IOLoopBase-519"><span class="linenos">519</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase-520"><a href="#IOLoopBase-520"><span class="linenos">520</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase-521"><a href="#IOLoopBase-521"><span class="linenos">521</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Base class for all IOMethod implementation (select, epoll, overlapped io, kqueue, etc.)
All his methods are called by the NetIOBase instance.</p>
</div>


                            <div id="IOLoopBase.__init__" class="classattr">
                                        <input id="IOLoopBase.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IOLoopBase</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">interface</span><span class="p">:</span> <span class="n"><a href="#NetIOBase">NetIOBase</a></span></span>)</span>

                <label class="view-source-button" for="IOLoopBase.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase.__init__-460"><a href="#IOLoopBase.__init__-460"><span class="linenos">460</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="IOLoopBase.__init__-461"><a href="#IOLoopBase.__init__-461"><span class="linenos">461</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="IOLoopBase.__init__-462"><a href="#IOLoopBase.__init__-462"><span class="linenos">462</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IOLoopBase.__init__-463"><a href="#IOLoopBase.__init__-463"><span class="linenos">463</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="IOLoopBase.interface" class="classattr">
                                <div class="attr variable">
            <span class="name">interface</span>

        
    </div>
    <a class="headerlink" href="#IOLoopBase.interface"></a>
    
    

                            </div>
                            <div id="IOLoopBase.should_be_closed" class="classattr">
                                <div class="attr variable">
            <span class="name">should_be_closed</span>

        
    </div>
    <a class="headerlink" href="#IOLoopBase.should_be_closed"></a>
    
    

                            </div>
                            <div id="IOLoopBase.loop_iteration" class="classattr">
                                        <input id="IOLoopBase.loop_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">loop_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">timeout</span><span class="o">=-</span><span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOLoopBase.loop_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase.loop_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase.loop_iteration-465"><a href="#IOLoopBase.loop_iteration-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="nf">loop_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="IOLoopBase.loop_iteration-466"><a href="#IOLoopBase.loop_iteration-466"><span class="linenos">466</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase.loop_iteration-467"><a href="#IOLoopBase.loop_iteration-467"><span class="linenos">467</span></a><span class="sd">        Single IO loop iteration.</span>
</span><span id="IOLoopBase.loop_iteration-468"><a href="#IOLoopBase.loop_iteration-468"><span class="linenos">468</span></a><span class="sd">        This method holds all IOMethod logic.</span>
</span><span id="IOLoopBase.loop_iteration-469"><a href="#IOLoopBase.loop_iteration-469"><span class="linenos">469</span></a><span class="sd">        :param timeout: float or int. If timeout is negative, the call will block until there is an event.</span>
</span><span id="IOLoopBase.loop_iteration-470"><a href="#IOLoopBase.loop_iteration-470"><span class="linenos">470</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase.loop_iteration-471"><a href="#IOLoopBase.loop_iteration-471"><span class="linenos">471</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase.loop_iteration-472"><a href="#IOLoopBase.loop_iteration-472"><span class="linenos">472</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Single IO loop iteration.
This method holds all IOMethod logic.
:param timeout: float or int. If timeout is negative, the call will block until there is an event.
:return:</p>
</div>


                            </div>
                            <div id="IOLoopBase.destroy" class="classattr">
                                        <input id="IOLoopBase.destroy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">destroy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOLoopBase.destroy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase.destroy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase.destroy-474"><a href="#IOLoopBase.destroy-474"><span class="linenos">474</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IOLoopBase.destroy-475"><a href="#IOLoopBase.destroy-475"><span class="linenos">475</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase.destroy-476"><a href="#IOLoopBase.destroy-476"><span class="linenos">476</span></a><span class="sd">        Initiates destruction process</span>
</span><span id="IOLoopBase.destroy-477"><a href="#IOLoopBase.destroy-477"><span class="linenos">477</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase.destroy-478"><a href="#IOLoopBase.destroy-478"><span class="linenos">478</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase.destroy-479"><a href="#IOLoopBase.destroy-479"><span class="linenos">479</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Initiates destruction process
:return:</p>
</div>


                            </div>
                            <div id="IOLoopBase.set__can_read" class="classattr">
                                        <input id="IOLoopBase.set__can_read-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set__can_read</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span>, </span><span class="param"><span class="n">state</span><span class="o">=</span><span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOLoopBase.set__can_read-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase.set__can_read"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase.set__can_read-481"><a href="#IOLoopBase.set__can_read-481"><span class="linenos">481</span></a>    <span class="k">def</span> <span class="nf">set__can_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IOLoopBase.set__can_read-482"><a href="#IOLoopBase.set__can_read-482"><span class="linenos">482</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase.set__can_read-483"><a href="#IOLoopBase.set__can_read-483"><span class="linenos">483</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to read&quot; checks for socket</span>
</span><span id="IOLoopBase.set__can_read-484"><a href="#IOLoopBase.set__can_read-484"><span class="linenos">484</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase.set__can_read-485"><a href="#IOLoopBase.set__can_read-485"><span class="linenos">485</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="IOLoopBase.set__can_read-486"><a href="#IOLoopBase.set__can_read-486"><span class="linenos">486</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase.set__can_read-487"><a href="#IOLoopBase.set__can_read-487"><span class="linenos">487</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase.set__can_read-488"><a href="#IOLoopBase.set__can_read-488"><span class="linenos">488</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will allow (True) or disallow (False) "socket available to read" checks for socket
:param conn: target socket
:param state: True - allow; False - disallow
:return:</p>
</div>


                            </div>
                            <div id="IOLoopBase.set__need_write" class="classattr">
                                        <input id="IOLoopBase.set__need_write-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set__need_write</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span>, </span><span class="param"><span class="n">state</span><span class="o">=</span><span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOLoopBase.set__need_write-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase.set__need_write"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase.set__need_write-490"><a href="#IOLoopBase.set__need_write-490"><span class="linenos">490</span></a>    <span class="k">def</span> <span class="nf">set__need_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IOLoopBase.set__need_write-491"><a href="#IOLoopBase.set__need_write-491"><span class="linenos">491</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase.set__need_write-492"><a href="#IOLoopBase.set__need_write-492"><span class="linenos">492</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to write&quot; checks for socket</span>
</span><span id="IOLoopBase.set__need_write-493"><a href="#IOLoopBase.set__need_write-493"><span class="linenos">493</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase.set__need_write-494"><a href="#IOLoopBase.set__need_write-494"><span class="linenos">494</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="IOLoopBase.set__need_write-495"><a href="#IOLoopBase.set__need_write-495"><span class="linenos">495</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase.set__need_write-496"><a href="#IOLoopBase.set__need_write-496"><span class="linenos">496</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase.set__need_write-497"><a href="#IOLoopBase.set__need_write-497"><span class="linenos">497</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will allow (True) or disallow (False) "socket available to write" checks for socket
:param conn: target socket
:param state: True - allow; False - disallow
:return:</p>
</div>


                            </div>
                            <div id="IOLoopBase.set__should_be_closed" class="classattr">
                                        <input id="IOLoopBase.set__should_be_closed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set__should_be_closed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOLoopBase.set__should_be_closed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase.set__should_be_closed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase.set__should_be_closed-499"><a href="#IOLoopBase.set__should_be_closed-499"><span class="linenos">499</span></a>    <span class="k">def</span> <span class="nf">set__should_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOLoopBase.set__should_be_closed-500"><a href="#IOLoopBase.set__should_be_closed-500"><span class="linenos">500</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase.set__should_be_closed-501"><a href="#IOLoopBase.set__should_be_closed-501"><span class="linenos">501</span></a><span class="sd">        Mark socket as &quot;should be closed&quot;</span>
</span><span id="IOLoopBase.set__should_be_closed-502"><a href="#IOLoopBase.set__should_be_closed-502"><span class="linenos">502</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase.set__should_be_closed-503"><a href="#IOLoopBase.set__should_be_closed-503"><span class="linenos">503</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase.set__should_be_closed-504"><a href="#IOLoopBase.set__should_be_closed-504"><span class="linenos">504</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase.set__should_be_closed-505"><a href="#IOLoopBase.set__should_be_closed-505"><span class="linenos">505</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Mark socket as "should be closed"
:param conn: target socket
:return:</p>
</div>


                            </div>
                            <div id="IOLoopBase.add_connection" class="classattr">
                                        <input id="IOLoopBase.add_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_connection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOLoopBase.add_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase.add_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase.add_connection-507"><a href="#IOLoopBase.add_connection-507"><span class="linenos">507</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOLoopBase.add_connection-508"><a href="#IOLoopBase.add_connection-508"><span class="linenos">508</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase.add_connection-509"><a href="#IOLoopBase.add_connection-509"><span class="linenos">509</span></a><span class="sd">        Will add socket to the internal connections list</span>
</span><span id="IOLoopBase.add_connection-510"><a href="#IOLoopBase.add_connection-510"><span class="linenos">510</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase.add_connection-511"><a href="#IOLoopBase.add_connection-511"><span class="linenos">511</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase.add_connection-512"><a href="#IOLoopBase.add_connection-512"><span class="linenos">512</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase.add_connection-513"><a href="#IOLoopBase.add_connection-513"><span class="linenos">513</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will add socket to the internal connections list
:param conn: target socket
:return:</p>
</div>


                            </div>
                            <div id="IOLoopBase.remove_connection" class="classattr">
                                        <input id="IOLoopBase.remove_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_connection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOLoopBase.remove_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOLoopBase.remove_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOLoopBase.remove_connection-515"><a href="#IOLoopBase.remove_connection-515"><span class="linenos">515</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOLoopBase.remove_connection-516"><a href="#IOLoopBase.remove_connection-516"><span class="linenos">516</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOLoopBase.remove_connection-517"><a href="#IOLoopBase.remove_connection-517"><span class="linenos">517</span></a><span class="sd">        Will remove socket from the internal connections list</span>
</span><span id="IOLoopBase.remove_connection-518"><a href="#IOLoopBase.remove_connection-518"><span class="linenos">518</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOLoopBase.remove_connection-519"><a href="#IOLoopBase.remove_connection-519"><span class="linenos">519</span></a><span class="sd">        :return:</span>
</span><span id="IOLoopBase.remove_connection-520"><a href="#IOLoopBase.remove_connection-520"><span class="linenos">520</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOLoopBase.remove_connection-521"><a href="#IOLoopBase.remove_connection-521"><span class="linenos">521</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will remove socket from the internal connections list
:param conn: target socket
:return:</p>
</div>


                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>