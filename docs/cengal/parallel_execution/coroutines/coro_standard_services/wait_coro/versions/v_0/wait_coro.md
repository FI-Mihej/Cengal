---
title: wait_coro
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.wait_coro<wbr>.versions<wbr>.v_0<wbr>.wait_coro    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-wait_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-wait_coro-view-source"><span>View Source</span></label>

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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;WaitCoro&#39;</span><span class="p">,</span> <span class="s1">&#39;PutSingleCoroParams&#39;</span><span class="p">,</span> <span class="s1">&#39;PSCP&#39;</span><span class="p">,</span> <span class="s1">&#39;WaitCoroRequest&#39;</span><span class="p">,</span> <span class="s1">&#39;CoroutineNotFoundError&#39;</span><span class="p">,</span> <span class="s1">&#39;SubCoroutineNotFoundError&#39;</span><span class="p">,</span> <span class="s1">&#39;TimeoutError&#39;</span><span class="p">,</span> <span class="s1">&#39;SubTimeoutError&#39;</span><span class="p">]</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.put_coro</span> <span class="kn">import</span> <span class="n">PutCoro</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.put_coro_list</span> <span class="kn">import</span> <span class="n">PutSingleCoroParams</span><span class="p">,</span> <span class="n">PSCP</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner</span> <span class="kn">import</span> <span class="n">timer_func_run_on</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.kill_coro</span> <span class="kn">import</span> <span class="n">kill_coro_on</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.conversion.reinterpret_cast</span> <span class="kn">import</span> <span class="n">reinterpret_cast</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">overload</span><span class="p">,</span> <span class="n">Type</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="k">class</span> <span class="nc">CoroutineNotFoundError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="k">pass</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="k">class</span> <span class="nc">SubCoroutineNotFoundError</span><span class="p">(</span><span class="n">CoroutineNotFoundError</span><span class="p">):</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="k">pass</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="k">class</span> <span class="nc">TimeoutError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="k">pass</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="k">class</span> <span class="nc">SubTimeoutError</span><span class="p">(</span><span class="ne">TimeoutError</span><span class="p">):</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="k">pass</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="k">class</span> <span class="nc">ServParams</span><span class="p">:</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="nd">@overload</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_request_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">TypedServiceRequest</span><span class="p">[</span><span class="n">ServiceResponseTypeVar</span><span class="p">]],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceResponseTypeVar</span><span class="p">:</span> <span class="o">...</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>    <span class="nd">@overload</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_request</span><span class="p">:</span> <span class="n">TypedServiceRequest</span><span class="p">[</span><span class="n">ServiceResponseTypeVar</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceResponseTypeVar</span><span class="p">:</span> <span class="o">...</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="nd">@overload</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">TypedService</span><span class="p">[</span><span class="n">ServiceResponseTypeVar</span><span class="p">]],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceResponseTypeVar</span><span class="p">:</span> <span class="o">...</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="nd">@overload</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="n">service_request</span><span class="p">:</span> <span class="n">TypedServiceRequest</span><span class="p">[</span><span class="n">ServiceResponseTypeVar</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceResponseTypeVar</span><span class="p">:</span> <span class="o">...</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    <span class="nd">@overload</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_request_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">ServiceRequest</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceResponseTypeVar</span><span class="p">:</span> <span class="o">...</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    <span class="nd">@overload</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_request</span><span class="p">:</span> <span class="n">ServiceRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceResponseTypeVar</span><span class="p">:</span> <span class="o">...</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    <span class="nd">@overload</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceResponseTypeVar</span><span class="p">:</span> <span class="o">...</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="nd">@overload</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="n">service_request</span><span class="p">:</span> <span class="n">ServiceRequest</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceResponseTypeVar</span><span class="p">:</span> <span class="o">...</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_type</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">service_type</span><span class="p">:</span> <span class="n">NormalizableServiceType</span> <span class="o">=</span> <span class="n">service_type</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">NormalizableServiceType</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_type</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a><span class="n">SP</span> <span class="o">=</span> <span class="n">ServParams</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="k">class</span> <span class="nc">WaitCoroRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result_required</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">provide_to_request_handler</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">timeout</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">kill_on_timeout</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">tree</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result_required</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">result_required</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="nf">list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>    <span class="k">def</span> <span class="nf">atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">put_single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">put_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]:</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">put_atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>    <span class="k">def</span> <span class="nf">put_fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    <span class="k">def</span> <span class="nf">serv_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]:</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them.</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a><span class="sd">        Args:</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a><span class="sd">        Returns:</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a><span class="sd">            List[Tuple[CoroID, Any, Optional[Exception]]]: _description_</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">serv_atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them. If one of the coroutines fails, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here).</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a><span class="sd">        Args:</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a><span class="sd">        Returns:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">serv_fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them. When one of coroutines finished, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here)</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a><span class="sd">        Args:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a><span class="sd">            num (int, optional): _description_. Defaults to 1.</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a><span class="sd">            measure_time (bool, optional): _description_. Defaults to False.</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a><span class="sd">        Returns:</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>    <span class="k">def</span> <span class="nf">serv_and_forget_single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params</span><span class="p">:</span> <span class="n">ServParams</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for a service request and returns immediately.</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="sd">        Args:</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="sd">            serv_params (ServParams): _description_</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a><span class="sd">        Returns:</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a><span class="sd">            _type_: _description_</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">11</span><span class="p">,</span> <span class="n">serv_params</span><span class="p">)</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">serv_and_forget_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and returns immediately.</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="sd">        Args:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a><span class="sd">        Returns:</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a><span class="sd">            _type_: _description_</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="k">class</span> <span class="nc">SingleMethod</span><span class="p">(</span><span class="n">ServiceRequestMethodMixin</span><span class="p">):</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service</span><span class="p">):</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">service</span><span class="p">)</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">single_called_by</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># Dict[CoroID, CoroID] # key - callable; value - requester</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_single_results</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>  <span class="c1"># (id, result, exception)</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result_required_by</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">WaitCoroRequest</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="n">requester_id</span><span class="p">:</span> <span class="n">CoroID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_coro</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="k">if</span> <span class="n">coro</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>            <span class="k">return</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">CoroutineNotFoundError</span><span class="p">(</span><span class="n">coro_id</span><span class="p">))</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">single_called_by</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">requester_id</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result_required_by</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">result_required</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>        <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">timeout</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>            <span class="k">def</span> <span class="nf">timeout_handler</span><span class="p">(</span><span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">single_called_by</span><span class="p">:</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">new_single_results</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="ne">TimeoutError</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)))</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>                    <span class="k">if</span> <span class="n">kill_on_timeout</span><span class="p">:</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>                        <span class="n">kill_coro_on</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">_loop</span><span class="p">),</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">tree</span><span class="p">)</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>            <span class="n">timer_func_run_on</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">_loop</span><span class="p">),</span> <span class="n">timeout</span><span class="p">,</span> <span class="n">timeout_handler</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">request</span><span class="o">.</span><span class="n">kill_on_timeout</span><span class="p">,</span> <span class="n">request</span><span class="o">.</span><span class="n">tree</span><span class="p">)</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">return</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_single_results</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>                <span class="n">requester_id</span><span class="p">:</span> <span class="n">CoroID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">single_called_by</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_required_by</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>                    <span class="k">if</span> <span class="n">CoroutineNotFoundError</span> <span class="o">==</span> <span class="nb">type</span><span class="p">(</span><span class="n">exception</span><span class="p">):</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>                        <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">SubCoroutineNotFoundError</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>                    <span class="k">elif</span> <span class="ne">TimeoutError</span> <span class="o">==</span> <span class="nb">type</span><span class="p">(</span><span class="n">exception</span><span class="p">):</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>                        <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">SubTimeoutError</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>                    
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">requester_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">requester_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>                
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_required_by</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">single_called_by</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>            <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>                <span class="k">pass</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_single_results</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_single_results</span><span class="p">)()</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>        <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_single_results</span><span class="p">)</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        <span class="k">if</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">single_called_by</span><span class="p">:</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_single_results</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">coro</span><span class="o">.</span><span class="n">last_result</span><span class="p">,</span> <span class="n">coro</span><span class="o">.</span><span class="n">exception</span><span class="p">))</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a><span class="k">class</span> <span class="nc">ListMethod</span><span class="p">(</span><span class="n">ServiceRequestMethodMixin</span><span class="p">):</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service</span><span class="p">):</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">service</span><span class="p">)</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">WaitCoroRequest</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[(</span><span class="n">Optional</span><span class="p">[</span><span class="n">CoroType</span><span class="p">],</span> <span class="n">Worker</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">)]])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>        <span class="n">requester_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">coro_list</span><span class="p">:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>            <span class="n">coro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_coro</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>            <span class="k">if</span> <span class="n">coro</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>                <span class="k">return</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">CoroutineNotFoundError</span><span class="p">(</span><span class="n">coro_id</span><span class="p">))</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>                <span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">list_called_by</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">requester_id</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>                <span class="k">if</span> <span class="n">requester_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">list_wait_by_caller</span><span class="p">:</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">list_wait_by_caller</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>                
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">list_wait_by_caller</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>                <span class="c1"># timeout: Optional[float] = request.timeout</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>                <span class="c1"># if timeout is not None:</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>                <span class="c1">#     def timeout_handler(requester_id: CoroID, coro_id: CoroID, kill_on_timeout: bool, tree: bool):</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>                <span class="c1">#         if coro_id in self.single_called_by:</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>                <span class="c1">#             self.new_single_results.add((coro_id, None, TimeoutError(coro_id)))</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>                <span class="c1">#             self.service.make_live()</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>                <span class="c1">#             if kill_on_timeout:</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                <span class="c1">#                 kill_coro_on(get_interface_and_loop_with_explicit_loop(self.service._loop), coro_id, tree)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>                    
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                <span class="c1">#     timer_func_run_on(get_interface_and_loop_with_explicit_loop(self.service._loop), timeout, timeout_handler, requester_id, coro_id, request.kill_on_timeout, request.tree)</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="k">return</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>        <span class="k">if</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">single_called_by</span><span class="p">:</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_list_results</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">coro</span><span class="o">.</span><span class="n">last_result</span><span class="p">,</span> <span class="n">coro</span><span class="o">.</span><span class="n">exception</span><span class="p">))</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>        
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a><span class="k">class</span> <span class="nc">PutListMethod</span><span class="p">(</span><span class="n">ServiceRequestMethodMixin</span><span class="p">):</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service</span><span class="p">):</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">service</span><span class="p">)</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">called_by</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">caller_results</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ready_requesters</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">WaitCoroRequest</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>        <span class="n">coroutines_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="n">results</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>        <span class="n">requester_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>            <span class="n">put_coro</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>            <span class="k">for</span> <span class="n">coro_request</span> <span class="ow">in</span> <span class="n">coro_list</span><span class="p">:</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>                <span class="n">result_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>                    <span class="n">coro_worker</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">coro_request</span><span class="p">()</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>                    <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="n">put_coro</span><span class="o">.</span><span class="n">put_from_other_service</span><span class="p">(</span><span class="n">requester_id</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>                    <span class="n">coroutines_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>                    <span class="n">result_coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>                    <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">result_coro_id</span><span class="p">,</span> <span class="n">exception</span><span class="p">))</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">results</span><span class="p">,</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">coroutines_list</span><span class="p">:</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">results</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>            
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>            <span class="k">if</span> <span class="n">requester_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">:</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>            <span class="k">if</span> <span class="n">requester_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">:</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>            <span class="k">if</span> <span class="n">requester_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_results</span><span class="p">:</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">caller_results</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>                 <span class="kc">None</span><span class="p">]</span> <span class="o">*</span> <span class="nb">len</span><span class="p">(</span><span class="n">coroutines_list</span><span class="p">)</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">coro</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">coroutines_list</span><span class="p">):</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>                <span class="n">coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">called_by</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">requester_id</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">][</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">index</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>                <span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>            <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">timeout</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>            <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>                <span class="k">def</span> <span class="nf">timeout_handler</span><span class="p">(</span><span class="n">requester_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">,</span> <span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>                    <span class="k">if</span> <span class="n">requester_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">:</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>                        <span class="k">return</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>                    
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>                    <span class="n">caller_waiting_set</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>                    <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">caller_waiting_set</span><span class="p">:</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">called_by</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>                        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">][</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">][</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">caller_results</span><span class="p">[</span><span class="n">requester_id</span><span class="p">][</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">coro</span><span class="o">.</span><span class="n">exception</span><span class="p">)</span>  <span class="c1"># TODO: should return TimeoutError exception instead</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>                        <span class="k">if</span> <span class="n">kill_on_timeout</span><span class="p">:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>                            <span class="n">kill_coro_on</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">_loop</span><span class="p">),</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">tree</span><span class="p">)</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">ready_requesters</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">requester_id</span><span class="p">)</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>                
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>                <span class="n">timer_func_run_on</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">_loop</span><span class="p">),</span> <span class="n">timeout</span><span class="p">,</span> <span class="n">timeout_handler</span><span class="p">,</span> <span class="n">requester_id</span><span class="p">,</span> <span class="n">request</span><span class="o">.</span><span class="n">kill_on_timeout</span><span class="p">,</span> <span class="n">request</span><span class="o">.</span><span class="n">tree</span><span class="p">)</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>        <span class="n">ready_requesters_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ready_requesters</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ready_requesters</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">ready_requesters_buff</span><span class="p">)()</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>        <span class="k">for</span> <span class="n">requester_id</span> <span class="ow">in</span> <span class="n">ready_requesters_buff</span><span class="p">:</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">requester_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_results</span><span class="p">[</span><span class="n">requester_id</span><span class="p">],</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_results</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">ready_requesters</span><span class="p">)</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">called_by</span><span class="p">:</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>            <span class="n">requester_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">called_by</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">called_by</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]:</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">caller_waiting_set</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>            
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>            <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">][</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">][</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">caller_results</span><span class="p">[</span><span class="n">requester_id</span><span class="p">][</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">coro</span><span class="o">.</span><span class="n">last_result</span><span class="p">,</span> <span class="n">coro</span><span class="o">.</span><span class="n">exception</span><span class="p">)</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]:</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_indexes</span><span class="p">[</span><span class="n">requester_id</span><span class="p">]</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">ready_requesters</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">requester_id</span><span class="p">)</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a><span class="k">class</span> <span class="nc">WaitCoro</span><span class="p">(</span><span class="n">Service</span><span class="p">):</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">):</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">WaitCoro</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_single</span> <span class="o">=</span> <span class="n">SingleMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_list</span> <span class="o">=</span> <span class="n">ListMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span> <span class="o">=</span> <span class="n">PutListMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>            <span class="mi">0</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="p">,</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>            <span class="mi">1</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>            <span class="mi">2</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>            <span class="mi">3</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>            <span class="mi">4</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>            <span class="mi">5</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="p">,</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>            <span class="mi">6</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>            <span class="mi">7</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>        <span class="p">}</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">WaitCoroRequest</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>            
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="k">return</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">WrongServiceRequestError</span><span class="p">())</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="o">.</span><span class="n">full_processing_iteration</span><span class="p">()</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="o">.</span><span class="n">full_processing_iteration</span><span class="p">()</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_work</span><span class="p">():</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>    <span class="k">def</span> <span class="nf">not_implemented</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a><span class="n">WaitCoroRequest</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">WaitCoro</span>
</span></pre></div>


            </section>
                <section id="WaitCoro">
                            <input id="WaitCoro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">WaitCoro</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</span>):

                <label class="view-source-button" for="WaitCoro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoro-405"><a href="#WaitCoro-405"><span class="linenos">405</span></a><span class="k">class</span> <span class="nc">WaitCoro</span><span class="p">(</span><span class="n">Service</span><span class="p">):</span>
