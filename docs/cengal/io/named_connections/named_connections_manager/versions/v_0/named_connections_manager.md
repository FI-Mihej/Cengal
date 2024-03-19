---
title: named_connections_manager
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.io<wbr>.named_connections<wbr>.named_connections_manager<wbr>.versions<wbr>.v_0<wbr>.named_connections_manager    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-named_connections_manager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-named_connections_manager-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="sd">Module Docstring</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.1.1&quot;</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="kn">from</span> <span class="nn">cengal.data_generation.id_generator</span> <span class="kn">import</span> <span class="n">IDGenerator</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="kn">from</span> <span class="nn">cengal.data_containers.fast_fifo</span> <span class="kn">import</span> <span class="n">FIFODequeWithLengthControl</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values</span> <span class="kn">import</span> <span class="n">ValueCache</span><span class="p">,</span> <span class="n">ValueExistence</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">weakref</span> <span class="kn">import</span> <span class="n">ref</span><span class="p">,</span> <span class="n">ReferenceType</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">Type</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="c1"># class NamedConnectionsTransport:</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="c1">#     def disconnect(self):</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="c1">#         raise NotImplementedError</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="c1">#     def disconnected(self):</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="c1">#         ...</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="c1">#     def eof(self) -&gt; bool:</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="c1">#         ...</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="k">class</span> <span class="nc">NamedConnectionsClient</span><span class="p">:</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReferenceType</span><span class="p">[</span><span class="s1">&#39;NamedConnectionsServer&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span><span class="p">:</span> <span class="n">FIFODequeWithLengthControl</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span><span class="p">:</span> <span class="n">FIFODequeWithLengthControl</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="k">def</span> <span class="nf">callback__bind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="s1">&#39;NamedConnectionsServer&#39;</span><span class="p">):</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="sd">        Args:</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="sd">            server (NamedConnectionsServer): _description_</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span> <span class="o">=</span> <span class="n">ref</span><span class="p">(</span><span class="n">server</span><span class="p">)</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>    
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>    <span class="k">def</span> <span class="nf">callback__unbind</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="k">def</span> <span class="nf">callback__data_to_client_added</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="sd">        Raises:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="k">def</span> <span class="nf">callback__server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="sd">        Raises:</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="k">def</span> <span class="nf">callback__is_client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a><span class="sd">        Raises:</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="sd">        Returns:</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="sd">            bool: _description_</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">callback__stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback. No additional data from the server will be provided. No read from the server side will be made.</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a><span class="sd">        Raises:</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="nf">data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="nf">is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="sd">        Returns:</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a><span class="sd">            bool: _description_</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>            <span class="k">return</span> <span class="n">server</span><span class="o">.</span><span class="n">callback__is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    <span class="k">def</span> <span class="nf">client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>    
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method. Server should not call it. Server should call NamedConnectionsClient.callback__stop() when wants to close connection</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__client_stopped</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a><span class="k">class</span> <span class="nc">NamedConnectionsServer</span><span class="p">:</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="c1"># def __init__(self, server_id: bytes, named_connections_manager: Optional[&#39;NamedConnectionsManager&#39;] = None) -&gt; None:</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    <span class="c1">#     self.id: bytes = server_id</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="c1">#     if named_connections_manager:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="c1">#         self.named_connections_manager: ReferenceType[&#39;NamedConnectionsManager&#39;] = ref(named_connections_manager)</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>    <span class="c1">#     else:</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="c1">#         self.named_connections_manager = None</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    <span class="c1">#     self.bind_clients: Dict[int, NamedConnectionsClient] = dict()</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">named_connections_manager</span><span class="p">:</span> <span class="s1">&#39;NamedConnectionsManager&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">named_connections_manager</span><span class="p">:</span> <span class="n">ReferenceType</span><span class="p">[</span><span class="s1">&#39;NamedConnectionsManager&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref</span><span class="p">(</span><span class="n">named_connections_manager</span><span class="p">)</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    <span class="k">def</span> <span class="nf">bind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">callback__bind</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">unbind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>            <span class="k">pass</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>            <span class="n">client</span><span class="o">.</span><span class="n">callback__unbind</span><span class="p">()</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>    
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    <span class="k">def</span> <span class="nf">callback__data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>    
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>    <span class="k">def</span> <span class="nf">callback__is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>    <span class="k">def</span> <span class="nf">callback__client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>    
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>    <span class="k">def</span> <span class="nf">callback__client_stopped</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can emit this callback. No additional data from the client will be provided. No read from the client side will be made.</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a><span class="sd">        Raises:</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="k">class</span> <span class="nc">NamedConnectionsManager</span><span class="p">:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">:</span> <span class="n">IDGenerator</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">NamedConnectionsClient</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="n">NamedConnectionsServer</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>    
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>    <span class="k">def</span> <span class="nf">create_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">NamedConnectionsClient</span><span class="p">],</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NamedConnectionsClient</span><span class="p">:</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span> <span class="o">=</span> <span class="n">client_type</span><span class="p">(</span><span class="n">server_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">()</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_unbind_client_impl</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="k">return</span> <span class="n">client_id</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>    
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>    <span class="k">def</span> <span class="nf">register_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_id</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">()</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>            <span class="k">if</span> <span class="n">server_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="k">return</span> <span class="n">client_id</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    <span class="k">def</span> <span class="nf">register_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="n">NamedConnectionsServer</span><span class="p">):</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>        <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server</span><span class="o">.</span><span class="n">id</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;NamedConnectionsServer already registered&#39;</span><span class="p">)</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>        
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">server</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="n">unbind_clients</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>            <span class="k">for</span> <span class="n">client</span> <span class="ow">in</span> <span class="n">unbind_clients</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                <span class="n">server</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>    <span class="k">def</span> <span class="nf">unregister_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="n">NamedConnectionsServer</span><span class="p">):</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>        <span class="n">server_clients</span> <span class="o">=</span> <span class="n">server</span><span class="o">.</span><span class="n">bind_clients</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        <span class="k">for</span> <span class="n">client_id</span><span class="p">,</span> <span class="n">client</span> <span class="ow">in</span> <span class="n">server_clients</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_client</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>        
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            <span class="k">pass</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">unregister_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">id</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>            <span class="k">pass</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>    <span class="k">def</span> <span class="nf">unbind_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_unbind_client_impl</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>    <span class="k">def</span> <span class="nf">_unbind_client_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">id</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="n">server_id</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_id</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">rebind_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Force rebind client to another server</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">server_id</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>    
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>    <span class="c1"># def put_client_message_to_server_queue(self, message):</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>    <span class="c1">#     ...</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>    
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>    <span class="c1"># def put_server_message_to_client_queue(self, message):</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>    <span class="c1">#     ...</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>    
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>    <span class="c1"># def client_to_server_queue_len(self):</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>    <span class="c1">#     ...</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>    
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>    <span class="c1"># def server_to_client_queue_len(self):</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>    <span class="c1">#     ...</span>
</span></pre></div>


            </section>
                <section id="NamedConnectionsClient">
                            <input id="NamedConnectionsClient-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">NamedConnectionsClient</span>:

                <label class="view-source-button" for="NamedConnectionsClient-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient-54"><a href="#NamedConnectionsClient-54"><span class="linenos"> 54</span></a><span class="k">class</span> <span class="nc">NamedConnectionsClient</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-55"><a href="#NamedConnectionsClient-55"><span class="linenos"> 55</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-56"><a href="#NamedConnectionsClient-56"><span class="linenos"> 56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="NamedConnectionsClient-57"><a href="#NamedConnectionsClient-57"><span class="linenos"> 57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="NamedConnectionsClient-58"><a href="#NamedConnectionsClient-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReferenceType</span><span class="p">[</span><span class="s1">&#39;NamedConnectionsServer&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="NamedConnectionsClient-59"><a href="#NamedConnectionsClient-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span><span class="p">:</span> <span class="n">FIFODequeWithLengthControl</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span><span id="NamedConnectionsClient-60"><a href="#NamedConnectionsClient-60"><span class="linenos"> 60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span><span class="p">:</span> <span class="n">FIFODequeWithLengthControl</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span><span id="NamedConnectionsClient-61"><a href="#NamedConnectionsClient-61"><span class="linenos"> 61</span></a>    
