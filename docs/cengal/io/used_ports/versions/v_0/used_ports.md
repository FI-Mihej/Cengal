---
title: used_ports
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.io<wbr>.used_ports<wbr>.versions<wbr>.v_0<wbr>.used_ports    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-used_ports-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-used_ports-view-source"><span>View Source</span></label>

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
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;PortStatus&#39;</span><span class="p">,</span> <span class="s1">&#39;Table&#39;</span><span class="p">,</span> <span class="s1">&#39;Protocol&#39;</span><span class="p">,</span> <span class="s1">&#39;purify_ports&#39;</span><span class="p">,</span> <span class="s1">&#39;get_tables&#39;</span><span class="p">,</span> <span class="s1">&#39;used_ports&#39;</span><span class="p">,</span> <span class="s1">&#39;PortLord&#39;</span><span class="p">,</span> <span class="s1">&#39;PortInfo&#39;</span><span class="p">,</span> <span class="s1">&#39;UsedPorts&#39;</span><span class="p">,</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">,</span> <span class="s1">&#39;unify_ports&#39;</span><span class="p">,</span> <span class="s1">&#39;UnaceptablePortsRangeTypeError&#39;</span><span class="p">]</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">import</span> <span class="nn">pickle</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Any</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">namedtuple</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.path_manager</span> <span class="kn">import</span> <span class="n">path_relative_to_src</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="k">class</span> <span class="nc">PortStatus</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="n">na</span> <span class="o">=</span> <span class="s1">&#39;N/A&#39;</span>                 <span class="c1"># In programming APIs (not in communication between hosts), requests a system-allocated (dynamic) port</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>    <span class="n">yes</span> <span class="o">=</span> <span class="s1">&#39;Yes&#39;</span>                <span class="c1"># Described protocol is assigned for this port by IANA and is standardized, specified, or widely used for such.</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="n">unofficial</span> <span class="o">=</span> <span class="s1">&#39;Unofficial&#39;</span>  <span class="c1"># Described protocol is not assigned for this port by IANA but is standardized, specified, or widely used for such.</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    <span class="n">assigned</span> <span class="o">=</span> <span class="s1">&#39;Assigned&#39;</span>      <span class="c1"># Described protocol is assigned by IANA for this port, but is not standardized, specified, or widely used for such.</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="n">no</span> <span class="o">=</span> <span class="s1">&#39;No&#39;</span>                  <span class="c1"># Described protocol is not assigned by IANA, standardized, specified, or widely used for the port.</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="n">reserved</span> <span class="o">=</span> <span class="s1">&#39;Reserved&#39;</span>      <span class="c1"># Port is reserved by IANA, generally to prevent collision having its previous use removed. The port number may be available for assignment upon request to IANA.</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="k">class</span> <span class="nc">Table</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="n">system</span> <span class="o">=</span> <span class="s1">&#39;system&#39;</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="n">user</span> <span class="o">=</span> <span class="s1">&#39;user&#39;</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="n">ephemeral</span> <span class="o">=</span> <span class="s1">&#39;ephemeral&#39;</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="k">class</span> <span class="nc">Protocol</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="n">tcp</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="n">udp</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="n">sctp</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    <span class="n">dccp</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="n">_tables</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Table</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="n">_known_tables_names</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;system&#39;</span><span class="p">,</span> <span class="s1">&#39;user&#39;</span><span class="p">,</span> <span class="s1">&#39;ephemeral&#39;</span><span class="p">}</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="n">_used_ports</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="k">def</span> <span class="nf">_purify_item</span><span class="p">(</span><span class="n">item</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">PortStatus</span><span class="p">:</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="k">if</span> <span class="n">item</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="k">return</span> <span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="k">return</span> <span class="n">PortStatus</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="k">def</span> <span class="nf">get_tables</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Table</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">]]:</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="k">global</span> <span class="n">_tables</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="k">if</span> <span class="n">_tables</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="n">tables</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Table</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>        <span class="k">for</span> <span class="n">table_name</span> <span class="ow">in</span> <span class="n">_known_tables_names</span><span class="p">:</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path_relative_to_src</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;data/table_</span><span class="si">{</span><span class="n">table_name</span><span class="si">}</span><span class="s1">.pickle&#39;</span><span class="p">),</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>                <span class="n">tables</span><span class="p">[</span><span class="n">Table</span><span class="p">(</span><span class="n">table_name</span><span class="p">)]</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="n">_tables</span> <span class="o">=</span> <span class="n">tables</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="k">return</span> <span class="n">_tables</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="k">def</span> <span class="nf">used_ports</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="s1">&#39;UsedPorts&#39;</span><span class="p">:</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="k">global</span> <span class="n">_used_ports</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>    <span class="k">if</span> <span class="n">_used_ports</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="n">_used_ports</span> <span class="o">=</span> <span class="n">UsedPorts</span><span class="p">()</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>    <span class="k">return</span> <span class="n">_used_ports</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a><span class="n">PortLord</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s1">&#39;PortLord&#39;</span><span class="p">,</span> <span class="s1">&#39;tcp udp sctp dccp description&#39;</span><span class="p">)</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="k">class</span> <span class="nc">PortInfo</span><span class="p">:</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">port_lords</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n">PortLord</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">port</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span> <span class="o">=</span> <span class="n">port_lords</span> <span class="ow">or</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">port_lord</span><span class="p">:</span> <span class="n">PortLord</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">)</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span><span class="p">)</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a><span class="k">class</span> <span class="nc">UsedPorts</span><span class="p">:</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">PortInfo</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">([</span><span class="n">PortInfo</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">65536</span><span class="p">)])</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tables</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="n">Table</span><span class="o">.</span><span class="n">system</span><span class="p">:</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1024</span><span class="p">),</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>            <span class="n">Table</span><span class="o">.</span><span class="n">user</span><span class="p">:</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">1024</span><span class="p">,</span> <span class="mi">49152</span><span class="p">),</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>            <span class="n">Table</span><span class="o">.</span><span class="n">ephemeral</span><span class="p">:</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">49152</span><span class="p">,</span> <span class="mi">65536</span><span class="p">),</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="p">}</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="n">raw_tables</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Table</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="n">get_tables</span><span class="p">()</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="k">for</span> <span class="n">table_name</span><span class="p">,</span> <span class="n">raw_table</span> <span class="ow">in</span> <span class="n">raw_tables</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>            <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">raw_table</span><span class="p">:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>                <span class="n">port_or_range</span><span class="p">,</span> <span class="n">tcp</span><span class="p">,</span> <span class="n">udp</span><span class="p">,</span> <span class="n">sctp</span><span class="p">,</span> <span class="n">dccp</span><span class="p">,</span> <span class="n">description</span> <span class="o">=</span> <span class="n">row</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>                <span class="n">port_lord</span> <span class="o">=</span> <span class="n">PortLord</span><span class="p">(</span><span class="n">_purify_item</span><span class="p">(</span><span class="n">tcp</span><span class="p">),</span> <span class="n">_purify_item</span><span class="p">(</span><span class="n">udp</span><span class="p">),</span> <span class="n">_purify_item</span><span class="p">(</span><span class="n">sctp</span><span class="p">),</span> <span class="n">_purify_item</span><span class="p">(</span><span class="n">dccp</span><span class="p">),</span> <span class="n">description</span><span class="p">)</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>                    <span class="k">for</span> <span class="n">port</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="nb">int</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">[</span><span class="n">port</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">)</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">)]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">)</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="n">not_used_port</span> <span class="o">=</span> <span class="n">PortLord</span><span class="p">(</span><span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span><span class="p">,</span> <span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span><span class="p">,</span> <span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span><span class="p">,</span> <span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span><span class="p">,</span> <span class="nb">str</span><span class="p">())</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="k">for</span> <span class="n">port_info</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">:</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">port_info</span><span class="o">.</span><span class="n">port_lords</span><span class="p">:</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>                <span class="n">port_info</span><span class="o">.</span><span class="n">port_lords</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">not_used_port</span><span class="p">)</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">port</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">:</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="k">return</span> <span class="n">PortsIterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">,</span> <span class="n">statuses</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">range</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]],</span> <span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">:</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="k">return</span> <span class="n">PortsIterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">,</span> <span class="n">statuses</span><span class="p">,</span> <span class="n">desired_number_of_ports</span><span class="p">)</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>    
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]],</span> <span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">:</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="p">(</span><span class="n">protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">,</span> <span class="n">statuses</span><span class="p">,</span> <span class="n">desired_number_of_ports</span><span class="p">)</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a><span class="k">class</span> <span class="nc">UnaceptablePortsRangeTypeError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="k">pass</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a><span class="k">class</span> <span class="nc">PortsIterator</span><span class="p">:</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">used_ports</span><span class="p">:</span> <span class="n">UsedPorts</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]],</span> <span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">used_ports</span><span class="p">:</span> <span class="n">UsedPorts</span> <span class="o">=</span> <span class="n">used_ports</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span> <span class="o">=</span> <span class="n">protocol</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="p">:</span> <span class="nb">slice</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="n">port_or_range</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">slice</span><span class="p">):</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="n">port_or_range</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="o">*</span><span class="n">port_or_range</span><span class="p">)</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="k">raise</span> <span class="n">UnaceptablePortsRangeTypeError</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">statuses</span><span class="p">,</span> <span class="n">PortStatus</span><span class="p">):</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="n">statuses</span> <span class="o">=</span> <span class="p">{</span><span class="n">statuses</span><span class="p">}</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]]</span> <span class="o">=</span> <span class="n">statuses</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">desired_number_of_ports</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    <span class="k">def</span> <span class="fm">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="fm">__next__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="n">ports_range</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_impl</span><span class="p">()</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="k">return</span> <span class="n">ports_range</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>    
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>    <span class="k">def</span> <span class="nf">_iter_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">slice</span><span class="p">:</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">stop</span><span class="p">:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>            <span class="k">raise</span> <span class="ne">StopIteration</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">stop</span><span class="p">:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="n">result_range_stop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            <span class="k">for</span> <span class="n">offset</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">desired_number_of_ports</span><span class="p">):</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>                <span class="n">port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+</span> <span class="n">offset</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>                
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>                <span class="n">port_info</span><span class="p">:</span> <span class="n">PortInfo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">used_ports</span><span class="o">.</span><span class="n">table</span><span class="p">[</span><span class="n">port</span><span class="p">]</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>                <span class="n">port_statuses</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>                <span class="k">for</span> <span class="n">port_lord</span> <span class="ow">in</span> <span class="n">port_info</span><span class="o">.</span><span class="n">port_lords</span><span class="p">:</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>                    <span class="n">port_statuses</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">protocol</span><span class="o">.</span><span class="n">value</span><span class="p">])</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>                
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>                <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">port_statuses</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">statuses</span><span class="p">):</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>                    <span class="n">is_good</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>                    <span class="n">is_good</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>                
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>                <span class="k">if</span> <span class="n">is_good</span><span class="p">:</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>                    <span class="n">result_range_stop</span> <span class="o">=</span> <span class="n">port</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>                    <span class="n">result_range_stop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="n">port</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>                    <span class="k">break</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>            
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>            <span class="k">if</span> <span class="n">result_range_stop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>                <span class="k">return</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">first_port</span><span class="p">,</span> <span class="n">result_range_stop</span><span class="p">)</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="k">raise</span> <span class="ne">StopIteration</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>    
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_impl</span><span class="p">()</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="k">except</span> <span class="ne">StopIteration</span><span class="p">:</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>    <span class="k">def</span> <span class="nf">shift_only</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>    <span class="k">def</span> <span class="nf">shift</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="p">()</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>    <span class="k">def</span> <span class="nf">put_only</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="n">num</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="n">num</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="p">()</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a><span class="k">def</span> <span class="nf">purify_ports</span><span class="p">(</span><span class="n">ports_range</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]:</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>    <span class="n">start</span> <span class="o">=</span> <span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>    <span class="n">stop</span> <span class="o">=</span> <span class="n">ports_range</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>    <span class="k">if</span> <span class="n">start</span> <span class="o">==</span> <span class="n">stop</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>        <span class="k">return</span> <span class="n">start</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        <span class="k">return</span> <span class="n">start</span><span class="p">,</span> <span class="n">stop</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a><span class="k">def</span> <span class="nf">unify_ports</span><span class="p">(</span><span class="n">ports_range</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]:</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>    <span class="n">start</span> <span class="o">=</span> <span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>    <span class="n">stop</span> <span class="o">=</span> <span class="n">ports_range</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>    <span class="k">return</span> <span class="n">start</span><span class="p">,</span> <span class="n">stop</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>    
</span></pre></div>


            </section>
                <section id="PortStatus">
                            <input id="PortStatus-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PortStatus</span><wbr>(<span class="base">builtins.str</span>, <span class="base">enum.Enum</span>):

                <label class="view-source-button" for="PortStatus-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortStatus"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortStatus-45"><a href="#PortStatus-45"><span class="linenos">45</span></a><span class="k">class</span> <span class="nc">PortStatus</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
