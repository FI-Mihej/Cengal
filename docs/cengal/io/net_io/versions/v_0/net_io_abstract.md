---
title: net_io_abstract
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.io<wbr>.net_io<wbr>.versions<wbr>.v_0<wbr>.net_io_abstract    </h1>

                
                        <input id="mod-net_io_abstract-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-net_io_abstract-view-source"><span>View Source</span></label>

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
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="sd">Module Docstring</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.1.1&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="k">class</span> <span class="nc">LoopIsAlreadyBegun</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="sd">    You can not run NetIOUserApi.start() if it was already started (and still running).</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="k">pass</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="k">class</span> <span class="nc">WrongConnectionType</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="sd">    You cannot run NetIOUserApi.make_connection() for ConnectionType.active_accepted connection. This kind of</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="sd">    connections are made only from (and by) inside of IO loop and logic itself.</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="k">pass</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="k">class</span> <span class="nc">CanNotMakeConnection</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="sd">    Currently not used. If there will be some exception on connect() call - it will be raised without any changes.</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="k">pass</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="k">class</span> <span class="nc">ConnectionType</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="n">passive</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># passive socket (bind())</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="n">active_accepted</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># active accepted socket (accept())</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="n">active_connected</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># active connected socket (connect())</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="k">class</span> <span class="nc">ConnectionState</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="n">not_connected_yet</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># socket is not in connection process</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="n">waiting_for_connection</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># socket is in connection process (async connection is delayed)</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="n">connected</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># socket is successfully connected</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="n">worker_fault</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># there was unhandled exception from one of the WorkerBase callbacks</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="n">io_fault</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># there was some IO trouble</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="n">waiting_for_disconnection</span> <span class="o">=</span> <span class="mi">5</span>  <span class="c1"># connection was marked as &quot;should be closed&quot; but was not closed yet</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="n">disconnected</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># socket is closed</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a><span class="k">class</span> <span class="nc">ConnectionInfo</span><span class="p">:</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>                 <span class="n">worker_obj</span><span class="p">,</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="sd">        :param worker_obj: constructed worker object (see WorkerBase for more info). If this is a passive</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="sd">            connection - it (worker_obj) will be inherited by the descendant active_accepted connections</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a><span class="sd">            by copy.copy() call (see WorkerBase.__copy__() method for more info)</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a><span class="sd">        :param connection_type: see ConnectionType() description</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="sd">        :param socket_address:  see socket.bind()/socket.connect() docs</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="sd">        :param socket_family: see socket.socket() docs</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="sd">        :param socket_type: see socket.socket() docs</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="sd">        :param socket_protocol: see socket.socket() docs</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a><span class="sd">        :param socket_fileno: see socket.socket() docs</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a><span class="sd">        :param backlog: see socket.listen() docs</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">worker_obj</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a><span class="k">class</span> <span class="nc">Connection</span><span class="p">:</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a><span class="sd">    Connection class. Usually created by IO loop or by IO API. But you can also create it by yourself</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>                 <span class="n">connection_id</span><span class="p">,</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>                 <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span><span class="p">,</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>                 <span class="n">connection_and_address_pair</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">,</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span><span class="p">,</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>                 <span class="n">connection_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>                 <span class="p">):</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="sd">        :param connection_id: unique connection identificator (unique within the IO object). You may use some random</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a><span class="sd">            GUID if you are creating connection by your self.</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a><span class="sd">        :param connection_and_address_pair: (conn, address) tuple where conn is connected socket (or it can be socket</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a><span class="sd">            is in the process of connection. But only if it was made by IO loop.).</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="sd">        :param connection_state: see ConnectionState for more information</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a><span class="sd">        :param connection_name: name of the connection (if it was provided)</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_info</span> <span class="o">=</span> <span class="n">connection_info</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">conn</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">address</span> <span class="o">=</span> <span class="n">connection_and_address_pair</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_name</span> <span class="o">=</span> <span class="n">connection_name</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">worker_obj</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>  <span class="c1"># already read data</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="p">)</span>  <span class="c1"># this data should be written</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_write_call</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="k">def</span> <span class="nf">add_must_be_written_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a><span class="sd">        Use this method to add data to output buffers</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a><span class="sd">        :param data: some new output data to be send through this connection</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a><span class="sd">        :return:</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a><span class="k">class</span> <span class="nc">NetIOUserApi</span><span class="p">:</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a><span class="sd">    You may rely and use freely use methods of this base class from inside your program or from inside your worker</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a><span class="sd">    (WorkerBase).</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_connections</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">passive_connections</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_id</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_name</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_fileno</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a><span class="sd">        Will start IO loop</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a><span class="sd">        :param destroy_on_finish: if True - destroy() will be called from inside of this method</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a><span class="sd">        :return:</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a><span class="sd">        Will initiate IO loop stop process</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a><span class="sd">        :return:</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>    <span class="k">def</span> <span class="nf">make_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span><span class="o">-&gt;</span><span class="n">Connection</span><span class="p">:</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a><span class="sd">        Will create connection from given connection_info object. Than connection will be established. Immediate or</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a><span class="sd">        delayed - depends on the connection type:</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="sd">        - ConnectionType.passive - immediate;</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">        - ConnectionType.active_connected - delayed.</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="sd">        In both cases WorkerBase.on_connect will be called immediately after connection will be successfully</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a><span class="sd">        established (IF it will be successfully established).</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a><span class="sd">        :param name: name of the connection. If you&#39;ll provide it - you will be able to find this connection in</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a><span class="sd">            NetIOUserApi.connection_by_name dictionary by it&#39;s name.</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a><span class="sd">        :return:</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a><span class="sd">        Will register already established connection. You need to use this method for example if you have already</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a><span class="sd">        connected socket</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="sd">        :param connection:</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a><span class="sd">        :return:</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a><span class="sd">        Will close and remove connection</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a><span class="sd">        :param connection:</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="sd">        :return:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>    <span class="k">def</span> <span class="nf">check_is_connection_need_to_sent_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a><span class="sd">        Will check connection to output data presence. It is automatically called after EACH WorkerBase callback call</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a><span class="sd">        by the IO loop. But if you are filling other connection&#39;s output buffer - you&#39;ll need to make this call for that</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a><span class="sd">        connection by your self.</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a><span class="sd">        :param connection:</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a><span class="sd">        :return:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a><span class="k">class</span> <span class="nc">NetIOCallbacks</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a><span class="sd">    Callbacks from this class will be called from inside (and by) IOMethodBase loop.</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>    <span class="k">def</span> <span class="nf">on_accept_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>    <span class="k">def</span> <span class="nf">on_connected</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>    <span class="k">def</span> <span class="nf">on_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>    <span class="k">def</span> <span class="nf">on_close</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a><span class="k">class</span> <span class="nc">NetIOBase</span><span class="p">(</span><span class="n">NetIOUserApi</span><span class="p">,</span> <span class="n">NetIOCallbacks</span><span class="p">):</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a><span class="sd">    Base class for any IO implementation (Linux, BSD, Windows, cross platform, etc.).</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a><span class="sd">        :param transport: class of the desired IOMethod. Instance (object) will be created by NetIOBase itself</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">method</span> <span class="o">=</span> <span class="n">transport</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a><span class="k">class</span> <span class="nc">WorkerBase</span><span class="p">:</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a><span class="sd">    Base class for all workers.</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a><span class="sd">    on_* callbacks will be called by the IO loop.</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a><span class="sd">    General info:</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a><span class="sd">    You can read input data from self.connection at any time (see &quot;Caution&quot; section of __init__ doc string) from any</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a><span class="sd">    callback.</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a><span class="sd">    You can write output data (to be send) to self.connection at any time (see &quot;Caution&quot;) from any callback.</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api</span><span class="p">:</span> <span class="n">NetIOUserApi</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a><span class="sd">        Caution:</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a><span class="sd">        Please do not rely on self.api and self.connection inside of your __init__ constructor: it is guaranteed that</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a><span class="sd">        they will be set before any callback call, but not at the construction process.</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a><span class="sd">        :param api: link to the constructed network io object</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a><span class="sd">        :param connection: link to the constructed connection object</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">api</span> <span class="o">=</span> <span class="n">api</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection</span> <span class="o">=</span> <span class="n">connection</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>    <span class="k">def</span> <span class="nf">on_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a><span class="sd">        Will be called after connection successfully established</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a><span class="sd">        :return:</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        <span class="k">pass</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a><span class="sd">        Will be called if there is some NEW data in the connection input buffer</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a><span class="sd">        :return:</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>        <span class="k">pass</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">on_no_more_data_to_write</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a><span class="sd">        Will be called after all data is sent.</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a><span class="sd">        Normally it will be called once (one single shot after each portion of out data is sent).</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a><span class="sd">        If you&#39;ll set self.connection.force_write_call to True state - this callback may be called continuously</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a><span class="sd">        (but not guaranteed: it depends of used IOMethod implementation)</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a><span class="sd">        :return:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>        <span class="k">pass</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>    <span class="k">def</span> <span class="nf">on_connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a><span class="sd">        Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a><span class="sd">        At this time, self.connection.connection_state is already set to ConnectionState.disconnected.</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a><span class="sd">        :return:</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>        <span class="k">pass</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a><span class="sd">        This method SHOULD be implemented. It should create a new instance and copy some global (shared) data from</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a><span class="sd">        current object to that new instance. It will be called when new peer is connected to existing passive connection</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a><span class="sd">        So this is the way you may use to give all new connection some links to some global data by worker object of</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a><span class="sd">        the passive connection replication process.</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a><span class="sd">        :return:</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a><span class="nd">@contextmanager</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a><span class="k">def</span> <span class="nf">net_io</span><span class="p">(</span><span class="n">net_io_obj</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a><span class="sd">    Context manager.</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a><span class="sd">    Usage:</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a><span class="sd">    main_io = NetIOBase()</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a><span class="sd">    with(net_io(main_io)) as io:</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a><span class="sd">        print(&#39;Preparing connections&#39;)</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a><span class="sd">        connection1 = io.make_connection(...)</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a><span class="sd">        connection2 = io.make_connection(...)</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a><span class="sd">        k = c + 12</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a><span class="sd">        ...</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a><span class="sd">        connectionN = io.make_connection(...)</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a><span class="sd">        print(&#39;Starting IO loop&#39;)</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a><span class="sd">    print(&#39;IO loop was finished properly&#39;)</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a><span class="sd">    :param net_io_obj: constructed IO instance (object)</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a><span class="sd">    :return:</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="k">yield</span> <span class="n">net_io_obj</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="n">net_io_obj</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        <span class="n">net_io_obj</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a><span class="k">class</span> <span class="nc">IOMethodBase</span><span class="p">:</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a><span class="sd">    Base class for all IOMethod implementation (select, epoll, overlapped io, kqueue, etc.)</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a><span class="sd">    All his methods are called by the NetIOBase instance.</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>        <span class="k">pass</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>    <span class="k">def</span> <span class="nf">loop_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a><span class="sd">        Single IO loop iteration.</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a><span class="sd">        This method holds all IOMethod logic.</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a><span class="sd">        :return:</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a><span class="sd">        Initiates destruction process</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a><span class="sd">        :return:</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>    <span class="k">def</span> <span class="nf">set__can_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to read&quot; checks for socket</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a><span class="sd">        :return:</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>    <span class="k">def</span> <span class="nf">set__need_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to write&quot; checks for socket</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a><span class="sd">        :return:</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>    <span class="k">def</span> <span class="nf">set__should_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a><span class="sd">        Mark socket as &quot;should be closed&quot;</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a><span class="sd">        :return:</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a><span class="sd">        Will add socket to the internal connections list</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a><span class="sd">        :return:</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a><span class="sd">        Will remove socket from the internal connections list</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a><span class="sd">        :return:</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopIsAlreadyBegun-42"><a href="#LoopIsAlreadyBegun-42"><span class="linenos">42</span></a><span class="k">class</span> <span class="nc">LoopIsAlreadyBegun</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="LoopIsAlreadyBegun-43"><a href="#LoopIsAlreadyBegun-43"><span class="linenos">43</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="LoopIsAlreadyBegun-44"><a href="#LoopIsAlreadyBegun-44"><span class="linenos">44</span></a><span class="sd">    You can not run NetIOUserApi.start() if it was already started (and still running).</span>
</span><span id="LoopIsAlreadyBegun-45"><a href="#LoopIsAlreadyBegun-45"><span class="linenos">45</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="LoopIsAlreadyBegun-46"><a href="#LoopIsAlreadyBegun-46"><span class="linenos">46</span></a>    <span class="k">pass</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="WrongConnectionType-49"><a href="#WrongConnectionType-49"><span class="linenos">49</span></a><span class="k">class</span> <span class="nc">WrongConnectionType</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="WrongConnectionType-50"><a href="#WrongConnectionType-50"><span class="linenos">50</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WrongConnectionType-51"><a href="#WrongConnectionType-51"><span class="linenos">51</span></a><span class="sd">    You cannot run NetIOUserApi.make_connection() for ConnectionType.active_accepted connection. This kind of</span>
</span><span id="WrongConnectionType-52"><a href="#WrongConnectionType-52"><span class="linenos">52</span></a><span class="sd">    connections are made only from (and by) inside of IO loop and logic itself.</span>
</span><span id="WrongConnectionType-53"><a href="#WrongConnectionType-53"><span class="linenos">53</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="WrongConnectionType-54"><a href="#WrongConnectionType-54"><span class="linenos">54</span></a>    <span class="k">pass</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="CanNotMakeConnection-57"><a href="#CanNotMakeConnection-57"><span class="linenos">57</span></a><span class="k">class</span> <span class="nc">CanNotMakeConnection</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="CanNotMakeConnection-58"><a href="#CanNotMakeConnection-58"><span class="linenos">58</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="CanNotMakeConnection-59"><a href="#CanNotMakeConnection-59"><span class="linenos">59</span></a><span class="sd">    Currently not used. If there will be some exception on connect() call - it will be raised without any changes.</span>
</span><span id="CanNotMakeConnection-60"><a href="#CanNotMakeConnection-60"><span class="linenos">60</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="CanNotMakeConnection-61"><a href="#CanNotMakeConnection-61"><span class="linenos">61</span></a>    <span class="k">pass</span>
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
                <section id="ConnectionType">
                            <input id="ConnectionType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ConnectionType</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="ConnectionType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionType-64"><a href="#ConnectionType-64"><span class="linenos">64</span></a><span class="k">class</span> <span class="nc">ConnectionType</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="ConnectionType-65"><a href="#ConnectionType-65"><span class="linenos">65</span></a>    <span class="n">passive</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># passive socket (bind())</span>