</span><span id="NamedConnectionsClient-62"><a href="#NamedConnectionsClient-62"><span class="linenos"> 62</span></a>    <span class="k">def</span> <span class="nf">callback__bind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="s1">&#39;NamedConnectionsServer&#39;</span><span class="p">):</span>
</span><span id="NamedConnectionsClient-63"><a href="#NamedConnectionsClient-63"><span class="linenos"> 63</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient-64"><a href="#NamedConnectionsClient-64"><span class="linenos"> 64</span></a>
</span><span id="NamedConnectionsClient-65"><a href="#NamedConnectionsClient-65"><span class="linenos"> 65</span></a><span class="sd">        Args:</span>
</span><span id="NamedConnectionsClient-66"><a href="#NamedConnectionsClient-66"><span class="linenos"> 66</span></a><span class="sd">            server (NamedConnectionsServer): _description_</span>
</span><span id="NamedConnectionsClient-67"><a href="#NamedConnectionsClient-67"><span class="linenos"> 67</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-68"><a href="#NamedConnectionsClient-68"><span class="linenos"> 68</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span> <span class="o">=</span> <span class="n">ref</span><span class="p">(</span><span class="n">server</span><span class="p">)</span>
</span><span id="NamedConnectionsClient-69"><a href="#NamedConnectionsClient-69"><span class="linenos"> 69</span></a>    
</span><span id="NamedConnectionsClient-70"><a href="#NamedConnectionsClient-70"><span class="linenos"> 70</span></a>    <span class="k">def</span> <span class="nf">callback__unbind</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient-71"><a href="#NamedConnectionsClient-71"><span class="linenos"> 71</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient-72"><a href="#NamedConnectionsClient-72"><span class="linenos"> 72</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-73"><a href="#NamedConnectionsClient-73"><span class="linenos"> 73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="NamedConnectionsClient-74"><a href="#NamedConnectionsClient-74"><span class="linenos"> 74</span></a>
</span><span id="NamedConnectionsClient-75"><a href="#NamedConnectionsClient-75"><span class="linenos"> 75</span></a>    <span class="k">def</span> <span class="nf">callback__data_to_client_added</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient-76"><a href="#NamedConnectionsClient-76"><span class="linenos"> 76</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient-77"><a href="#NamedConnectionsClient-77"><span class="linenos"> 77</span></a>
</span><span id="NamedConnectionsClient-78"><a href="#NamedConnectionsClient-78"><span class="linenos"> 78</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsClient-79"><a href="#NamedConnectionsClient-79"><span class="linenos"> 79</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsClient-80"><a href="#NamedConnectionsClient-80"><span class="linenos"> 80</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-81"><a href="#NamedConnectionsClient-81"><span class="linenos"> 81</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="NamedConnectionsClient-82"><a href="#NamedConnectionsClient-82"><span class="linenos"> 82</span></a>    
</span><span id="NamedConnectionsClient-83"><a href="#NamedConnectionsClient-83"><span class="linenos"> 83</span></a>    <span class="k">def</span> <span class="nf">callback__server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient-84"><a href="#NamedConnectionsClient-84"><span class="linenos"> 84</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient-85"><a href="#NamedConnectionsClient-85"><span class="linenos"> 85</span></a>
</span><span id="NamedConnectionsClient-86"><a href="#NamedConnectionsClient-86"><span class="linenos"> 86</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsClient-87"><a href="#NamedConnectionsClient-87"><span class="linenos"> 87</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsClient-88"><a href="#NamedConnectionsClient-88"><span class="linenos"> 88</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-89"><a href="#NamedConnectionsClient-89"><span class="linenos"> 89</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="NamedConnectionsClient-90"><a href="#NamedConnectionsClient-90"><span class="linenos"> 90</span></a>
</span><span id="NamedConnectionsClient-91"><a href="#NamedConnectionsClient-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="nf">callback__is_client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-92"><a href="#NamedConnectionsClient-92"><span class="linenos"> 92</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient-93"><a href="#NamedConnectionsClient-93"><span class="linenos"> 93</span></a>
</span><span id="NamedConnectionsClient-94"><a href="#NamedConnectionsClient-94"><span class="linenos"> 94</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsClient-95"><a href="#NamedConnectionsClient-95"><span class="linenos"> 95</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsClient-96"><a href="#NamedConnectionsClient-96"><span class="linenos"> 96</span></a>
</span><span id="NamedConnectionsClient-97"><a href="#NamedConnectionsClient-97"><span class="linenos"> 97</span></a><span class="sd">        Returns:</span>
</span><span id="NamedConnectionsClient-98"><a href="#NamedConnectionsClient-98"><span class="linenos"> 98</span></a><span class="sd">            bool: _description_</span>
</span><span id="NamedConnectionsClient-99"><a href="#NamedConnectionsClient-99"><span class="linenos"> 99</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-100"><a href="#NamedConnectionsClient-100"><span class="linenos">100</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="NamedConnectionsClient-101"><a href="#NamedConnectionsClient-101"><span class="linenos">101</span></a>    
</span><span id="NamedConnectionsClient-102"><a href="#NamedConnectionsClient-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">callback__stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient-103"><a href="#NamedConnectionsClient-103"><span class="linenos">103</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback. No additional data from the server will be provided. No read from the server side will be made.</span>
</span><span id="NamedConnectionsClient-104"><a href="#NamedConnectionsClient-104"><span class="linenos">104</span></a>
</span><span id="NamedConnectionsClient-105"><a href="#NamedConnectionsClient-105"><span class="linenos">105</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsClient-106"><a href="#NamedConnectionsClient-106"><span class="linenos">106</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsClient-107"><a href="#NamedConnectionsClient-107"><span class="linenos">107</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-108"><a href="#NamedConnectionsClient-108"><span class="linenos">108</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="NamedConnectionsClient-109"><a href="#NamedConnectionsClient-109"><span class="linenos">109</span></a>    
</span><span id="NamedConnectionsClient-110"><a href="#NamedConnectionsClient-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient-111"><a href="#NamedConnectionsClient-111"><span class="linenos">111</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="NamedConnectionsClient-112"><a href="#NamedConnectionsClient-112"><span class="linenos">112</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-113"><a href="#NamedConnectionsClient-113"><span class="linenos">113</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsClient-114"><a href="#NamedConnectionsClient-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-115"><a href="#NamedConnectionsClient-115"><span class="linenos">115</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="NamedConnectionsClient-116"><a href="#NamedConnectionsClient-116"><span class="linenos">116</span></a>    
</span><span id="NamedConnectionsClient-117"><a href="#NamedConnectionsClient-117"><span class="linenos">117</span></a>    <span class="k">def</span> <span class="nf">is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-118"><a href="#NamedConnectionsClient-118"><span class="linenos">118</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="NamedConnectionsClient-119"><a href="#NamedConnectionsClient-119"><span class="linenos">119</span></a>
</span><span id="NamedConnectionsClient-120"><a href="#NamedConnectionsClient-120"><span class="linenos">120</span></a><span class="sd">        Returns:</span>
</span><span id="NamedConnectionsClient-121"><a href="#NamedConnectionsClient-121"><span class="linenos">121</span></a><span class="sd">            bool: _description_</span>
</span><span id="NamedConnectionsClient-122"><a href="#NamedConnectionsClient-122"><span class="linenos">122</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-123"><a href="#NamedConnectionsClient-123"><span class="linenos">123</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsClient-124"><a href="#NamedConnectionsClient-124"><span class="linenos">124</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-125"><a href="#NamedConnectionsClient-125"><span class="linenos">125</span></a>            <span class="k">return</span> <span class="n">server</span><span class="o">.</span><span class="n">callback__is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="NamedConnectionsClient-126"><a href="#NamedConnectionsClient-126"><span class="linenos">126</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-127"><a href="#NamedConnectionsClient-127"><span class="linenos">127</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="NamedConnectionsClient-128"><a href="#NamedConnectionsClient-128"><span class="linenos">128</span></a>
</span><span id="NamedConnectionsClient-129"><a href="#NamedConnectionsClient-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient-130"><a href="#NamedConnectionsClient-130"><span class="linenos">130</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="NamedConnectionsClient-131"><a href="#NamedConnectionsClient-131"><span class="linenos">131</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-132"><a href="#NamedConnectionsClient-132"><span class="linenos">132</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsClient-133"><a href="#NamedConnectionsClient-133"><span class="linenos">133</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-134"><a href="#NamedConnectionsClient-134"><span class="linenos">134</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="NamedConnectionsClient-135"><a href="#NamedConnectionsClient-135"><span class="linenos">135</span></a>    
</span><span id="NamedConnectionsClient-136"><a href="#NamedConnectionsClient-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient-137"><a href="#NamedConnectionsClient-137"><span class="linenos">137</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method. Server should not call it. Server should call NamedConnectionsClient.callback__stop() when wants to close connection</span>
</span><span id="NamedConnectionsClient-138"><a href="#NamedConnectionsClient-138"><span class="linenos">138</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient-139"><a href="#NamedConnectionsClient-139"><span class="linenos">139</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsClient-140"><a href="#NamedConnectionsClient-140"><span class="linenos">140</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsClient-141"><a href="#NamedConnectionsClient-141"><span class="linenos">141</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__client_stopped</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="NamedConnectionsClient.__init__" class="classattr">
                                        <input id="NamedConnectionsClient.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">NamedConnectionsClient</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span>,</span><span class="param">	<span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span></span>)</span>

                <label class="view-source-button" for="NamedConnectionsClient.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.__init__-55"><a href="#NamedConnectionsClient.__init__-55"><span class="linenos">55</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="NamedConnectionsClient.__init__-56"><a href="#NamedConnectionsClient.__init__-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="NamedConnectionsClient.__init__-57"><a href="#NamedConnectionsClient.__init__-57"><span class="linenos">57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="NamedConnectionsClient.__init__-58"><a href="#NamedConnectionsClient.__init__-58"><span class="linenos">58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ReferenceType</span><span class="p">[</span><span class="s1">&#39;NamedConnectionsServer&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="NamedConnectionsClient.__init__-59"><a href="#NamedConnectionsClient.__init__-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client</span><span class="p">:</span> <span class="n">FIFODequeWithLengthControl</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span><span id="NamedConnectionsClient.__init__-60"><a href="#NamedConnectionsClient.__init__-60"><span class="linenos">60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client</span><span class="p">:</span> <span class="n">FIFODequeWithLengthControl</span> <span class="o">=</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsClient.id" class="classattr">
                                <div class="attr variable">
            <span class="name">id</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsClient.id"></a>
    
    

                            </div>
                            <div id="NamedConnectionsClient.server_id" class="classattr">
                                <div class="attr variable">
            <span class="name">server_id</span><span class="annotation">: bytes</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsClient.server_id"></a>
    
    

                            </div>
                            <div id="NamedConnectionsClient.server_ref" class="classattr">
                                <div class="attr variable">
            <span class="name">server_ref</span><span class="annotation">: &#34;Optional[ReferenceType[&#39;NamedConnectionsServer&#39;]]&#34;</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsClient.server_ref"></a>
    
    

                            </div>
                            <div id="NamedConnectionsClient.input_from_client" class="classattr">
                                <div class="attr variable">
            <span class="name">input_from_client</span><span class="annotation">: cengal.data_containers.fast_fifo.versions.v_1.fast_fifo.FIFODequeWithLengthControl</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsClient.input_from_client"></a>
    
    

                            </div>
                            <div id="NamedConnectionsClient.output_to_client" class="classattr">
                                <div class="attr variable">
            <span class="name">output_to_client</span><span class="annotation">: cengal.data_containers.fast_fifo.versions.v_1.fast_fifo.FIFODequeWithLengthControl</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsClient.output_to_client"></a>
    
    

                            </div>
                            <div id="NamedConnectionsClient.callback__bind" class="classattr">
                                        <input id="NamedConnectionsClient.callback__bind-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__bind</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">server</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsServer">NamedConnectionsServer</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.callback__bind-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.callback__bind"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.callback__bind-62"><a href="#NamedConnectionsClient.callback__bind-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="nf">callback__bind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="s1">&#39;NamedConnectionsServer&#39;</span><span class="p">):</span>