</span><span id="WaitCoro-406"><a href="#WaitCoro-406"><span class="linenos">406</span></a>
</span><span id="WaitCoro-407"><a href="#WaitCoro-407"><span class="linenos">407</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">):</span>
</span><span id="WaitCoro-408"><a href="#WaitCoro-408"><span class="linenos">408</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">WaitCoro</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="WaitCoro-409"><a href="#WaitCoro-409"><span class="linenos">409</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_single</span> <span class="o">=</span> <span class="n">SingleMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="WaitCoro-410"><a href="#WaitCoro-410"><span class="linenos">410</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_list</span> <span class="o">=</span> <span class="n">ListMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="WaitCoro-411"><a href="#WaitCoro-411"><span class="linenos">411</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span> <span class="o">=</span> <span class="n">PutListMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="WaitCoro-412"><a href="#WaitCoro-412"><span class="linenos">412</span></a>
</span><span id="WaitCoro-413"><a href="#WaitCoro-413"><span class="linenos">413</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="WaitCoro-414"><a href="#WaitCoro-414"><span class="linenos">414</span></a>            <span class="mi">0</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="p">,</span>
</span><span id="WaitCoro-415"><a href="#WaitCoro-415"><span class="linenos">415</span></a>            <span class="mi">1</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro-416"><a href="#WaitCoro-416"><span class="linenos">416</span></a>            <span class="mi">2</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro-417"><a href="#WaitCoro-417"><span class="linenos">417</span></a>            <span class="mi">3</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro-418"><a href="#WaitCoro-418"><span class="linenos">418</span></a>            <span class="mi">4</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro-419"><a href="#WaitCoro-419"><span class="linenos">419</span></a>            <span class="mi">5</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="p">,</span>
</span><span id="WaitCoro-420"><a href="#WaitCoro-420"><span class="linenos">420</span></a>            <span class="mi">6</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro-421"><a href="#WaitCoro-421"><span class="linenos">421</span></a>            <span class="mi">7</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span>
</span><span id="WaitCoro-422"><a href="#WaitCoro-422"><span class="linenos">422</span></a>        <span class="p">}</span>
</span><span id="WaitCoro-423"><a href="#WaitCoro-423"><span class="linenos">423</span></a>
</span><span id="WaitCoro-424"><a href="#WaitCoro-424"><span class="linenos">424</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">WaitCoroRequest</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="WaitCoro-425"><a href="#WaitCoro-425"><span class="linenos">425</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="WaitCoro-426"><a href="#WaitCoro-426"><span class="linenos">426</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="WaitCoro-427"><a href="#WaitCoro-427"><span class="linenos">427</span></a>            
</span><span id="WaitCoro-428"><a href="#WaitCoro-428"><span class="linenos">428</span></a>        <span class="k">return</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">WrongServiceRequestError</span><span class="p">())</span>
</span><span id="WaitCoro-429"><a href="#WaitCoro-429"><span class="linenos">429</span></a>
</span><span id="WaitCoro-430"><a href="#WaitCoro-430"><span class="linenos">430</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WaitCoro-431"><a href="#WaitCoro-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="o">.</span><span class="n">full_processing_iteration</span><span class="p">()</span>
</span><span id="WaitCoro-432"><a href="#WaitCoro-432"><span class="linenos">432</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="o">.</span><span class="n">full_processing_iteration</span><span class="p">()</span>
</span><span id="WaitCoro-433"><a href="#WaitCoro-433"><span class="linenos">433</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_work</span><span class="p">():</span>
</span><span id="WaitCoro-434"><a href="#WaitCoro-434"><span class="linenos">434</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="WaitCoro-435"><a href="#WaitCoro-435"><span class="linenos">435</span></a>
</span><span id="WaitCoro-436"><a href="#WaitCoro-436"><span class="linenos">436</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="WaitCoro-437"><a href="#WaitCoro-437"><span class="linenos">437</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span>
</span><span id="WaitCoro-438"><a href="#WaitCoro-438"><span class="linenos">438</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="WaitCoro-439"><a href="#WaitCoro-439"><span class="linenos">439</span></a>
</span><span id="WaitCoro-440"><a href="#WaitCoro-440"><span class="linenos">440</span></a>    <span class="k">def</span> <span class="nf">not_implemented</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WaitCoro-441"><a href="#WaitCoro-441"><span class="linenos">441</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="WaitCoro.__init__" class="classattr">
                                        <input id="WaitCoro.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">WaitCoro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">loop</span></span>)</span>

                <label class="view-source-button" for="WaitCoro.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoro.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoro.__init__-407"><a href="#WaitCoro.__init__-407"><span class="linenos">407</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">):</span>