</span><span id="PortStatus-46"><a href="#PortStatus-46"><span class="linenos">46</span></a>    <span class="n">na</span> <span class="o">=</span> <span class="s1">&#39;N/A&#39;</span>                 <span class="c1"># In programming APIs (not in communication between hosts), requests a system-allocated (dynamic) port</span>
</span><span id="PortStatus-47"><a href="#PortStatus-47"><span class="linenos">47</span></a>    <span class="n">yes</span> <span class="o">=</span> <span class="s1">&#39;Yes&#39;</span>                <span class="c1"># Described protocol is assigned for this port by IANA and is standardized, specified, or widely used for such.</span>
</span><span id="PortStatus-48"><a href="#PortStatus-48"><span class="linenos">48</span></a>    <span class="n">unofficial</span> <span class="o">=</span> <span class="s1">&#39;Unofficial&#39;</span>  <span class="c1"># Described protocol is not assigned for this port by IANA but is standardized, specified, or widely used for such.</span>
</span><span id="PortStatus-49"><a href="#PortStatus-49"><span class="linenos">49</span></a>    <span class="n">assigned</span> <span class="o">=</span> <span class="s1">&#39;Assigned&#39;</span>      <span class="c1"># Described protocol is assigned by IANA for this port, but is not standardized, specified, or widely used for such.</span>
</span><span id="PortStatus-50"><a href="#PortStatus-50"><span class="linenos">50</span></a>    <span class="n">no</span> <span class="o">=</span> <span class="s1">&#39;No&#39;</span>                  <span class="c1"># Described protocol is not assigned by IANA, standardized, specified, or widely used for the port.</span>
</span><span id="PortStatus-51"><a href="#PortStatus-51"><span class="linenos">51</span></a>    <span class="n">reserved</span> <span class="o">=</span> <span class="s1">&#39;Reserved&#39;</span>      <span class="c1"># Port is reserved by IANA, generally to prevent collision having its previous use removed. The port number may be available for assignment upon request to IANA.</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="PortStatus.na" class="classattr">
                                <div class="attr variable">
            <span class="name">na</span>        =
<span class="default_value">&lt;<a href="#PortStatus.na">PortStatus.na</a>: &#39;N/A&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#PortStatus.na"></a>
    
    

                            </div>
                            <div id="PortStatus.yes" class="classattr">
                                <div class="attr variable">
            <span class="name">yes</span>        =
<span class="default_value">&lt;<a href="#PortStatus.yes">PortStatus.yes</a>: &#39;Yes&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#PortStatus.yes"></a>
    
    

                            </div>
                            <div id="PortStatus.unofficial" class="classattr">
                                <div class="attr variable">
            <span class="name">unofficial</span>        =
<span class="default_value">&lt;<a href="#PortStatus.unofficial">PortStatus.unofficial</a>: &#39;Unofficial&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#PortStatus.unofficial"></a>
    
    

                            </div>
                            <div id="PortStatus.assigned" class="classattr">
                                <div class="attr variable">
            <span class="name">assigned</span>        =
<span class="default_value">&lt;<a href="#PortStatus.assigned">PortStatus.assigned</a>: &#39;Assigned&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#PortStatus.assigned"></a>
    
    

                            </div>
                            <div id="PortStatus.no" class="classattr">
                                <div class="attr variable">
            <span class="name">no</span>        =