</span><span id="NamedConnectionsClient.callback__bind-63"><a href="#NamedConnectionsClient.callback__bind-63"><span class="linenos">63</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient.callback__bind-64"><a href="#NamedConnectionsClient.callback__bind-64"><span class="linenos">64</span></a>
</span><span id="NamedConnectionsClient.callback__bind-65"><a href="#NamedConnectionsClient.callback__bind-65"><span class="linenos">65</span></a><span class="sd">        Args:</span>
</span><span id="NamedConnectionsClient.callback__bind-66"><a href="#NamedConnectionsClient.callback__bind-66"><span class="linenos">66</span></a><span class="sd">            server (NamedConnectionsServer): _description_</span>
</span><span id="NamedConnectionsClient.callback__bind-67"><a href="#NamedConnectionsClient.callback__bind-67"><span class="linenos">67</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.callback__bind-68"><a href="#NamedConnectionsClient.callback__bind-68"><span class="linenos">68</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span> <span class="o">=</span> <span class="n">ref</span><span class="p">(</span><span class="n">server</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Server can emit this callback</p>

<p>Args:
    server (NamedConnectionsServer): _description_</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.callback__unbind" class="classattr">
                                        <input id="NamedConnectionsClient.callback__unbind-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__unbind</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.callback__unbind-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.callback__unbind"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.callback__unbind-70"><a href="#NamedConnectionsClient.callback__unbind-70"><span class="linenos">70</span></a>    <span class="k">def</span> <span class="nf">callback__unbind</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient.callback__unbind-71"><a href="#NamedConnectionsClient.callback__unbind-71"><span class="linenos">71</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient.callback__unbind-72"><a href="#NamedConnectionsClient.callback__unbind-72"><span class="linenos">72</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.callback__unbind-73"><a href="#NamedConnectionsClient.callback__unbind-73"><span class="linenos">73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


            <div class="docstring"><p>Server can emit this callback</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.callback__data_to_client_added" class="classattr">
                                        <input id="NamedConnectionsClient.callback__data_to_client_added-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__data_to_client_added</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.callback__data_to_client_added-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.callback__data_to_client_added"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.callback__data_to_client_added-75"><a href="#NamedConnectionsClient.callback__data_to_client_added-75"><span class="linenos">75</span></a>    <span class="k">def</span> <span class="nf">callback__data_to_client_added</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient.callback__data_to_client_added-76"><a href="#NamedConnectionsClient.callback__data_to_client_added-76"><span class="linenos">76</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient.callback__data_to_client_added-77"><a href="#NamedConnectionsClient.callback__data_to_client_added-77"><span class="linenos">77</span></a>
</span><span id="NamedConnectionsClient.callback__data_to_client_added-78"><a href="#NamedConnectionsClient.callback__data_to_client_added-78"><span class="linenos">78</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsClient.callback__data_to_client_added-79"><a href="#NamedConnectionsClient.callback__data_to_client_added-79"><span class="linenos">79</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsClient.callback__data_to_client_added-80"><a href="#NamedConnectionsClient.callback__data_to_client_added-80"><span class="linenos">80</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.callback__data_to_client_added-81"><a href="#NamedConnectionsClient.callback__data_to_client_added-81"><span class="linenos">81</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Server can emit this callback</p>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.callback__server_ready_for_data" class="classattr">
                                        <input id="NamedConnectionsClient.callback__server_ready_for_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__server_ready_for_data</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.callback__server_ready_for_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.callback__server_ready_for_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.callback__server_ready_for_data-83"><a href="#NamedConnectionsClient.callback__server_ready_for_data-83"><span class="linenos">83</span></a>    <span class="k">def</span> <span class="nf">callback__server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient.callback__server_ready_for_data-84"><a href="#NamedConnectionsClient.callback__server_ready_for_data-84"><span class="linenos">84</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient.callback__server_ready_for_data-85"><a href="#NamedConnectionsClient.callback__server_ready_for_data-85"><span class="linenos">85</span></a>
</span><span id="NamedConnectionsClient.callback__server_ready_for_data-86"><a href="#NamedConnectionsClient.callback__server_ready_for_data-86"><span class="linenos">86</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsClient.callback__server_ready_for_data-87"><a href="#NamedConnectionsClient.callback__server_ready_for_data-87"><span class="linenos">87</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsClient.callback__server_ready_for_data-88"><a href="#NamedConnectionsClient.callback__server_ready_for_data-88"><span class="linenos">88</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.callback__server_ready_for_data-89"><a href="#NamedConnectionsClient.callback__server_ready_for_data-89"><span class="linenos">89</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Server can emit this callback</p>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.callback__is_client_ready_for_data" class="classattr">
                                        <input id="NamedConnectionsClient.callback__is_client_ready_for_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__is_client_ready_for_data</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.callback__is_client_ready_for_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.callback__is_client_ready_for_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-91"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="nf">callback__is_client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-92"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-92"><span class="linenos"> 92</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback</span>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-93"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-93"><span class="linenos"> 93</span></a>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-94"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-94"><span class="linenos"> 94</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-95"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-95"><span class="linenos"> 95</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-96"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-96"><span class="linenos"> 96</span></a>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-97"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-97"><span class="linenos"> 97</span></a><span class="sd">        Returns:</span>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-98"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-98"><span class="linenos"> 98</span></a><span class="sd">            bool: _description_</span>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-99"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-99"><span class="linenos"> 99</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.callback__is_client_ready_for_data-100"><a href="#NamedConnectionsClient.callback__is_client_ready_for_data-100"><span class="linenos">100</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Server can emit this callback</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.callback__stop" class="classattr">
                                        <input id="NamedConnectionsClient.callback__stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.callback__stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.callback__stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.callback__stop-102"><a href="#NamedConnectionsClient.callback__stop-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">callback__stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient.callback__stop-103"><a href="#NamedConnectionsClient.callback__stop-103"><span class="linenos">103</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Server can emit this callback. No additional data from the server will be provided. No read from the server side will be made.</span>