</span><span id="WaitCoro.__init__-408"><a href="#WaitCoro.__init__-408"><span class="linenos">408</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">WaitCoro</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="WaitCoro.__init__-409"><a href="#WaitCoro.__init__-409"><span class="linenos">409</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_single</span> <span class="o">=</span> <span class="n">SingleMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="WaitCoro.__init__-410"><a href="#WaitCoro.__init__-410"><span class="linenos">410</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_list</span> <span class="o">=</span> <span class="n">ListMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="WaitCoro.__init__-411"><a href="#WaitCoro.__init__-411"><span class="linenos">411</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span> <span class="o">=</span> <span class="n">PutListMethod</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="WaitCoro.__init__-412"><a href="#WaitCoro.__init__-412"><span class="linenos">412</span></a>
</span><span id="WaitCoro.__init__-413"><a href="#WaitCoro.__init__-413"><span class="linenos">413</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="WaitCoro.__init__-414"><a href="#WaitCoro.__init__-414"><span class="linenos">414</span></a>            <span class="mi">0</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="p">,</span>
</span><span id="WaitCoro.__init__-415"><a href="#WaitCoro.__init__-415"><span class="linenos">415</span></a>            <span class="mi">1</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro.__init__-416"><a href="#WaitCoro.__init__-416"><span class="linenos">416</span></a>            <span class="mi">2</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro.__init__-417"><a href="#WaitCoro.__init__-417"><span class="linenos">417</span></a>            <span class="mi">3</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro.__init__-418"><a href="#WaitCoro.__init__-418"><span class="linenos">418</span></a>            <span class="mi">4</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro.__init__-419"><a href="#WaitCoro.__init__-419"><span class="linenos">419</span></a>            <span class="mi">5</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="p">,</span>
</span><span id="WaitCoro.__init__-420"><a href="#WaitCoro.__init__-420"><span class="linenos">420</span></a>            <span class="mi">6</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span><span class="p">,</span>
</span><span id="WaitCoro.__init__-421"><a href="#WaitCoro.__init__-421"><span class="linenos">421</span></a>            <span class="mi">7</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">not_implemented</span>
</span><span id="WaitCoro.__init__-422"><a href="#WaitCoro.__init__-422"><span class="linenos">422</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoro.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="WaitCoro.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n"><a href="#WaitCoroRequest">WaitCoroRequest</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="WaitCoro.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoro.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoro.single_task_registration_or_immediate_processing-424"><a href="#WaitCoro.single_task_registration_or_immediate_processing-424"><span class="linenos">424</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">WaitCoroRequest</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="WaitCoro.single_task_registration_or_immediate_processing-425"><a href="#WaitCoro.single_task_registration_or_immediate_processing-425"><span class="linenos">425</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="WaitCoro.single_task_registration_or_immediate_processing-426"><a href="#WaitCoro.single_task_registration_or_immediate_processing-426"><span class="linenos">426</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="WaitCoro.single_task_registration_or_immediate_processing-427"><a href="#WaitCoro.single_task_registration_or_immediate_processing-427"><span class="linenos">427</span></a>            
</span><span id="WaitCoro.single_task_registration_or_immediate_processing-428"><a href="#WaitCoro.single_task_registration_or_immediate_processing-428"><span class="linenos">428</span></a>        <span class="k">return</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">WrongServiceRequestError</span><span class="p">())</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoro.full_processing_iteration" class="classattr">
                                        <input id="WaitCoro.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="WaitCoro.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoro.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoro.full_processing_iteration-430"><a href="#WaitCoro.full_processing_iteration-430"><span class="linenos">430</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WaitCoro.full_processing_iteration-431"><a href="#WaitCoro.full_processing_iteration-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="o">.</span><span class="n">full_processing_iteration</span><span class="p">()</span>