<span class="default_value">&lt;<a href="#PortStatus.no">PortStatus.no</a>: &#39;No&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#PortStatus.no"></a>
    
    

                            </div>
                            <div id="PortStatus.reserved" class="classattr">
                                <div class="attr variable">
            <span class="name">reserved</span>        =
<span class="default_value">&lt;<a href="#PortStatus.reserved">PortStatus.reserved</a>: &#39;Reserved&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#PortStatus.reserved"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="PortStatus.name" class="variable">name</dd>
                <dd id="PortStatus.value" class="variable">value</dd>

            </div>
            <div><dt>builtins.str</dt>
                                <dd id="PortStatus.encode" class="function">encode</dd>
                <dd id="PortStatus.replace" class="function">replace</dd>
                <dd id="PortStatus.split" class="function">split</dd>
                <dd id="PortStatus.rsplit" class="function">rsplit</dd>
                <dd id="PortStatus.join" class="function">join</dd>
                <dd id="PortStatus.capitalize" class="function">capitalize</dd>
                <dd id="PortStatus.casefold" class="function">casefold</dd>
                <dd id="PortStatus.title" class="function">title</dd>
                <dd id="PortStatus.center" class="function">center</dd>
                <dd id="PortStatus.count" class="function">count</dd>
                <dd id="PortStatus.expandtabs" class="function">expandtabs</dd>
                <dd id="PortStatus.find" class="function">find</dd>
                <dd id="PortStatus.partition" class="function">partition</dd>
                <dd id="PortStatus.index" class="function">index</dd>
                <dd id="PortStatus.ljust" class="function">ljust</dd>
                <dd id="PortStatus.lower" class="function">lower</dd>
                <dd id="PortStatus.lstrip" class="function">lstrip</dd>
                <dd id="PortStatus.rfind" class="function">rfind</dd>
                <dd id="PortStatus.rindex" class="function">rindex</dd>
                <dd id="PortStatus.rjust" class="function">rjust</dd>
                <dd id="PortStatus.rstrip" class="function">rstrip</dd>
                <dd id="PortStatus.rpartition" class="function">rpartition</dd>
                <dd id="PortStatus.splitlines" class="function">splitlines</dd>
                <dd id="PortStatus.strip" class="function">strip</dd>
                <dd id="PortStatus.swapcase" class="function">swapcase</dd>
                <dd id="PortStatus.translate" class="function">translate</dd>
                <dd id="PortStatus.upper" class="function">upper</dd>
                <dd id="PortStatus.startswith" class="function">startswith</dd>
                <dd id="PortStatus.endswith" class="function">endswith</dd>
                <dd id="PortStatus.isascii" class="function">isascii</dd>
                <dd id="PortStatus.islower" class="function">islower</dd>
                <dd id="PortStatus.isupper" class="function">isupper</dd>
                <dd id="PortStatus.istitle" class="function">istitle</dd>
                <dd id="PortStatus.isspace" class="function">isspace</dd>
                <dd id="PortStatus.isdecimal" class="function">isdecimal</dd>
                <dd id="PortStatus.isdigit" class="function">isdigit</dd>
                <dd id="PortStatus.isnumeric" class="function">isnumeric</dd>
                <dd id="PortStatus.isalpha" class="function">isalpha</dd>
                <dd id="PortStatus.isalnum" class="function">isalnum</dd>
                <dd id="PortStatus.isidentifier" class="function">isidentifier</dd>
                <dd id="PortStatus.isprintable" class="function">isprintable</dd>
                <dd id="PortStatus.zfill" class="function">zfill</dd>
                <dd id="PortStatus.format" class="function">format</dd>
                <dd id="PortStatus.format_map" class="function">format_map</dd>
                <dd id="PortStatus.maketrans" class="function">maketrans</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Table">
                            <input id="Table-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Table</span><wbr>(<span class="base">builtins.str</span>, <span class="base">enum.Enum</span>):

                <label class="view-source-button" for="Table-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Table"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Table-54"><a href="#Table-54"><span class="linenos">54</span></a><span class="k">class</span> <span class="nc">Table</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">Enum</span><span class="p">):</span>
</span><span id="Table-55"><a href="#Table-55"><span class="linenos">55</span></a>    <span class="n">system</span> <span class="o">=</span> <span class="s1">&#39;system&#39;</span>
</span><span id="Table-56"><a href="#Table-56"><span class="linenos">56</span></a>    <span class="n">user</span> <span class="o">=</span> <span class="s1">&#39;user&#39;</span>
</span><span id="Table-57"><a href="#Table-57"><span class="linenos">57</span></a>    <span class="n">ephemeral</span> <span class="o">=</span> <span class="s1">&#39;ephemeral&#39;</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="Table.system" class="classattr">
                                <div class="attr variable">
            <span class="name">system</span>        =
<span class="default_value">&lt;<a href="#Table.system">Table.system</a>: &#39;system&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#Table.system"></a>
    
    

                            </div>
                            <div id="Table.user" class="classattr">
                                <div class="attr variable">
            <span class="name">user</span>        =
<span class="default_value">&lt;<a href="#Table.user">Table.user</a>: &#39;user&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#Table.user"></a>
    
    

                            </div>
                            <div id="Table.ephemeral" class="classattr">
                                <div class="attr variable">
            <span class="name">ephemeral</span>        =
<span class="default_value">&lt;<a href="#Table.ephemeral">Table.ephemeral</a>: &#39;ephemeral&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#Table.ephemeral"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="Table.name" class="variable">name</dd>
                <dd id="Table.value" class="variable">value</dd>

            </div>
            <div><dt>builtins.str</dt>
                                <dd id="Table.encode" class="function">encode</dd>
                <dd id="Table.replace" class="function">replace</dd>
                <dd id="Table.split" class="function">split</dd>
                <dd id="Table.rsplit" class="function">rsplit</dd>
                <dd id="Table.join" class="function">join</dd>
                <dd id="Table.capitalize" class="function">capitalize</dd>
                <dd id="Table.casefold" class="function">casefold</dd>
                <dd id="Table.title" class="function">title</dd>
                <dd id="Table.center" class="function">center</dd>
                <dd id="Table.count" class="function">count</dd>
                <dd id="Table.expandtabs" class="function">expandtabs</dd>
                <dd id="Table.find" class="function">find</dd>
                <dd id="Table.partition" class="function">partition</dd>
                <dd id="Table.index" class="function">index</dd>
                <dd id="Table.ljust" class="function">ljust</dd>
                <dd id="Table.lower" class="function">lower</dd>
                <dd id="Table.lstrip" class="function">lstrip</dd>
                <dd id="Table.rfind" class="function">rfind</dd>
                <dd id="Table.rindex" class="function">rindex</dd>
                <dd id="Table.rjust" class="function">rjust</dd>
                <dd id="Table.rstrip" class="function">rstrip</dd>
                <dd id="Table.rpartition" class="function">rpartition</dd>
                <dd id="Table.splitlines" class="function">splitlines</dd>
                <dd id="Table.strip" class="function">strip</dd>
                <dd id="Table.swapcase" class="function">swapcase</dd>
                <dd id="Table.translate" class="function">translate</dd>
                <dd id="Table.upper" class="function">upper</dd>
                <dd id="Table.startswith" class="function">startswith</dd>
                <dd id="Table.endswith" class="function">endswith</dd>
                <dd id="Table.isascii" class="function">isascii</dd>
                <dd id="Table.islower" class="function">islower</dd>
                <dd id="Table.isupper" class="function">isupper</dd>
                <dd id="Table.istitle" class="function">istitle</dd>
                <dd id="Table.isspace" class="function">isspace</dd>
                <dd id="Table.isdecimal" class="function">isdecimal</dd>
                <dd id="Table.isdigit" class="function">isdigit</dd>
                <dd id="Table.isnumeric" class="function">isnumeric</dd>
                <dd id="Table.isalpha" class="function">isalpha</dd>
                <dd id="Table.isalnum" class="function">isalnum</dd>
                <dd id="Table.isidentifier" class="function">isidentifier</dd>
                <dd id="Table.isprintable" class="function">isprintable</dd>
                <dd id="Table.zfill" class="function">zfill</dd>
                <dd id="Table.format" class="function">format</dd>
                <dd id="Table.format_map" class="function">format_map</dd>
                <dd id="Table.maketrans" class="function">maketrans</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Protocol">
                            <input id="Protocol-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Protocol</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="Protocol-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Protocol"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Protocol-60"><a href="#Protocol-60"><span class="linenos">60</span></a><span class="k">class</span> <span class="nc">Protocol</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="Protocol-61"><a href="#Protocol-61"><span class="linenos">61</span></a>    <span class="n">tcp</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Protocol-62"><a href="#Protocol-62"><span class="linenos">62</span></a>    <span class="n">udp</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Protocol-63"><a href="#Protocol-63"><span class="linenos">63</span></a>    <span class="n">sctp</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="Protocol-64"><a href="#Protocol-64"><span class="linenos">64</span></a>    <span class="n">dccp</span> <span class="o">=</span> <span class="mi">3</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="Protocol.tcp" class="classattr">
                                <div class="attr variable">
            <span class="name">tcp</span>        =