</span><span id="ConnectionType-66"><a href="#ConnectionType-66"><span class="linenos">66</span></a>    <span class="n">active_accepted</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># active accepted socket (accept())</span>
</span><span id="ConnectionType-67"><a href="#ConnectionType-67"><span class="linenos">67</span></a>    <span class="n">active_connected</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># active connected socket (connect())</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="ConnectionType.passive" class="classattr">
                                <div class="attr variable">
            <span class="name">passive</span>        =
<span class="default_value">&lt;<a href="#ConnectionType.passive">ConnectionType.passive</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionType.passive"></a>
    
    

                            </div>
                            <div id="ConnectionType.active_accepted" class="classattr">
                                <div class="attr variable">
            <span class="name">active_accepted</span>        =
<span class="default_value">&lt;<a href="#ConnectionType.active_accepted">ConnectionType.active_accepted</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionType.active_accepted"></a>
    
    

                            </div>
                            <div id="ConnectionType.active_connected" class="classattr">
                                <div class="attr variable">
            <span class="name">active_connected</span>        =
<span class="default_value">&lt;<a href="#ConnectionType.active_connected">ConnectionType.active_connected</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionType.active_connected"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="ConnectionType.name" class="variable">name</dd>
                <dd id="ConnectionType.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ConnectionState">
                            <input id="ConnectionState-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ConnectionState</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="ConnectionState-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionState"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionState-70"><a href="#ConnectionState-70"><span class="linenos">70</span></a><span class="k">class</span> <span class="nc">ConnectionState</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="ConnectionState-71"><a href="#ConnectionState-71"><span class="linenos">71</span></a>    <span class="n">not_connected_yet</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># socket is not in connection process</span>
</span><span id="ConnectionState-72"><a href="#ConnectionState-72"><span class="linenos">72</span></a>    <span class="n">waiting_for_connection</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># socket is in connection process (async connection is delayed)</span>
</span><span id="ConnectionState-73"><a href="#ConnectionState-73"><span class="linenos">73</span></a>    <span class="n">connected</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># socket is successfully connected</span>
</span><span id="ConnectionState-74"><a href="#ConnectionState-74"><span class="linenos">74</span></a>    <span class="n">worker_fault</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># there was unhandled exception from one of the WorkerBase callbacks</span>
</span><span id="ConnectionState-75"><a href="#ConnectionState-75"><span class="linenos">75</span></a>    <span class="n">io_fault</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># there was some IO trouble</span>
</span><span id="ConnectionState-76"><a href="#ConnectionState-76"><span class="linenos">76</span></a>    <span class="n">waiting_for_disconnection</span> <span class="o">=</span> <span class="mi">5</span>  <span class="c1"># connection was marked as &quot;should be closed&quot; but was not closed yet</span>
</span><span id="ConnectionState-77"><a href="#ConnectionState-77"><span class="linenos">77</span></a>    <span class="n">disconnected</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># socket is closed</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="ConnectionState.not_connected_yet" class="classattr">
                                <div class="attr variable">
            <span class="name">not_connected_yet</span>        =
<span class="default_value">&lt;<a href="#ConnectionState.not_connected_yet">ConnectionState.not_connected_yet</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.not_connected_yet"></a>
    
    

                            </div>
                            <div id="ConnectionState.waiting_for_connection" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_for_connection</span>        =
<span class="default_value">&lt;<a href="#ConnectionState.waiting_for_connection">ConnectionState.waiting_for_connection</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.waiting_for_connection"></a>
    
    

                            </div>
                            <div id="ConnectionState.connected" class="classattr">
                                <div class="attr variable">
            <span class="name">connected</span>        =
<span class="default_value">&lt;<a href="#ConnectionState.connected">ConnectionState.connected</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.connected"></a>
    
    

                            </div>
                            <div id="ConnectionState.worker_fault" class="classattr">
                                <div class="attr variable">
            <span class="name">worker_fault</span>        =
<span class="default_value">&lt;<a href="#ConnectionState.worker_fault">ConnectionState.worker_fault</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.worker_fault"></a>
    
    

                            </div>
                            <div id="ConnectionState.io_fault" class="classattr">
                                <div class="attr variable">
            <span class="name">io_fault</span>        =
<span class="default_value">&lt;<a href="#ConnectionState.io_fault">ConnectionState.io_fault</a>: 4&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.io_fault"></a>
    
    

                            </div>
                            <div id="ConnectionState.waiting_for_disconnection" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_for_disconnection</span>        =
<span class="default_value">&lt;<a href="#ConnectionState.waiting_for_disconnection">ConnectionState.waiting_for_disconnection</a>: 5&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.waiting_for_disconnection"></a>
    
    

                            </div>
                            <div id="ConnectionState.disconnected" class="classattr">
                                <div class="attr variable">
            <span class="name">disconnected</span>        =
<span class="default_value">&lt;<a href="#ConnectionState.disconnected">ConnectionState.disconnected</a>: 6&gt;</span>

        
    </div>
    <a class="headerlink" href="#ConnectionState.disconnected"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="ConnectionState.name" class="variable">name</dd>
                <dd id="ConnectionState.value" class="variable">value</dd>

            </div>
                                </dl>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionInfo-80"><a href="#ConnectionInfo-80"><span class="linenos"> 80</span></a><span class="k">class</span> <span class="nc">ConnectionInfo</span><span class="p">:</span>
</span><span id="ConnectionInfo-81"><a href="#ConnectionInfo-81"><span class="linenos"> 81</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="ConnectionInfo-82"><a href="#ConnectionInfo-82"><span class="linenos"> 82</span></a>                 <span class="n">worker_obj</span><span class="p">,</span>
</span><span id="ConnectionInfo-83"><a href="#ConnectionInfo-83"><span class="linenos"> 83</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="ConnectionInfo-84"><a href="#ConnectionInfo-84"><span class="linenos"> 84</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionInfo-85"><a href="#ConnectionInfo-85"><span class="linenos"> 85</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="ConnectionInfo-86"><a href="#ConnectionInfo-86"><span class="linenos"> 86</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="ConnectionInfo-87"><a href="#ConnectionInfo-87"><span class="linenos"> 87</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="ConnectionInfo-88"><a href="#ConnectionInfo-88"><span class="linenos"> 88</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionInfo-89"><a href="#ConnectionInfo-89"><span class="linenos"> 89</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
</span><span id="ConnectionInfo-90"><a href="#ConnectionInfo-90"><span class="linenos"> 90</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ConnectionInfo-91"><a href="#ConnectionInfo-91"><span class="linenos"> 91</span></a><span class="sd">        :param worker_obj: constructed worker object (see WorkerBase for more info). If this is a passive</span>
</span><span id="ConnectionInfo-92"><a href="#ConnectionInfo-92"><span class="linenos"> 92</span></a><span class="sd">            connection - it (worker_obj) will be inherited by the descendant active_accepted connections</span>
</span><span id="ConnectionInfo-93"><a href="#ConnectionInfo-93"><span class="linenos"> 93</span></a><span class="sd">            by copy.copy() call (see WorkerBase.__copy__() method for more info)</span>
</span><span id="ConnectionInfo-94"><a href="#ConnectionInfo-94"><span class="linenos"> 94</span></a><span class="sd">        :param connection_type: see ConnectionType() description</span>
</span><span id="ConnectionInfo-95"><a href="#ConnectionInfo-95"><span class="linenos"> 95</span></a><span class="sd">        :param socket_address:  see socket.bind()/socket.connect() docs</span>
</span><span id="ConnectionInfo-96"><a href="#ConnectionInfo-96"><span class="linenos"> 96</span></a><span class="sd">        :param socket_family: see socket.socket() docs</span>
</span><span id="ConnectionInfo-97"><a href="#ConnectionInfo-97"><span class="linenos"> 97</span></a><span class="sd">        :param socket_type: see socket.socket() docs</span>
</span><span id="ConnectionInfo-98"><a href="#ConnectionInfo-98"><span class="linenos"> 98</span></a><span class="sd">        :param socket_protocol: see socket.socket() docs</span>
</span><span id="ConnectionInfo-99"><a href="#ConnectionInfo-99"><span class="linenos"> 99</span></a><span class="sd">        :param socket_fileno: see socket.socket() docs</span>
</span><span id="ConnectionInfo-100"><a href="#ConnectionInfo-100"><span class="linenos">100</span></a><span class="sd">        :param backlog: see socket.listen() docs</span>
</span><span id="ConnectionInfo-101"><a href="#ConnectionInfo-101"><span class="linenos">101</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="ConnectionInfo-102"><a href="#ConnectionInfo-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">worker_obj</span>
</span><span id="ConnectionInfo-103"><a href="#ConnectionInfo-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="ConnectionInfo-104"><a href="#ConnectionInfo-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="ConnectionInfo-105"><a href="#ConnectionInfo-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="ConnectionInfo-106"><a href="#ConnectionInfo-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="ConnectionInfo-107"><a href="#ConnectionInfo-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="ConnectionInfo-108"><a href="#ConnectionInfo-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="ConnectionInfo-109"><a href="#ConnectionInfo-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
</span></pre></div>


    

                            <div id="ConnectionInfo.__init__" class="classattr">
                                        <input id="ConnectionInfo.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ConnectionInfo</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">worker_obj</span>,</span><span class="param">	<span class="n">connection_type</span><span class="p">:</span> <span class="n"><a href="#ConnectionType">ConnectionType</a></span>,</span><span class="param">	<span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">socket_family</span><span class="o">=&lt;</span><span class="n">AddressFamily</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">:</span> <span class="mi">2</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">socket_type</span><span class="o">=&lt;</span><span class="n">SocketKind</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span>,</span><span class="param">	<span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">backlog</span><span class="o">=</span><span class="mi">0</span></span>)</span>

                <label class="view-source-button" for="ConnectionInfo.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ConnectionInfo.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ConnectionInfo.__init__-81"><a href="#ConnectionInfo.__init__-81"><span class="linenos"> 81</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-82"><a href="#ConnectionInfo.__init__-82"><span class="linenos"> 82</span></a>                 <span class="n">worker_obj</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-83"><a href="#ConnectionInfo.__init__-83"><span class="linenos"> 83</span></a>                 <span class="n">connection_type</span><span class="p">:</span> <span class="n">ConnectionType</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-84"><a href="#ConnectionInfo.__init__-84"><span class="linenos"> 84</span></a>                 <span class="n">socket_address</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-85"><a href="#ConnectionInfo.__init__-85"><span class="linenos"> 85</span></a>                 <span class="n">socket_family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-86"><a href="#ConnectionInfo.__init__-86"><span class="linenos"> 86</span></a>                 <span class="n">socket_type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-87"><a href="#ConnectionInfo.__init__-87"><span class="linenos"> 87</span></a>                 <span class="n">socket_protocol</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-88"><a href="#ConnectionInfo.__init__-88"><span class="linenos"> 88</span></a>                 <span class="n">socket_fileno</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="ConnectionInfo.__init__-89"><a href="#ConnectionInfo.__init__-89"><span class="linenos"> 89</span></a>                 <span class="n">backlog</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