</span><span id="WaitCoro.full_processing_iteration-432"><a href="#WaitCoro.full_processing_iteration-432"><span class="linenos">432</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="o">.</span><span class="n">full_processing_iteration</span><span class="p">()</span>
</span><span id="WaitCoro.full_processing_iteration-433"><a href="#WaitCoro.full_processing_iteration-433"><span class="linenos">433</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_work</span><span class="p">():</span>
</span><span id="WaitCoro.full_processing_iteration-434"><a href="#WaitCoro.full_processing_iteration-434"><span class="linenos">434</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoro.in_work" class="classattr">
                                        <input id="WaitCoro.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="WaitCoro.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoro.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoro.in_work-436"><a href="#WaitCoro.in_work-436"><span class="linenos">436</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="WaitCoro.in_work-437"><a href="#WaitCoro.in_work-437"><span class="linenos">437</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_single</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_put_list</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span>
</span><span id="WaitCoro.in_work-438"><a href="#WaitCoro.in_work-438"><span class="linenos">438</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="WaitCoro.not_implemented" class="classattr">
                                        <input id="WaitCoro.not_implemented-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">not_implemented</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="WaitCoro.not_implemented-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoro.not_implemented"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoro.not_implemented-440"><a href="#WaitCoro.not_implemented-440"><span class="linenos">440</span></a>    <span class="k">def</span> <span class="nf">not_implemented</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="WaitCoro.not_implemented-441"><a href="#WaitCoro.not_implemented-441"><span class="linenos">441</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="WaitCoro.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="WaitCoro.iteration" class="function">iteration</dd>
                <dd id="WaitCoro.make_response" class="function">make_response</dd>
                <dd id="WaitCoro.register_response" class="function">register_response</dd>
                <dd id="WaitCoro.put_task" class="function">put_task</dd>
                <dd id="WaitCoro.resolve_request" class="function">resolve_request</dd>
                <dd id="WaitCoro.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="WaitCoro.in_forground_work" class="function">in_forground_work</dd>
                <dd id="WaitCoro.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="WaitCoro.time_left_before_next_event" class="function">time_left_before_next_event</dd>
                <dd id="WaitCoro.is_low_latency" class="function">is_low_latency</dd>
                <dd id="WaitCoro.make_live" class="function">make_live</dd>
                <dd id="WaitCoro.make_dead" class="function">make_dead</dd>
                <dd id="WaitCoro.service_id_impl" class="function">service_id_impl</dd>
                <dd id="WaitCoro.service_id" class="function">service_id</dd>
                <dd id="WaitCoro.destroy" class="function">destroy</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="PutSingleCoroParams">
                            <input id="PutSingleCoroParams-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PutSingleCoroParams</span>:

                <label class="view-source-button" for="PutSingleCoroParams-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PutSingleCoroParams"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PutSingleCoroParams-50"><a href="#PutSingleCoroParams-50"><span class="linenos">50</span></a><span class="k">class</span> <span class="nc">PutSingleCoroParams</span><span class="p">:</span>
</span><span id="PutSingleCoroParams-51"><a href="#PutSingleCoroParams-51"><span class="linenos">51</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PutSingleCoroParams-52"><a href="#PutSingleCoroParams-52"><span class="linenos">52</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span> <span class="o">=</span> <span class="n">coro_worker</span>
</span><span id="PutSingleCoroParams-53"><a href="#PutSingleCoroParams-53"><span class="linenos">53</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="PutSingleCoroParams-54"><a href="#PutSingleCoroParams-54"><span class="linenos">54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="PutSingleCoroParams-55"><a href="#PutSingleCoroParams-55"><span class="linenos">55</span></a>    
</span><span id="PutSingleCoroParams-56"><a href="#PutSingleCoroParams-56"><span class="linenos">56</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="PutSingleCoroParams-57"><a href="#PutSingleCoroParams-57"><span class="linenos">57</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_worker</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span></pre></div>


    

                            <div id="PutSingleCoroParams.__init__" class="classattr">
                                        <input id="PutSingleCoroParams.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">PutSingleCoroParams</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ExplicitWorker</span><span class="p">,</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="PutSingleCoroParams.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PutSingleCoroParams.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PutSingleCoroParams.__init__-51"><a href="#PutSingleCoroParams.__init__-51"><span class="linenos">51</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PutSingleCoroParams.__init__-52"><a href="#PutSingleCoroParams.__init__-52"><span class="linenos">52</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_worker</span><span class="p">:</span> <span class="n">AnyWorker</span> <span class="o">=</span> <span class="n">coro_worker</span>
</span><span id="PutSingleCoroParams.__init__-53"><a href="#PutSingleCoroParams.__init__-53"><span class="linenos">53</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="PutSingleCoroParams.__init__-54"><a href="#PutSingleCoroParams.__init__-54"><span class="linenos">54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            </div>
                            <div id="PutSingleCoroParams.coro_worker" class="classattr">
                                <div class="attr variable">
            <span class="name">coro_worker</span><span class="annotation">: Union[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ExplicitWorker, collections.abc.Callable[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Interface, Any], collections.abc.Callable[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Interface, Awaitable[Any]]]</span>

        
    </div>
    <a class="headerlink" href="#PutSingleCoroParams.coro_worker"></a>
    
    

                            </div>
                            <div id="PutSingleCoroParams.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span><span class="annotation">: Tuple</span>

        
    </div>
    <a class="headerlink" href="#PutSingleCoroParams.args"></a>
    
    

                            </div>
                            <div id="PutSingleCoroParams.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span><span class="annotation">: Dict</span>

        
    </div>
    <a class="headerlink" href="#PutSingleCoroParams.kwargs"></a>
    
    

                            </div>
                </section>
                <section id="PSCP">
                    <div class="attr variable">
            <span class="name">PSCP</span>        =
<input id="PSCP-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="PSCP-view-value"></label><span class="default_value">&lt;class &#39;<a href="#PutSingleCoroParams">PutSingleCoroParams</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#PSCP"></a>
    
    

                </section>
                <section id="WaitCoroRequest">
                            <input id="WaitCoroRequest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">WaitCoroRequest</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</span>):

                <label class="view-source-button" for="WaitCoroRequest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest-103"><a href="#WaitCoroRequest-103"><span class="linenos">103</span></a><span class="k">class</span> <span class="nc">WaitCoroRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="WaitCoroRequest-104"><a href="#WaitCoroRequest-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result_required</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="WaitCoroRequest-105"><a href="#WaitCoroRequest-105"><span class="linenos">105</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="WaitCoroRequest-106"><a href="#WaitCoroRequest-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">provide_to_request_handler</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="WaitCoroRequest-107"><a href="#WaitCoroRequest-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">timeout</span>