<span class="default_value">&lt;<a href="#Protocol.tcp">Protocol.tcp</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#Protocol.tcp"></a>
    
    

                            </div>
                            <div id="Protocol.udp" class="classattr">
                                <div class="attr variable">
            <span class="name">udp</span>        =
<span class="default_value">&lt;<a href="#Protocol.udp">Protocol.udp</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#Protocol.udp"></a>
    
    

                            </div>
                            <div id="Protocol.sctp" class="classattr">
                                <div class="attr variable">
            <span class="name">sctp</span>        =
<span class="default_value">&lt;<a href="#Protocol.sctp">Protocol.sctp</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#Protocol.sctp"></a>
    
    

                            </div>
                            <div id="Protocol.dccp" class="classattr">
                                <div class="attr variable">
            <span class="name">dccp</span>        =
<span class="default_value">&lt;<a href="#Protocol.dccp">Protocol.dccp</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#Protocol.dccp"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="Protocol.name" class="variable">name</dd>
                <dd id="Protocol.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="purify_ports">
                            <input id="purify_ports-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">purify_ports</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">ports_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">slice</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="purify_ports-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#purify_ports"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="purify_ports-233"><a href="#purify_ports-233"><span class="linenos">233</span></a><span class="k">def</span> <span class="nf">purify_ports</span><span class="p">(</span><span class="n">ports_range</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]:</span>
</span><span id="purify_ports-234"><a href="#purify_ports-234"><span class="linenos">234</span></a>    <span class="n">start</span> <span class="o">=</span> <span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="purify_ports-235"><a href="#purify_ports-235"><span class="linenos">235</span></a>    <span class="n">stop</span> <span class="o">=</span> <span class="n">ports_range</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="purify_ports-236"><a href="#purify_ports-236"><span class="linenos">236</span></a>    <span class="k">if</span> <span class="n">start</span> <span class="o">==</span> <span class="n">stop</span><span class="p">:</span>
</span><span id="purify_ports-237"><a href="#purify_ports-237"><span class="linenos">237</span></a>        <span class="k">return</span> <span class="n">start</span>
</span><span id="purify_ports-238"><a href="#purify_ports-238"><span class="linenos">238</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="purify_ports-239"><a href="#purify_ports-239"><span class="linenos">239</span></a>        <span class="k">return</span> <span class="n">start</span><span class="p">,</span> <span class="n">stop</span>
</span></pre></div>


    

                </section>
                <section id="get_tables">
                            <input id="get_tables-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_tables</span><span class="signature pdoc-code condensed">(<span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="n"><a href="#Table">Table</a></span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="get_tables-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_tables"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_tables-79"><a href="#get_tables-79"><span class="linenos">79</span></a><span class="k">def</span> <span class="nf">get_tables</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Table</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">]]:</span>
</span><span id="get_tables-80"><a href="#get_tables-80"><span class="linenos">80</span></a>    <span class="k">global</span> <span class="n">_tables</span>
</span><span id="get_tables-81"><a href="#get_tables-81"><span class="linenos">81</span></a>    <span class="k">if</span> <span class="n">_tables</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_tables-82"><a href="#get_tables-82"><span class="linenos">82</span></a>        <span class="n">tables</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Table</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="get_tables-83"><a href="#get_tables-83"><span class="linenos">83</span></a>        <span class="k">for</span> <span class="n">table_name</span> <span class="ow">in</span> <span class="n">_known_tables_names</span><span class="p">:</span>
</span><span id="get_tables-84"><a href="#get_tables-84"><span class="linenos">84</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">path_relative_to_src</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;data/table_</span><span class="si">{</span><span class="n">table_name</span><span class="si">}</span><span class="s1">.pickle&#39;</span><span class="p">),</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="get_tables-85"><a href="#get_tables-85"><span class="linenos">85</span></a>                <span class="n">tables</span><span class="p">[</span><span class="n">Table</span><span class="p">(</span><span class="n">table_name</span><span class="p">)]</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="get_tables-86"><a href="#get_tables-86"><span class="linenos">86</span></a>
</span><span id="get_tables-87"><a href="#get_tables-87"><span class="linenos">87</span></a>        <span class="n">_tables</span> <span class="o">=</span> <span class="n">tables</span>
</span><span id="get_tables-88"><a href="#get_tables-88"><span class="linenos">88</span></a>    
</span><span id="get_tables-89"><a href="#get_tables-89"><span class="linenos">89</span></a>    <span class="k">return</span> <span class="n">_tables</span>
</span></pre></div>


    

                </section>
                <section id="used_ports">
                            <input id="used_ports-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">used_ports</span><span class="signature pdoc-code condensed">(<span class="return-annotation">) -> <span class="n"><a href="#UsedPorts">UsedPorts</a></span>:</span></span>

                <label class="view-source-button" for="used_ports-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#used_ports"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="used_ports-92"><a href="#used_ports-92"><span class="linenos">92</span></a><span class="k">def</span> <span class="nf">used_ports</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="s1">&#39;UsedPorts&#39;</span><span class="p">:</span>
</span><span id="used_ports-93"><a href="#used_ports-93"><span class="linenos">93</span></a>    <span class="k">global</span> <span class="n">_used_ports</span>
</span><span id="used_ports-94"><a href="#used_ports-94"><span class="linenos">94</span></a>    <span class="k">if</span> <span class="n">_used_ports</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="used_ports-95"><a href="#used_ports-95"><span class="linenos">95</span></a>        <span class="n">_used_ports</span> <span class="o">=</span> <span class="n">UsedPorts</span><span class="p">()</span>
</span><span id="used_ports-96"><a href="#used_ports-96"><span class="linenos">96</span></a>    
</span><span id="used_ports-97"><a href="#used_ports-97"><span class="linenos">97</span></a>    <span class="k">return</span> <span class="n">_used_ports</span>
</span></pre></div>


    

                </section>
                <section id="PortLord">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PortLord</span><wbr>(<span class="base">builtins.tuple</span>):

        
    </div>
    <a class="headerlink" href="#PortLord"></a>
    
            <div class="docstring"><p>PortLord(tcp, udp, sctp, dccp, description)</p>
</div>


                            <div id="PortLord.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">PortLord</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">tcp</span>, </span><span class="param"><span class="n">udp</span>, </span><span class="param"><span class="n">sctp</span>, </span><span class="param"><span class="n">dccp</span>, </span><span class="param"><span class="n">description</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#PortLord.__init__"></a>
    
            <div class="docstring"><p>Create new instance of PortLord(tcp, udp, sctp, dccp, description)</p>
</div>


                            </div>
                            <div id="PortLord.tcp" class="classattr">
                                <div class="attr variable">
            <span class="name">tcp</span>

        
    </div>
    <a class="headerlink" href="#PortLord.tcp"></a>
    
            <div class="docstring"><p>Alias for field number 0</p>
</div>


                            </div>
                            <div id="PortLord.udp" class="classattr">
                                <div class="attr variable">
            <span class="name">udp</span>

        
    </div>
    <a class="headerlink" href="#PortLord.udp"></a>
    
            <div class="docstring"><p>Alias for field number 1</p>