</span><span id="ConnectionInfo.__init__-90"><a href="#ConnectionInfo.__init__-90"><span class="linenos"> 90</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ConnectionInfo.__init__-91"><a href="#ConnectionInfo.__init__-91"><span class="linenos"> 91</span></a><span class="sd">        :param worker_obj: constructed worker object (see WorkerBase for more info). If this is a passive</span>
</span><span id="ConnectionInfo.__init__-92"><a href="#ConnectionInfo.__init__-92"><span class="linenos"> 92</span></a><span class="sd">            connection - it (worker_obj) will be inherited by the descendant active_accepted connections</span>
</span><span id="ConnectionInfo.__init__-93"><a href="#ConnectionInfo.__init__-93"><span class="linenos"> 93</span></a><span class="sd">            by copy.copy() call (see WorkerBase.__copy__() method for more info)</span>
</span><span id="ConnectionInfo.__init__-94"><a href="#ConnectionInfo.__init__-94"><span class="linenos"> 94</span></a><span class="sd">        :param connection_type: see ConnectionType() description</span>
</span><span id="ConnectionInfo.__init__-95"><a href="#ConnectionInfo.__init__-95"><span class="linenos"> 95</span></a><span class="sd">        :param socket_address:  see socket.bind()/socket.connect() docs</span>
</span><span id="ConnectionInfo.__init__-96"><a href="#ConnectionInfo.__init__-96"><span class="linenos"> 96</span></a><span class="sd">        :param socket_family: see socket.socket() docs</span>
</span><span id="ConnectionInfo.__init__-97"><a href="#ConnectionInfo.__init__-97"><span class="linenos"> 97</span></a><span class="sd">        :param socket_type: see socket.socket() docs</span>
</span><span id="ConnectionInfo.__init__-98"><a href="#ConnectionInfo.__init__-98"><span class="linenos"> 98</span></a><span class="sd">        :param socket_protocol: see socket.socket() docs</span>
</span><span id="ConnectionInfo.__init__-99"><a href="#ConnectionInfo.__init__-99"><span class="linenos"> 99</span></a><span class="sd">        :param socket_fileno: see socket.socket() docs</span>
</span><span id="ConnectionInfo.__init__-100"><a href="#ConnectionInfo.__init__-100"><span class="linenos">100</span></a><span class="sd">        :param backlog: see socket.listen() docs</span>
</span><span id="ConnectionInfo.__init__-101"><a href="#ConnectionInfo.__init__-101"><span class="linenos">101</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="ConnectionInfo.__init__-102"><a href="#ConnectionInfo.__init__-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">worker_obj</span>
</span><span id="ConnectionInfo.__init__-103"><a href="#ConnectionInfo.__init__-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_type</span> <span class="o">=</span> <span class="n">connection_type</span>
</span><span id="ConnectionInfo.__init__-104"><a href="#ConnectionInfo.__init__-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_address</span> <span class="o">=</span> <span class="n">socket_address</span>
</span><span id="ConnectionInfo.__init__-105"><a href="#ConnectionInfo.__init__-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_family</span> <span class="o">=</span> <span class="n">socket_family</span>
</span><span id="ConnectionInfo.__init__-106"><a href="#ConnectionInfo.__init__-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket_type</span>
</span><span id="ConnectionInfo.__init__-107"><a href="#ConnectionInfo.__init__-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_protocol</span> <span class="o">=</span> <span class="n">socket_protocol</span>
</span><span id="ConnectionInfo.__init__-108"><a href="#ConnectionInfo.__init__-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_fileno</span> <span class="o">=</span> <span class="n">socket_fileno</span>
</span><span id="ConnectionInfo.__init__-109"><a href="#ConnectionInfo.__init__-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">backlog</span> <span class="o">=</span> <span class="n">backlog</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection-112"><a href="#Connection-112"><span class="linenos">112</span></a><span class="k">class</span> <span class="nc">Connection</span><span class="p">:</span>
</span><span id="Connection-113"><a href="#Connection-113"><span class="linenos">113</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection-114"><a href="#Connection-114"><span class="linenos">114</span></a><span class="sd">    Connection class. Usually created by IO loop or by IO API. But you can also create it by yourself</span>
</span><span id="Connection-115"><a href="#Connection-115"><span class="linenos">115</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="Connection-116"><a href="#Connection-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="Connection-117"><a href="#Connection-117"><span class="linenos">117</span></a>                 <span class="n">connection_id</span><span class="p">,</span>
</span><span id="Connection-118"><a href="#Connection-118"><span class="linenos">118</span></a>                 <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span><span class="p">,</span>
</span><span id="Connection-119"><a href="#Connection-119"><span class="linenos">119</span></a>                 <span class="n">connection_and_address_pair</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">,</span>
</span><span id="Connection-120"><a href="#Connection-120"><span class="linenos">120</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span><span class="p">,</span>
</span><span id="Connection-121"><a href="#Connection-121"><span class="linenos">121</span></a>                 <span class="n">connection_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="Connection-122"><a href="#Connection-122"><span class="linenos">122</span></a>                 <span class="p">):</span>
</span><span id="Connection-123"><a href="#Connection-123"><span class="linenos">123</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection-124"><a href="#Connection-124"><span class="linenos">124</span></a><span class="sd">        :param connection_id: unique connection identificator (unique within the IO object). You may use some random</span>
</span><span id="Connection-125"><a href="#Connection-125"><span class="linenos">125</span></a><span class="sd">            GUID if you are creating connection by your self.</span>
</span><span id="Connection-126"><a href="#Connection-126"><span class="linenos">126</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="Connection-127"><a href="#Connection-127"><span class="linenos">127</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="Connection-128"><a href="#Connection-128"><span class="linenos">128</span></a><span class="sd">        :param connection_and_address_pair: (conn, address) tuple where conn is connected socket (or it can be socket</span>
</span><span id="Connection-129"><a href="#Connection-129"><span class="linenos">129</span></a><span class="sd">            is in the process of connection. But only if it was made by IO loop.).</span>
</span><span id="Connection-130"><a href="#Connection-130"><span class="linenos">130</span></a><span class="sd">        :param connection_state: see ConnectionState for more information</span>
</span><span id="Connection-131"><a href="#Connection-131"><span class="linenos">131</span></a><span class="sd">        :param connection_name: name of the connection (if it was provided)</span>
</span><span id="Connection-132"><a href="#Connection-132"><span class="linenos">132</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection-133"><a href="#Connection-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="Connection-134"><a href="#Connection-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_info</span> <span class="o">=</span> <span class="n">connection_info</span>
</span><span id="Connection-135"><a href="#Connection-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">conn</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">address</span> <span class="o">=</span> <span class="n">connection_and_address_pair</span>
</span><span id="Connection-136"><a href="#Connection-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="Connection-137"><a href="#Connection-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_name</span> <span class="o">=</span> <span class="n">connection_name</span>
</span><span id="Connection-138"><a href="#Connection-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">worker_obj</span>
</span><span id="Connection-139"><a href="#Connection-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>  <span class="c1"># already read data</span>
</span><span id="Connection-140"><a href="#Connection-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="p">)</span>  <span class="c1"># this data should be written</span>
</span><span id="Connection-141"><a href="#Connection-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_write_call</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Connection-142"><a href="#Connection-142"><span class="linenos">142</span></a>
</span><span id="Connection-143"><a href="#Connection-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="nf">add_must_be_written_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="Connection-144"><a href="#Connection-144"><span class="linenos">144</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection-145"><a href="#Connection-145"><span class="linenos">145</span></a><span class="sd">        Use this method to add data to output buffers</span>
</span><span id="Connection-146"><a href="#Connection-146"><span class="linenos">146</span></a><span class="sd">        :param data: some new output data to be send through this connection</span>
</span><span id="Connection-147"><a href="#Connection-147"><span class="linenos">147</span></a><span class="sd">        :return:</span>
</span><span id="Connection-148"><a href="#Connection-148"><span class="linenos">148</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection-149"><a href="#Connection-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.__init__-116"><a href="#Connection.__init__-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="Connection.__init__-117"><a href="#Connection.__init__-117"><span class="linenos">117</span></a>                 <span class="n">connection_id</span><span class="p">,</span>
</span><span id="Connection.__init__-118"><a href="#Connection.__init__-118"><span class="linenos">118</span></a>                 <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span><span class="p">,</span>
</span><span id="Connection.__init__-119"><a href="#Connection.__init__-119"><span class="linenos">119</span></a>                 <span class="n">connection_and_address_pair</span><span class="p">:</span> <span class="nb">tuple</span><span class="p">,</span>
</span><span id="Connection.__init__-120"><a href="#Connection.__init__-120"><span class="linenos">120</span></a>                 <span class="n">connection_state</span><span class="p">:</span> <span class="n">ConnectionState</span><span class="p">,</span>
</span><span id="Connection.__init__-121"><a href="#Connection.__init__-121"><span class="linenos">121</span></a>                 <span class="n">connection_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="Connection.__init__-122"><a href="#Connection.__init__-122"><span class="linenos">122</span></a>                 <span class="p">):</span>
</span><span id="Connection.__init__-123"><a href="#Connection.__init__-123"><span class="linenos">123</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection.__init__-124"><a href="#Connection.__init__-124"><span class="linenos">124</span></a><span class="sd">        :param connection_id: unique connection identificator (unique within the IO object). You may use some random</span>
</span><span id="Connection.__init__-125"><a href="#Connection.__init__-125"><span class="linenos">125</span></a><span class="sd">            GUID if you are creating connection by your self.</span>
</span><span id="Connection.__init__-126"><a href="#Connection.__init__-126"><span class="linenos">126</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="Connection.__init__-127"><a href="#Connection.__init__-127"><span class="linenos">127</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="Connection.__init__-128"><a href="#Connection.__init__-128"><span class="linenos">128</span></a><span class="sd">        :param connection_and_address_pair: (conn, address) tuple where conn is connected socket (or it can be socket</span>
</span><span id="Connection.__init__-129"><a href="#Connection.__init__-129"><span class="linenos">129</span></a><span class="sd">            is in the process of connection. But only if it was made by IO loop.).</span>
</span><span id="Connection.__init__-130"><a href="#Connection.__init__-130"><span class="linenos">130</span></a><span class="sd">        :param connection_state: see ConnectionState for more information</span>
</span><span id="Connection.__init__-131"><a href="#Connection.__init__-131"><span class="linenos">131</span></a><span class="sd">        :param connection_name: name of the connection (if it was provided)</span>
</span><span id="Connection.__init__-132"><a href="#Connection.__init__-132"><span class="linenos">132</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection.__init__-133"><a href="#Connection.__init__-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_id</span> <span class="o">=</span> <span class="n">connection_id</span>
</span><span id="Connection.__init__-134"><a href="#Connection.__init__-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_info</span> <span class="o">=</span> <span class="n">connection_info</span>
</span><span id="Connection.__init__-135"><a href="#Connection.__init__-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">conn</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">address</span> <span class="o">=</span> <span class="n">connection_and_address_pair</span>
</span><span id="Connection.__init__-136"><a href="#Connection.__init__-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_state</span> <span class="o">=</span> <span class="n">connection_state</span>
</span><span id="Connection.__init__-137"><a href="#Connection.__init__-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_name</span> <span class="o">=</span> <span class="n">connection_name</span>
</span><span id="Connection.__init__-138"><a href="#Connection.__init__-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_obj</span> <span class="o">=</span> <span class="n">connection_info</span><span class="o">.</span><span class="n">worker_obj</span>
</span><span id="Connection.__init__-139"><a href="#Connection.__init__-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_data</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>  <span class="c1"># already read data</span>
</span><span id="Connection.__init__-140"><a href="#Connection.__init__-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="p">)</span>  <span class="c1"># this data should be written</span>
</span><span id="Connection.__init__-141"><a href="#Connection.__init__-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_write_call</span> <span class="o">=</span> <span class="kc">False</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="Connection.add_must_be_written_data-143"><a href="#Connection.add_must_be_written_data-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="nf">add_must_be_written_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="Connection.add_must_be_written_data-144"><a href="#Connection.add_must_be_written_data-144"><span class="linenos">144</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Connection.add_must_be_written_data-145"><a href="#Connection.add_must_be_written_data-145"><span class="linenos">145</span></a><span class="sd">        Use this method to add data to output buffers</span>
</span><span id="Connection.add_must_be_written_data-146"><a href="#Connection.add_must_be_written_data-146"><span class="linenos">146</span></a><span class="sd">        :param data: some new output data to be send through this connection</span>
</span><span id="Connection.add_must_be_written_data-147"><a href="#Connection.add_must_be_written_data-147"><span class="linenos">147</span></a><span class="sd">        :return:</span>
</span><span id="Connection.add_must_be_written_data-148"><a href="#Connection.add_must_be_written_data-148"><span class="linenos">148</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Connection.add_must_be_written_data-149"><a href="#Connection.add_must_be_written_data-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span> <span class="o">=</span> <span class="nb">memoryview</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">must_be_written_data</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi-152"><a href="#NetIOUserApi-152"><span class="linenos">152</span></a><span class="k">class</span> <span class="nc">NetIOUserApi</span><span class="p">:</span>
</span><span id="NetIOUserApi-153"><a href="#NetIOUserApi-153"><span class="linenos">153</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-154"><a href="#NetIOUserApi-154"><span class="linenos">154</span></a><span class="sd">    You may rely and use freely use methods of this base class from inside your program or from inside your worker</span>
</span><span id="NetIOUserApi-155"><a href="#NetIOUserApi-155"><span class="linenos">155</span></a><span class="sd">    (WorkerBase).</span>
</span><span id="NetIOUserApi-156"><a href="#NetIOUserApi-156"><span class="linenos">156</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-157"><a href="#NetIOUserApi-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOUserApi-158"><a href="#NetIOUserApi-158"><span class="linenos">158</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="NetIOUserApi-159"><a href="#NetIOUserApi-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_connections</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="NetIOUserApi-160"><a href="#NetIOUserApi-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">passive_connections</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="NetIOUserApi-161"><a href="#NetIOUserApi-161"><span class="linenos">161</span></a>
</span><span id="NetIOUserApi-162"><a href="#NetIOUserApi-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_id</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NetIOUserApi-163"><a href="#NetIOUserApi-163"><span class="linenos">163</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_name</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NetIOUserApi-164"><a href="#NetIOUserApi-164"><span class="linenos">164</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection_by_fileno</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NetIOUserApi-165"><a href="#NetIOUserApi-165"><span class="linenos">165</span></a>
</span><span id="NetIOUserApi-166"><a href="#NetIOUserApi-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="NetIOUserApi-167"><a href="#NetIOUserApi-167"><span class="linenos">167</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-168"><a href="#NetIOUserApi-168"><span class="linenos">168</span></a><span class="sd">        Will start IO loop</span>
</span><span id="NetIOUserApi-169"><a href="#NetIOUserApi-169"><span class="linenos">169</span></a><span class="sd">        :param destroy_on_finish: if True - destroy() will be called from inside of this method</span>
</span><span id="NetIOUserApi-170"><a href="#NetIOUserApi-170"><span class="linenos">170</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-171"><a href="#NetIOUserApi-171"><span class="linenos">171</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-172"><a href="#NetIOUserApi-172"><span class="linenos">172</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-173"><a href="#NetIOUserApi-173"><span class="linenos">173</span></a>
</span><span id="NetIOUserApi-174"><a href="#NetIOUserApi-174"><span class="linenos">174</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOUserApi-175"><a href="#NetIOUserApi-175"><span class="linenos">175</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-176"><a href="#NetIOUserApi-176"><span class="linenos">176</span></a><span class="sd">        Will initiate IO loop stop process</span>
</span><span id="NetIOUserApi-177"><a href="#NetIOUserApi-177"><span class="linenos">177</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-178"><a href="#NetIOUserApi-178"><span class="linenos">178</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-179"><a href="#NetIOUserApi-179"><span class="linenos">179</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-180"><a href="#NetIOUserApi-180"><span class="linenos">180</span></a>
</span><span id="NetIOUserApi-181"><a href="#NetIOUserApi-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">make_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span><span class="o">-&gt;</span><span class="n">Connection</span><span class="p">:</span>
</span><span id="NetIOUserApi-182"><a href="#NetIOUserApi-182"><span class="linenos">182</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-183"><a href="#NetIOUserApi-183"><span class="linenos">183</span></a><span class="sd">        Will create connection from given connection_info object. Than connection will be established. Immediate or</span>
</span><span id="NetIOUserApi-184"><a href="#NetIOUserApi-184"><span class="linenos">184</span></a><span class="sd">        delayed - depends on the connection type:</span>
</span><span id="NetIOUserApi-185"><a href="#NetIOUserApi-185"><span class="linenos">185</span></a><span class="sd">        - ConnectionType.passive - immediate;</span>
</span><span id="NetIOUserApi-186"><a href="#NetIOUserApi-186"><span class="linenos">186</span></a><span class="sd">        - ConnectionType.active_connected - delayed.</span>
</span><span id="NetIOUserApi-187"><a href="#NetIOUserApi-187"><span class="linenos">187</span></a><span class="sd">        In both cases WorkerBase.on_connect will be called immediately after connection will be successfully</span>
</span><span id="NetIOUserApi-188"><a href="#NetIOUserApi-188"><span class="linenos">188</span></a><span class="sd">        established (IF it will be successfully established).</span>
</span><span id="NetIOUserApi-189"><a href="#NetIOUserApi-189"><span class="linenos">189</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="NetIOUserApi-190"><a href="#NetIOUserApi-190"><span class="linenos">190</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="NetIOUserApi-191"><a href="#NetIOUserApi-191"><span class="linenos">191</span></a><span class="sd">        :param name: name of the connection. If you&#39;ll provide it - you will be able to find this connection in</span>
</span><span id="NetIOUserApi-192"><a href="#NetIOUserApi-192"><span class="linenos">192</span></a><span class="sd">            NetIOUserApi.connection_by_name dictionary by it&#39;s name.</span>
</span><span id="NetIOUserApi-193"><a href="#NetIOUserApi-193"><span class="linenos">193</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-194"><a href="#NetIOUserApi-194"><span class="linenos">194</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-195"><a href="#NetIOUserApi-195"><span class="linenos">195</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-196"><a href="#NetIOUserApi-196"><span class="linenos">196</span></a>
</span><span id="NetIOUserApi-197"><a href="#NetIOUserApi-197"><span class="linenos">197</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi-198"><a href="#NetIOUserApi-198"><span class="linenos">198</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-199"><a href="#NetIOUserApi-199"><span class="linenos">199</span></a><span class="sd">        Will register already established connection. You need to use this method for example if you have already</span>
</span><span id="NetIOUserApi-200"><a href="#NetIOUserApi-200"><span class="linenos">200</span></a><span class="sd">        connected socket</span>
</span><span id="NetIOUserApi-201"><a href="#NetIOUserApi-201"><span class="linenos">201</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi-202"><a href="#NetIOUserApi-202"><span class="linenos">202</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-203"><a href="#NetIOUserApi-203"><span class="linenos">203</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-204"><a href="#NetIOUserApi-204"><span class="linenos">204</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-205"><a href="#NetIOUserApi-205"><span class="linenos">205</span></a>
</span><span id="NetIOUserApi-206"><a href="#NetIOUserApi-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi-207"><a href="#NetIOUserApi-207"><span class="linenos">207</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-208"><a href="#NetIOUserApi-208"><span class="linenos">208</span></a><span class="sd">        Will close and remove connection</span>
</span><span id="NetIOUserApi-209"><a href="#NetIOUserApi-209"><span class="linenos">209</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi-210"><a href="#NetIOUserApi-210"><span class="linenos">210</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-211"><a href="#NetIOUserApi-211"><span class="linenos">211</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-212"><a href="#NetIOUserApi-212"><span class="linenos">212</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOUserApi-213"><a href="#NetIOUserApi-213"><span class="linenos">213</span></a>
</span><span id="NetIOUserApi-214"><a href="#NetIOUserApi-214"><span class="linenos">214</span></a>    <span class="k">def</span> <span class="nf">check_is_connection_need_to_sent_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi-215"><a href="#NetIOUserApi-215"><span class="linenos">215</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-216"><a href="#NetIOUserApi-216"><span class="linenos">216</span></a><span class="sd">        Will check connection to output data presence. It is automatically called after EACH WorkerBase callback call</span>
</span><span id="NetIOUserApi-217"><a href="#NetIOUserApi-217"><span class="linenos">217</span></a><span class="sd">        by the IO loop. But if you are filling other connection&#39;s output buffer - you&#39;ll need to make this call for that</span>
</span><span id="NetIOUserApi-218"><a href="#NetIOUserApi-218"><span class="linenos">218</span></a><span class="sd">        connection by your self.</span>
</span><span id="NetIOUserApi-219"><a href="#NetIOUserApi-219"><span class="linenos">219</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi-220"><a href="#NetIOUserApi-220"><span class="linenos">220</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi-221"><a href="#NetIOUserApi-221"><span class="linenos">221</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi-222"><a href="#NetIOUserApi-222"><span class="linenos">222</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.start-166"><a href="#NetIOUserApi.start-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="NetIOUserApi.start-167"><a href="#NetIOUserApi.start-167"><span class="linenos">167</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.start-168"><a href="#NetIOUserApi.start-168"><span class="linenos">168</span></a><span class="sd">        Will start IO loop</span>
</span><span id="NetIOUserApi.start-169"><a href="#NetIOUserApi.start-169"><span class="linenos">169</span></a><span class="sd">        :param destroy_on_finish: if True - destroy() will be called from inside of this method</span>
</span><span id="NetIOUserApi.start-170"><a href="#NetIOUserApi.start-170"><span class="linenos">170</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.start-171"><a href="#NetIOUserApi.start-171"><span class="linenos">171</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.start-172"><a href="#NetIOUserApi.start-172"><span class="linenos">172</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.stop-174"><a href="#NetIOUserApi.stop-174"><span class="linenos">174</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOUserApi.stop-175"><a href="#NetIOUserApi.stop-175"><span class="linenos">175</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.stop-176"><a href="#NetIOUserApi.stop-176"><span class="linenos">176</span></a><span class="sd">        Will initiate IO loop stop process</span>
</span><span id="NetIOUserApi.stop-177"><a href="#NetIOUserApi.stop-177"><span class="linenos">177</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.stop-178"><a href="#NetIOUserApi.stop-178"><span class="linenos">178</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.stop-179"><a href="#NetIOUserApi.stop-179"><span class="linenos">179</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.make_connection-181"><a href="#NetIOUserApi.make_connection-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">make_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection_info</span><span class="p">:</span> <span class="n">ConnectionInfo</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span><span class="o">-&gt;</span><span class="n">Connection</span><span class="p">:</span>
</span><span id="NetIOUserApi.make_connection-182"><a href="#NetIOUserApi.make_connection-182"><span class="linenos">182</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.make_connection-183"><a href="#NetIOUserApi.make_connection-183"><span class="linenos">183</span></a><span class="sd">        Will create connection from given connection_info object. Than connection will be established. Immediate or</span>
</span><span id="NetIOUserApi.make_connection-184"><a href="#NetIOUserApi.make_connection-184"><span class="linenos">184</span></a><span class="sd">        delayed - depends on the connection type:</span>
</span><span id="NetIOUserApi.make_connection-185"><a href="#NetIOUserApi.make_connection-185"><span class="linenos">185</span></a><span class="sd">        - ConnectionType.passive - immediate;</span>
</span><span id="NetIOUserApi.make_connection-186"><a href="#NetIOUserApi.make_connection-186"><span class="linenos">186</span></a><span class="sd">        - ConnectionType.active_connected - delayed.</span>
</span><span id="NetIOUserApi.make_connection-187"><a href="#NetIOUserApi.make_connection-187"><span class="linenos">187</span></a><span class="sd">        In both cases WorkerBase.on_connect will be called immediately after connection will be successfully</span>
</span><span id="NetIOUserApi.make_connection-188"><a href="#NetIOUserApi.make_connection-188"><span class="linenos">188</span></a><span class="sd">        established (IF it will be successfully established).</span>
</span><span id="NetIOUserApi.make_connection-189"><a href="#NetIOUserApi.make_connection-189"><span class="linenos">189</span></a><span class="sd">        :param connection_info: new connection will be created using information provided in connection_info object.</span>
</span><span id="NetIOUserApi.make_connection-190"><a href="#NetIOUserApi.make_connection-190"><span class="linenos">190</span></a><span class="sd">            See ConnectionInfo() for more information</span>
</span><span id="NetIOUserApi.make_connection-191"><a href="#NetIOUserApi.make_connection-191"><span class="linenos">191</span></a><span class="sd">        :param name: name of the connection. If you&#39;ll provide it - you will be able to find this connection in</span>
</span><span id="NetIOUserApi.make_connection-192"><a href="#NetIOUserApi.make_connection-192"><span class="linenos">192</span></a><span class="sd">            NetIOUserApi.connection_by_name dictionary by it&#39;s name.</span>
</span><span id="NetIOUserApi.make_connection-193"><a href="#NetIOUserApi.make_connection-193"><span class="linenos">193</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.make_connection-194"><a href="#NetIOUserApi.make_connection-194"><span class="linenos">194</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.make_connection-195"><a href="#NetIOUserApi.make_connection-195"><span class="linenos">195</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.add_connection-197"><a href="#NetIOUserApi.add_connection-197"><span class="linenos">197</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi.add_connection-198"><a href="#NetIOUserApi.add_connection-198"><span class="linenos">198</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.add_connection-199"><a href="#NetIOUserApi.add_connection-199"><span class="linenos">199</span></a><span class="sd">        Will register already established connection. You need to use this method for example if you have already</span>
</span><span id="NetIOUserApi.add_connection-200"><a href="#NetIOUserApi.add_connection-200"><span class="linenos">200</span></a><span class="sd">        connected socket</span>
</span><span id="NetIOUserApi.add_connection-201"><a href="#NetIOUserApi.add_connection-201"><span class="linenos">201</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi.add_connection-202"><a href="#NetIOUserApi.add_connection-202"><span class="linenos">202</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.add_connection-203"><a href="#NetIOUserApi.add_connection-203"><span class="linenos">203</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.add_connection-204"><a href="#NetIOUserApi.add_connection-204"><span class="linenos">204</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.remove_connection-206"><a href="#NetIOUserApi.remove_connection-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi.remove_connection-207"><a href="#NetIOUserApi.remove_connection-207"><span class="linenos">207</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.remove_connection-208"><a href="#NetIOUserApi.remove_connection-208"><span class="linenos">208</span></a><span class="sd">        Will close and remove connection</span>
</span><span id="NetIOUserApi.remove_connection-209"><a href="#NetIOUserApi.remove_connection-209"><span class="linenos">209</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi.remove_connection-210"><a href="#NetIOUserApi.remove_connection-210"><span class="linenos">210</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.remove_connection-211"><a href="#NetIOUserApi.remove_connection-211"><span class="linenos">211</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.remove_connection-212"><a href="#NetIOUserApi.remove_connection-212"><span class="linenos">212</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-214"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-214"><span class="linenos">214</span></a>    <span class="k">def</span> <span class="nf">check_is_connection_need_to_sent_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-215"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-215"><span class="linenos">215</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-216"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-216"><span class="linenos">216</span></a><span class="sd">        Will check connection to output data presence. It is automatically called after EACH WorkerBase callback call</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-217"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-217"><span class="linenos">217</span></a><span class="sd">        by the IO loop. But if you are filling other connection&#39;s output buffer - you&#39;ll need to make this call for that</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-218"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-218"><span class="linenos">218</span></a><span class="sd">        connection by your self.</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-219"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-219"><span class="linenos">219</span></a><span class="sd">        :param connection:</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-220"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-220"><span class="linenos">220</span></a><span class="sd">        :return:</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-221"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-221"><span class="linenos">221</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOUserApi.check_is_connection_need_to_sent_data-222"><a href="#NetIOUserApi.check_is_connection_need_to_sent_data-222"><span class="linenos">222</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks-225"><a href="#NetIOCallbacks-225"><span class="linenos">225</span></a><span class="k">class</span> <span class="nc">NetIOCallbacks</span><span class="p">:</span>
</span><span id="NetIOCallbacks-226"><a href="#NetIOCallbacks-226"><span class="linenos">226</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOCallbacks-227"><a href="#NetIOCallbacks-227"><span class="linenos">227</span></a><span class="sd">    Callbacks from this class will be called from inside (and by) IOMethodBase loop.</span>
</span><span id="NetIOCallbacks-228"><a href="#NetIOCallbacks-228"><span class="linenos">228</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="NetIOCallbacks-229"><a href="#NetIOCallbacks-229"><span class="linenos">229</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOCallbacks-230"><a href="#NetIOCallbacks-230"><span class="linenos">230</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="NetIOCallbacks-231"><a href="#NetIOCallbacks-231"><span class="linenos">231</span></a>
</span><span id="NetIOCallbacks-232"><a href="#NetIOCallbacks-232"><span class="linenos">232</span></a>    <span class="k">def</span> <span class="nf">on_accept_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-233"><a href="#NetIOCallbacks-233"><span class="linenos">233</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOCallbacks-234"><a href="#NetIOCallbacks-234"><span class="linenos">234</span></a>
</span><span id="NetIOCallbacks-235"><a href="#NetIOCallbacks-235"><span class="linenos">235</span></a>    <span class="k">def</span> <span class="nf">on_connected</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-236"><a href="#NetIOCallbacks-236"><span class="linenos">236</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOCallbacks-237"><a href="#NetIOCallbacks-237"><span class="linenos">237</span></a>
</span><span id="NetIOCallbacks-238"><a href="#NetIOCallbacks-238"><span class="linenos">238</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-239"><a href="#NetIOCallbacks-239"><span class="linenos">239</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOCallbacks-240"><a href="#NetIOCallbacks-240"><span class="linenos">240</span></a>
</span><span id="NetIOCallbacks-241"><a href="#NetIOCallbacks-241"><span class="linenos">241</span></a>    <span class="k">def</span> <span class="nf">on_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-242"><a href="#NetIOCallbacks-242"><span class="linenos">242</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="NetIOCallbacks-243"><a href="#NetIOCallbacks-243"><span class="linenos">243</span></a>
</span><span id="NetIOCallbacks-244"><a href="#NetIOCallbacks-244"><span class="linenos">244</span></a>    <span class="k">def</span> <span class="nf">on_close</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks-245"><a href="#NetIOCallbacks-245"><span class="linenos">245</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_accept_connection-232"><a href="#NetIOCallbacks.on_accept_connection-232"><span class="linenos">232</span></a>    <span class="k">def</span> <span class="nf">on_accept_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_accept_connection-233"><a href="#NetIOCallbacks.on_accept_connection-233"><span class="linenos">233</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_connected-235"><a href="#NetIOCallbacks.on_connected-235"><span class="linenos">235</span></a>    <span class="k">def</span> <span class="nf">on_connected</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_connected-236"><a href="#NetIOCallbacks.on_connected-236"><span class="linenos">236</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_read-238"><a href="#NetIOCallbacks.on_read-238"><span class="linenos">238</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_read-239"><a href="#NetIOCallbacks.on_read-239"><span class="linenos">239</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_write-241"><a href="#NetIOCallbacks.on_write-241"><span class="linenos">241</span></a>    <span class="k">def</span> <span class="nf">on_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_write-242"><a href="#NetIOCallbacks.on_write-242"><span class="linenos">242</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOCallbacks.on_close-244"><a href="#NetIOCallbacks.on_close-244"><span class="linenos">244</span></a>    <span class="k">def</span> <span class="nf">on_close</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="p">):</span>
</span><span id="NetIOCallbacks.on_close-245"><a href="#NetIOCallbacks.on_close-245"><span class="linenos">245</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOBase-248"><a href="#NetIOBase-248"><span class="linenos">248</span></a><span class="k">class</span> <span class="nc">NetIOBase</span><span class="p">(</span><span class="n">NetIOUserApi</span><span class="p">,</span> <span class="n">NetIOCallbacks</span><span class="p">):</span>
</span><span id="NetIOBase-249"><a href="#NetIOBase-249"><span class="linenos">249</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOBase-250"><a href="#NetIOBase-250"><span class="linenos">250</span></a><span class="sd">    Base class for any IO implementation (Linux, BSD, Windows, cross platform, etc.).</span>
</span><span id="NetIOBase-251"><a href="#NetIOBase-251"><span class="linenos">251</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="NetIOBase-252"><a href="#NetIOBase-252"><span class="linenos">252</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="NetIOBase-253"><a href="#NetIOBase-253"><span class="linenos">253</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOBase-254"><a href="#NetIOBase-254"><span class="linenos">254</span></a>
</span><span id="NetIOBase-255"><a href="#NetIOBase-255"><span class="linenos">255</span></a><span class="sd">        :param transport: class of the desired IOMethod. Instance (object) will be created by NetIOBase itself</span>
</span><span id="NetIOBase-256"><a href="#NetIOBase-256"><span class="linenos">256</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOBase-257"><a href="#NetIOBase-257"><span class="linenos">257</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="NetIOBase-258"><a href="#NetIOBase-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">method</span> <span class="o">=</span> <span class="n">transport</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="NetIOBase-259"><a href="#NetIOBase-259"><span class="linenos">259</span></a>
</span><span id="NetIOBase-260"><a href="#NetIOBase-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOBase-261"><a href="#NetIOBase-261"><span class="linenos">261</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOBase.__init__-252"><a href="#NetIOBase.__init__-252"><span class="linenos">252</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="NetIOBase.__init__-253"><a href="#NetIOBase.__init__-253"><span class="linenos">253</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="NetIOBase.__init__-254"><a href="#NetIOBase.__init__-254"><span class="linenos">254</span></a>
</span><span id="NetIOBase.__init__-255"><a href="#NetIOBase.__init__-255"><span class="linenos">255</span></a><span class="sd">        :param transport: class of the desired IOMethod. Instance (object) will be created by NetIOBase itself</span>
</span><span id="NetIOBase.__init__-256"><a href="#NetIOBase.__init__-256"><span class="linenos">256</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NetIOBase.__init__-257"><a href="#NetIOBase.__init__-257"><span class="linenos">257</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="NetIOBase.__init__-258"><a href="#NetIOBase.__init__-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">method</span> <span class="o">=</span> <span class="n">transport</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="NetIOBase.destroy-260"><a href="#NetIOBase.destroy-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NetIOBase.destroy-261"><a href="#NetIOBase.destroy-261"><span class="linenos">261</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase-264"><a href="#WorkerBase-264"><span class="linenos">264</span></a><span class="k">class</span> <span class="nc">WorkerBase</span><span class="p">:</span>
</span><span id="WorkerBase-265"><a href="#WorkerBase-265"><span class="linenos">265</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-266"><a href="#WorkerBase-266"><span class="linenos">266</span></a><span class="sd">    Base class for all workers.</span>
</span><span id="WorkerBase-267"><a href="#WorkerBase-267"><span class="linenos">267</span></a><span class="sd">    on_* callbacks will be called by the IO loop.</span>
</span><span id="WorkerBase-268"><a href="#WorkerBase-268"><span class="linenos">268</span></a>
</span><span id="WorkerBase-269"><a href="#WorkerBase-269"><span class="linenos">269</span></a><span class="sd">    General info:</span>
</span><span id="WorkerBase-270"><a href="#WorkerBase-270"><span class="linenos">270</span></a><span class="sd">    You can read input data from self.connection at any time (see &quot;Caution&quot; section of __init__ doc string) from any</span>
</span><span id="WorkerBase-271"><a href="#WorkerBase-271"><span class="linenos">271</span></a><span class="sd">    callback.</span>
</span><span id="WorkerBase-272"><a href="#WorkerBase-272"><span class="linenos">272</span></a><span class="sd">    You can write output data (to be send) to self.connection at any time (see &quot;Caution&quot;) from any callback.</span>
</span><span id="WorkerBase-273"><a href="#WorkerBase-273"><span class="linenos">273</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="WorkerBase-274"><a href="#WorkerBase-274"><span class="linenos">274</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api</span><span class="p">:</span> <span class="n">NetIOUserApi</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="WorkerBase-275"><a href="#WorkerBase-275"><span class="linenos">275</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-276"><a href="#WorkerBase-276"><span class="linenos">276</span></a><span class="sd">        Caution:</span>
</span><span id="WorkerBase-277"><a href="#WorkerBase-277"><span class="linenos">277</span></a><span class="sd">        Please do not rely on self.api and self.connection inside of your __init__ constructor: it is guaranteed that</span>
</span><span id="WorkerBase-278"><a href="#WorkerBase-278"><span class="linenos">278</span></a><span class="sd">        they will be set before any callback call, but not at the construction process.</span>
</span><span id="WorkerBase-279"><a href="#WorkerBase-279"><span class="linenos">279</span></a>
</span><span id="WorkerBase-280"><a href="#WorkerBase-280"><span class="linenos">280</span></a><span class="sd">        :param api: link to the constructed network io object</span>
</span><span id="WorkerBase-281"><a href="#WorkerBase-281"><span class="linenos">281</span></a><span class="sd">        :param connection: link to the constructed connection object</span>
</span><span id="WorkerBase-282"><a href="#WorkerBase-282"><span class="linenos">282</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-283"><a href="#WorkerBase-283"><span class="linenos">283</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">api</span> <span class="o">=</span> <span class="n">api</span>
</span><span id="WorkerBase-284"><a href="#WorkerBase-284"><span class="linenos">284</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection</span> <span class="o">=</span> <span class="n">connection</span>
</span><span id="WorkerBase-285"><a href="#WorkerBase-285"><span class="linenos">285</span></a>
</span><span id="WorkerBase-286"><a href="#WorkerBase-286"><span class="linenos">286</span></a>    <span class="k">def</span> <span class="nf">on_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-287"><a href="#WorkerBase-287"><span class="linenos">287</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-288"><a href="#WorkerBase-288"><span class="linenos">288</span></a><span class="sd">        Will be called after connection successfully established</span>
</span><span id="WorkerBase-289"><a href="#WorkerBase-289"><span class="linenos">289</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-290"><a href="#WorkerBase-290"><span class="linenos">290</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-291"><a href="#WorkerBase-291"><span class="linenos">291</span></a>        <span class="k">pass</span>
</span><span id="WorkerBase-292"><a href="#WorkerBase-292"><span class="linenos">292</span></a>
</span><span id="WorkerBase-293"><a href="#WorkerBase-293"><span class="linenos">293</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-294"><a href="#WorkerBase-294"><span class="linenos">294</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-295"><a href="#WorkerBase-295"><span class="linenos">295</span></a><span class="sd">        Will be called if there is some NEW data in the connection input buffer</span>
</span><span id="WorkerBase-296"><a href="#WorkerBase-296"><span class="linenos">296</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-297"><a href="#WorkerBase-297"><span class="linenos">297</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-298"><a href="#WorkerBase-298"><span class="linenos">298</span></a>        <span class="k">pass</span>
</span><span id="WorkerBase-299"><a href="#WorkerBase-299"><span class="linenos">299</span></a>
</span><span id="WorkerBase-300"><a href="#WorkerBase-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="nf">on_no_more_data_to_write</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-301"><a href="#WorkerBase-301"><span class="linenos">301</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-302"><a href="#WorkerBase-302"><span class="linenos">302</span></a><span class="sd">        Will be called after all data is sent.</span>
</span><span id="WorkerBase-303"><a href="#WorkerBase-303"><span class="linenos">303</span></a><span class="sd">        Normally it will be called once (one single shot after each portion of out data is sent).</span>
</span><span id="WorkerBase-304"><a href="#WorkerBase-304"><span class="linenos">304</span></a><span class="sd">        If you&#39;ll set self.connection.force_write_call to True state - this callback may be called continuously</span>
</span><span id="WorkerBase-305"><a href="#WorkerBase-305"><span class="linenos">305</span></a><span class="sd">        (but not guaranteed: it depends of used IOMethod implementation)</span>
</span><span id="WorkerBase-306"><a href="#WorkerBase-306"><span class="linenos">306</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-307"><a href="#WorkerBase-307"><span class="linenos">307</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-308"><a href="#WorkerBase-308"><span class="linenos">308</span></a>        <span class="k">pass</span>
</span><span id="WorkerBase-309"><a href="#WorkerBase-309"><span class="linenos">309</span></a>
</span><span id="WorkerBase-310"><a href="#WorkerBase-310"><span class="linenos">310</span></a>    <span class="k">def</span> <span class="nf">on_connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-311"><a href="#WorkerBase-311"><span class="linenos">311</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-312"><a href="#WorkerBase-312"><span class="linenos">312</span></a><span class="sd">        Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.</span>
</span><span id="WorkerBase-313"><a href="#WorkerBase-313"><span class="linenos">313</span></a><span class="sd">        At this time, self.connection.connection_state is already set to ConnectionState.disconnected.</span>
</span><span id="WorkerBase-314"><a href="#WorkerBase-314"><span class="linenos">314</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-315"><a href="#WorkerBase-315"><span class="linenos">315</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-316"><a href="#WorkerBase-316"><span class="linenos">316</span></a>        <span class="k">pass</span>
</span><span id="WorkerBase-317"><a href="#WorkerBase-317"><span class="linenos">317</span></a>
</span><span id="WorkerBase-318"><a href="#WorkerBase-318"><span class="linenos">318</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase-319"><a href="#WorkerBase-319"><span class="linenos">319</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase-320"><a href="#WorkerBase-320"><span class="linenos">320</span></a><span class="sd">        This method SHOULD be implemented. It should create a new instance and copy some global (shared) data from</span>
</span><span id="WorkerBase-321"><a href="#WorkerBase-321"><span class="linenos">321</span></a><span class="sd">        current object to that new instance. It will be called when new peer is connected to existing passive connection</span>
</span><span id="WorkerBase-322"><a href="#WorkerBase-322"><span class="linenos">322</span></a><span class="sd">        So this is the way you may use to give all new connection some links to some global data by worker object of</span>
</span><span id="WorkerBase-323"><a href="#WorkerBase-323"><span class="linenos">323</span></a><span class="sd">        the passive connection replication process.</span>
</span><span id="WorkerBase-324"><a href="#WorkerBase-324"><span class="linenos">324</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase-325"><a href="#WorkerBase-325"><span class="linenos">325</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase-326"><a href="#WorkerBase-326"><span class="linenos">326</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.__init__-274"><a href="#WorkerBase.__init__-274"><span class="linenos">274</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">api</span><span class="p">:</span> <span class="n">NetIOUserApi</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">connection</span><span class="p">:</span> <span class="n">Connection</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="WorkerBase.__init__-275"><a href="#WorkerBase.__init__-275"><span class="linenos">275</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.__init__-276"><a href="#WorkerBase.__init__-276"><span class="linenos">276</span></a><span class="sd">        Caution:</span>
</span><span id="WorkerBase.__init__-277"><a href="#WorkerBase.__init__-277"><span class="linenos">277</span></a><span class="sd">        Please do not rely on self.api and self.connection inside of your __init__ constructor: it is guaranteed that</span>
</span><span id="WorkerBase.__init__-278"><a href="#WorkerBase.__init__-278"><span class="linenos">278</span></a><span class="sd">        they will be set before any callback call, but not at the construction process.</span>
</span><span id="WorkerBase.__init__-279"><a href="#WorkerBase.__init__-279"><span class="linenos">279</span></a>
</span><span id="WorkerBase.__init__-280"><a href="#WorkerBase.__init__-280"><span class="linenos">280</span></a><span class="sd">        :param api: link to the constructed network io object</span>
</span><span id="WorkerBase.__init__-281"><a href="#WorkerBase.__init__-281"><span class="linenos">281</span></a><span class="sd">        :param connection: link to the constructed connection object</span>
</span><span id="WorkerBase.__init__-282"><a href="#WorkerBase.__init__-282"><span class="linenos">282</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.__init__-283"><a href="#WorkerBase.__init__-283"><span class="linenos">283</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">api</span> <span class="o">=</span> <span class="n">api</span>
</span><span id="WorkerBase.__init__-284"><a href="#WorkerBase.__init__-284"><span class="linenos">284</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">connection</span> <span class="o">=</span> <span class="n">connection</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.on_connect-286"><a href="#WorkerBase.on_connect-286"><span class="linenos">286</span></a>    <span class="k">def</span> <span class="nf">on_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase.on_connect-287"><a href="#WorkerBase.on_connect-287"><span class="linenos">287</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_connect-288"><a href="#WorkerBase.on_connect-288"><span class="linenos">288</span></a><span class="sd">        Will be called after connection successfully established</span>
</span><span id="WorkerBase.on_connect-289"><a href="#WorkerBase.on_connect-289"><span class="linenos">289</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase.on_connect-290"><a href="#WorkerBase.on_connect-290"><span class="linenos">290</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_connect-291"><a href="#WorkerBase.on_connect-291"><span class="linenos">291</span></a>        <span class="k">pass</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.on_read-293"><a href="#WorkerBase.on_read-293"><span class="linenos">293</span></a>    <span class="k">def</span> <span class="nf">on_read</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase.on_read-294"><a href="#WorkerBase.on_read-294"><span class="linenos">294</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_read-295"><a href="#WorkerBase.on_read-295"><span class="linenos">295</span></a><span class="sd">        Will be called if there is some NEW data in the connection input buffer</span>
</span><span id="WorkerBase.on_read-296"><a href="#WorkerBase.on_read-296"><span class="linenos">296</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase.on_read-297"><a href="#WorkerBase.on_read-297"><span class="linenos">297</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_read-298"><a href="#WorkerBase.on_read-298"><span class="linenos">298</span></a>        <span class="k">pass</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.on_no_more_data_to_write-300"><a href="#WorkerBase.on_no_more_data_to_write-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="nf">on_no_more_data_to_write</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase.on_no_more_data_to_write-301"><a href="#WorkerBase.on_no_more_data_to_write-301"><span class="linenos">301</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_no_more_data_to_write-302"><a href="#WorkerBase.on_no_more_data_to_write-302"><span class="linenos">302</span></a><span class="sd">        Will be called after all data is sent.</span>
</span><span id="WorkerBase.on_no_more_data_to_write-303"><a href="#WorkerBase.on_no_more_data_to_write-303"><span class="linenos">303</span></a><span class="sd">        Normally it will be called once (one single shot after each portion of out data is sent).</span>
</span><span id="WorkerBase.on_no_more_data_to_write-304"><a href="#WorkerBase.on_no_more_data_to_write-304"><span class="linenos">304</span></a><span class="sd">        If you&#39;ll set self.connection.force_write_call to True state - this callback may be called continuously</span>
</span><span id="WorkerBase.on_no_more_data_to_write-305"><a href="#WorkerBase.on_no_more_data_to_write-305"><span class="linenos">305</span></a><span class="sd">        (but not guaranteed: it depends of used IOMethod implementation)</span>
</span><span id="WorkerBase.on_no_more_data_to_write-306"><a href="#WorkerBase.on_no_more_data_to_write-306"><span class="linenos">306</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase.on_no_more_data_to_write-307"><a href="#WorkerBase.on_no_more_data_to_write-307"><span class="linenos">307</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_no_more_data_to_write-308"><a href="#WorkerBase.on_no_more_data_to_write-308"><span class="linenos">308</span></a>        <span class="k">pass</span>
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
            <div class="pdoc-code codehilite"><pre><span></span><span id="WorkerBase.on_connection_lost-310"><a href="#WorkerBase.on_connection_lost-310"><span class="linenos">310</span></a>    <span class="k">def</span> <span class="nf">on_connection_lost</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WorkerBase.on_connection_lost-311"><a href="#WorkerBase.on_connection_lost-311"><span class="linenos">311</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_connection_lost-312"><a href="#WorkerBase.on_connection_lost-312"><span class="linenos">312</span></a><span class="sd">        Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.</span>