</span><span id="NamedConnectionsClient.callback__stop-104"><a href="#NamedConnectionsClient.callback__stop-104"><span class="linenos">104</span></a>
</span><span id="NamedConnectionsClient.callback__stop-105"><a href="#NamedConnectionsClient.callback__stop-105"><span class="linenos">105</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsClient.callback__stop-106"><a href="#NamedConnectionsClient.callback__stop-106"><span class="linenos">106</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsClient.callback__stop-107"><a href="#NamedConnectionsClient.callback__stop-107"><span class="linenos">107</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.callback__stop-108"><a href="#NamedConnectionsClient.callback__stop-108"><span class="linenos">108</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Server can emit this callback. No additional data from the server will be provided. No read from the server side will be made.</p>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.data_to_server_added" class="classattr">
                                        <input id="NamedConnectionsClient.data_to_server_added-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">data_to_server_added</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.data_to_server_added-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.data_to_server_added"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.data_to_server_added-110"><a href="#NamedConnectionsClient.data_to_server_added-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient.data_to_server_added-111"><a href="#NamedConnectionsClient.data_to_server_added-111"><span class="linenos">111</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="NamedConnectionsClient.data_to_server_added-112"><a href="#NamedConnectionsClient.data_to_server_added-112"><span class="linenos">112</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.data_to_server_added-113"><a href="#NamedConnectionsClient.data_to_server_added-113"><span class="linenos">113</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsClient.data_to_server_added-114"><a href="#NamedConnectionsClient.data_to_server_added-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsClient.data_to_server_added-115"><a href="#NamedConnectionsClient.data_to_server_added-115"><span class="linenos">115</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Client can call this method</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.is_server_ready_for_data" class="classattr">
                                        <input id="NamedConnectionsClient.is_server_ready_for_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_server_ready_for_data</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.is_server_ready_for_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.is_server_ready_for_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.is_server_ready_for_data-117"><a href="#NamedConnectionsClient.is_server_ready_for_data-117"><span class="linenos">117</span></a>    <span class="k">def</span> <span class="nf">is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-118"><a href="#NamedConnectionsClient.is_server_ready_for_data-118"><span class="linenos">118</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-119"><a href="#NamedConnectionsClient.is_server_ready_for_data-119"><span class="linenos">119</span></a>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-120"><a href="#NamedConnectionsClient.is_server_ready_for_data-120"><span class="linenos">120</span></a><span class="sd">        Returns:</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-121"><a href="#NamedConnectionsClient.is_server_ready_for_data-121"><span class="linenos">121</span></a><span class="sd">            bool: _description_</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-122"><a href="#NamedConnectionsClient.is_server_ready_for_data-122"><span class="linenos">122</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-123"><a href="#NamedConnectionsClient.is_server_ready_for_data-123"><span class="linenos">123</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-124"><a href="#NamedConnectionsClient.is_server_ready_for_data-124"><span class="linenos">124</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-125"><a href="#NamedConnectionsClient.is_server_ready_for_data-125"><span class="linenos">125</span></a>            <span class="k">return</span> <span class="n">server</span><span class="o">.</span><span class="n">callback__is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-126"><a href="#NamedConnectionsClient.is_server_ready_for_data-126"><span class="linenos">126</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="NamedConnectionsClient.is_server_ready_for_data-127"><a href="#NamedConnectionsClient.is_server_ready_for_data-127"><span class="linenos">127</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


            <div class="docstring"><p>Client can call this method</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.client_ready_for_data" class="classattr">
                                        <input id="NamedConnectionsClient.client_ready_for_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">client_ready_for_data</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.client_ready_for_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.client_ready_for_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.client_ready_for_data-129"><a href="#NamedConnectionsClient.client_ready_for_data-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient.client_ready_for_data-130"><a href="#NamedConnectionsClient.client_ready_for_data-130"><span class="linenos">130</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method</span>
</span><span id="NamedConnectionsClient.client_ready_for_data-131"><a href="#NamedConnectionsClient.client_ready_for_data-131"><span class="linenos">131</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.client_ready_for_data-132"><a href="#NamedConnectionsClient.client_ready_for_data-132"><span class="linenos">132</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsClient.client_ready_for_data-133"><a href="#NamedConnectionsClient.client_ready_for_data-133"><span class="linenos">133</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsClient.client_ready_for_data-134"><a href="#NamedConnectionsClient.client_ready_for_data-134"><span class="linenos">134</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Client can call this method</p>
</div>


                            </div>
                            <div id="NamedConnectionsClient.stop" class="classattr">
                                        <input id="NamedConnectionsClient.stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsClient.stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsClient.stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsClient.stop-136"><a href="#NamedConnectionsClient.stop-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="NamedConnectionsClient.stop-137"><a href="#NamedConnectionsClient.stop-137"><span class="linenos">137</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can call this method. Server should not call it. Server should call NamedConnectionsClient.callback__stop() when wants to close connection</span>
</span><span id="NamedConnectionsClient.stop-138"><a href="#NamedConnectionsClient.stop-138"><span class="linenos">138</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsClient.stop-139"><a href="#NamedConnectionsClient.stop-139"><span class="linenos">139</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsClient.stop-140"><a href="#NamedConnectionsClient.stop-140"><span class="linenos">140</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsClient.stop-141"><a href="#NamedConnectionsClient.stop-141"><span class="linenos">141</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">callback__client_stopped</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Client can call this method. Server should not call it. Server should call <a href="#NamedConnectionsClient.callback__stop">NamedConnectionsClient.callback__stop()</a> when wants to close connection</p>
</div>


                            </div>
                </section>
                <section id="NamedConnectionsServer">
                            <input id="NamedConnectionsServer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">NamedConnectionsServer</span>:

                <label class="view-source-button" for="NamedConnectionsServer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsServer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsServer-145"><a href="#NamedConnectionsServer-145"><span class="linenos">145</span></a><span class="k">class</span> <span class="nc">NamedConnectionsServer</span><span class="p">:</span>
</span><span id="NamedConnectionsServer-146"><a href="#NamedConnectionsServer-146"><span class="linenos">146</span></a>    <span class="c1"># def __init__(self, server_id: bytes, named_connections_manager: Optional[&#39;NamedConnectionsManager&#39;] = None) -&gt; None:</span>
</span><span id="NamedConnectionsServer-147"><a href="#NamedConnectionsServer-147"><span class="linenos">147</span></a>    <span class="c1">#     self.id: bytes = server_id</span>
</span><span id="NamedConnectionsServer-148"><a href="#NamedConnectionsServer-148"><span class="linenos">148</span></a>    <span class="c1">#     if named_connections_manager:</span>
</span><span id="NamedConnectionsServer-149"><a href="#NamedConnectionsServer-149"><span class="linenos">149</span></a>    <span class="c1">#         self.named_connections_manager: ReferenceType[&#39;NamedConnectionsManager&#39;] = ref(named_connections_manager)</span>
</span><span id="NamedConnectionsServer-150"><a href="#NamedConnectionsServer-150"><span class="linenos">150</span></a>    <span class="c1">#     else:</span>
</span><span id="NamedConnectionsServer-151"><a href="#NamedConnectionsServer-151"><span class="linenos">151</span></a>    <span class="c1">#         self.named_connections_manager = None</span>
</span><span id="NamedConnectionsServer-152"><a href="#NamedConnectionsServer-152"><span class="linenos">152</span></a>        
</span><span id="NamedConnectionsServer-153"><a href="#NamedConnectionsServer-153"><span class="linenos">153</span></a>    <span class="c1">#     self.bind_clients: Dict[int, NamedConnectionsClient] = dict()</span>
</span><span id="NamedConnectionsServer-154"><a href="#NamedConnectionsServer-154"><span class="linenos">154</span></a>
</span><span id="NamedConnectionsServer-155"><a href="#NamedConnectionsServer-155"><span class="linenos">155</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">named_connections_manager</span><span class="p">:</span> <span class="s1">&#39;NamedConnectionsManager&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="NamedConnectionsServer-156"><a href="#NamedConnectionsServer-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="NamedConnectionsServer-157"><a href="#NamedConnectionsServer-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">named_connections_manager</span><span class="p">:</span> <span class="n">ReferenceType</span><span class="p">[</span><span class="s1">&#39;NamedConnectionsManager&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref</span><span class="p">(</span><span class="n">named_connections_manager</span><span class="p">)</span>
</span><span id="NamedConnectionsServer-158"><a href="#NamedConnectionsServer-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NamedConnectionsServer-159"><a href="#NamedConnectionsServer-159"><span class="linenos">159</span></a>
</span><span id="NamedConnectionsServer-160"><a href="#NamedConnectionsServer-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">bind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer-161"><a href="#NamedConnectionsServer-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsServer-162"><a href="#NamedConnectionsServer-162"><span class="linenos">162</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">callback__bind</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="NamedConnectionsServer-163"><a href="#NamedConnectionsServer-163"><span class="linenos">163</span></a>
</span><span id="NamedConnectionsServer-164"><a href="#NamedConnectionsServer-164"><span class="linenos">164</span></a>    <span class="k">def</span> <span class="nf">unbind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer-165"><a href="#NamedConnectionsServer-165"><span class="linenos">165</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="NamedConnectionsServer-166"><a href="#NamedConnectionsServer-166"><span class="linenos">166</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="NamedConnectionsServer-167"><a href="#NamedConnectionsServer-167"><span class="linenos">167</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="NamedConnectionsServer-168"><a href="#NamedConnectionsServer-168"><span class="linenos">168</span></a>            <span class="k">pass</span>
</span><span id="NamedConnectionsServer-169"><a href="#NamedConnectionsServer-169"><span class="linenos">169</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="NamedConnectionsServer-170"><a href="#NamedConnectionsServer-170"><span class="linenos">170</span></a>            <span class="n">client</span><span class="o">.</span><span class="n">callback__unbind</span><span class="p">()</span>
</span><span id="NamedConnectionsServer-171"><a href="#NamedConnectionsServer-171"><span class="linenos">171</span></a>    
</span><span id="NamedConnectionsServer-172"><a href="#NamedConnectionsServer-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="nf">callback__data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer-173"><a href="#NamedConnectionsServer-173"><span class="linenos">173</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="NamedConnectionsServer-174"><a href="#NamedConnectionsServer-174"><span class="linenos">174</span></a>    
</span><span id="NamedConnectionsServer-175"><a href="#NamedConnectionsServer-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">callback__is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="NamedConnectionsServer-176"><a href="#NamedConnectionsServer-176"><span class="linenos">176</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="NamedConnectionsServer-177"><a href="#NamedConnectionsServer-177"><span class="linenos">177</span></a>
</span><span id="NamedConnectionsServer-178"><a href="#NamedConnectionsServer-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">callback__client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer-179"><a href="#NamedConnectionsServer-179"><span class="linenos">179</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="NamedConnectionsServer-180"><a href="#NamedConnectionsServer-180"><span class="linenos">180</span></a>    
</span><span id="NamedConnectionsServer-181"><a href="#NamedConnectionsServer-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">callback__client_stopped</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer-182"><a href="#NamedConnectionsServer-182"><span class="linenos">182</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can emit this callback. No additional data from the client will be provided. No read from the client side will be made.</span>
</span><span id="NamedConnectionsServer-183"><a href="#NamedConnectionsServer-183"><span class="linenos">183</span></a>
</span><span id="NamedConnectionsServer-184"><a href="#NamedConnectionsServer-184"><span class="linenos">184</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsServer-185"><a href="#NamedConnectionsServer-185"><span class="linenos">185</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsServer-186"><a href="#NamedConnectionsServer-186"><span class="linenos">186</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsServer-187"><a href="#NamedConnectionsServer-187"><span class="linenos">187</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="NamedConnectionsServer.__init__" class="classattr">
                                        <input id="NamedConnectionsServer.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">NamedConnectionsServer</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span>,</span><span class="param">	<span class="n">named_connections_manager</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsManager">NamedConnectionsManager</a></span></span>)</span>

                <label class="view-source-button" for="NamedConnectionsServer.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsServer.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsServer.__init__-155"><a href="#NamedConnectionsServer.__init__-155"><span class="linenos">155</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">named_connections_manager</span><span class="p">:</span> <span class="s1">&#39;NamedConnectionsManager&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="NamedConnectionsServer.__init__-156"><a href="#NamedConnectionsServer.__init__-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="NamedConnectionsServer.__init__-157"><a href="#NamedConnectionsServer.__init__-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">named_connections_manager</span><span class="p">:</span> <span class="n">ReferenceType</span><span class="p">[</span><span class="s1">&#39;NamedConnectionsManager&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">ref</span><span class="p">(</span><span class="n">named_connections_manager</span><span class="p">)</span>