</div>


                            </div>
                            <div id="PortLord.sctp" class="classattr">
                                <div class="attr variable">
            <span class="name">sctp</span>

        
    </div>
    <a class="headerlink" href="#PortLord.sctp"></a>
    
            <div class="docstring"><p>Alias for field number 2</p>
</div>


                            </div>
                            <div id="PortLord.dccp" class="classattr">
                                <div class="attr variable">
            <span class="name">dccp</span>

        
    </div>
    <a class="headerlink" href="#PortLord.dccp"></a>
    
            <div class="docstring"><p>Alias for field number 3</p>
</div>


                            </div>
                            <div id="PortLord.description" class="classattr">
                                <div class="attr variable">
            <span class="name">description</span>

        
    </div>
    <a class="headerlink" href="#PortLord.description"></a>
    
            <div class="docstring"><p>Alias for field number 4</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.tuple</dt>
                                <dd id="PortLord.index" class="function">index</dd>
                <dd id="PortLord.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="PortInfo">
                            <input id="PortInfo-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PortInfo</span>:

                <label class="view-source-button" for="PortInfo-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortInfo"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortInfo-103"><a href="#PortInfo-103"><span class="linenos">103</span></a><span class="k">class</span> <span class="nc">PortInfo</span><span class="p">:</span>
</span><span id="PortInfo-104"><a href="#PortInfo-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">port_lords</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n">PortLord</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortInfo-105"><a href="#PortInfo-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">port</span>
</span><span id="PortInfo-106"><a href="#PortInfo-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span> <span class="o">=</span> <span class="n">port_lords</span> <span class="ow">or</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="PortInfo-107"><a href="#PortInfo-107"><span class="linenos">107</span></a>    
</span><span id="PortInfo-108"><a href="#PortInfo-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">port_lord</span><span class="p">:</span> <span class="n">PortLord</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="PortInfo-109"><a href="#PortInfo-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">)</span>
</span><span id="PortInfo-110"><a href="#PortInfo-110"><span class="linenos">110</span></a>        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="PortInfo.__init__" class="classattr">
                                        <input id="PortInfo.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">PortInfo</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">port</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">port_lords</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n"><a href="#PortLord">PortLord</a></span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="PortInfo.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortInfo.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortInfo.__init__-104"><a href="#PortInfo.__init__-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">port</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">port_lords</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n">PortLord</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortInfo.__init__-105"><a href="#PortInfo.__init__-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">port</span>
</span><span id="PortInfo.__init__-106"><a href="#PortInfo.__init__-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span> <span class="o">=</span> <span class="n">port_lords</span> <span class="ow">or</span> <span class="nb">set</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="PortInfo.port" class="classattr">
                                <div class="attr variable">
            <span class="name">port</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#PortInfo.port"></a>
    
    

                            </div>
                            <div id="PortInfo.port_lords" class="classattr">
                                <div class="attr variable">
            <span class="name">port_lords</span>

        
    </div>
    <a class="headerlink" href="#PortInfo.port_lords"></a>
    
    

                            </div>
                            <div id="PortInfo.add" class="classattr">
                                        <input id="PortInfo.add-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">port_lord</span><span class="p">:</span> <span class="n"><a href="#PortLord">PortLord</a></span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="PortInfo.add-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortInfo.add"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortInfo.add-108"><a href="#PortInfo.add-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">port_lord</span><span class="p">:</span> <span class="n">PortLord</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="PortInfo.add-109"><a href="#PortInfo.add-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">)</span>
</span><span id="PortInfo.add-110"><a href="#PortInfo.add-110"><span class="linenos">110</span></a>        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">port_lords</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="UsedPorts">
                            <input id="UsedPorts-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UsedPorts</span>:

                <label class="view-source-button" for="UsedPorts-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UsedPorts"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UsedPorts-113"><a href="#UsedPorts-113"><span class="linenos">113</span></a><span class="k">class</span> <span class="nc">UsedPorts</span><span class="p">:</span>
</span><span id="UsedPorts-114"><a href="#UsedPorts-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="UsedPorts-115"><a href="#UsedPorts-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">PortInfo</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">([</span><span class="n">PortInfo</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">65536</span><span class="p">)])</span>
</span><span id="UsedPorts-116"><a href="#UsedPorts-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tables</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="UsedPorts-117"><a href="#UsedPorts-117"><span class="linenos">117</span></a>            <span class="n">Table</span><span class="o">.</span><span class="n">system</span><span class="p">:</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1024</span><span class="p">),</span>
</span><span id="UsedPorts-118"><a href="#UsedPorts-118"><span class="linenos">118</span></a>            <span class="n">Table</span><span class="o">.</span><span class="n">user</span><span class="p">:</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">1024</span><span class="p">,</span> <span class="mi">49152</span><span class="p">),</span>
</span><span id="UsedPorts-119"><a href="#UsedPorts-119"><span class="linenos">119</span></a>            <span class="n">Table</span><span class="o">.</span><span class="n">ephemeral</span><span class="p">:</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">49152</span><span class="p">,</span> <span class="mi">65536</span><span class="p">),</span>
</span><span id="UsedPorts-120"><a href="#UsedPorts-120"><span class="linenos">120</span></a>        <span class="p">}</span>
</span><span id="UsedPorts-121"><a href="#UsedPorts-121"><span class="linenos">121</span></a>        <span class="n">raw_tables</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Table</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">]]</span> <span class="o">=</span> <span class="n">get_tables</span><span class="p">()</span>
</span><span id="UsedPorts-122"><a href="#UsedPorts-122"><span class="linenos">122</span></a>        <span class="k">for</span> <span class="n">table_name</span><span class="p">,</span> <span class="n">raw_table</span> <span class="ow">in</span> <span class="n">raw_tables</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="UsedPorts-123"><a href="#UsedPorts-123"><span class="linenos">123</span></a>            <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">raw_table</span><span class="p">:</span>
</span><span id="UsedPorts-124"><a href="#UsedPorts-124"><span class="linenos">124</span></a>                <span class="n">port_or_range</span><span class="p">,</span> <span class="n">tcp</span><span class="p">,</span> <span class="n">udp</span><span class="p">,</span> <span class="n">sctp</span><span class="p">,</span> <span class="n">dccp</span><span class="p">,</span> <span class="n">description</span> <span class="o">=</span> <span class="n">row</span>
</span><span id="UsedPorts-125"><a href="#UsedPorts-125"><span class="linenos">125</span></a>                <span class="n">port_lord</span> <span class="o">=</span> <span class="n">PortLord</span><span class="p">(</span><span class="n">_purify_item</span><span class="p">(</span><span class="n">tcp</span><span class="p">),</span> <span class="n">_purify_item</span><span class="p">(</span><span class="n">udp</span><span class="p">),</span> <span class="n">_purify_item</span><span class="p">(</span><span class="n">sctp</span><span class="p">),</span> <span class="n">_purify_item</span><span class="p">(</span><span class="n">dccp</span><span class="p">),</span> <span class="n">description</span><span class="p">)</span>
</span><span id="UsedPorts-126"><a href="#UsedPorts-126"><span class="linenos">126</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="UsedPorts-127"><a href="#UsedPorts-127"><span class="linenos">127</span></a>                    <span class="k">for</span> <span class="n">port</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="nb">int</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="UsedPorts-128"><a href="#UsedPorts-128"><span class="linenos">128</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">[</span><span class="n">port</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">)</span>
</span><span id="UsedPorts-129"><a href="#UsedPorts-129"><span class="linenos">129</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="UsedPorts-130"><a href="#UsedPorts-130"><span class="linenos">130</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">)]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">)</span>
</span><span id="UsedPorts-131"><a href="#UsedPorts-131"><span class="linenos">131</span></a>        
</span><span id="UsedPorts-132"><a href="#UsedPorts-132"><span class="linenos">132</span></a>        <span class="n">not_used_port</span> <span class="o">=</span> <span class="n">PortLord</span><span class="p">(</span><span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span><span class="p">,</span> <span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span><span class="p">,</span> <span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span><span class="p">,</span> <span class="n">PortStatus</span><span class="o">.</span><span class="n">no</span><span class="p">,</span> <span class="nb">str</span><span class="p">())</span>
</span><span id="UsedPorts-133"><a href="#UsedPorts-133"><span class="linenos">133</span></a>        <span class="k">for</span> <span class="n">port_info</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">:</span>
</span><span id="UsedPorts-134"><a href="#UsedPorts-134"><span class="linenos">134</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">port_info</span><span class="o">.</span><span class="n">port_lords</span><span class="p">:</span>
</span><span id="UsedPorts-135"><a href="#UsedPorts-135"><span class="linenos">135</span></a>                <span class="n">port_info</span><span class="o">.</span><span class="n">port_lords</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">not_used_port</span><span class="p">)</span>
</span><span id="UsedPorts-136"><a href="#UsedPorts-136"><span class="linenos">136</span></a>    
</span><span id="UsedPorts-137"><a href="#UsedPorts-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">port</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">:</span>
</span><span id="UsedPorts-138"><a href="#UsedPorts-138"><span class="linenos">138</span></a>        <span class="k">return</span> <span class="n">PortsIterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">,</span> <span class="n">statuses</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="UsedPorts-139"><a href="#UsedPorts-139"><span class="linenos">139</span></a>    
</span><span id="UsedPorts-140"><a href="#UsedPorts-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">range</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]],</span> <span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">:</span>
</span><span id="UsedPorts-141"><a href="#UsedPorts-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="n">PortsIterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">,</span> <span class="n">statuses</span><span class="p">,</span> <span class="n">desired_number_of_ports</span><span class="p">)</span>
</span><span id="UsedPorts-142"><a href="#UsedPorts-142"><span class="linenos">142</span></a>    
</span><span id="UsedPorts-143"><a href="#UsedPorts-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]],</span> <span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">:</span>
</span><span id="UsedPorts-144"><a href="#UsedPorts-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="p">(</span><span class="n">protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">,</span> <span class="n">statuses</span><span class="p">,</span> <span class="n">desired_number_of_ports</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="UsedPorts.table" class="classattr">
                                <div class="attr variable">
            <span class="name">table</span><span class="annotation">: List[<a href="#PortInfo">PortInfo</a>]</span>

        
    </div>
    <a class="headerlink" href="#UsedPorts.table"></a>
    
    

                            </div>
                            <div id="UsedPorts.tables" class="classattr">
                                <div class="attr variable">
            <span class="name">tables</span>

        
    </div>
    <a class="headerlink" href="#UsedPorts.tables"></a>
    
    

                            </div>
                            <div id="UsedPorts.port" class="classattr">
                                        <input id="UsedPorts.port-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">port</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">protocol</span><span class="p">:</span> <span class="n"><a href="#Protocol">Protocol</a></span>,</span><span class="param">	<span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>,</span><span class="param">	<span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#PortStatus">PortStatus</a></span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n"><a href="#PortStatus">PortStatus</a></span><span class="p">]]</span></span><span class="return-annotation">) -> <span class="n"><a href="#PortsIterator">PortsIterator</a></span>:</span></span>

                <label class="view-source-button" for="UsedPorts.port-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UsedPorts.port"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UsedPorts.port-137"><a href="#UsedPorts.port-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">port</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">:</span>