</span><span id="WaitCoroRequest-108"><a href="#WaitCoroRequest-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">kill_on_timeout</span>
</span><span id="WaitCoroRequest-109"><a href="#WaitCoroRequest-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">tree</span>
</span><span id="WaitCoroRequest-110"><a href="#WaitCoroRequest-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result_required</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">result_required</span>
</span><span id="WaitCoroRequest-111"><a href="#WaitCoroRequest-111"><span class="linenos">111</span></a>
</span><span id="WaitCoroRequest-112"><a href="#WaitCoroRequest-112"><span class="linenos">112</span></a>    <span class="k">def</span> <span class="nf">single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="WaitCoroRequest-113"><a href="#WaitCoroRequest-113"><span class="linenos">113</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="WaitCoroRequest-114"><a href="#WaitCoroRequest-114"><span class="linenos">114</span></a>
</span><span id="WaitCoroRequest-115"><a href="#WaitCoroRequest-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="nf">list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest-116"><a href="#WaitCoroRequest-116"><span class="linenos">116</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span><span id="WaitCoroRequest-117"><a href="#WaitCoroRequest-117"><span class="linenos">117</span></a>
</span><span id="WaitCoroRequest-118"><a href="#WaitCoroRequest-118"><span class="linenos">118</span></a>    <span class="k">def</span> <span class="nf">atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest-119"><a href="#WaitCoroRequest-119"><span class="linenos">119</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span><span id="WaitCoroRequest-120"><a href="#WaitCoroRequest-120"><span class="linenos">120</span></a>
</span><span id="WaitCoroRequest-121"><a href="#WaitCoroRequest-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="nf">fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest-122"><a href="#WaitCoroRequest-122"><span class="linenos">122</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span><span id="WaitCoroRequest-123"><a href="#WaitCoroRequest-123"><span class="linenos">123</span></a>
</span><span id="WaitCoroRequest-124"><a href="#WaitCoroRequest-124"><span class="linenos">124</span></a>    <span class="k">def</span> <span class="nf">put_single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest-125"><a href="#WaitCoroRequest-125"><span class="linenos">125</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="WaitCoroRequest-126"><a href="#WaitCoroRequest-126"><span class="linenos">126</span></a>
</span><span id="WaitCoroRequest-127"><a href="#WaitCoroRequest-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">put_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]:</span>
</span><span id="WaitCoroRequest-128"><a href="#WaitCoroRequest-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span><span id="WaitCoroRequest-129"><a href="#WaitCoroRequest-129"><span class="linenos">129</span></a>
</span><span id="WaitCoroRequest-130"><a href="#WaitCoroRequest-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="nf">put_atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest-131"><a href="#WaitCoroRequest-131"><span class="linenos">131</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span><span id="WaitCoroRequest-132"><a href="#WaitCoroRequest-132"><span class="linenos">132</span></a>
</span><span id="WaitCoroRequest-133"><a href="#WaitCoroRequest-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">put_fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest-134"><a href="#WaitCoroRequest-134"><span class="linenos">134</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span><span id="WaitCoroRequest-135"><a href="#WaitCoroRequest-135"><span class="linenos">135</span></a>
</span><span id="WaitCoroRequest-136"><a href="#WaitCoroRequest-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">serv_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]:</span>
</span><span id="WaitCoroRequest-137"><a href="#WaitCoroRequest-137"><span class="linenos">137</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them.</span>
</span><span id="WaitCoroRequest-138"><a href="#WaitCoroRequest-138"><span class="linenos">138</span></a>
</span><span id="WaitCoroRequest-139"><a href="#WaitCoroRequest-139"><span class="linenos">139</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest-140"><a href="#WaitCoroRequest-140"><span class="linenos">140</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="WaitCoroRequest-141"><a href="#WaitCoroRequest-141"><span class="linenos">141</span></a>
</span><span id="WaitCoroRequest-142"><a href="#WaitCoroRequest-142"><span class="linenos">142</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest-143"><a href="#WaitCoroRequest-143"><span class="linenos">143</span></a><span class="sd">            List[Tuple[CoroID, Any, Optional[Exception]]]: _description_</span>
</span><span id="WaitCoroRequest-144"><a href="#WaitCoroRequest-144"><span class="linenos">144</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest-145"><a href="#WaitCoroRequest-145"><span class="linenos">145</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span><span id="WaitCoroRequest-146"><a href="#WaitCoroRequest-146"><span class="linenos">146</span></a>
</span><span id="WaitCoroRequest-147"><a href="#WaitCoroRequest-147"><span class="linenos">147</span></a>    <span class="k">def</span> <span class="nf">serv_atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest-148"><a href="#WaitCoroRequest-148"><span class="linenos">148</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them. If one of the coroutines fails, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here).</span>
</span><span id="WaitCoroRequest-149"><a href="#WaitCoroRequest-149"><span class="linenos">149</span></a>
</span><span id="WaitCoroRequest-150"><a href="#WaitCoroRequest-150"><span class="linenos">150</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest-151"><a href="#WaitCoroRequest-151"><span class="linenos">151</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="WaitCoroRequest-152"><a href="#WaitCoroRequest-152"><span class="linenos">152</span></a>
</span><span id="WaitCoroRequest-153"><a href="#WaitCoroRequest-153"><span class="linenos">153</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest-154"><a href="#WaitCoroRequest-154"><span class="linenos">154</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="WaitCoroRequest-155"><a href="#WaitCoroRequest-155"><span class="linenos">155</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest-156"><a href="#WaitCoroRequest-156"><span class="linenos">156</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span><span id="WaitCoroRequest-157"><a href="#WaitCoroRequest-157"><span class="linenos">157</span></a>
</span><span id="WaitCoroRequest-158"><a href="#WaitCoroRequest-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">serv_fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest-159"><a href="#WaitCoroRequest-159"><span class="linenos">159</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them. When one of coroutines finished, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here)</span>
</span><span id="WaitCoroRequest-160"><a href="#WaitCoroRequest-160"><span class="linenos">160</span></a>
</span><span id="WaitCoroRequest-161"><a href="#WaitCoroRequest-161"><span class="linenos">161</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest-162"><a href="#WaitCoroRequest-162"><span class="linenos">162</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="WaitCoroRequest-163"><a href="#WaitCoroRequest-163"><span class="linenos">163</span></a><span class="sd">            num (int, optional): _description_. Defaults to 1.</span>
</span><span id="WaitCoroRequest-164"><a href="#WaitCoroRequest-164"><span class="linenos">164</span></a><span class="sd">            measure_time (bool, optional): _description_. Defaults to False.</span>
</span><span id="WaitCoroRequest-165"><a href="#WaitCoroRequest-165"><span class="linenos">165</span></a>
</span><span id="WaitCoroRequest-166"><a href="#WaitCoroRequest-166"><span class="linenos">166</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest-167"><a href="#WaitCoroRequest-167"><span class="linenos">167</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="WaitCoroRequest-168"><a href="#WaitCoroRequest-168"><span class="linenos">168</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest-169"><a href="#WaitCoroRequest-169"><span class="linenos">169</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span><span id="WaitCoroRequest-170"><a href="#WaitCoroRequest-170"><span class="linenos">170</span></a>
</span><span id="WaitCoroRequest-171"><a href="#WaitCoroRequest-171"><span class="linenos">171</span></a>    <span class="k">def</span> <span class="nf">serv_and_forget_single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params</span><span class="p">:</span> <span class="n">ServParams</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="WaitCoroRequest-172"><a href="#WaitCoroRequest-172"><span class="linenos">172</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for a service request and returns immediately.</span>
</span><span id="WaitCoroRequest-173"><a href="#WaitCoroRequest-173"><span class="linenos">173</span></a>
</span><span id="WaitCoroRequest-174"><a href="#WaitCoroRequest-174"><span class="linenos">174</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest-175"><a href="#WaitCoroRequest-175"><span class="linenos">175</span></a><span class="sd">            serv_params (ServParams): _description_</span>
</span><span id="WaitCoroRequest-176"><a href="#WaitCoroRequest-176"><span class="linenos">176</span></a>
</span><span id="WaitCoroRequest-177"><a href="#WaitCoroRequest-177"><span class="linenos">177</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest-178"><a href="#WaitCoroRequest-178"><span class="linenos">178</span></a><span class="sd">            _type_: _description_</span>
</span><span id="WaitCoroRequest-179"><a href="#WaitCoroRequest-179"><span class="linenos">179</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest-180"><a href="#WaitCoroRequest-180"><span class="linenos">180</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">11</span><span class="p">,</span> <span class="n">serv_params</span><span class="p">)</span>
</span><span id="WaitCoroRequest-181"><a href="#WaitCoroRequest-181"><span class="linenos">181</span></a>
</span><span id="WaitCoroRequest-182"><a href="#WaitCoroRequest-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">serv_and_forget_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="WaitCoroRequest-183"><a href="#WaitCoroRequest-183"><span class="linenos">183</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and returns immediately.</span>
</span><span id="WaitCoroRequest-184"><a href="#WaitCoroRequest-184"><span class="linenos">184</span></a>
</span><span id="WaitCoroRequest-185"><a href="#WaitCoroRequest-185"><span class="linenos">185</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest-186"><a href="#WaitCoroRequest-186"><span class="linenos">186</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="WaitCoroRequest-187"><a href="#WaitCoroRequest-187"><span class="linenos">187</span></a>
</span><span id="WaitCoroRequest-188"><a href="#WaitCoroRequest-188"><span class="linenos">188</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest-189"><a href="#WaitCoroRequest-189"><span class="linenos">189</span></a><span class="sd">            _type_: _description_</span>
</span><span id="WaitCoroRequest-190"><a href="#WaitCoroRequest-190"><span class="linenos">190</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest-191"><a href="#WaitCoroRequest-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="WaitCoroRequest.__init__" class="classattr">
                                        <input id="WaitCoroRequest.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">WaitCoroRequest</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">timeout</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">result_required</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span>)</span>

                <label class="view-source-button" for="WaitCoroRequest.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.__init__-104"><a href="#WaitCoroRequest.__init__-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result_required</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="WaitCoroRequest.__init__-105"><a href="#WaitCoroRequest.__init__-105"><span class="linenos">105</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="WaitCoroRequest.__init__-106"><a href="#WaitCoroRequest.__init__-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">provide_to_request_handler</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="WaitCoroRequest.__init__-107"><a href="#WaitCoroRequest.__init__-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="n">timeout</span>