</span><span id="NamedConnectionsServer.__init__-158"><a href="#NamedConnectionsServer.__init__-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsServer.id" class="classattr">
                                <div class="attr variable">
            <span class="name">id</span><span class="annotation">: bytes</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsServer.id"></a>
    
    

                            </div>
                            <div id="NamedConnectionsServer.named_connections_manager" class="classattr">
                                <div class="attr variable">
            <span class="name">named_connections_manager</span><span class="annotation">: &#34;ReferenceType[&#39;NamedConnectionsManager&#39;]&#34;</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsServer.named_connections_manager"></a>
    
    

                            </div>
                            <div id="NamedConnectionsServer.bind_clients" class="classattr">
                                <div class="attr variable">
            <span class="name">bind_clients</span><span class="annotation">: Dict[int, <a href="#NamedConnectionsClient">NamedConnectionsClient</a>]</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsServer.bind_clients"></a>
    
    

                            </div>
                            <div id="NamedConnectionsServer.bind" class="classattr">
                                        <input id="NamedConnectionsServer.bind-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bind</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsServer.bind-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsServer.bind"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsServer.bind-160"><a href="#NamedConnectionsServer.bind-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">bind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer.bind-161"><a href="#NamedConnectionsServer.bind-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsServer.bind-162"><a href="#NamedConnectionsServer.bind-162"><span class="linenos">162</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">callback__bind</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsServer.unbind" class="classattr">
                                        <input id="NamedConnectionsServer.unbind-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">unbind</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsServer.unbind-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsServer.unbind"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsServer.unbind-164"><a href="#NamedConnectionsServer.unbind-164"><span class="linenos">164</span></a>    <span class="k">def</span> <span class="nf">unbind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer.unbind-165"><a href="#NamedConnectionsServer.unbind-165"><span class="linenos">165</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="NamedConnectionsServer.unbind-166"><a href="#NamedConnectionsServer.unbind-166"><span class="linenos">166</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="NamedConnectionsServer.unbind-167"><a href="#NamedConnectionsServer.unbind-167"><span class="linenos">167</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="NamedConnectionsServer.unbind-168"><a href="#NamedConnectionsServer.unbind-168"><span class="linenos">168</span></a>            <span class="k">pass</span>
</span><span id="NamedConnectionsServer.unbind-169"><a href="#NamedConnectionsServer.unbind-169"><span class="linenos">169</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="NamedConnectionsServer.unbind-170"><a href="#NamedConnectionsServer.unbind-170"><span class="linenos">170</span></a>            <span class="n">client</span><span class="o">.</span><span class="n">callback__unbind</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsServer.callback__data_to_server_added" class="classattr">
                                        <input id="NamedConnectionsServer.callback__data_to_server_added-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__data_to_server_added</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsServer.callback__data_to_server_added-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsServer.callback__data_to_server_added"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsServer.callback__data_to_server_added-172"><a href="#NamedConnectionsServer.callback__data_to_server_added-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="nf">callback__data_to_server_added</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer.callback__data_to_server_added-173"><a href="#NamedConnectionsServer.callback__data_to_server_added-173"><span class="linenos">173</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsServer.callback__is_server_ready_for_data" class="classattr">
                                        <input id="NamedConnectionsServer.callback__is_server_ready_for_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__is_server_ready_for_data</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="NamedConnectionsServer.callback__is_server_ready_for_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsServer.callback__is_server_ready_for_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsServer.callback__is_server_ready_for_data-175"><a href="#NamedConnectionsServer.callback__is_server_ready_for_data-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">callback__is_server_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="NamedConnectionsServer.callback__is_server_ready_for_data-176"><a href="#NamedConnectionsServer.callback__is_server_ready_for_data-176"><span class="linenos">176</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsServer.callback__client_ready_for_data" class="classattr">
                                        <input id="NamedConnectionsServer.callback__client_ready_for_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__client_ready_for_data</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsServer.callback__client_ready_for_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsServer.callback__client_ready_for_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsServer.callback__client_ready_for_data-178"><a href="#NamedConnectionsServer.callback__client_ready_for_data-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">callback__client_ready_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer.callback__client_ready_for_data-179"><a href="#NamedConnectionsServer.callback__client_ready_for_data-179"><span class="linenos">179</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsServer.callback__client_stopped" class="classattr">
                                        <input id="NamedConnectionsServer.callback__client_stopped-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback__client_stopped</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsServer.callback__client_stopped-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsServer.callback__client_stopped"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsServer.callback__client_stopped-181"><a href="#NamedConnectionsServer.callback__client_stopped-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">callback__client_stopped</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsServer.callback__client_stopped-182"><a href="#NamedConnectionsServer.callback__client_stopped-182"><span class="linenos">182</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Client can emit this callback. No additional data from the client will be provided. No read from the client side will be made.</span>
</span><span id="NamedConnectionsServer.callback__client_stopped-183"><a href="#NamedConnectionsServer.callback__client_stopped-183"><span class="linenos">183</span></a>
</span><span id="NamedConnectionsServer.callback__client_stopped-184"><a href="#NamedConnectionsServer.callback__client_stopped-184"><span class="linenos">184</span></a><span class="sd">        Raises:</span>
</span><span id="NamedConnectionsServer.callback__client_stopped-185"><a href="#NamedConnectionsServer.callback__client_stopped-185"><span class="linenos">185</span></a><span class="sd">            NotImplementedError: _description_</span>
</span><span id="NamedConnectionsServer.callback__client_stopped-186"><a href="#NamedConnectionsServer.callback__client_stopped-186"><span class="linenos">186</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsServer.callback__client_stopped-187"><a href="#NamedConnectionsServer.callback__client_stopped-187"><span class="linenos">187</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Client can emit this callback. No additional data from the client will be provided. No read from the client side will be made.</p>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                </section>
                <section id="NamedConnectionsManager">
                            <input id="NamedConnectionsManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">NamedConnectionsManager</span>:

                <label class="view-source-button" for="NamedConnectionsManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager-190"><a href="#NamedConnectionsManager-190"><span class="linenos">190</span></a><span class="k">class</span> <span class="nc">NamedConnectionsManager</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-191"><a href="#NamedConnectionsManager-191"><span class="linenos">191</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-192"><a href="#NamedConnectionsManager-192"><span class="linenos">192</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="NamedConnectionsManager-193"><a href="#NamedConnectionsManager-193"><span class="linenos">193</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">:</span> <span class="n">IDGenerator</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-194"><a href="#NamedConnectionsManager-194"><span class="linenos">194</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-195"><a href="#NamedConnectionsManager-195"><span class="linenos">195</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">NamedConnectionsClient</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-196"><a href="#NamedConnectionsManager-196"><span class="linenos">196</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-197"><a href="#NamedConnectionsManager-197"><span class="linenos">197</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="n">NamedConnectionsServer</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-198"><a href="#NamedConnectionsManager-198"><span class="linenos">198</span></a>    