</span><span id="UsedPorts.port-138"><a href="#UsedPorts.port-138"><span class="linenos">138</span></a>        <span class="k">return</span> <span class="n">PortsIterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">,</span> <span class="n">statuses</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="UsedPorts.range" class="classattr">
                                        <input id="UsedPorts.range-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">range</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">protocol</span><span class="p">:</span> <span class="n"><a href="#Protocol">Protocol</a></span>,</span><span class="param">	<span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>,</span><span class="param">	<span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#PortStatus">PortStatus</a></span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n"><a href="#PortStatus">PortStatus</a></span><span class="p">]]</span>,</span><span class="param">	<span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="n"><a href="#PortsIterator">PortsIterator</a></span>:</span></span>

                <label class="view-source-button" for="UsedPorts.range-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UsedPorts.range"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UsedPorts.range-140"><a href="#UsedPorts.range-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">range</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]],</span> <span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PortsIterator&#39;</span><span class="p">:</span>
</span><span id="UsedPorts.range-141"><a href="#UsedPorts.range-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="n">PortsIterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">,</span> <span class="n">statuses</span><span class="p">,</span> <span class="n">desired_number_of_ports</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="PortsIterator">
                            <input id="PortsIterator-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PortsIterator</span>:

                <label class="view-source-button" for="PortsIterator-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortsIterator"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortsIterator-151"><a href="#PortsIterator-151"><span class="linenos">151</span></a><span class="k">class</span> <span class="nc">PortsIterator</span><span class="p">:</span>