</span><span id="WaitCoroRequest.__init__-108"><a href="#WaitCoroRequest.__init__-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kill_on_timeout</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">kill_on_timeout</span>
</span><span id="WaitCoroRequest.__init__-109"><a href="#WaitCoroRequest.__init__-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">tree</span>
</span><span id="WaitCoroRequest.__init__-110"><a href="#WaitCoroRequest.__init__-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result_required</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">result_required</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.provide_to_request_handler" class="classattr">
                                <div class="attr variable">
            <span class="name">provide_to_request_handler</span>

        
    </div>
    <a class="headerlink" href="#WaitCoroRequest.provide_to_request_handler"></a>
    
    

                            </div>
                            <div id="WaitCoroRequest.timeout" class="classattr">
                                <div class="attr variable">
            <span class="name">timeout</span><span class="annotation">: Union[float, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#WaitCoroRequest.timeout"></a>
    
    

                            </div>
                            <div id="WaitCoroRequest.kill_on_timeout" class="classattr">
                                <div class="attr variable">
            <span class="name">kill_on_timeout</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#WaitCoroRequest.kill_on_timeout"></a>
    
    

                            </div>
                            <div id="WaitCoroRequest.tree" class="classattr">
                                <div class="attr variable">
            <span class="name">tree</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#WaitCoroRequest.tree"></a>
    
    

                            </div>
                            <div id="WaitCoroRequest.result_required" class="classattr">
                                <div class="attr variable">
            <span class="name">result_required</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#WaitCoroRequest.result_required"></a>
    
    

                            </div>
                            <div id="WaitCoroRequest.single" class="classattr">
                                        <input id="WaitCoroRequest.single-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.single-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.single"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.single-112"><a href="#WaitCoroRequest.single-112"><span class="linenos">112</span></a>    <span class="k">def</span> <span class="nf">single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="WaitCoroRequest.single-113"><a href="#WaitCoroRequest.single-113"><span class="linenos">113</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.list" class="classattr">
                                        <input id="WaitCoroRequest.list-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">list</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.list-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.list"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.list-115"><a href="#WaitCoroRequest.list-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="nf">list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest.list-116"><a href="#WaitCoroRequest.list-116"><span class="linenos">116</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.atomic" class="classattr">
                                        <input id="WaitCoroRequest.atomic-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">atomic</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.atomic-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.atomic"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.atomic-118"><a href="#WaitCoroRequest.atomic-118"><span class="linenos">118</span></a>    <span class="k">def</span> <span class="nf">atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest.atomic-119"><a href="#WaitCoroRequest.atomic-119"><span class="linenos">119</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.fastest" class="classattr">
                                        <input id="WaitCoroRequest.fastest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">fastest</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>,</span><span class="param">	<span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span>,</span><span class="param">	<span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.fastest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.fastest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.fastest-121"><a href="#WaitCoroRequest.fastest-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="nf">fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CoroID</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest.fastest-122"><a href="#WaitCoroRequest.fastest-122"><span class="linenos">122</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.put_single" class="classattr">
                                        <input id="WaitCoroRequest.put_single-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_single</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.put_single-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.put_single"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.put_single-124"><a href="#WaitCoroRequest.put_single-124"><span class="linenos">124</span></a>    <span class="k">def</span> <span class="nf">put_single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest.put_single-125"><a href="#WaitCoroRequest.put_single-125"><span class="linenos">125</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.put_list" class="classattr">
                                        <input id="WaitCoroRequest.put_list-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_list</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="n"><a href="#PutSingleCoroParams">PutSingleCoroParams</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="ne">Exception</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]]</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.put_list-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.put_list"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.put_list-127"><a href="#WaitCoroRequest.put_list-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">put_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]:</span>
</span><span id="WaitCoroRequest.put_list-128"><a href="#WaitCoroRequest.put_list-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.put_atomic" class="classattr">
                                        <input id="WaitCoroRequest.put_atomic-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_atomic</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="n"><a href="#PutSingleCoroParams">PutSingleCoroParams</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.put_atomic-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.put_atomic"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.put_atomic-130"><a href="#WaitCoroRequest.put_atomic-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="nf">put_atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest.put_atomic-131"><a href="#WaitCoroRequest.put_atomic-131"><span class="linenos">131</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.put_fastest" class="classattr">
                                        <input id="WaitCoroRequest.put_fastest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_fastest</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="n"><a href="#PutSingleCoroParams">PutSingleCoroParams</a></span><span class="p">]</span>,</span><span class="param">	<span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span>,</span><span class="param">	<span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.put_fastest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.put_fastest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.put_fastest-133"><a href="#WaitCoroRequest.put_fastest-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">put_fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">PutSingleCoroParams</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest.put_fastest-134"><a href="#WaitCoroRequest.put_fastest-134"><span class="linenos">134</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">coro_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="WaitCoroRequest.serv_list" class="classattr">
                                        <input id="WaitCoroRequest.serv_list-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serv_list</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">serv_params_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">ServParams</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="ne">Exception</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]]</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.serv_list-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.serv_list"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.serv_list-136"><a href="#WaitCoroRequest.serv_list-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">serv_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]:</span>
</span><span id="WaitCoroRequest.serv_list-137"><a href="#WaitCoroRequest.serv_list-137"><span class="linenos">137</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them.</span>
</span><span id="WaitCoroRequest.serv_list-138"><a href="#WaitCoroRequest.serv_list-138"><span class="linenos">138</span></a>
</span><span id="WaitCoroRequest.serv_list-139"><a href="#WaitCoroRequest.serv_list-139"><span class="linenos">139</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest.serv_list-140"><a href="#WaitCoroRequest.serv_list-140"><span class="linenos">140</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="WaitCoroRequest.serv_list-141"><a href="#WaitCoroRequest.serv_list-141"><span class="linenos">141</span></a>
</span><span id="WaitCoroRequest.serv_list-142"><a href="#WaitCoroRequest.serv_list-142"><span class="linenos">142</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest.serv_list-143"><a href="#WaitCoroRequest.serv_list-143"><span class="linenos">143</span></a><span class="sd">            List[Tuple[CoroID, Any, Optional[Exception]]]: _description_</span>
</span><span id="WaitCoroRequest.serv_list-144"><a href="#WaitCoroRequest.serv_list-144"><span class="linenos">144</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest.serv_list-145"><a href="#WaitCoroRequest.serv_list-145"><span class="linenos">145</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Creates a coroutine for each service request and waits for the result of each of them.</p>

<p>Args:
    serv_params_list (Sequence[ServParams]): _description_</p>

<p>Returns:
    List[Tuple[CoroID, Any, Optional[Exception]]]: _description_</p>
</div>


                            </div>
                            <div id="WaitCoroRequest.serv_atomic" class="classattr">
                                        <input id="WaitCoroRequest.serv_atomic-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serv_atomic</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">serv_params_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">ServParams</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.serv_atomic-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.serv_atomic"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.serv_atomic-147"><a href="#WaitCoroRequest.serv_atomic-147"><span class="linenos">147</span></a>    <span class="k">def</span> <span class="nf">serv_atomic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest.serv_atomic-148"><a href="#WaitCoroRequest.serv_atomic-148"><span class="linenos">148</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them. If one of the coroutines fails, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here).</span>
</span><span id="WaitCoroRequest.serv_atomic-149"><a href="#WaitCoroRequest.serv_atomic-149"><span class="linenos">149</span></a>
</span><span id="WaitCoroRequest.serv_atomic-150"><a href="#WaitCoroRequest.serv_atomic-150"><span class="linenos">150</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest.serv_atomic-151"><a href="#WaitCoroRequest.serv_atomic-151"><span class="linenos">151</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="WaitCoroRequest.serv_atomic-152"><a href="#WaitCoroRequest.serv_atomic-152"><span class="linenos">152</span></a>
</span><span id="WaitCoroRequest.serv_atomic-153"><a href="#WaitCoroRequest.serv_atomic-153"><span class="linenos">153</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest.serv_atomic-154"><a href="#WaitCoroRequest.serv_atomic-154"><span class="linenos">154</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="WaitCoroRequest.serv_atomic-155"><a href="#WaitCoroRequest.serv_atomic-155"><span class="linenos">155</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest.serv_atomic-156"><a href="#WaitCoroRequest.serv_atomic-156"><span class="linenos">156</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Creates a coroutine for each service request and waits for the result of each of them. If one of the coroutines fails, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here).</p>

<p>Args:
    serv_params_list (Sequence[ServParams]): _description_</p>

<p>Returns:
    ServiceRequest: _description_</p>
</div>


                            </div>
                            <div id="WaitCoroRequest.serv_fastest" class="classattr">
                                        <input id="WaitCoroRequest.serv_fastest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serv_fastest</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">serv_params_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">ServParams</span><span class="p">]</span>,</span><span class="param">	<span class="n">num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span>,</span><span class="param">	<span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.serv_fastest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.serv_fastest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.serv_fastest-158"><a href="#WaitCoroRequest.serv_fastest-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">serv_fastest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">],</span> <span class="n">num</span><span class="p">:</span> <span class="nb">int</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">:</span> <span class="nb">bool</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="WaitCoroRequest.serv_fastest-159"><a href="#WaitCoroRequest.serv_fastest-159"><span class="linenos">159</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and waits for the result of each of them. When one of coroutines finished, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here)</span>