</span><span id="NamedConnectionsManager-199"><a href="#NamedConnectionsManager-199"><span class="linenos">199</span></a>    <span class="k">def</span> <span class="nf">create_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">NamedConnectionsClient</span><span class="p">],</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NamedConnectionsClient</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-200"><a href="#NamedConnectionsManager-200"><span class="linenos">200</span></a>        <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span> <span class="o">=</span> <span class="n">client_type</span><span class="p">(</span><span class="n">server_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-201"><a href="#NamedConnectionsManager-201"><span class="linenos">201</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-202"><a href="#NamedConnectionsManager-202"><span class="linenos">202</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="NamedConnectionsManager-203"><a href="#NamedConnectionsManager-203"><span class="linenos">203</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-204"><a href="#NamedConnectionsManager-204"><span class="linenos">204</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager-205"><a href="#NamedConnectionsManager-205"><span class="linenos">205</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-206"><a href="#NamedConnectionsManager-206"><span class="linenos">206</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-207"><a href="#NamedConnectionsManager-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_unbind_client_impl</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-208"><a href="#NamedConnectionsManager-208"><span class="linenos">208</span></a>        
</span><span id="NamedConnectionsManager-209"><a href="#NamedConnectionsManager-209"><span class="linenos">209</span></a>        <span class="k">return</span> <span class="n">client_id</span>
</span><span id="NamedConnectionsManager-210"><a href="#NamedConnectionsManager-210"><span class="linenos">210</span></a>    
</span><span id="NamedConnectionsManager-211"><a href="#NamedConnectionsManager-211"><span class="linenos">211</span></a>    <span class="k">def</span> <span class="nf">register_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-212"><a href="#NamedConnectionsManager-212"><span class="linenos">212</span></a>        <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_id</span>
</span><span id="NamedConnectionsManager-213"><a href="#NamedConnectionsManager-213"><span class="linenos">213</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-214"><a href="#NamedConnectionsManager-214"><span class="linenos">214</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="NamedConnectionsManager-215"><a href="#NamedConnectionsManager-215"><span class="linenos">215</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-216"><a href="#NamedConnectionsManager-216"><span class="linenos">216</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager-217"><a href="#NamedConnectionsManager-217"><span class="linenos">217</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-218"><a href="#NamedConnectionsManager-218"><span class="linenos">218</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-219"><a href="#NamedConnectionsManager-219"><span class="linenos">219</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager-220"><a href="#NamedConnectionsManager-220"><span class="linenos">220</span></a>            <span class="k">if</span> <span class="n">server_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-221"><a href="#NamedConnectionsManager-221"><span class="linenos">221</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-222"><a href="#NamedConnectionsManager-222"><span class="linenos">222</span></a>            
</span><span id="NamedConnectionsManager-223"><a href="#NamedConnectionsManager-223"><span class="linenos">223</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-224"><a href="#NamedConnectionsManager-224"><span class="linenos">224</span></a>        
</span><span id="NamedConnectionsManager-225"><a href="#NamedConnectionsManager-225"><span class="linenos">225</span></a>        <span class="k">return</span> <span class="n">client_id</span>
</span><span id="NamedConnectionsManager-226"><a href="#NamedConnectionsManager-226"><span class="linenos">226</span></a>
</span><span id="NamedConnectionsManager-227"><a href="#NamedConnectionsManager-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="nf">register_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="n">NamedConnectionsServer</span><span class="p">):</span>
</span><span id="NamedConnectionsManager-228"><a href="#NamedConnectionsManager-228"><span class="linenos">228</span></a>        <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server</span><span class="o">.</span><span class="n">id</span>
</span><span id="NamedConnectionsManager-229"><a href="#NamedConnectionsManager-229"><span class="linenos">229</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-230"><a href="#NamedConnectionsManager-230"><span class="linenos">230</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;NamedConnectionsServer already registered&#39;</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-231"><a href="#NamedConnectionsManager-231"><span class="linenos">231</span></a>        
</span><span id="NamedConnectionsManager-232"><a href="#NamedConnectionsManager-232"><span class="linenos">232</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">server</span>
</span><span id="NamedConnectionsManager-233"><a href="#NamedConnectionsManager-233"><span class="linenos">233</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-234"><a href="#NamedConnectionsManager-234"><span class="linenos">234</span></a>            <span class="n">unbind_clients</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span>
</span><span id="NamedConnectionsManager-235"><a href="#NamedConnectionsManager-235"><span class="linenos">235</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span>
</span><span id="NamedConnectionsManager-236"><a href="#NamedConnectionsManager-236"><span class="linenos">236</span></a>            <span class="k">for</span> <span class="n">client</span> <span class="ow">in</span> <span class="n">unbind_clients</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-237"><a href="#NamedConnectionsManager-237"><span class="linenos">237</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="NamedConnectionsManager-238"><a href="#NamedConnectionsManager-238"><span class="linenos">238</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager-239"><a href="#NamedConnectionsManager-239"><span class="linenos">239</span></a>                <span class="n">server</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-240"><a href="#NamedConnectionsManager-240"><span class="linenos">240</span></a>
</span><span id="NamedConnectionsManager-241"><a href="#NamedConnectionsManager-241"><span class="linenos">241</span></a>    <span class="k">def</span> <span class="nf">unregister_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="n">NamedConnectionsServer</span><span class="p">):</span>
</span><span id="NamedConnectionsManager-242"><a href="#NamedConnectionsManager-242"><span class="linenos">242</span></a>        <span class="n">server_clients</span> <span class="o">=</span> <span class="n">server</span><span class="o">.</span><span class="n">bind_clients</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-243"><a href="#NamedConnectionsManager-243"><span class="linenos">243</span></a>        <span class="k">for</span> <span class="n">client_id</span><span class="p">,</span> <span class="n">client</span> <span class="ow">in</span> <span class="n">server_clients</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-244"><a href="#NamedConnectionsManager-244"><span class="linenos">244</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_client</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-245"><a href="#NamedConnectionsManager-245"><span class="linenos">245</span></a>        
</span><span id="NamedConnectionsManager-246"><a href="#NamedConnectionsManager-246"><span class="linenos">246</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-247"><a href="#NamedConnectionsManager-247"><span class="linenos">247</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="NamedConnectionsManager-248"><a href="#NamedConnectionsManager-248"><span class="linenos">248</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-249"><a href="#NamedConnectionsManager-249"><span class="linenos">249</span></a>            <span class="k">pass</span>
</span><span id="NamedConnectionsManager-250"><a href="#NamedConnectionsManager-250"><span class="linenos">250</span></a>
</span><span id="NamedConnectionsManager-251"><a href="#NamedConnectionsManager-251"><span class="linenos">251</span></a>    <span class="k">def</span> <span class="nf">unregister_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsManager-252"><a href="#NamedConnectionsManager-252"><span class="linenos">252</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-253"><a href="#NamedConnectionsManager-253"><span class="linenos">253</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-254"><a href="#NamedConnectionsManager-254"><span class="linenos">254</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-255"><a href="#NamedConnectionsManager-255"><span class="linenos">255</span></a>        
</span><span id="NamedConnectionsManager-256"><a href="#NamedConnectionsManager-256"><span class="linenos">256</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">id</span>
</span><span id="NamedConnectionsManager-257"><a href="#NamedConnectionsManager-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-258"><a href="#NamedConnectionsManager-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-259"><a href="#NamedConnectionsManager-259"><span class="linenos">259</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-260"><a href="#NamedConnectionsManager-260"><span class="linenos">260</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-261"><a href="#NamedConnectionsManager-261"><span class="linenos">261</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-262"><a href="#NamedConnectionsManager-262"><span class="linenos">262</span></a>            <span class="k">pass</span>
</span><span id="NamedConnectionsManager-263"><a href="#NamedConnectionsManager-263"><span class="linenos">263</span></a>
</span><span id="NamedConnectionsManager-264"><a href="#NamedConnectionsManager-264"><span class="linenos">264</span></a>    <span class="k">def</span> <span class="nf">unbind_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsManager-265"><a href="#NamedConnectionsManager-265"><span class="linenos">265</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-266"><a href="#NamedConnectionsManager-266"><span class="linenos">266</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-267"><a href="#NamedConnectionsManager-267"><span class="linenos">267</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-268"><a href="#NamedConnectionsManager-268"><span class="linenos">268</span></a>
</span><span id="NamedConnectionsManager-269"><a href="#NamedConnectionsManager-269"><span class="linenos">269</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_unbind_client_impl</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-270"><a href="#NamedConnectionsManager-270"><span class="linenos">270</span></a>
</span><span id="NamedConnectionsManager-271"><a href="#NamedConnectionsManager-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="nf">_unbind_client_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsManager-272"><a href="#NamedConnectionsManager-272"><span class="linenos">272</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">id</span>
</span><span id="NamedConnectionsManager-273"><a href="#NamedConnectionsManager-273"><span class="linenos">273</span></a>        <span class="n">server_id</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_id</span>
</span><span id="NamedConnectionsManager-274"><a href="#NamedConnectionsManager-274"><span class="linenos">274</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-275"><a href="#NamedConnectionsManager-275"><span class="linenos">275</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager-276"><a href="#NamedConnectionsManager-276"><span class="linenos">276</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager-277"><a href="#NamedConnectionsManager-277"><span class="linenos">277</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="NamedConnectionsManager-278"><a href="#NamedConnectionsManager-278"><span class="linenos">278</span></a>        
</span><span id="NamedConnectionsManager-279"><a href="#NamedConnectionsManager-279"><span class="linenos">279</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-280"><a href="#NamedConnectionsManager-280"><span class="linenos">280</span></a>
</span><span id="NamedConnectionsManager-281"><a href="#NamedConnectionsManager-281"><span class="linenos">281</span></a>    <span class="k">def</span> <span class="nf">rebind_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="NamedConnectionsManager-282"><a href="#NamedConnectionsManager-282"><span class="linenos">282</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Force rebind client to another server</span>
</span><span id="NamedConnectionsManager-283"><a href="#NamedConnectionsManager-283"><span class="linenos">283</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsManager-284"><a href="#NamedConnectionsManager-284"><span class="linenos">284</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-285"><a href="#NamedConnectionsManager-285"><span class="linenos">285</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">server_id</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="NamedConnectionsManager-286"><a href="#NamedConnectionsManager-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager-287"><a href="#NamedConnectionsManager-287"><span class="linenos">287</span></a>    
</span><span id="NamedConnectionsManager-288"><a href="#NamedConnectionsManager-288"><span class="linenos">288</span></a>    <span class="c1"># def put_client_message_to_server_queue(self, message):</span>
</span><span id="NamedConnectionsManager-289"><a href="#NamedConnectionsManager-289"><span class="linenos">289</span></a>    <span class="c1">#     ...</span>
</span><span id="NamedConnectionsManager-290"><a href="#NamedConnectionsManager-290"><span class="linenos">290</span></a>    
</span><span id="NamedConnectionsManager-291"><a href="#NamedConnectionsManager-291"><span class="linenos">291</span></a>    <span class="c1"># def put_server_message_to_client_queue(self, message):</span>
</span><span id="NamedConnectionsManager-292"><a href="#NamedConnectionsManager-292"><span class="linenos">292</span></a>    <span class="c1">#     ...</span>
</span><span id="NamedConnectionsManager-293"><a href="#NamedConnectionsManager-293"><span class="linenos">293</span></a>    
</span><span id="NamedConnectionsManager-294"><a href="#NamedConnectionsManager-294"><span class="linenos">294</span></a>    <span class="c1"># def client_to_server_queue_len(self):</span>
</span><span id="NamedConnectionsManager-295"><a href="#NamedConnectionsManager-295"><span class="linenos">295</span></a>    <span class="c1">#     ...</span>
</span><span id="NamedConnectionsManager-296"><a href="#NamedConnectionsManager-296"><span class="linenos">296</span></a>    
</span><span id="NamedConnectionsManager-297"><a href="#NamedConnectionsManager-297"><span class="linenos">297</span></a>    <span class="c1"># def server_to_client_queue_len(self):</span>
</span><span id="NamedConnectionsManager-298"><a href="#NamedConnectionsManager-298"><span class="linenos">298</span></a>    <span class="c1">#     ...</span>
</span></pre></div>


    

                            <div id="NamedConnectionsManager.__init__" class="classattr">
                                        <input id="NamedConnectionsManager.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">NamedConnectionsManager</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span></span>)</span>

                <label class="view-source-button" for="NamedConnectionsManager.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager.__init__-191"><a href="#NamedConnectionsManager.__init__-191"><span class="linenos">191</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.__init__-192"><a href="#NamedConnectionsManager.__init__-192"><span class="linenos">192</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ValueExistence</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="NamedConnectionsManager.__init__-193"><a href="#NamedConnectionsManager.__init__-193"><span class="linenos">193</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">:</span> <span class="n">IDGenerator</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.__init__-194"><a href="#NamedConnectionsManager.__init__-194"><span class="linenos">194</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.__init__-195"><a href="#NamedConnectionsManager.__init__-195"><span class="linenos">195</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">NamedConnectionsClient</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.__init__-196"><a href="#NamedConnectionsManager.__init__-196"><span class="linenos">196</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NamedConnectionsClient</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.__init__-197"><a href="#NamedConnectionsManager.__init__-197"><span class="linenos">197</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="n">NamedConnectionsServer</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsManager.external_data_full_size" class="classattr">
                                <div class="attr variable">
            <span class="name">external_data_full_size</span><span class="annotation">: cengal.code_flow_control.smart_values.versions.v_2.smart_values.ValueExistence</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsManager.external_data_full_size"></a>
    
    

                            </div>
                            <div id="NamedConnectionsManager.gen_client_id" class="classattr">
                                <div class="attr variable">
            <span class="name">gen_client_id</span><span class="annotation">: &lt;built-in function IDGenerator&gt;</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsManager.gen_client_id"></a>
    
    

                            </div>
                            <div id="NamedConnectionsManager.unbind_clients" class="classattr">
                                <div class="attr variable">
            <span class="name">unbind_clients</span><span class="annotation">: Dict[int, <a href="#NamedConnectionsClient">NamedConnectionsClient</a>]</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsManager.unbind_clients"></a>
    
    

                            </div>
                            <div id="NamedConnectionsManager.unbind_clients_per_server" class="classattr">
                                <div class="attr variable">
            <span class="name">unbind_clients_per_server</span><span class="annotation">: Dict[str, Set[<a href="#NamedConnectionsClient">NamedConnectionsClient</a>]]</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsManager.unbind_clients_per_server"></a>
    
    

                            </div>
                            <div id="NamedConnectionsManager.bind_clients" class="classattr">
                                <div class="attr variable">
            <span class="name">bind_clients</span><span class="annotation">: Dict[int, <a href="#NamedConnectionsClient">NamedConnectionsClient</a>]</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsManager.bind_clients"></a>
    
    

                            </div>
                            <div id="NamedConnectionsManager.servers" class="classattr">
                                <div class="attr variable">
            <span class="name">servers</span><span class="annotation">: Dict[bytes, <a href="#NamedConnectionsServer">NamedConnectionsServer</a>]</span>

        
    </div>
    <a class="headerlink" href="#NamedConnectionsManager.servers"></a>
    
    

                            </div>
                            <div id="NamedConnectionsManager.create_client" class="classattr">
                                        <input id="NamedConnectionsManager.create_client-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">create_client</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span><span class="p">]</span>,</span><span class="param">	<span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span>:</span></span>

                <label class="view-source-button" for="NamedConnectionsManager.create_client-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager.create_client"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager.create_client-199"><a href="#NamedConnectionsManager.create_client-199"><span class="linenos">199</span></a>    <span class="k">def</span> <span class="nf">create_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">NamedConnectionsClient</span><span class="p">],</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">NamedConnectionsClient</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.create_client-200"><a href="#NamedConnectionsManager.create_client-200"><span class="linenos">200</span></a>        <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span> <span class="o">=</span> <span class="n">client_type</span><span class="p">(</span><span class="n">server_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">external_data_full_size</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.create_client-201"><a href="#NamedConnectionsManager.create_client-201"><span class="linenos">201</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.create_client-202"><a href="#NamedConnectionsManager.create_client-202"><span class="linenos">202</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="NamedConnectionsManager.create_client-203"><a href="#NamedConnectionsManager.create_client-203"><span class="linenos">203</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.create_client-204"><a href="#NamedConnectionsManager.create_client-204"><span class="linenos">204</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager.create_client-205"><a href="#NamedConnectionsManager.create_client-205"><span class="linenos">205</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.create_client-206"><a href="#NamedConnectionsManager.create_client-206"><span class="linenos">206</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.create_client-207"><a href="#NamedConnectionsManager.create_client-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_unbind_client_impl</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.create_client-208"><a href="#NamedConnectionsManager.create_client-208"><span class="linenos">208</span></a>        