</span><span id="PortsIterator-152"><a href="#PortsIterator-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">used_ports</span><span class="p">:</span> <span class="n">UsedPorts</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]],</span> <span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortsIterator-153"><a href="#PortsIterator-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">used_ports</span><span class="p">:</span> <span class="n">UsedPorts</span> <span class="o">=</span> <span class="n">used_ports</span>
</span><span id="PortsIterator-154"><a href="#PortsIterator-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span> <span class="o">=</span> <span class="n">protocol</span>
</span><span id="PortsIterator-155"><a href="#PortsIterator-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="p">:</span> <span class="nb">slice</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="PortsIterator-156"><a href="#PortsIterator-156"><span class="linenos">156</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="PortsIterator-157"><a href="#PortsIterator-157"><span class="linenos">157</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="n">port_or_range</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="PortsIterator-158"><a href="#PortsIterator-158"><span class="linenos">158</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">slice</span><span class="p">):</span>
</span><span id="PortsIterator-159"><a href="#PortsIterator-159"><span class="linenos">159</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="n">port_or_range</span>
</span><span id="PortsIterator-160"><a href="#PortsIterator-160"><span class="linenos">160</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="PortsIterator-161"><a href="#PortsIterator-161"><span class="linenos">161</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="o">*</span><span class="n">port_or_range</span><span class="p">)</span>
</span><span id="PortsIterator-162"><a href="#PortsIterator-162"><span class="linenos">162</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PortsIterator-163"><a href="#PortsIterator-163"><span class="linenos">163</span></a>            <span class="k">raise</span> <span class="n">UnaceptablePortsRangeTypeError</span>
</span><span id="PortsIterator-164"><a href="#PortsIterator-164"><span class="linenos">164</span></a>        
</span><span id="PortsIterator-165"><a href="#PortsIterator-165"><span class="linenos">165</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">statuses</span><span class="p">,</span> <span class="n">PortStatus</span><span class="p">):</span>
</span><span id="PortsIterator-166"><a href="#PortsIterator-166"><span class="linenos">166</span></a>            <span class="n">statuses</span> <span class="o">=</span> <span class="p">{</span><span class="n">statuses</span><span class="p">}</span>
</span><span id="PortsIterator-167"><a href="#PortsIterator-167"><span class="linenos">167</span></a>        
</span><span id="PortsIterator-168"><a href="#PortsIterator-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]]</span> <span class="o">=</span> <span class="n">statuses</span>
</span><span id="PortsIterator-169"><a href="#PortsIterator-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">desired_number_of_ports</span>
</span><span id="PortsIterator-170"><a href="#PortsIterator-170"><span class="linenos">170</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="PortsIterator-171"><a href="#PortsIterator-171"><span class="linenos">171</span></a>
</span><span id="PortsIterator-172"><a href="#PortsIterator-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="fm">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="PortsIterator-173"><a href="#PortsIterator-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="PortsIterator-174"><a href="#PortsIterator-174"><span class="linenos">174</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="PortsIterator-175"><a href="#PortsIterator-175"><span class="linenos">175</span></a>
</span><span id="PortsIterator-176"><a href="#PortsIterator-176"><span class="linenos">176</span></a>    <span class="k">def</span> <span class="fm">__next__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="PortsIterator-177"><a href="#PortsIterator-177"><span class="linenos">177</span></a>        <span class="n">ports_range</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_impl</span><span class="p">()</span>
</span><span id="PortsIterator-178"><a href="#PortsIterator-178"><span class="linenos">178</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="PortsIterator-179"><a href="#PortsIterator-179"><span class="linenos">179</span></a>        <span class="k">return</span> <span class="n">ports_range</span>
</span><span id="PortsIterator-180"><a href="#PortsIterator-180"><span class="linenos">180</span></a>    
</span><span id="PortsIterator-181"><a href="#PortsIterator-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">_iter_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">slice</span><span class="p">:</span>
</span><span id="PortsIterator-182"><a href="#PortsIterator-182"><span class="linenos">182</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">stop</span><span class="p">:</span>
</span><span id="PortsIterator-183"><a href="#PortsIterator-183"><span class="linenos">183</span></a>            <span class="k">raise</span> <span class="ne">StopIteration</span>
</span><span id="PortsIterator-184"><a href="#PortsIterator-184"><span class="linenos">184</span></a>        
</span><span id="PortsIterator-185"><a href="#PortsIterator-185"><span class="linenos">185</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">stop</span><span class="p">:</span>
</span><span id="PortsIterator-186"><a href="#PortsIterator-186"><span class="linenos">186</span></a>            <span class="n">result_range_stop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="PortsIterator-187"><a href="#PortsIterator-187"><span class="linenos">187</span></a>            <span class="k">for</span> <span class="n">offset</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">desired_number_of_ports</span><span class="p">):</span>
</span><span id="PortsIterator-188"><a href="#PortsIterator-188"><span class="linenos">188</span></a>                <span class="n">port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+</span> <span class="n">offset</span>
</span><span id="PortsIterator-189"><a href="#PortsIterator-189"><span class="linenos">189</span></a>                
</span><span id="PortsIterator-190"><a href="#PortsIterator-190"><span class="linenos">190</span></a>                <span class="n">port_info</span><span class="p">:</span> <span class="n">PortInfo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">used_ports</span><span class="o">.</span><span class="n">table</span><span class="p">[</span><span class="n">port</span><span class="p">]</span>
</span><span id="PortsIterator-191"><a href="#PortsIterator-191"><span class="linenos">191</span></a>                <span class="n">port_statuses</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="PortsIterator-192"><a href="#PortsIterator-192"><span class="linenos">192</span></a>                <span class="k">for</span> <span class="n">port_lord</span> <span class="ow">in</span> <span class="n">port_info</span><span class="o">.</span><span class="n">port_lords</span><span class="p">:</span>
</span><span id="PortsIterator-193"><a href="#PortsIterator-193"><span class="linenos">193</span></a>                    <span class="n">port_statuses</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">port_lord</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">protocol</span><span class="o">.</span><span class="n">value</span><span class="p">])</span>
</span><span id="PortsIterator-194"><a href="#PortsIterator-194"><span class="linenos">194</span></a>                
</span><span id="PortsIterator-195"><a href="#PortsIterator-195"><span class="linenos">195</span></a>                <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">port_statuses</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">statuses</span><span class="p">):</span>
</span><span id="PortsIterator-196"><a href="#PortsIterator-196"><span class="linenos">196</span></a>                    <span class="n">is_good</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="PortsIterator-197"><a href="#PortsIterator-197"><span class="linenos">197</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="PortsIterator-198"><a href="#PortsIterator-198"><span class="linenos">198</span></a>                    <span class="n">is_good</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="PortsIterator-199"><a href="#PortsIterator-199"><span class="linenos">199</span></a>                
</span><span id="PortsIterator-200"><a href="#PortsIterator-200"><span class="linenos">200</span></a>                <span class="k">if</span> <span class="n">is_good</span><span class="p">:</span>
</span><span id="PortsIterator-201"><a href="#PortsIterator-201"><span class="linenos">201</span></a>                    <span class="n">result_range_stop</span> <span class="o">=</span> <span class="n">port</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="PortsIterator-202"><a href="#PortsIterator-202"><span class="linenos">202</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="PortsIterator-203"><a href="#PortsIterator-203"><span class="linenos">203</span></a>                    <span class="n">result_range_stop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="PortsIterator-204"><a href="#PortsIterator-204"><span class="linenos">204</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="n">port</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="PortsIterator-205"><a href="#PortsIterator-205"><span class="linenos">205</span></a>                    <span class="k">break</span>
</span><span id="PortsIterator-206"><a href="#PortsIterator-206"><span class="linenos">206</span></a>            
</span><span id="PortsIterator-207"><a href="#PortsIterator-207"><span class="linenos">207</span></a>            <span class="k">if</span> <span class="n">result_range_stop</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortsIterator-208"><a href="#PortsIterator-208"><span class="linenos">208</span></a>                <span class="k">return</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">first_port</span><span class="p">,</span> <span class="n">result_range_stop</span><span class="p">)</span>
</span><span id="PortsIterator-209"><a href="#PortsIterator-209"><span class="linenos">209</span></a>        
</span><span id="PortsIterator-210"><a href="#PortsIterator-210"><span class="linenos">210</span></a>        <span class="k">raise</span> <span class="ne">StopIteration</span>
</span><span id="PortsIterator-211"><a href="#PortsIterator-211"><span class="linenos">211</span></a>    
</span><span id="PortsIterator-212"><a href="#PortsIterator-212"><span class="linenos">212</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="PortsIterator-213"><a href="#PortsIterator-213"><span class="linenos">213</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="PortsIterator-214"><a href="#PortsIterator-214"><span class="linenos">214</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_impl</span><span class="p">()</span>
</span><span id="PortsIterator-215"><a href="#PortsIterator-215"><span class="linenos">215</span></a>        <span class="k">except</span> <span class="ne">StopIteration</span><span class="p">:</span>
</span><span id="PortsIterator-216"><a href="#PortsIterator-216"><span class="linenos">216</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="PortsIterator-217"><a href="#PortsIterator-217"><span class="linenos">217</span></a>
</span><span id="PortsIterator-218"><a href="#PortsIterator-218"><span class="linenos">218</span></a>    <span class="k">def</span> <span class="nf">shift_only</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortsIterator-219"><a href="#PortsIterator-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="PortsIterator-220"><a href="#PortsIterator-220"><span class="linenos">220</span></a>
</span><span id="PortsIterator-221"><a href="#PortsIterator-221"><span class="linenos">221</span></a>    <span class="k">def</span> <span class="nf">shift</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="PortsIterator-222"><a href="#PortsIterator-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="PortsIterator-223"><a href="#PortsIterator-223"><span class="linenos">223</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="p">()</span>
</span><span id="PortsIterator-224"><a href="#PortsIterator-224"><span class="linenos">224</span></a>
</span><span id="PortsIterator-225"><a href="#PortsIterator-225"><span class="linenos">225</span></a>    <span class="k">def</span> <span class="nf">put_only</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortsIterator-226"><a href="#PortsIterator-226"><span class="linenos">226</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="n">num</span>
</span><span id="PortsIterator-227"><a href="#PortsIterator-227"><span class="linenos">227</span></a>
</span><span id="PortsIterator-228"><a href="#PortsIterator-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="PortsIterator-229"><a href="#PortsIterator-229"><span class="linenos">229</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="n">num</span>
</span><span id="PortsIterator-230"><a href="#PortsIterator-230"><span class="linenos">230</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="PortsIterator.__init__" class="classattr">
                                        <input id="PortsIterator.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">PortsIterator</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">used_ports</span><span class="p">:</span> <span class="n"><a href="#UsedPorts">UsedPorts</a></span>,</span><span class="param">	<span class="n">protocol</span><span class="p">:</span> <span class="n"><a href="#Protocol">Protocol</a></span>,</span><span class="param">	<span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>,</span><span class="param">	<span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#PortStatus">PortStatus</a></span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n"><a href="#PortStatus">PortStatus</a></span><span class="p">]]</span>,</span><span class="param">	<span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span></span>)</span>

                <label class="view-source-button" for="PortsIterator.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortsIterator.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortsIterator.__init__-152"><a href="#PortsIterator.__init__-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">used_ports</span><span class="p">:</span> <span class="n">UsedPorts</span><span class="p">,</span> <span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span><span class="p">,</span> <span class="n">port_or_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]],</span> <span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortsIterator.__init__-153"><a href="#PortsIterator.__init__-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">used_ports</span><span class="p">:</span> <span class="n">UsedPorts</span> <span class="o">=</span> <span class="n">used_ports</span>