</span><span id="WorkerBase.on_connection_lost-313"><a href="#WorkerBase.on_connection_lost-313"><span class="linenos">313</span></a><span class="sd">        At this time, self.connection.connection_state is already set to ConnectionState.disconnected.</span>
</span><span id="WorkerBase.on_connection_lost-314"><a href="#WorkerBase.on_connection_lost-314"><span class="linenos">314</span></a><span class="sd">        :return:</span>
</span><span id="WorkerBase.on_connection_lost-315"><a href="#WorkerBase.on_connection_lost-315"><span class="linenos">315</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="WorkerBase.on_connection_lost-316"><a href="#WorkerBase.on_connection_lost-316"><span class="linenos">316</span></a>        <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Will be called AFTER connection socket was actually closed and removed from IOMethod checking list.
At this time, self.connection.connection_state is already set to <a href="#ConnectionState.disconnected">ConnectionState.disconnected</a>.
:return:</p>
</div>


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
            <div class="pdoc-code codehilite"><pre><span></span><span id="net_io-329"><a href="#net_io-329"><span class="linenos">329</span></a><span class="nd">@contextmanager</span>
</span><span id="net_io-330"><a href="#net_io-330"><span class="linenos">330</span></a><span class="k">def</span> <span class="nf">net_io</span><span class="p">(</span><span class="n">net_io_obj</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="net_io-331"><a href="#net_io-331"><span class="linenos">331</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="net_io-332"><a href="#net_io-332"><span class="linenos">332</span></a><span class="sd">    Context manager.</span>
</span><span id="net_io-333"><a href="#net_io-333"><span class="linenos">333</span></a><span class="sd">    Usage:</span>
</span><span id="net_io-334"><a href="#net_io-334"><span class="linenos">334</span></a>
</span><span id="net_io-335"><a href="#net_io-335"><span class="linenos">335</span></a><span class="sd">    main_io = NetIOBase()</span>
</span><span id="net_io-336"><a href="#net_io-336"><span class="linenos">336</span></a><span class="sd">    with(net_io(main_io)) as io:</span>
</span><span id="net_io-337"><a href="#net_io-337"><span class="linenos">337</span></a><span class="sd">        print(&#39;Preparing connections&#39;)</span>
</span><span id="net_io-338"><a href="#net_io-338"><span class="linenos">338</span></a><span class="sd">        connection1 = io.make_connection(...)</span>
</span><span id="net_io-339"><a href="#net_io-339"><span class="linenos">339</span></a><span class="sd">        connection2 = io.make_connection(...)</span>
</span><span id="net_io-340"><a href="#net_io-340"><span class="linenos">340</span></a><span class="sd">        k = c + 12</span>
</span><span id="net_io-341"><a href="#net_io-341"><span class="linenos">341</span></a><span class="sd">        ...</span>
</span><span id="net_io-342"><a href="#net_io-342"><span class="linenos">342</span></a><span class="sd">        connectionN = io.make_connection(...)</span>
</span><span id="net_io-343"><a href="#net_io-343"><span class="linenos">343</span></a><span class="sd">        print(&#39;Starting IO loop&#39;)</span>
</span><span id="net_io-344"><a href="#net_io-344"><span class="linenos">344</span></a><span class="sd">    print(&#39;IO loop was finished properly&#39;)</span>
</span><span id="net_io-345"><a href="#net_io-345"><span class="linenos">345</span></a>
</span><span id="net_io-346"><a href="#net_io-346"><span class="linenos">346</span></a>
</span><span id="net_io-347"><a href="#net_io-347"><span class="linenos">347</span></a><span class="sd">    :param net_io_obj: constructed IO instance (object)</span>
</span><span id="net_io-348"><a href="#net_io-348"><span class="linenos">348</span></a><span class="sd">    :return:</span>
</span><span id="net_io-349"><a href="#net_io-349"><span class="linenos">349</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="net_io-350"><a href="#net_io-350"><span class="linenos">350</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="net_io-351"><a href="#net_io-351"><span class="linenos">351</span></a>        <span class="k">yield</span> <span class="n">net_io_obj</span>
</span><span id="net_io-352"><a href="#net_io-352"><span class="linenos">352</span></a>        <span class="n">net_io_obj</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="n">destroy_on_finish</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="net_io-353"><a href="#net_io-353"><span class="linenos">353</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="net_io-354"><a href="#net_io-354"><span class="linenos">354</span></a>        <span class="n">net_io_obj</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
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
                <section id="IOMethodBase">
                            <input id="IOMethodBase-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IOMethodBase</span>:

                <label class="view-source-button" for="IOMethodBase-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase-357"><a href="#IOMethodBase-357"><span class="linenos">357</span></a><span class="k">class</span> <span class="nc">IOMethodBase</span><span class="p">:</span>
</span><span id="IOMethodBase-358"><a href="#IOMethodBase-358"><span class="linenos">358</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase-359"><a href="#IOMethodBase-359"><span class="linenos">359</span></a><span class="sd">    Base class for all IOMethod implementation (select, epoll, overlapped io, kqueue, etc.)</span>
</span><span id="IOMethodBase-360"><a href="#IOMethodBase-360"><span class="linenos">360</span></a><span class="sd">    All his methods are called by the NetIOBase instance.</span>
</span><span id="IOMethodBase-361"><a href="#IOMethodBase-361"><span class="linenos">361</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="IOMethodBase-362"><a href="#IOMethodBase-362"><span class="linenos">362</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="IOMethodBase-363"><a href="#IOMethodBase-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="IOMethodBase-364"><a href="#IOMethodBase-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IOMethodBase-365"><a href="#IOMethodBase-365"><span class="linenos">365</span></a>        <span class="k">pass</span>
</span><span id="IOMethodBase-366"><a href="#IOMethodBase-366"><span class="linenos">366</span></a>
</span><span id="IOMethodBase-367"><a href="#IOMethodBase-367"><span class="linenos">367</span></a>    <span class="k">def</span> <span class="nf">loop_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IOMethodBase-368"><a href="#IOMethodBase-368"><span class="linenos">368</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase-369"><a href="#IOMethodBase-369"><span class="linenos">369</span></a><span class="sd">        Single IO loop iteration.</span>
</span><span id="IOMethodBase-370"><a href="#IOMethodBase-370"><span class="linenos">370</span></a><span class="sd">        This method holds all IOMethod logic.</span>
</span><span id="IOMethodBase-371"><a href="#IOMethodBase-371"><span class="linenos">371</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase-372"><a href="#IOMethodBase-372"><span class="linenos">372</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase-373"><a href="#IOMethodBase-373"><span class="linenos">373</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOMethodBase-374"><a href="#IOMethodBase-374"><span class="linenos">374</span></a>
</span><span id="IOMethodBase-375"><a href="#IOMethodBase-375"><span class="linenos">375</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IOMethodBase-376"><a href="#IOMethodBase-376"><span class="linenos">376</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase-377"><a href="#IOMethodBase-377"><span class="linenos">377</span></a><span class="sd">        Initiates destruction process</span>
</span><span id="IOMethodBase-378"><a href="#IOMethodBase-378"><span class="linenos">378</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase-379"><a href="#IOMethodBase-379"><span class="linenos">379</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase-380"><a href="#IOMethodBase-380"><span class="linenos">380</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOMethodBase-381"><a href="#IOMethodBase-381"><span class="linenos">381</span></a>
</span><span id="IOMethodBase-382"><a href="#IOMethodBase-382"><span class="linenos">382</span></a>    <span class="k">def</span> <span class="nf">set__can_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IOMethodBase-383"><a href="#IOMethodBase-383"><span class="linenos">383</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase-384"><a href="#IOMethodBase-384"><span class="linenos">384</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to read&quot; checks for socket</span>
</span><span id="IOMethodBase-385"><a href="#IOMethodBase-385"><span class="linenos">385</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase-386"><a href="#IOMethodBase-386"><span class="linenos">386</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="IOMethodBase-387"><a href="#IOMethodBase-387"><span class="linenos">387</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase-388"><a href="#IOMethodBase-388"><span class="linenos">388</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase-389"><a href="#IOMethodBase-389"><span class="linenos">389</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOMethodBase-390"><a href="#IOMethodBase-390"><span class="linenos">390</span></a>
</span><span id="IOMethodBase-391"><a href="#IOMethodBase-391"><span class="linenos">391</span></a>    <span class="k">def</span> <span class="nf">set__need_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IOMethodBase-392"><a href="#IOMethodBase-392"><span class="linenos">392</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase-393"><a href="#IOMethodBase-393"><span class="linenos">393</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to write&quot; checks for socket</span>
</span><span id="IOMethodBase-394"><a href="#IOMethodBase-394"><span class="linenos">394</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase-395"><a href="#IOMethodBase-395"><span class="linenos">395</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="IOMethodBase-396"><a href="#IOMethodBase-396"><span class="linenos">396</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase-397"><a href="#IOMethodBase-397"><span class="linenos">397</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase-398"><a href="#IOMethodBase-398"><span class="linenos">398</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOMethodBase-399"><a href="#IOMethodBase-399"><span class="linenos">399</span></a>
</span><span id="IOMethodBase-400"><a href="#IOMethodBase-400"><span class="linenos">400</span></a>    <span class="k">def</span> <span class="nf">set__should_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOMethodBase-401"><a href="#IOMethodBase-401"><span class="linenos">401</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase-402"><a href="#IOMethodBase-402"><span class="linenos">402</span></a><span class="sd">        Mark socket as &quot;should be closed&quot;</span>
</span><span id="IOMethodBase-403"><a href="#IOMethodBase-403"><span class="linenos">403</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase-404"><a href="#IOMethodBase-404"><span class="linenos">404</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase-405"><a href="#IOMethodBase-405"><span class="linenos">405</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase-406"><a href="#IOMethodBase-406"><span class="linenos">406</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOMethodBase-407"><a href="#IOMethodBase-407"><span class="linenos">407</span></a>
</span><span id="IOMethodBase-408"><a href="#IOMethodBase-408"><span class="linenos">408</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOMethodBase-409"><a href="#IOMethodBase-409"><span class="linenos">409</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase-410"><a href="#IOMethodBase-410"><span class="linenos">410</span></a><span class="sd">        Will add socket to the internal connections list</span>
</span><span id="IOMethodBase-411"><a href="#IOMethodBase-411"><span class="linenos">411</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase-412"><a href="#IOMethodBase-412"><span class="linenos">412</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase-413"><a href="#IOMethodBase-413"><span class="linenos">413</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase-414"><a href="#IOMethodBase-414"><span class="linenos">414</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="IOMethodBase-415"><a href="#IOMethodBase-415"><span class="linenos">415</span></a>
</span><span id="IOMethodBase-416"><a href="#IOMethodBase-416"><span class="linenos">416</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOMethodBase-417"><a href="#IOMethodBase-417"><span class="linenos">417</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase-418"><a href="#IOMethodBase-418"><span class="linenos">418</span></a><span class="sd">        Will remove socket from the internal connections list</span>
</span><span id="IOMethodBase-419"><a href="#IOMethodBase-419"><span class="linenos">419</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase-420"><a href="#IOMethodBase-420"><span class="linenos">420</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase-421"><a href="#IOMethodBase-421"><span class="linenos">421</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase-422"><a href="#IOMethodBase-422"><span class="linenos">422</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Base class for all IOMethod implementation (select, epoll, overlapped io, kqueue, etc.)
All his methods are called by the NetIOBase instance.</p>
</div>


                            <div id="IOMethodBase.__init__" class="classattr">
                                        <input id="IOMethodBase.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IOMethodBase</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">interface</span><span class="p">:</span> <span class="n"><a href="#NetIOBase">NetIOBase</a></span></span>)</span>

                <label class="view-source-button" for="IOMethodBase.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase.__init__-362"><a href="#IOMethodBase.__init__-362"><span class="linenos">362</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">NetIOBase</span><span class="p">):</span>
</span><span id="IOMethodBase.__init__-363"><a href="#IOMethodBase.__init__-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="IOMethodBase.__init__-364"><a href="#IOMethodBase.__init__-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">should_be_closed</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IOMethodBase.__init__-365"><a href="#IOMethodBase.__init__-365"><span class="linenos">365</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="IOMethodBase.interface" class="classattr">
                                <div class="attr variable">
            <span class="name">interface</span>

        
    </div>
    <a class="headerlink" href="#IOMethodBase.interface"></a>
    
    

                            </div>
                            <div id="IOMethodBase.should_be_closed" class="classattr">
                                <div class="attr variable">
            <span class="name">should_be_closed</span>

        
    </div>
    <a class="headerlink" href="#IOMethodBase.should_be_closed"></a>
    
    

                            </div>
                            <div id="IOMethodBase.loop_iteration" class="classattr">
                                        <input id="IOMethodBase.loop_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">loop_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">timeout</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOMethodBase.loop_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase.loop_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase.loop_iteration-367"><a href="#IOMethodBase.loop_iteration-367"><span class="linenos">367</span></a>    <span class="k">def</span> <span class="nf">loop_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IOMethodBase.loop_iteration-368"><a href="#IOMethodBase.loop_iteration-368"><span class="linenos">368</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase.loop_iteration-369"><a href="#IOMethodBase.loop_iteration-369"><span class="linenos">369</span></a><span class="sd">        Single IO loop iteration.</span>
</span><span id="IOMethodBase.loop_iteration-370"><a href="#IOMethodBase.loop_iteration-370"><span class="linenos">370</span></a><span class="sd">        This method holds all IOMethod logic.</span>
</span><span id="IOMethodBase.loop_iteration-371"><a href="#IOMethodBase.loop_iteration-371"><span class="linenos">371</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase.loop_iteration-372"><a href="#IOMethodBase.loop_iteration-372"><span class="linenos">372</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase.loop_iteration-373"><a href="#IOMethodBase.loop_iteration-373"><span class="linenos">373</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Single IO loop iteration.
This method holds all IOMethod logic.
:return:</p>
</div>


                            </div>
                            <div id="IOMethodBase.destroy" class="classattr">
                                        <input id="IOMethodBase.destroy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">destroy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOMethodBase.destroy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase.destroy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase.destroy-375"><a href="#IOMethodBase.destroy-375"><span class="linenos">375</span></a>    <span class="k">def</span> <span class="nf">destroy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IOMethodBase.destroy-376"><a href="#IOMethodBase.destroy-376"><span class="linenos">376</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase.destroy-377"><a href="#IOMethodBase.destroy-377"><span class="linenos">377</span></a><span class="sd">        Initiates destruction process</span>
</span><span id="IOMethodBase.destroy-378"><a href="#IOMethodBase.destroy-378"><span class="linenos">378</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase.destroy-379"><a href="#IOMethodBase.destroy-379"><span class="linenos">379</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase.destroy-380"><a href="#IOMethodBase.destroy-380"><span class="linenos">380</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Initiates destruction process
:return:</p>
</div>


                            </div>
                            <div id="IOMethodBase.set__can_read" class="classattr">
                                        <input id="IOMethodBase.set__can_read-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set__can_read</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span>, </span><span class="param"><span class="n">state</span><span class="o">=</span><span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOMethodBase.set__can_read-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase.set__can_read"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase.set__can_read-382"><a href="#IOMethodBase.set__can_read-382"><span class="linenos">382</span></a>    <span class="k">def</span> <span class="nf">set__can_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IOMethodBase.set__can_read-383"><a href="#IOMethodBase.set__can_read-383"><span class="linenos">383</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase.set__can_read-384"><a href="#IOMethodBase.set__can_read-384"><span class="linenos">384</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to read&quot; checks for socket</span>
</span><span id="IOMethodBase.set__can_read-385"><a href="#IOMethodBase.set__can_read-385"><span class="linenos">385</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase.set__can_read-386"><a href="#IOMethodBase.set__can_read-386"><span class="linenos">386</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="IOMethodBase.set__can_read-387"><a href="#IOMethodBase.set__can_read-387"><span class="linenos">387</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase.set__can_read-388"><a href="#IOMethodBase.set__can_read-388"><span class="linenos">388</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase.set__can_read-389"><a href="#IOMethodBase.set__can_read-389"><span class="linenos">389</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will allow (True) or disallow (False) "socket available to read" checks for socket
:param conn: target socket
:param state: True - allow; False - disallow
:return:</p>
</div>


                            </div>
                            <div id="IOMethodBase.set__need_write" class="classattr">
                                        <input id="IOMethodBase.set__need_write-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set__need_write</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span>, </span><span class="param"><span class="n">state</span><span class="o">=</span><span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOMethodBase.set__need_write-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase.set__need_write"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase.set__need_write-391"><a href="#IOMethodBase.set__need_write-391"><span class="linenos">391</span></a>    <span class="k">def</span> <span class="nf">set__need_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IOMethodBase.set__need_write-392"><a href="#IOMethodBase.set__need_write-392"><span class="linenos">392</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase.set__need_write-393"><a href="#IOMethodBase.set__need_write-393"><span class="linenos">393</span></a><span class="sd">        Will allow (True) or disallow (False) &quot;socket available to write&quot; checks for socket</span>
</span><span id="IOMethodBase.set__need_write-394"><a href="#IOMethodBase.set__need_write-394"><span class="linenos">394</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase.set__need_write-395"><a href="#IOMethodBase.set__need_write-395"><span class="linenos">395</span></a><span class="sd">        :param state: True - allow; False - disallow</span>
</span><span id="IOMethodBase.set__need_write-396"><a href="#IOMethodBase.set__need_write-396"><span class="linenos">396</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase.set__need_write-397"><a href="#IOMethodBase.set__need_write-397"><span class="linenos">397</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase.set__need_write-398"><a href="#IOMethodBase.set__need_write-398"><span class="linenos">398</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will allow (True) or disallow (False) "socket available to write" checks for socket
:param conn: target socket
:param state: True - allow; False - disallow
:return:</p>
</div>


                            </div>
                            <div id="IOMethodBase.set__should_be_closed" class="classattr">
                                        <input id="IOMethodBase.set__should_be_closed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set__should_be_closed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOMethodBase.set__should_be_closed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase.set__should_be_closed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase.set__should_be_closed-400"><a href="#IOMethodBase.set__should_be_closed-400"><span class="linenos">400</span></a>    <span class="k">def</span> <span class="nf">set__should_be_closed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOMethodBase.set__should_be_closed-401"><a href="#IOMethodBase.set__should_be_closed-401"><span class="linenos">401</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase.set__should_be_closed-402"><a href="#IOMethodBase.set__should_be_closed-402"><span class="linenos">402</span></a><span class="sd">        Mark socket as &quot;should be closed&quot;</span>
</span><span id="IOMethodBase.set__should_be_closed-403"><a href="#IOMethodBase.set__should_be_closed-403"><span class="linenos">403</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase.set__should_be_closed-404"><a href="#IOMethodBase.set__should_be_closed-404"><span class="linenos">404</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase.set__should_be_closed-405"><a href="#IOMethodBase.set__should_be_closed-405"><span class="linenos">405</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase.set__should_be_closed-406"><a href="#IOMethodBase.set__should_be_closed-406"><span class="linenos">406</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Mark socket as "should be closed"
:param conn: target socket
:return:</p>
</div>


                            </div>
                            <div id="IOMethodBase.add_connection" class="classattr">
                                        <input id="IOMethodBase.add_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_connection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOMethodBase.add_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase.add_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase.add_connection-408"><a href="#IOMethodBase.add_connection-408"><span class="linenos">408</span></a>    <span class="k">def</span> <span class="nf">add_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOMethodBase.add_connection-409"><a href="#IOMethodBase.add_connection-409"><span class="linenos">409</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase.add_connection-410"><a href="#IOMethodBase.add_connection-410"><span class="linenos">410</span></a><span class="sd">        Will add socket to the internal connections list</span>
</span><span id="IOMethodBase.add_connection-411"><a href="#IOMethodBase.add_connection-411"><span class="linenos">411</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase.add_connection-412"><a href="#IOMethodBase.add_connection-412"><span class="linenos">412</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase.add_connection-413"><a href="#IOMethodBase.add_connection-413"><span class="linenos">413</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase.add_connection-414"><a href="#IOMethodBase.add_connection-414"><span class="linenos">414</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will add socket to the internal connections list
:param conn: target socket
:return:</p>
</div>


                            </div>
                            <div id="IOMethodBase.remove_connection" class="classattr">
                                        <input id="IOMethodBase.remove_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_connection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IOMethodBase.remove_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IOMethodBase.remove_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IOMethodBase.remove_connection-416"><a href="#IOMethodBase.remove_connection-416"><span class="linenos">416</span></a>    <span class="k">def</span> <span class="nf">remove_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">conn</span><span class="p">:</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">):</span>
</span><span id="IOMethodBase.remove_connection-417"><a href="#IOMethodBase.remove_connection-417"><span class="linenos">417</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IOMethodBase.remove_connection-418"><a href="#IOMethodBase.remove_connection-418"><span class="linenos">418</span></a><span class="sd">        Will remove socket from the internal connections list</span>
</span><span id="IOMethodBase.remove_connection-419"><a href="#IOMethodBase.remove_connection-419"><span class="linenos">419</span></a><span class="sd">        :param conn: target socket</span>
</span><span id="IOMethodBase.remove_connection-420"><a href="#IOMethodBase.remove_connection-420"><span class="linenos">420</span></a><span class="sd">        :return:</span>
</span><span id="IOMethodBase.remove_connection-421"><a href="#IOMethodBase.remove_connection-421"><span class="linenos">421</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IOMethodBase.remove_connection-422"><a href="#IOMethodBase.remove_connection-422"><span class="linenos">422</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
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