</span><span id="NamedConnectionsManager.create_client-209"><a href="#NamedConnectionsManager.create_client-209"><span class="linenos">209</span></a>        <span class="k">return</span> <span class="n">client_id</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsManager.register_client" class="classattr">
                                        <input id="NamedConnectionsManager.register_client-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_client</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="NamedConnectionsManager.register_client-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager.register_client"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager.register_client-211"><a href="#NamedConnectionsManager.register_client-211"><span class="linenos">211</span></a>    <span class="k">def</span> <span class="nf">register_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.register_client-212"><a href="#NamedConnectionsManager.register_client-212"><span class="linenos">212</span></a>        <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_id</span>
</span><span id="NamedConnectionsManager.register_client-213"><a href="#NamedConnectionsManager.register_client-213"><span class="linenos">213</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_client_id</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.register_client-214"><a href="#NamedConnectionsManager.register_client-214"><span class="linenos">214</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">id</span> <span class="o">=</span> <span class="n">client_id</span>
</span><span id="NamedConnectionsManager.register_client-215"><a href="#NamedConnectionsManager.register_client-215"><span class="linenos">215</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.register_client-216"><a href="#NamedConnectionsManager.register_client-216"><span class="linenos">216</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager.register_client-217"><a href="#NamedConnectionsManager.register_client-217"><span class="linenos">217</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.register_client-218"><a href="#NamedConnectionsManager.register_client-218"><span class="linenos">218</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.register_client-219"><a href="#NamedConnectionsManager.register_client-219"><span class="linenos">219</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">[</span><span class="n">client_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager.register_client-220"><a href="#NamedConnectionsManager.register_client-220"><span class="linenos">220</span></a>            <span class="k">if</span> <span class="n">server_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.register_client-221"><a href="#NamedConnectionsManager.register_client-221"><span class="linenos">221</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.register_client-222"><a href="#NamedConnectionsManager.register_client-222"><span class="linenos">222</span></a>            
</span><span id="NamedConnectionsManager.register_client-223"><a href="#NamedConnectionsManager.register_client-223"><span class="linenos">223</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.register_client-224"><a href="#NamedConnectionsManager.register_client-224"><span class="linenos">224</span></a>        
</span><span id="NamedConnectionsManager.register_client-225"><a href="#NamedConnectionsManager.register_client-225"><span class="linenos">225</span></a>        <span class="k">return</span> <span class="n">client_id</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsManager.register_server" class="classattr">
                                        <input id="NamedConnectionsManager.register_server-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_server</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">server</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsServer">NamedConnectionsServer</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsManager.register_server-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager.register_server"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager.register_server-227"><a href="#NamedConnectionsManager.register_server-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="nf">register_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="n">NamedConnectionsServer</span><span class="p">):</span>