</span><span id="WaitCoroRequest.serv_fastest-160"><a href="#WaitCoroRequest.serv_fastest-160"><span class="linenos">160</span></a>
</span><span id="WaitCoroRequest.serv_fastest-161"><a href="#WaitCoroRequest.serv_fastest-161"><span class="linenos">161</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest.serv_fastest-162"><a href="#WaitCoroRequest.serv_fastest-162"><span class="linenos">162</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="WaitCoroRequest.serv_fastest-163"><a href="#WaitCoroRequest.serv_fastest-163"><span class="linenos">163</span></a><span class="sd">            num (int, optional): _description_. Defaults to 1.</span>
</span><span id="WaitCoroRequest.serv_fastest-164"><a href="#WaitCoroRequest.serv_fastest-164"><span class="linenos">164</span></a><span class="sd">            measure_time (bool, optional): _description_. Defaults to False.</span>
</span><span id="WaitCoroRequest.serv_fastest-165"><a href="#WaitCoroRequest.serv_fastest-165"><span class="linenos">165</span></a>
</span><span id="WaitCoroRequest.serv_fastest-166"><a href="#WaitCoroRequest.serv_fastest-166"><span class="linenos">166</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest.serv_fastest-167"><a href="#WaitCoroRequest.serv_fastest-167"><span class="linenos">167</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="WaitCoroRequest.serv_fastest-168"><a href="#WaitCoroRequest.serv_fastest-168"><span class="linenos">168</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest.serv_fastest-169"><a href="#WaitCoroRequest.serv_fastest-169"><span class="linenos">169</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">,</span> <span class="n">num</span><span class="p">,</span> <span class="n">measure_time</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Creates a coroutine for each service request and waits for the result of each of them. When one of coroutines finished, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here)</p>

<p>Args:
    serv_params_list (Sequence[ServParams]): _description_
    num (int, optional): _description_. Defaults to 1.
    measure_time (bool, optional): _description_. Defaults to False.</p>

<p>Returns:
    ServiceRequest: _description_</p>
</div>


                            </div>
                            <div id="WaitCoroRequest.serv_and_forget_single" class="classattr">
                                        <input id="WaitCoroRequest.serv_and_forget_single-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serv_and_forget_single</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">serv_params</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">ServParams</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.serv_and_forget_single-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.serv_and_forget_single"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.serv_and_forget_single-171"><a href="#WaitCoroRequest.serv_and_forget_single-171"><span class="linenos">171</span></a>    <span class="k">def</span> <span class="nf">serv_and_forget_single</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params</span><span class="p">:</span> <span class="n">ServParams</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="WaitCoroRequest.serv_and_forget_single-172"><a href="#WaitCoroRequest.serv_and_forget_single-172"><span class="linenos">172</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for a service request and returns immediately.</span>