</span><span id="PortsIterator.__init__-154"><a href="#PortsIterator.__init__-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">protocol</span><span class="p">:</span> <span class="n">Protocol</span> <span class="o">=</span> <span class="n">protocol</span>
</span><span id="PortsIterator.__init__-155"><a href="#PortsIterator.__init__-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="p">:</span> <span class="nb">slice</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="PortsIterator.__init__-156"><a href="#PortsIterator.__init__-156"><span class="linenos">156</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="PortsIterator.__init__-157"><a href="#PortsIterator.__init__-157"><span class="linenos">157</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="n">port_or_range</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="PortsIterator.__init__-158"><a href="#PortsIterator.__init__-158"><span class="linenos">158</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">slice</span><span class="p">):</span>
</span><span id="PortsIterator.__init__-159"><a href="#PortsIterator.__init__-159"><span class="linenos">159</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="n">port_or_range</span>
</span><span id="PortsIterator.__init__-160"><a href="#PortsIterator.__init__-160"><span class="linenos">160</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">port_or_range</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="PortsIterator.__init__-161"><a href="#PortsIterator.__init__-161"><span class="linenos">161</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="o">*</span><span class="n">port_or_range</span><span class="p">)</span>
</span><span id="PortsIterator.__init__-162"><a href="#PortsIterator.__init__-162"><span class="linenos">162</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PortsIterator.__init__-163"><a href="#PortsIterator.__init__-163"><span class="linenos">163</span></a>            <span class="k">raise</span> <span class="n">UnaceptablePortsRangeTypeError</span>
</span><span id="PortsIterator.__init__-164"><a href="#PortsIterator.__init__-164"><span class="linenos">164</span></a>        
</span><span id="PortsIterator.__init__-165"><a href="#PortsIterator.__init__-165"><span class="linenos">165</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">statuses</span><span class="p">,</span> <span class="n">PortStatus</span><span class="p">):</span>
</span><span id="PortsIterator.__init__-166"><a href="#PortsIterator.__init__-166"><span class="linenos">166</span></a>            <span class="n">statuses</span> <span class="o">=</span> <span class="p">{</span><span class="n">statuses</span><span class="p">}</span>
</span><span id="PortsIterator.__init__-167"><a href="#PortsIterator.__init__-167"><span class="linenos">167</span></a>        
</span><span id="PortsIterator.__init__-168"><a href="#PortsIterator.__init__-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">statuses</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">PortStatus</span><span class="p">]]</span> <span class="o">=</span> <span class="n">statuses</span>
</span><span id="PortsIterator.__init__-169"><a href="#PortsIterator.__init__-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">desired_number_of_ports</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">desired_number_of_ports</span>
</span><span id="PortsIterator.__init__-170"><a href="#PortsIterator.__init__-170"><span class="linenos">170</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span></pre></div>


    

                            </div>
                            <div id="PortsIterator.used_ports" class="classattr">
                                <div class="attr variable">
            <span class="name">used_ports</span><span class="annotation">: <a href="#UsedPorts">UsedPorts</a></span>

        
    </div>
    <a class="headerlink" href="#PortsIterator.used_ports"></a>
    
    

                            </div>
                            <div id="PortsIterator.protocol" class="classattr">
                                <div class="attr variable">
            <span class="name">protocol</span><span class="annotation">: <a href="#Protocol">Protocol</a></span>

        
    </div>
    <a class="headerlink" href="#PortsIterator.protocol"></a>
    
    

                            </div>
                            <div id="PortsIterator.ports_range" class="classattr">
                                <div class="attr variable">
            <span class="name">ports_range</span><span class="annotation">: slice</span>

        
    </div>
    <a class="headerlink" href="#PortsIterator.ports_range"></a>
    
    

                            </div>
                            <div id="PortsIterator.statuses" class="classattr">
                                <div class="attr variable">
            <span class="name">statuses</span><span class="annotation">: Union[<a href="#PortStatus">PortStatus</a>, Set[<a href="#PortStatus">PortStatus</a>]]</span>

        
    </div>
    <a class="headerlink" href="#PortsIterator.statuses"></a>
    
    

                            </div>
                            <div id="PortsIterator.desired_number_of_ports" class="classattr">
                                <div class="attr variable">
            <span class="name">desired_number_of_ports</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#PortsIterator.desired_number_of_ports"></a>
    
    

                            </div>
                            <div id="PortsIterator.first_port" class="classattr">
                                <div class="attr variable">
            <span class="name">first_port</span>

        
    </div>
    <a class="headerlink" href="#PortsIterator.first_port"></a>
    
    

                            </div>
                            <div id="PortsIterator.shift_only" class="classattr">
                                        <input id="PortsIterator.shift_only-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">shift_only</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="PortsIterator.shift_only-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortsIterator.shift_only"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortsIterator.shift_only-218"><a href="#PortsIterator.shift_only-218"><span class="linenos">218</span></a>    <span class="k">def</span> <span class="nf">shift_only</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortsIterator.shift_only-219"><a href="#PortsIterator.shift_only-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+=</span> <span class="n">num</span>
</span></pre></div>


    

                            </div>
                            <div id="PortsIterator.shift" class="classattr">
                                        <input id="PortsIterator.shift-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">shift</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="nb">slice</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="PortsIterator.shift-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortsIterator.shift"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortsIterator.shift-221"><a href="#PortsIterator.shift-221"><span class="linenos">221</span></a>    <span class="k">def</span> <span class="nf">shift</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="PortsIterator.shift-222"><a href="#PortsIterator.shift-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="PortsIterator.shift-223"><a href="#PortsIterator.shift-223"><span class="linenos">223</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="PortsIterator.put_only" class="classattr">
                                        <input id="PortsIterator.put_only-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_only</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">num</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="PortsIterator.put_only-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortsIterator.put_only"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortsIterator.put_only-225"><a href="#PortsIterator.put_only-225"><span class="linenos">225</span></a>    <span class="k">def</span> <span class="nf">put_only</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PortsIterator.put_only-226"><a href="#PortsIterator.put_only-226"><span class="linenos">226</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="n">num</span>
</span></pre></div>


    

                            </div>
                            <div id="PortsIterator.put" class="classattr">
                                        <input id="PortsIterator.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">num</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="nb">slice</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="PortsIterator.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PortsIterator.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PortsIterator.put-228"><a href="#PortsIterator.put-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="PortsIterator.put-229"><a href="#PortsIterator.put-229"><span class="linenos">229</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">first_port</span> <span class="o">=</span> <span class="n">num</span>
</span><span id="PortsIterator.put-230"><a href="#PortsIterator.put-230"><span class="linenos">230</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="unify_ports">
                            <input id="unify_ports-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">unify_ports</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">ports_range</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">slice</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="unify_ports-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#unify_ports"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="unify_ports-242"><a href="#unify_ports-242"><span class="linenos">242</span></a><span class="k">def</span> <span class="nf">unify_ports</span><span class="p">(</span><span class="n">ports_range</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]:</span>
</span><span id="unify_ports-243"><a href="#unify_ports-243"><span class="linenos">243</span></a>    <span class="n">start</span> <span class="o">=</span> <span class="n">ports_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="unify_ports-244"><a href="#unify_ports-244"><span class="linenos">244</span></a>    <span class="n">stop</span> <span class="o">=</span> <span class="n">ports_range</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="unify_ports-245"><a href="#unify_ports-245"><span class="linenos">245</span></a>    <span class="k">return</span> <span class="n">start</span><span class="p">,</span> <span class="n">stop</span>
</span></pre></div>


    

                </section>
                <section id="UnaceptablePortsRangeTypeError">
                            <input id="UnaceptablePortsRangeTypeError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UnaceptablePortsRangeTypeError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="UnaceptablePortsRangeTypeError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UnaceptablePortsRangeTypeError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UnaceptablePortsRangeTypeError-147"><a href="#UnaceptablePortsRangeTypeError-147"><span class="linenos">147</span></a><span class="k">class</span> <span class="nc">UnaceptablePortsRangeTypeError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="UnaceptablePortsRangeTypeError-148"><a href="#UnaceptablePortsRangeTypeError-148"><span class="linenos">148</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="UnaceptablePortsRangeTypeError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="UnaceptablePortsRangeTypeError.with_traceback" class="function">with_traceback</dd>
                <dd id="UnaceptablePortsRangeTypeError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>