</span><span id="NamedConnectionsManager.register_server-228"><a href="#NamedConnectionsManager.register_server-228"><span class="linenos">228</span></a>        <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">server</span><span class="o">.</span><span class="n">id</span>
</span><span id="NamedConnectionsManager.register_server-229"><a href="#NamedConnectionsManager.register_server-229"><span class="linenos">229</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.register_server-230"><a href="#NamedConnectionsManager.register_server-230"><span class="linenos">230</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;NamedConnectionsServer already registered&#39;</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.register_server-231"><a href="#NamedConnectionsManager.register_server-231"><span class="linenos">231</span></a>        
</span><span id="NamedConnectionsManager.register_server-232"><a href="#NamedConnectionsManager.register_server-232"><span class="linenos">232</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">server</span>
</span><span id="NamedConnectionsManager.register_server-233"><a href="#NamedConnectionsManager.register_server-233"><span class="linenos">233</span></a>        <span class="k">if</span> <span class="n">server_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.register_server-234"><a href="#NamedConnectionsManager.register_server-234"><span class="linenos">234</span></a>            <span class="n">unbind_clients</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span>
</span><span id="NamedConnectionsManager.register_server-235"><a href="#NamedConnectionsManager.register_server-235"><span class="linenos">235</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span>
</span><span id="NamedConnectionsManager.register_server-236"><a href="#NamedConnectionsManager.register_server-236"><span class="linenos">236</span></a>            <span class="k">for</span> <span class="n">client</span> <span class="ow">in</span> <span class="n">unbind_clients</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.register_server-237"><a href="#NamedConnectionsManager.register_server-237"><span class="linenos">237</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="NamedConnectionsManager.register_server-238"><a href="#NamedConnectionsManager.register_server-238"><span class="linenos">238</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">]</span> <span class="o">=</span> <span class="n">client</span>
</span><span id="NamedConnectionsManager.register_server-239"><a href="#NamedConnectionsManager.register_server-239"><span class="linenos">239</span></a>                <span class="n">server</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsManager.unregister_server" class="classattr">
                                        <input id="NamedConnectionsManager.unregister_server-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">unregister_server</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">server</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsServer">NamedConnectionsServer</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsManager.unregister_server-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager.unregister_server"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager.unregister_server-241"><a href="#NamedConnectionsManager.unregister_server-241"><span class="linenos">241</span></a>    <span class="k">def</span> <span class="nf">unregister_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server</span><span class="p">:</span> <span class="n">NamedConnectionsServer</span><span class="p">):</span>
</span><span id="NamedConnectionsManager.unregister_server-242"><a href="#NamedConnectionsManager.unregister_server-242"><span class="linenos">242</span></a>        <span class="n">server_clients</span> <span class="o">=</span> <span class="n">server</span><span class="o">.</span><span class="n">bind_clients</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.unregister_server-243"><a href="#NamedConnectionsManager.unregister_server-243"><span class="linenos">243</span></a>        <span class="k">for</span> <span class="n">client_id</span><span class="p">,</span> <span class="n">client</span> <span class="ow">in</span> <span class="n">server_clients</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.unregister_server-244"><a href="#NamedConnectionsManager.unregister_server-244"><span class="linenos">244</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_client</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.unregister_server-245"><a href="#NamedConnectionsManager.unregister_server-245"><span class="linenos">245</span></a>        
</span><span id="NamedConnectionsManager.unregister_server-246"><a href="#NamedConnectionsManager.unregister_server-246"><span class="linenos">246</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.unregister_server-247"><a href="#NamedConnectionsManager.unregister_server-247"><span class="linenos">247</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server</span><span class="o">.</span><span class="n">id</span><span class="p">]</span>
</span><span id="NamedConnectionsManager.unregister_server-248"><a href="#NamedConnectionsManager.unregister_server-248"><span class="linenos">248</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.unregister_server-249"><a href="#NamedConnectionsManager.unregister_server-249"><span class="linenos">249</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsManager.unregister_client" class="classattr">
                                        <input id="NamedConnectionsManager.unregister_client-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">unregister_client</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsManager.unregister_client-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager.unregister_client"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager.unregister_client-251"><a href="#NamedConnectionsManager.unregister_client-251"><span class="linenos">251</span></a>    <span class="k">def</span> <span class="nf">unregister_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsManager.unregister_client-252"><a href="#NamedConnectionsManager.unregister_client-252"><span class="linenos">252</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.unregister_client-253"><a href="#NamedConnectionsManager.unregister_client-253"><span class="linenos">253</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.unregister_client-254"><a href="#NamedConnectionsManager.unregister_client-254"><span class="linenos">254</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.unregister_client-255"><a href="#NamedConnectionsManager.unregister_client-255"><span class="linenos">255</span></a>        
</span><span id="NamedConnectionsManager.unregister_client-256"><a href="#NamedConnectionsManager.unregister_client-256"><span class="linenos">256</span></a>        <span class="n">client_id</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">id</span>
</span><span id="NamedConnectionsManager.unregister_client-257"><a href="#NamedConnectionsManager.unregister_client-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">bind_clients</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.unregister_client-258"><a href="#NamedConnectionsManager.unregister_client-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">client_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.unregister_client-259"><a href="#NamedConnectionsManager.unregister_client-259"><span class="linenos">259</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.unregister_client-260"><a href="#NamedConnectionsManager.unregister_client-260"><span class="linenos">260</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">unbind_clients_per_server</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.unregister_client-261"><a href="#NamedConnectionsManager.unregister_client-261"><span class="linenos">261</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.unregister_client-262"><a href="#NamedConnectionsManager.unregister_client-262"><span class="linenos">262</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsManager.unbind_client" class="classattr">
                                        <input id="NamedConnectionsManager.unbind_client-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">unbind_client</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsManager.unbind_client-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager.unbind_client"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager.unbind_client-264"><a href="#NamedConnectionsManager.unbind_client-264"><span class="linenos">264</span></a>    <span class="k">def</span> <span class="nf">unbind_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">):</span>
</span><span id="NamedConnectionsManager.unbind_client-265"><a href="#NamedConnectionsManager.unbind_client-265"><span class="linenos">265</span></a>        <span class="n">server</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">server_ref</span><span class="p">()</span>
</span><span id="NamedConnectionsManager.unbind_client-266"><a href="#NamedConnectionsManager.unbind_client-266"><span class="linenos">266</span></a>        <span class="k">if</span> <span class="n">server</span><span class="p">:</span>
</span><span id="NamedConnectionsManager.unbind_client-267"><a href="#NamedConnectionsManager.unbind_client-267"><span class="linenos">267</span></a>            <span class="n">server</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.unbind_client-268"><a href="#NamedConnectionsManager.unbind_client-268"><span class="linenos">268</span></a>
</span><span id="NamedConnectionsManager.unbind_client-269"><a href="#NamedConnectionsManager.unbind_client-269"><span class="linenos">269</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_unbind_client_impl</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="NamedConnectionsManager.rebind_client" class="classattr">
                                        <input id="NamedConnectionsManager.rebind_client-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">rebind_client</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client</span><span class="p">:</span> <span class="n"><a href="#NamedConnectionsClient">NamedConnectionsClient</a></span>,</span><span class="param">	<span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="NamedConnectionsManager.rebind_client-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#NamedConnectionsManager.rebind_client"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="NamedConnectionsManager.rebind_client-281"><a href="#NamedConnectionsManager.rebind_client-281"><span class="linenos">281</span></a>    <span class="k">def</span> <span class="nf">rebind_client</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">NamedConnectionsClient</span><span class="p">,</span> <span class="n">server_id</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="NamedConnectionsManager.rebind_client-282"><a href="#NamedConnectionsManager.rebind_client-282"><span class="linenos">282</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Force rebind client to another server</span>
</span><span id="NamedConnectionsManager.rebind_client-283"><a href="#NamedConnectionsManager.rebind_client-283"><span class="linenos">283</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="NamedConnectionsManager.rebind_client-284"><a href="#NamedConnectionsManager.rebind_client-284"><span class="linenos">284</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">client</span><span class="o">.</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">unbind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span><span id="NamedConnectionsManager.rebind_client-285"><a href="#NamedConnectionsManager.rebind_client-285"><span class="linenos">285</span></a>        <span class="n">client</span><span class="o">.</span><span class="n">server_id</span> <span class="o">=</span> <span class="n">server_id</span>
</span><span id="NamedConnectionsManager.rebind_client-286"><a href="#NamedConnectionsManager.rebind_client-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">servers</span><span class="p">[</span><span class="n">server_id</span><span class="p">]</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="n">client</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Force rebind client to another server</p>
</div>


                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>