</span><span id="WaitCoroRequest.serv_and_forget_single-173"><a href="#WaitCoroRequest.serv_and_forget_single-173"><span class="linenos">173</span></a>
</span><span id="WaitCoroRequest.serv_and_forget_single-174"><a href="#WaitCoroRequest.serv_and_forget_single-174"><span class="linenos">174</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest.serv_and_forget_single-175"><a href="#WaitCoroRequest.serv_and_forget_single-175"><span class="linenos">175</span></a><span class="sd">            serv_params (ServParams): _description_</span>
</span><span id="WaitCoroRequest.serv_and_forget_single-176"><a href="#WaitCoroRequest.serv_and_forget_single-176"><span class="linenos">176</span></a>
</span><span id="WaitCoroRequest.serv_and_forget_single-177"><a href="#WaitCoroRequest.serv_and_forget_single-177"><span class="linenos">177</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest.serv_and_forget_single-178"><a href="#WaitCoroRequest.serv_and_forget_single-178"><span class="linenos">178</span></a><span class="sd">            _type_: _description_</span>
</span><span id="WaitCoroRequest.serv_and_forget_single-179"><a href="#WaitCoroRequest.serv_and_forget_single-179"><span class="linenos">179</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest.serv_and_forget_single-180"><a href="#WaitCoroRequest.serv_and_forget_single-180"><span class="linenos">180</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">11</span><span class="p">,</span> <span class="n">serv_params</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Creates a coroutine for a service request and returns immediately.</p>

<p>Args:
    serv_params (ServParams): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                            </div>
                            <div id="WaitCoroRequest.serv_and_forget_list" class="classattr">
                                        <input id="WaitCoroRequest.serv_and_forget_list-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serv_and_forget_list</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">serv_params_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">wait_coro</span><span class="o">.</span><span class="n">ServParams</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="WaitCoroRequest.serv_and_forget_list-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WaitCoroRequest.serv_and_forget_list"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WaitCoroRequest.serv_and_forget_list-182"><a href="#WaitCoroRequest.serv_and_forget_list-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">serv_and_forget_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">ServParams</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="WaitCoroRequest.serv_and_forget_list-183"><a href="#WaitCoroRequest.serv_and_forget_list-183"><span class="linenos">183</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Creates a coroutine for each service request and returns immediately.</span>
</span><span id="WaitCoroRequest.serv_and_forget_list-184"><a href="#WaitCoroRequest.serv_and_forget_list-184"><span class="linenos">184</span></a>
</span><span id="WaitCoroRequest.serv_and_forget_list-185"><a href="#WaitCoroRequest.serv_and_forget_list-185"><span class="linenos">185</span></a><span class="sd">        Args:</span>
</span><span id="WaitCoroRequest.serv_and_forget_list-186"><a href="#WaitCoroRequest.serv_and_forget_list-186"><span class="linenos">186</span></a><span class="sd">            serv_params_list (Sequence[ServParams]): _description_</span>
</span><span id="WaitCoroRequest.serv_and_forget_list-187"><a href="#WaitCoroRequest.serv_and_forget_list-187"><span class="linenos">187</span></a>
</span><span id="WaitCoroRequest.serv_and_forget_list-188"><a href="#WaitCoroRequest.serv_and_forget_list-188"><span class="linenos">188</span></a><span class="sd">        Returns:</span>
</span><span id="WaitCoroRequest.serv_and_forget_list-189"><a href="#WaitCoroRequest.serv_and_forget_list-189"><span class="linenos">189</span></a><span class="sd">            _type_: _description_</span>
</span><span id="WaitCoroRequest.serv_and_forget_list-190"><a href="#WaitCoroRequest.serv_and_forget_list-190"><span class="linenos">190</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="WaitCoroRequest.serv_and_forget_list-191"><a href="#WaitCoroRequest.serv_and_forget_list-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="n">serv_params_list</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Creates a coroutine for each service request and returns immediately.</p>

<p>Args:
    serv_params_list (Sequence[ServParams]): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                            </div>
                            <div id="WaitCoroRequest.default_service_type" class="classattr">
                                <div class="attr variable">
            <span class="name">default_service_type</span><span class="annotation">: Union[type[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service], NoneType]</span>        =
<input id="WaitCoroRequest.default_service_type-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="WaitCoroRequest.default_service_type-view-value"></label><span class="default_value">&lt;class &#39;<a href="#WaitCoro">WaitCoro</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#WaitCoroRequest.default_service_type"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</dt>
                                <dd id="WaitCoroRequest.default__request__type__" class="variable">default__request__type__</dd>
                <dd id="WaitCoroRequest.request_type" class="variable">request_type</dd>
                <dd id="WaitCoroRequest.args" class="variable">args</dd>
                <dd id="WaitCoroRequest.kwargs" class="variable">kwargs</dd>
                <dd id="WaitCoroRequest.interface" class="function">interface</dd>
                <dd id="WaitCoroRequest.i" class="function">i</dd>
                <dd id="WaitCoroRequest.async_interface" class="function">async_interface</dd>
                <dd id="WaitCoroRequest.ai" class="function">ai</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CoroutineNotFoundError">
                            <input id="CoroutineNotFoundError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CoroutineNotFoundError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="CoroutineNotFoundError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroutineNotFoundError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroutineNotFoundError-50"><a href="#CoroutineNotFoundError-50"><span class="linenos">50</span></a><span class="k">class</span> <span class="nc">CoroutineNotFoundError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="CoroutineNotFoundError-51"><a href="#CoroutineNotFoundError-51"><span class="linenos">51</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="CoroutineNotFoundError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="CoroutineNotFoundError.with_traceback" class="function">with_traceback</dd>
                <dd id="CoroutineNotFoundError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="SubCoroutineNotFoundError">
                            <input id="SubCoroutineNotFoundError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SubCoroutineNotFoundError</span><wbr>(<span class="base"><a href="#CoroutineNotFoundError">CoroutineNotFoundError</a></span>):

                <label class="view-source-button" for="SubCoroutineNotFoundError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubCoroutineNotFoundError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubCoroutineNotFoundError-54"><a href="#SubCoroutineNotFoundError-54"><span class="linenos">54</span></a><span class="k">class</span> <span class="nc">SubCoroutineNotFoundError</span><span class="p">(</span><span class="n">CoroutineNotFoundError</span><span class="p">):</span>
</span><span id="SubCoroutineNotFoundError-55"><a href="#SubCoroutineNotFoundError-55"><span class="linenos">55</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="SubCoroutineNotFoundError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="SubCoroutineNotFoundError.with_traceback" class="function">with_traceback</dd>
                <dd id="SubCoroutineNotFoundError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TimeoutError">
                            <input id="TimeoutError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TimeoutError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="TimeoutError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimeoutError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimeoutError-58"><a href="#TimeoutError-58"><span class="linenos">58</span></a><span class="k">class</span> <span class="nc">TimeoutError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="TimeoutError-59"><a href="#TimeoutError-59"><span class="linenos">59</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="TimeoutError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="TimeoutError.with_traceback" class="function">with_traceback</dd>
                <dd id="TimeoutError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="SubTimeoutError">
                            <input id="SubTimeoutError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SubTimeoutError</span><wbr>(<span class="base"><a href="#TimeoutError">TimeoutError</a></span>):

                <label class="view-source-button" for="SubTimeoutError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubTimeoutError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubTimeoutError-62"><a href="#SubTimeoutError-62"><span class="linenos">62</span></a><span class="k">class</span> <span class="nc">SubTimeoutError</span><span class="p">(</span><span class="ne">TimeoutError</span><span class="p">):</span>
</span><span id="SubTimeoutError-63"><a href="#SubTimeoutError-63"><span class="linenos">63</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="SubTimeoutError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="SubTimeoutError.with_traceback" class="function">with_traceback</dd>
                <dd id="SubTimeoutError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>