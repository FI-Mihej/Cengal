---
title: known_asyncio_compatible_loops
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.asyncio_loop<wbr>.versions<wbr>.v_0<wbr>.known_asyncio_compatible_loops    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-known_asyncio_compatible_loops-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-known_asyncio_compatible_loops-view-source"><span>View Source</span></label>

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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.1&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;prepare_loop&#39;</span><span class="p">,</span> <span class="s1">&#39;restore_loop&#39;</span><span class="p">,</span> <span class="s1">&#39;DerivedFromProactorEventLoop&#39;</span><span class="p">,</span> <span class="s1">&#39;DerivedFromSelectorEventLoop&#39;</span><span class="p">,</span> <span class="s1">&#39;DerivedFromUVLoop&#39;</span><span class="p">]</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">Coro</span><span class="p">,</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="n">current_interface</span><span class="p">,</span> <span class="n">current_coro_scheduler</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">,</span> <span class="n">cs_acoro</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.conversion.reinterpret_cast</span> <span class="kn">import</span> <span class="n">reinterpret_cast</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.conversion.reinterpret_cast_management.manager</span> <span class="kn">import</span> <span class="n">BaseAutoDerivedObjWrapper</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">SelectorEventLoop</span><span class="p">,</span> <span class="n">AbstractEventLoop</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="n">_proactor_present</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>    <span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">ProactorEventLoop</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="n">_proactor_present</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="k">pass</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="kn">from</span> <span class="nn">uvloop</span> <span class="kn">import</span> <span class="n">Loop</span> <span class="k">as</span> <span class="n">UVLoop</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Any</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="k">def</span> <span class="nf">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="k">def</span> <span class="nf">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="k">def</span> <span class="nf">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="c1"># Method scheduling a coroutine object: create a task.</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="c1"># Methods for interacting with threads.</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="k">def</span> <span class="nf">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="k">def</span> <span class="nf">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a><span class="k">def</span> <span class="nf">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a><span class="k">def</span> <span class="nf">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a><span class="c1"># Signal handling.</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a><span class="k">def</span> <span class="nf">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>    <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="k">class</span> <span class="nc">LoopWrapper</span><span class="p">(</span><span class="n">BaseAutoDerivedObjWrapper</span><span class="p">):</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">wrapping_required</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">planned_type_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="nb">issubclass</span><span class="p">(</span><span class="n">base_type</span><span class="p">,</span> <span class="n">AbstractEventLoop</span><span class="p">)</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">methods</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>            <span class="s1">&#39;call_soon&#39;</span><span class="p">:</span> <span class="n">call_soon</span><span class="p">,</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>            <span class="s1">&#39;call_later&#39;</span><span class="p">:</span> <span class="n">call_later</span><span class="p">,</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>            <span class="s1">&#39;call_at&#39;</span><span class="p">:</span> <span class="n">call_at</span><span class="p">,</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>            <span class="s1">&#39;create_task&#39;</span><span class="p">:</span> <span class="n">create_task</span><span class="p">,</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>            <span class="s1">&#39;call_soon_threadsafe&#39;</span><span class="p">:</span> <span class="n">call_soon_threadsafe</span><span class="p">,</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>            <span class="s1">&#39;run_in_executor&#39;</span><span class="p">:</span> <span class="n">run_in_executor</span><span class="p">,</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>            <span class="s1">&#39;add_reader&#39;</span><span class="p">:</span> <span class="n">add_reader</span><span class="p">,</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>            <span class="s1">&#39;add_writer&#39;</span><span class="p">:</span> <span class="n">add_writer</span><span class="p">,</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>            <span class="s1">&#39;add_signal_handler&#39;</span><span class="p">:</span> <span class="n">add_signal_handler</span><span class="p">,</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="p">}</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a><span class="n">_lw</span><span class="p">:</span> <span class="n">LoopWrapper</span> <span class="o">=</span> <span class="n">LoopWrapper</span><span class="p">()</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a><span class="k">def</span> <span class="nf">prepare_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">AbstractEventLoop</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">:</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="k">if</span> <span class="n">_proactor_present</span> <span class="ow">and</span> <span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span> <span class="ow">is</span> <span class="n">ProactorEventLoop</span><span class="p">:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">DerivedFromProactorEventLoop</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="k">return</span> <span class="n">ProactorEventLoop</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span> <span class="ow">is</span> <span class="n">SelectorEventLoop</span><span class="p">:</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">DerivedFromSelectorEventLoop</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>    <span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span> <span class="ow">is</span> <span class="n">UVLoop</span><span class="p">:</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">DerivedFromUVLoop</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="k">return</span> <span class="n">UVLoop</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">AbstractEventLoop</span><span class="p">):</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="n">original_type</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="n">_lw</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="k">return</span> <span class="n">original_type</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s1">&#39;Unknown loop type: </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)))</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a><span class="k">def</span> <span class="nf">restore_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">original_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>    <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">original_type</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a><span class="k">if</span> <span class="n">_proactor_present</span><span class="p">:</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>    <span class="k">class</span> <span class="nc">DerivedFromProactorEventLoop</span><span class="p">(</span><span class="n">ProactorEventLoop</span><span class="p">):</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>        <span class="k">def</span> <span class="nf">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="k">def</span> <span class="nf">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>        <span class="k">def</span> <span class="nf">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="c1"># Method scheduling a coroutine object: create a task.</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="c1"># Methods for interacting with threads.</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="k">def</span> <span class="nf">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="k">def</span> <span class="nf">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="k">def</span> <span class="nf">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>        <span class="k">def</span> <span class="nf">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        <span class="c1"># Signal handling.</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>        <span class="k">def</span> <span class="nf">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="k">return</span> <span class="n">ProactorEventLoop</span><span class="o">.</span><span class="n">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a><span class="k">class</span> <span class="nc">DerivedFromSelectorEventLoop</span><span class="p">(</span><span class="n">SelectorEventLoop</span><span class="p">):</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>    <span class="k">def</span> <span class="nf">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>    <span class="k">def</span> <span class="nf">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="nf">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>    <span class="c1"># Method scheduling a coroutine object: create a task.</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>    <span class="c1"># Methods for interacting with threads.</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>    <span class="k">def</span> <span class="nf">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>    <span class="k">def</span> <span class="nf">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="nf">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>    <span class="c1"># Signal handling.</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>    <span class="k">def</span> <span class="nf">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="k">class</span> <span class="nc">DerivedFromUVLoop</span><span class="p">(</span><span class="n">UVLoop</span><span class="p">):</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>    <span class="k">def</span> <span class="nf">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>    <span class="k">def</span> <span class="nf">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>    <span class="k">def</span> <span class="nf">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>    <span class="c1"># Method scheduling a coroutine object: create a task.</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>    <span class="c1"># Methods for interacting with threads.</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>    <span class="k">def</span> <span class="nf">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>    <span class="k">def</span> <span class="nf">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>    <span class="k">def</span> <span class="nf">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="nf">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>    <span class="c1"># Signal handling.</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>    <span class="k">def</span> <span class="nf">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="prepare_loop">
                            <input id="prepare_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">prepare_loop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span></span><span class="return-annotation">) -> <span class="n">Type</span>:</span></span>

                <label class="view-source-button" for="prepare_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#prepare_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="prepare_loop-147"><a href="#prepare_loop-147"><span class="linenos">147</span></a><span class="k">def</span> <span class="nf">prepare_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">AbstractEventLoop</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Type</span><span class="p">:</span>
</span><span id="prepare_loop-148"><a href="#prepare_loop-148"><span class="linenos">148</span></a>    <span class="k">if</span> <span class="n">_proactor_present</span> <span class="ow">and</span> <span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span> <span class="ow">is</span> <span class="n">ProactorEventLoop</span><span class="p">:</span>
</span><span id="prepare_loop-149"><a href="#prepare_loop-149"><span class="linenos">149</span></a>        <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">DerivedFromProactorEventLoop</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="prepare_loop-150"><a href="#prepare_loop-150"><span class="linenos">150</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="prepare_loop-151"><a href="#prepare_loop-151"><span class="linenos">151</span></a>        <span class="k">return</span> <span class="n">ProactorEventLoop</span>
</span><span id="prepare_loop-152"><a href="#prepare_loop-152"><span class="linenos">152</span></a>    <span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span> <span class="ow">is</span> <span class="n">SelectorEventLoop</span><span class="p">:</span>
</span><span id="prepare_loop-153"><a href="#prepare_loop-153"><span class="linenos">153</span></a>        <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">DerivedFromSelectorEventLoop</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="prepare_loop-154"><a href="#prepare_loop-154"><span class="linenos">154</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="prepare_loop-155"><a href="#prepare_loop-155"><span class="linenos">155</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span>
</span><span id="prepare_loop-156"><a href="#prepare_loop-156"><span class="linenos">156</span></a>    <span class="k">elif</span> <span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span> <span class="ow">is</span> <span class="n">UVLoop</span><span class="p">:</span>
</span><span id="prepare_loop-157"><a href="#prepare_loop-157"><span class="linenos">157</span></a>        <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">DerivedFromUVLoop</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="prepare_loop-158"><a href="#prepare_loop-158"><span class="linenos">158</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="prepare_loop-159"><a href="#prepare_loop-159"><span class="linenos">159</span></a>        <span class="k">return</span> <span class="n">UVLoop</span>
</span><span id="prepare_loop-160"><a href="#prepare_loop-160"><span class="linenos">160</span></a>    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">AbstractEventLoop</span><span class="p">):</span>
</span><span id="prepare_loop-161"><a href="#prepare_loop-161"><span class="linenos">161</span></a>        <span class="n">original_type</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="prepare_loop-162"><a href="#prepare_loop-162"><span class="linenos">162</span></a>        <span class="n">_lw</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="prepare_loop-163"><a href="#prepare_loop-163"><span class="linenos">163</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="prepare_loop-164"><a href="#prepare_loop-164"><span class="linenos">164</span></a>        <span class="k">return</span> <span class="n">original_type</span>
</span><span id="prepare_loop-165"><a href="#prepare_loop-165"><span class="linenos">165</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="prepare_loop-166"><a href="#prepare_loop-166"><span class="linenos">166</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s1">&#39;Unknown loop type: </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">loop</span><span class="p">)))</span>
</span></pre></div>


    

                </section>
                <section id="restore_loop">
                            <input id="restore_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">restore_loop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>, </span><span class="param"><span class="n">original_type</span><span class="p">:</span> <span class="n">Type</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="restore_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#restore_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="restore_loop-169"><a href="#restore_loop-169"><span class="linenos">169</span></a><span class="k">def</span> <span class="nf">restore_loop</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">original_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="restore_loop-170"><a href="#restore_loop-170"><span class="linenos">170</span></a>    <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">original_type</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="DerivedFromProactorEventLoop">
                    <div class="attr variable">
            <span class="name">DerivedFromProactorEventLoop</span>

        
    </div>
    <a class="headerlink" href="#DerivedFromProactorEventLoop"></a>
    
    

                </section>
                <section id="DerivedFromSelectorEventLoop">
                            <input id="DerivedFromSelectorEventLoop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">DerivedFromSelectorEventLoop</span><wbr>(<span class="base">asyncio.unix_events._UnixSelectorEventLoop</span>):

                <label class="view-source-button" for="DerivedFromSelectorEventLoop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop-245"><a href="#DerivedFromSelectorEventLoop-245"><span class="linenos">245</span></a><span class="k">class</span> <span class="nc">DerivedFromSelectorEventLoop</span><span class="p">(</span><span class="n">SelectorEventLoop</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-246"><a href="#DerivedFromSelectorEventLoop-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="nf">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-247"><a href="#DerivedFromSelectorEventLoop-247"><span class="linenos">247</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-248"><a href="#DerivedFromSelectorEventLoop-248"><span class="linenos">248</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-249"><a href="#DerivedFromSelectorEventLoop-249"><span class="linenos">249</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-250"><a href="#DerivedFromSelectorEventLoop-250"><span class="linenos">250</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-251"><a href="#DerivedFromSelectorEventLoop-251"><span class="linenos">251</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-252"><a href="#DerivedFromSelectorEventLoop-252"><span class="linenos">252</span></a>
</span><span id="DerivedFromSelectorEventLoop-253"><a href="#DerivedFromSelectorEventLoop-253"><span class="linenos">253</span></a>    <span class="k">def</span> <span class="nf">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-254"><a href="#DerivedFromSelectorEventLoop-254"><span class="linenos">254</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-255"><a href="#DerivedFromSelectorEventLoop-255"><span class="linenos">255</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-256"><a href="#DerivedFromSelectorEventLoop-256"><span class="linenos">256</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-257"><a href="#DerivedFromSelectorEventLoop-257"><span class="linenos">257</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-258"><a href="#DerivedFromSelectorEventLoop-258"><span class="linenos">258</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-259"><a href="#DerivedFromSelectorEventLoop-259"><span class="linenos">259</span></a>
</span><span id="DerivedFromSelectorEventLoop-260"><a href="#DerivedFromSelectorEventLoop-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="nf">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-261"><a href="#DerivedFromSelectorEventLoop-261"><span class="linenos">261</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-262"><a href="#DerivedFromSelectorEventLoop-262"><span class="linenos">262</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-263"><a href="#DerivedFromSelectorEventLoop-263"><span class="linenos">263</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-264"><a href="#DerivedFromSelectorEventLoop-264"><span class="linenos">264</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-265"><a href="#DerivedFromSelectorEventLoop-265"><span class="linenos">265</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-266"><a href="#DerivedFromSelectorEventLoop-266"><span class="linenos">266</span></a>
</span><span id="DerivedFromSelectorEventLoop-267"><a href="#DerivedFromSelectorEventLoop-267"><span class="linenos">267</span></a>    <span class="c1"># Method scheduling a coroutine object: create a task.</span>
</span><span id="DerivedFromSelectorEventLoop-268"><a href="#DerivedFromSelectorEventLoop-268"><span class="linenos">268</span></a>
</span><span id="DerivedFromSelectorEventLoop-269"><a href="#DerivedFromSelectorEventLoop-269"><span class="linenos">269</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-270"><a href="#DerivedFromSelectorEventLoop-270"><span class="linenos">270</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-271"><a href="#DerivedFromSelectorEventLoop-271"><span class="linenos">271</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-272"><a href="#DerivedFromSelectorEventLoop-272"><span class="linenos">272</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-273"><a href="#DerivedFromSelectorEventLoop-273"><span class="linenos">273</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-274"><a href="#DerivedFromSelectorEventLoop-274"><span class="linenos">274</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-275"><a href="#DerivedFromSelectorEventLoop-275"><span class="linenos">275</span></a>
</span><span id="DerivedFromSelectorEventLoop-276"><a href="#DerivedFromSelectorEventLoop-276"><span class="linenos">276</span></a>    <span class="c1"># Methods for interacting with threads.</span>
</span><span id="DerivedFromSelectorEventLoop-277"><a href="#DerivedFromSelectorEventLoop-277"><span class="linenos">277</span></a>
</span><span id="DerivedFromSelectorEventLoop-278"><a href="#DerivedFromSelectorEventLoop-278"><span class="linenos">278</span></a>    <span class="k">def</span> <span class="nf">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-279"><a href="#DerivedFromSelectorEventLoop-279"><span class="linenos">279</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-280"><a href="#DerivedFromSelectorEventLoop-280"><span class="linenos">280</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-281"><a href="#DerivedFromSelectorEventLoop-281"><span class="linenos">281</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-282"><a href="#DerivedFromSelectorEventLoop-282"><span class="linenos">282</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-283"><a href="#DerivedFromSelectorEventLoop-283"><span class="linenos">283</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-284"><a href="#DerivedFromSelectorEventLoop-284"><span class="linenos">284</span></a>
</span><span id="DerivedFromSelectorEventLoop-285"><a href="#DerivedFromSelectorEventLoop-285"><span class="linenos">285</span></a>    <span class="k">def</span> <span class="nf">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-286"><a href="#DerivedFromSelectorEventLoop-286"><span class="linenos">286</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-287"><a href="#DerivedFromSelectorEventLoop-287"><span class="linenos">287</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-288"><a href="#DerivedFromSelectorEventLoop-288"><span class="linenos">288</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-289"><a href="#DerivedFromSelectorEventLoop-289"><span class="linenos">289</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-290"><a href="#DerivedFromSelectorEventLoop-290"><span class="linenos">290</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-291"><a href="#DerivedFromSelectorEventLoop-291"><span class="linenos">291</span></a>
</span><span id="DerivedFromSelectorEventLoop-292"><a href="#DerivedFromSelectorEventLoop-292"><span class="linenos">292</span></a>    <span class="k">def</span> <span class="nf">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-293"><a href="#DerivedFromSelectorEventLoop-293"><span class="linenos">293</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-294"><a href="#DerivedFromSelectorEventLoop-294"><span class="linenos">294</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-295"><a href="#DerivedFromSelectorEventLoop-295"><span class="linenos">295</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-296"><a href="#DerivedFromSelectorEventLoop-296"><span class="linenos">296</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-297"><a href="#DerivedFromSelectorEventLoop-297"><span class="linenos">297</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-298"><a href="#DerivedFromSelectorEventLoop-298"><span class="linenos">298</span></a>
</span><span id="DerivedFromSelectorEventLoop-299"><a href="#DerivedFromSelectorEventLoop-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-300"><a href="#DerivedFromSelectorEventLoop-300"><span class="linenos">300</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-301"><a href="#DerivedFromSelectorEventLoop-301"><span class="linenos">301</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-302"><a href="#DerivedFromSelectorEventLoop-302"><span class="linenos">302</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-303"><a href="#DerivedFromSelectorEventLoop-303"><span class="linenos">303</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-304"><a href="#DerivedFromSelectorEventLoop-304"><span class="linenos">304</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-305"><a href="#DerivedFromSelectorEventLoop-305"><span class="linenos">305</span></a>
</span><span id="DerivedFromSelectorEventLoop-306"><a href="#DerivedFromSelectorEventLoop-306"><span class="linenos">306</span></a>    <span class="c1"># Signal handling.</span>
</span><span id="DerivedFromSelectorEventLoop-307"><a href="#DerivedFromSelectorEventLoop-307"><span class="linenos">307</span></a>
</span><span id="DerivedFromSelectorEventLoop-308"><a href="#DerivedFromSelectorEventLoop-308"><span class="linenos">308</span></a>    <span class="k">def</span> <span class="nf">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop-309"><a href="#DerivedFromSelectorEventLoop-309"><span class="linenos">309</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop-310"><a href="#DerivedFromSelectorEventLoop-310"><span class="linenos">310</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop-311"><a href="#DerivedFromSelectorEventLoop-311"><span class="linenos">311</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop-312"><a href="#DerivedFromSelectorEventLoop-312"><span class="linenos">312</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop-313"><a href="#DerivedFromSelectorEventLoop-313"><span class="linenos">313</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Unix event loop.</p>

<p>Adds signal handling and UNIX Domain Socket support to SelectorEventLoop.</p>
</div>


                            <div id="DerivedFromSelectorEventLoop.call_soon" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.call_soon-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_soon</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.call_soon-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.call_soon"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.call_soon-246"><a href="#DerivedFromSelectorEventLoop.call_soon-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="nf">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon-247"><a href="#DerivedFromSelectorEventLoop.call_soon-247"><span class="linenos">247</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon-248"><a href="#DerivedFromSelectorEventLoop.call_soon-248"><span class="linenos">248</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon-249"><a href="#DerivedFromSelectorEventLoop.call_soon-249"><span class="linenos">249</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon-250"><a href="#DerivedFromSelectorEventLoop.call_soon-250"><span class="linenos">250</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon-251"><a href="#DerivedFromSelectorEventLoop.call_soon-251"><span class="linenos">251</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Arrange for a callback to be called as soon as possible.</p>

<p>This operates as a FIFO queue: callbacks are called in the
order in which they are registered.  Each callback will be
called exactly once.</p>

<p>Any positional arguments after the callback will be passed to
the callback when it is called.</p>
</div>


                            </div>
                            <div id="DerivedFromSelectorEventLoop.call_later" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.call_later-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_later</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">delay</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.call_later-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.call_later"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.call_later-253"><a href="#DerivedFromSelectorEventLoop.call_later-253"><span class="linenos">253</span></a>    <span class="k">def</span> <span class="nf">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.call_later-254"><a href="#DerivedFromSelectorEventLoop.call_later-254"><span class="linenos">254</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.call_later-255"><a href="#DerivedFromSelectorEventLoop.call_later-255"><span class="linenos">255</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.call_later-256"><a href="#DerivedFromSelectorEventLoop.call_later-256"><span class="linenos">256</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.call_later-257"><a href="#DerivedFromSelectorEventLoop.call_later-257"><span class="linenos">257</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.call_later-258"><a href="#DerivedFromSelectorEventLoop.call_later-258"><span class="linenos">258</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Arrange for a callback to be called at a given time.</p>

<p>Return a Handle: an opaque object with a cancel() method that
can be used to cancel the call.</p>

<p>The delay can be an int or float, expressed in seconds.  It is
always relative to the current time.</p>

<p>Each callback will be called exactly once.  If two callbacks
are scheduled for exactly the same time, it undefined which
will be called first.</p>

<p>Any positional arguments after the callback will be passed to
the callback when it is called.</p>
</div>


                            </div>
                            <div id="DerivedFromSelectorEventLoop.call_at" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.call_at-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_at</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">when</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.call_at-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.call_at"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.call_at-260"><a href="#DerivedFromSelectorEventLoop.call_at-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="nf">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.call_at-261"><a href="#DerivedFromSelectorEventLoop.call_at-261"><span class="linenos">261</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.call_at-262"><a href="#DerivedFromSelectorEventLoop.call_at-262"><span class="linenos">262</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.call_at-263"><a href="#DerivedFromSelectorEventLoop.call_at-263"><span class="linenos">263</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.call_at-264"><a href="#DerivedFromSelectorEventLoop.call_at-264"><span class="linenos">264</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.call_at-265"><a href="#DerivedFromSelectorEventLoop.call_at-265"><span class="linenos">265</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Like call_later(), but uses an absolute time.</p>

<p>Absolute time corresponds to the event loop's time() method.</p>
</div>


                            </div>
                            <div id="DerivedFromSelectorEventLoop.create_task" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.create_task-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">create_task</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.create_task-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.create_task"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.create_task-269"><a href="#DerivedFromSelectorEventLoop.create_task-269"><span class="linenos">269</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.create_task-270"><a href="#DerivedFromSelectorEventLoop.create_task-270"><span class="linenos">270</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.create_task-271"><a href="#DerivedFromSelectorEventLoop.create_task-271"><span class="linenos">271</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.create_task-272"><a href="#DerivedFromSelectorEventLoop.create_task-272"><span class="linenos">272</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.create_task-273"><a href="#DerivedFromSelectorEventLoop.create_task-273"><span class="linenos">273</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.create_task-274"><a href="#DerivedFromSelectorEventLoop.create_task-274"><span class="linenos">274</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Schedule a coroutine object.</p>

<p>Return a task object.</p>
</div>


                            </div>
                            <div id="DerivedFromSelectorEventLoop.call_soon_threadsafe" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.call_soon_threadsafe-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_soon_threadsafe</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.call_soon_threadsafe-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.call_soon_threadsafe"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.call_soon_threadsafe-278"><a href="#DerivedFromSelectorEventLoop.call_soon_threadsafe-278"><span class="linenos">278</span></a>    <span class="k">def</span> <span class="nf">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon_threadsafe-279"><a href="#DerivedFromSelectorEventLoop.call_soon_threadsafe-279"><span class="linenos">279</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon_threadsafe-280"><a href="#DerivedFromSelectorEventLoop.call_soon_threadsafe-280"><span class="linenos">280</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon_threadsafe-281"><a href="#DerivedFromSelectorEventLoop.call_soon_threadsafe-281"><span class="linenos">281</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon_threadsafe-282"><a href="#DerivedFromSelectorEventLoop.call_soon_threadsafe-282"><span class="linenos">282</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.call_soon_threadsafe-283"><a href="#DerivedFromSelectorEventLoop.call_soon_threadsafe-283"><span class="linenos">283</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Like call_soon(), but thread-safe.</p>
</div>


                            </div>
                            <div id="DerivedFromSelectorEventLoop.run_in_executor" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.run_in_executor-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run_in_executor</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">executor</span>, </span><span class="param"><span class="n">func</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.run_in_executor-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.run_in_executor"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.run_in_executor-285"><a href="#DerivedFromSelectorEventLoop.run_in_executor-285"><span class="linenos">285</span></a>    <span class="k">def</span> <span class="nf">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.run_in_executor-286"><a href="#DerivedFromSelectorEventLoop.run_in_executor-286"><span class="linenos">286</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.run_in_executor-287"><a href="#DerivedFromSelectorEventLoop.run_in_executor-287"><span class="linenos">287</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.run_in_executor-288"><a href="#DerivedFromSelectorEventLoop.run_in_executor-288"><span class="linenos">288</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.run_in_executor-289"><a href="#DerivedFromSelectorEventLoop.run_in_executor-289"><span class="linenos">289</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.run_in_executor-290"><a href="#DerivedFromSelectorEventLoop.run_in_executor-290"><span class="linenos">290</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="DerivedFromSelectorEventLoop.add_reader" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.add_reader-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_reader</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">fd</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.add_reader-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.add_reader"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.add_reader-292"><a href="#DerivedFromSelectorEventLoop.add_reader-292"><span class="linenos">292</span></a>    <span class="k">def</span> <span class="nf">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.add_reader-293"><a href="#DerivedFromSelectorEventLoop.add_reader-293"><span class="linenos">293</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.add_reader-294"><a href="#DerivedFromSelectorEventLoop.add_reader-294"><span class="linenos">294</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.add_reader-295"><a href="#DerivedFromSelectorEventLoop.add_reader-295"><span class="linenos">295</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.add_reader-296"><a href="#DerivedFromSelectorEventLoop.add_reader-296"><span class="linenos">296</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.add_reader-297"><a href="#DerivedFromSelectorEventLoop.add_reader-297"><span class="linenos">297</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Add a reader callback.</p>
</div>


                            </div>
                            <div id="DerivedFromSelectorEventLoop.add_writer" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.add_writer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_writer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">fd</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.add_writer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.add_writer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.add_writer-299"><a href="#DerivedFromSelectorEventLoop.add_writer-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.add_writer-300"><a href="#DerivedFromSelectorEventLoop.add_writer-300"><span class="linenos">300</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.add_writer-301"><a href="#DerivedFromSelectorEventLoop.add_writer-301"><span class="linenos">301</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.add_writer-302"><a href="#DerivedFromSelectorEventLoop.add_writer-302"><span class="linenos">302</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.add_writer-303"><a href="#DerivedFromSelectorEventLoop.add_writer-303"><span class="linenos">303</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.add_writer-304"><a href="#DerivedFromSelectorEventLoop.add_writer-304"><span class="linenos">304</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Add a writer callback..</p>
</div>


                            </div>
                            <div id="DerivedFromSelectorEventLoop.add_signal_handler" class="classattr">
                                        <input id="DerivedFromSelectorEventLoop.add_signal_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_signal_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">sig</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromSelectorEventLoop.add_signal_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromSelectorEventLoop.add_signal_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromSelectorEventLoop.add_signal_handler-308"><a href="#DerivedFromSelectorEventLoop.add_signal_handler-308"><span class="linenos">308</span></a>    <span class="k">def</span> <span class="nf">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromSelectorEventLoop.add_signal_handler-309"><a href="#DerivedFromSelectorEventLoop.add_signal_handler-309"><span class="linenos">309</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromSelectorEventLoop.add_signal_handler-310"><a href="#DerivedFromSelectorEventLoop.add_signal_handler-310"><span class="linenos">310</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromSelectorEventLoop.add_signal_handler-311"><a href="#DerivedFromSelectorEventLoop.add_signal_handler-311"><span class="linenos">311</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromSelectorEventLoop.add_signal_handler-312"><a href="#DerivedFromSelectorEventLoop.add_signal_handler-312"><span class="linenos">312</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromSelectorEventLoop.add_signal_handler-313"><a href="#DerivedFromSelectorEventLoop.add_signal_handler-313"><span class="linenos">313</span></a>        <span class="k">return</span> <span class="n">SelectorEventLoop</span><span class="o">.</span><span class="n">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Add a handler for a signal.  UNIX only.</p>

<p>Raise ValueError if the signal number is invalid or uncatchable.
Raise RuntimeError if there is a problem setting up the handler.</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>asyncio.unix_events._UnixSelectorEventLoop</dt>
                                <dd id="DerivedFromSelectorEventLoop.__init__" class="function">_UnixSelectorEventLoop</dd>
                <dd id="DerivedFromSelectorEventLoop.close" class="function">close</dd>
                <dd id="DerivedFromSelectorEventLoop.remove_signal_handler" class="function">remove_signal_handler</dd>
                <dd id="DerivedFromSelectorEventLoop.create_unix_connection" class="function">create_unix_connection</dd>
                <dd id="DerivedFromSelectorEventLoop.create_unix_server" class="function">create_unix_server</dd>

            </div>
            <div><dt>asyncio.selector_events.BaseSelectorEventLoop</dt>
                                <dd id="DerivedFromSelectorEventLoop.remove_reader" class="function">remove_reader</dd>
                <dd id="DerivedFromSelectorEventLoop.remove_writer" class="function">remove_writer</dd>
                <dd id="DerivedFromSelectorEventLoop.sock_recv" class="function">sock_recv</dd>
                <dd id="DerivedFromSelectorEventLoop.sock_recv_into" class="function">sock_recv_into</dd>
                <dd id="DerivedFromSelectorEventLoop.sock_sendall" class="function">sock_sendall</dd>
                <dd id="DerivedFromSelectorEventLoop.sock_connect" class="function">sock_connect</dd>
                <dd id="DerivedFromSelectorEventLoop.sock_accept" class="function">sock_accept</dd>

            </div>
            <div><dt>asyncio.base_events.BaseEventLoop</dt>
                                <dd id="DerivedFromSelectorEventLoop.slow_callback_duration" class="variable">slow_callback_duration</dd>
                <dd id="DerivedFromSelectorEventLoop.create_future" class="function">create_future</dd>
                <dd id="DerivedFromSelectorEventLoop.set_task_factory" class="function">set_task_factory</dd>
                <dd id="DerivedFromSelectorEventLoop.get_task_factory" class="function">get_task_factory</dd>
                <dd id="DerivedFromSelectorEventLoop.shutdown_asyncgens" class="function">shutdown_asyncgens</dd>
                <dd id="DerivedFromSelectorEventLoop.run_forever" class="function">run_forever</dd>
                <dd id="DerivedFromSelectorEventLoop.run_until_complete" class="function">run_until_complete</dd>
                <dd id="DerivedFromSelectorEventLoop.stop" class="function">stop</dd>
                <dd id="DerivedFromSelectorEventLoop.is_closed" class="function">is_closed</dd>
                <dd id="DerivedFromSelectorEventLoop.is_running" class="function">is_running</dd>
                <dd id="DerivedFromSelectorEventLoop.time" class="function">time</dd>
                <dd id="DerivedFromSelectorEventLoop.set_default_executor" class="function">set_default_executor</dd>
                <dd id="DerivedFromSelectorEventLoop.getaddrinfo" class="function">getaddrinfo</dd>
                <dd id="DerivedFromSelectorEventLoop.getnameinfo" class="function">getnameinfo</dd>
                <dd id="DerivedFromSelectorEventLoop.sock_sendfile" class="function">sock_sendfile</dd>
                <dd id="DerivedFromSelectorEventLoop.create_connection" class="function">create_connection</dd>
                <dd id="DerivedFromSelectorEventLoop.sendfile" class="function">sendfile</dd>
                <dd id="DerivedFromSelectorEventLoop.start_tls" class="function">start_tls</dd>
                <dd id="DerivedFromSelectorEventLoop.create_datagram_endpoint" class="function">create_datagram_endpoint</dd>
                <dd id="DerivedFromSelectorEventLoop.create_server" class="function">create_server</dd>
                <dd id="DerivedFromSelectorEventLoop.connect_accepted_socket" class="function">connect_accepted_socket</dd>
                <dd id="DerivedFromSelectorEventLoop.connect_read_pipe" class="function">connect_read_pipe</dd>
                <dd id="DerivedFromSelectorEventLoop.connect_write_pipe" class="function">connect_write_pipe</dd>
                <dd id="DerivedFromSelectorEventLoop.subprocess_shell" class="function">subprocess_shell</dd>
                <dd id="DerivedFromSelectorEventLoop.subprocess_exec" class="function">subprocess_exec</dd>
                <dd id="DerivedFromSelectorEventLoop.get_exception_handler" class="function">get_exception_handler</dd>
                <dd id="DerivedFromSelectorEventLoop.set_exception_handler" class="function">set_exception_handler</dd>
                <dd id="DerivedFromSelectorEventLoop.default_exception_handler" class="function">default_exception_handler</dd>
                <dd id="DerivedFromSelectorEventLoop.call_exception_handler" class="function">call_exception_handler</dd>
                <dd id="DerivedFromSelectorEventLoop.get_debug" class="function">get_debug</dd>
                <dd id="DerivedFromSelectorEventLoop.set_debug" class="function">set_debug</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="DerivedFromUVLoop">
                            <input id="DerivedFromUVLoop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">DerivedFromUVLoop</span><wbr>(<span class="base">uvloop.Loop</span>):

                <label class="view-source-button" for="DerivedFromUVLoop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop-316"><a href="#DerivedFromUVLoop-316"><span class="linenos">316</span></a><span class="k">class</span> <span class="nc">DerivedFromUVLoop</span><span class="p">(</span><span class="n">UVLoop</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-317"><a href="#DerivedFromUVLoop-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-318"><a href="#DerivedFromUVLoop-318"><span class="linenos">318</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-319"><a href="#DerivedFromUVLoop-319"><span class="linenos">319</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-320"><a href="#DerivedFromUVLoop-320"><span class="linenos">320</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-321"><a href="#DerivedFromUVLoop-321"><span class="linenos">321</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-322"><a href="#DerivedFromUVLoop-322"><span class="linenos">322</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-323"><a href="#DerivedFromUVLoop-323"><span class="linenos">323</span></a>
</span><span id="DerivedFromUVLoop-324"><a href="#DerivedFromUVLoop-324"><span class="linenos">324</span></a>    <span class="k">def</span> <span class="nf">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-325"><a href="#DerivedFromUVLoop-325"><span class="linenos">325</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-326"><a href="#DerivedFromUVLoop-326"><span class="linenos">326</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-327"><a href="#DerivedFromUVLoop-327"><span class="linenos">327</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-328"><a href="#DerivedFromUVLoop-328"><span class="linenos">328</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-329"><a href="#DerivedFromUVLoop-329"><span class="linenos">329</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-330"><a href="#DerivedFromUVLoop-330"><span class="linenos">330</span></a>
</span><span id="DerivedFromUVLoop-331"><a href="#DerivedFromUVLoop-331"><span class="linenos">331</span></a>    <span class="k">def</span> <span class="nf">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-332"><a href="#DerivedFromUVLoop-332"><span class="linenos">332</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-333"><a href="#DerivedFromUVLoop-333"><span class="linenos">333</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-334"><a href="#DerivedFromUVLoop-334"><span class="linenos">334</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-335"><a href="#DerivedFromUVLoop-335"><span class="linenos">335</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-336"><a href="#DerivedFromUVLoop-336"><span class="linenos">336</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-337"><a href="#DerivedFromUVLoop-337"><span class="linenos">337</span></a>
</span><span id="DerivedFromUVLoop-338"><a href="#DerivedFromUVLoop-338"><span class="linenos">338</span></a>    <span class="c1"># Method scheduling a coroutine object: create a task.</span>
</span><span id="DerivedFromUVLoop-339"><a href="#DerivedFromUVLoop-339"><span class="linenos">339</span></a>
</span><span id="DerivedFromUVLoop-340"><a href="#DerivedFromUVLoop-340"><span class="linenos">340</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-341"><a href="#DerivedFromUVLoop-341"><span class="linenos">341</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-342"><a href="#DerivedFromUVLoop-342"><span class="linenos">342</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-343"><a href="#DerivedFromUVLoop-343"><span class="linenos">343</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-344"><a href="#DerivedFromUVLoop-344"><span class="linenos">344</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-345"><a href="#DerivedFromUVLoop-345"><span class="linenos">345</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-346"><a href="#DerivedFromUVLoop-346"><span class="linenos">346</span></a>
</span><span id="DerivedFromUVLoop-347"><a href="#DerivedFromUVLoop-347"><span class="linenos">347</span></a>    <span class="c1"># Methods for interacting with threads.</span>
</span><span id="DerivedFromUVLoop-348"><a href="#DerivedFromUVLoop-348"><span class="linenos">348</span></a>
</span><span id="DerivedFromUVLoop-349"><a href="#DerivedFromUVLoop-349"><span class="linenos">349</span></a>    <span class="k">def</span> <span class="nf">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-350"><a href="#DerivedFromUVLoop-350"><span class="linenos">350</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-351"><a href="#DerivedFromUVLoop-351"><span class="linenos">351</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-352"><a href="#DerivedFromUVLoop-352"><span class="linenos">352</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-353"><a href="#DerivedFromUVLoop-353"><span class="linenos">353</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-354"><a href="#DerivedFromUVLoop-354"><span class="linenos">354</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-355"><a href="#DerivedFromUVLoop-355"><span class="linenos">355</span></a>
</span><span id="DerivedFromUVLoop-356"><a href="#DerivedFromUVLoop-356"><span class="linenos">356</span></a>    <span class="k">def</span> <span class="nf">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-357"><a href="#DerivedFromUVLoop-357"><span class="linenos">357</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-358"><a href="#DerivedFromUVLoop-358"><span class="linenos">358</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-359"><a href="#DerivedFromUVLoop-359"><span class="linenos">359</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-360"><a href="#DerivedFromUVLoop-360"><span class="linenos">360</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-361"><a href="#DerivedFromUVLoop-361"><span class="linenos">361</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-362"><a href="#DerivedFromUVLoop-362"><span class="linenos">362</span></a>
</span><span id="DerivedFromUVLoop-363"><a href="#DerivedFromUVLoop-363"><span class="linenos">363</span></a>    <span class="k">def</span> <span class="nf">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-364"><a href="#DerivedFromUVLoop-364"><span class="linenos">364</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-365"><a href="#DerivedFromUVLoop-365"><span class="linenos">365</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-366"><a href="#DerivedFromUVLoop-366"><span class="linenos">366</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-367"><a href="#DerivedFromUVLoop-367"><span class="linenos">367</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-368"><a href="#DerivedFromUVLoop-368"><span class="linenos">368</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-369"><a href="#DerivedFromUVLoop-369"><span class="linenos">369</span></a>
</span><span id="DerivedFromUVLoop-370"><a href="#DerivedFromUVLoop-370"><span class="linenos">370</span></a>    <span class="k">def</span> <span class="nf">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-371"><a href="#DerivedFromUVLoop-371"><span class="linenos">371</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-372"><a href="#DerivedFromUVLoop-372"><span class="linenos">372</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-373"><a href="#DerivedFromUVLoop-373"><span class="linenos">373</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-374"><a href="#DerivedFromUVLoop-374"><span class="linenos">374</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-375"><a href="#DerivedFromUVLoop-375"><span class="linenos">375</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-376"><a href="#DerivedFromUVLoop-376"><span class="linenos">376</span></a>
</span><span id="DerivedFromUVLoop-377"><a href="#DerivedFromUVLoop-377"><span class="linenos">377</span></a>    <span class="c1"># Signal handling.</span>
</span><span id="DerivedFromUVLoop-378"><a href="#DerivedFromUVLoop-378"><span class="linenos">378</span></a>
</span><span id="DerivedFromUVLoop-379"><a href="#DerivedFromUVLoop-379"><span class="linenos">379</span></a>    <span class="k">def</span> <span class="nf">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop-380"><a href="#DerivedFromUVLoop-380"><span class="linenos">380</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop-381"><a href="#DerivedFromUVLoop-381"><span class="linenos">381</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop-382"><a href="#DerivedFromUVLoop-382"><span class="linenos">382</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop-383"><a href="#DerivedFromUVLoop-383"><span class="linenos">383</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop-384"><a href="#DerivedFromUVLoop-384"><span class="linenos">384</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop()</p>
</div>


                            <div id="DerivedFromUVLoop.call_soon" class="classattr">
                                        <input id="DerivedFromUVLoop.call_soon-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_soon</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="n">context</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.call_soon-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.call_soon"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.call_soon-317"><a href="#DerivedFromUVLoop.call_soon-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.call_soon-318"><a href="#DerivedFromUVLoop.call_soon-318"><span class="linenos">318</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.call_soon-319"><a href="#DerivedFromUVLoop.call_soon-319"><span class="linenos">319</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.call_soon-320"><a href="#DerivedFromUVLoop.call_soon-320"><span class="linenos">320</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.call_soon-321"><a href="#DerivedFromUVLoop.call_soon-321"><span class="linenos">321</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.call_soon-322"><a href="#DerivedFromUVLoop.call_soon-322"><span class="linenos">322</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.call_soon(self, callback, *args, context=None)
Arrange for a callback to be called as soon as possible.</p>

<pre><code>    This operates as a FIFO queue: callbacks are called in the
    order in which they are registered.  Each callback will be
    called exactly once.

    Any positional arguments after the callback will be passed to
    the callback when it is called.
</code></pre>
</div>


                            </div>
                            <div id="DerivedFromUVLoop.call_later" class="classattr">
                                        <input id="DerivedFromUVLoop.call_later-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_later</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">delay</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="n">context</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.call_later-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.call_later"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.call_later-324"><a href="#DerivedFromUVLoop.call_later-324"><span class="linenos">324</span></a>    <span class="k">def</span> <span class="nf">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.call_later-325"><a href="#DerivedFromUVLoop.call_later-325"><span class="linenos">325</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.call_later-326"><a href="#DerivedFromUVLoop.call_later-326"><span class="linenos">326</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.call_later-327"><a href="#DerivedFromUVLoop.call_later-327"><span class="linenos">327</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.call_later-328"><a href="#DerivedFromUVLoop.call_later-328"><span class="linenos">328</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.call_later-329"><a href="#DerivedFromUVLoop.call_later-329"><span class="linenos">329</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.call_later(self, delay, callback, *args, context=None)
Arrange for a callback to be called at a given time.</p>

<pre><code>    Return a Handle: an opaque object with a cancel() method that
    can be used to cancel the call.

    The delay can be an int or float, expressed in seconds.  It is
    always relative to the current time.

    Each callback will be called exactly once.  If two callbacks
    are scheduled for exactly the same time, it undefined which
    will be called first.

    Any positional arguments after the callback will be passed to
    the callback when it is called.
</code></pre>
</div>


                            </div>
                            <div id="DerivedFromUVLoop.call_at" class="classattr">
                                        <input id="DerivedFromUVLoop.call_at-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_at</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">when</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="n">context</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.call_at-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.call_at"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.call_at-331"><a href="#DerivedFromUVLoop.call_at-331"><span class="linenos">331</span></a>    <span class="k">def</span> <span class="nf">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.call_at-332"><a href="#DerivedFromUVLoop.call_at-332"><span class="linenos">332</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.call_at-333"><a href="#DerivedFromUVLoop.call_at-333"><span class="linenos">333</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.call_at-334"><a href="#DerivedFromUVLoop.call_at-334"><span class="linenos">334</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.call_at-335"><a href="#DerivedFromUVLoop.call_at-335"><span class="linenos">335</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.call_at-336"><a href="#DerivedFromUVLoop.call_at-336"><span class="linenos">336</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_at</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">when</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.call_at(self, when, callback, *args, context=None)
Like call_later(), but uses an absolute time.</p>

<pre><code>    Absolute time corresponds to the event loop's time() method.
</code></pre>
</div>


                            </div>
                            <div id="DerivedFromUVLoop.create_task" class="classattr">
                                        <input id="DerivedFromUVLoop.create_task-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">create_task</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro</span>, </span><span class="param"><span class="o">*</span>, </span><span class="param"><span class="n">name</span><span class="o">=</span><span class="kc">None</span>, </span><span class="param"><span class="n">context</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.create_task-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.create_task"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.create_task-340"><a href="#DerivedFromUVLoop.create_task-340"><span class="linenos">340</span></a>    <span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.create_task-341"><a href="#DerivedFromUVLoop.create_task-341"><span class="linenos">341</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.create_task-342"><a href="#DerivedFromUVLoop.create_task-342"><span class="linenos">342</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.create_task-343"><a href="#DerivedFromUVLoop.create_task-343"><span class="linenos">343</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.create_task-344"><a href="#DerivedFromUVLoop.create_task-344"><span class="linenos">344</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.create_task-345"><a href="#DerivedFromUVLoop.create_task-345"><span class="linenos">345</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.create_task(self, coro, *, name=None, context=None)
Schedule a coroutine object.</p>

<pre><code>    Return a task object.

    If name is not None, task.set_name(name) will be called if the task
    object has the set_name attribute, true for default Task in Python 3.8.

    An optional keyword-only context argument allows specifying a custom
    contextvars.Context for the coro to run in. The current context copy is
    created when no context is provided.
</code></pre>
</div>


                            </div>
                            <div id="DerivedFromUVLoop.call_soon_threadsafe" class="classattr">
                                        <input id="DerivedFromUVLoop.call_soon_threadsafe-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_soon_threadsafe</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="n">context</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.call_soon_threadsafe-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.call_soon_threadsafe"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.call_soon_threadsafe-349"><a href="#DerivedFromUVLoop.call_soon_threadsafe-349"><span class="linenos">349</span></a>    <span class="k">def</span> <span class="nf">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.call_soon_threadsafe-350"><a href="#DerivedFromUVLoop.call_soon_threadsafe-350"><span class="linenos">350</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.call_soon_threadsafe-351"><a href="#DerivedFromUVLoop.call_soon_threadsafe-351"><span class="linenos">351</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.call_soon_threadsafe-352"><a href="#DerivedFromUVLoop.call_soon_threadsafe-352"><span class="linenos">352</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.call_soon_threadsafe-353"><a href="#DerivedFromUVLoop.call_soon_threadsafe-353"><span class="linenos">353</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.call_soon_threadsafe-354"><a href="#DerivedFromUVLoop.call_soon_threadsafe-354"><span class="linenos">354</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">call_soon_threadsafe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">context</span><span class="o">=</span><span class="n">context</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.call_soon_threadsafe(self, callback, *args, context=None)
Like call_soon(), but thread-safe.</p>
</div>


                            </div>
                            <div id="DerivedFromUVLoop.run_in_executor" class="classattr">
                                        <input id="DerivedFromUVLoop.run_in_executor-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run_in_executor</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">executor</span>, </span><span class="param"><span class="n">func</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.run_in_executor-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.run_in_executor"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.run_in_executor-356"><a href="#DerivedFromUVLoop.run_in_executor-356"><span class="linenos">356</span></a>    <span class="k">def</span> <span class="nf">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.run_in_executor-357"><a href="#DerivedFromUVLoop.run_in_executor-357"><span class="linenos">357</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.run_in_executor-358"><a href="#DerivedFromUVLoop.run_in_executor-358"><span class="linenos">358</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.run_in_executor-359"><a href="#DerivedFromUVLoop.run_in_executor-359"><span class="linenos">359</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.run_in_executor-360"><a href="#DerivedFromUVLoop.run_in_executor-360"><span class="linenos">360</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.run_in_executor-361"><a href="#DerivedFromUVLoop.run_in_executor-361"><span class="linenos">361</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">,</span> <span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.run_in_executor(self, executor, func, *args)</p>
</div>


                            </div>
                            <div id="DerivedFromUVLoop.add_reader" class="classattr">
                                        <input id="DerivedFromUVLoop.add_reader-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_reader</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">fd</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.add_reader-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.add_reader"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.add_reader-363"><a href="#DerivedFromUVLoop.add_reader-363"><span class="linenos">363</span></a>    <span class="k">def</span> <span class="nf">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.add_reader-364"><a href="#DerivedFromUVLoop.add_reader-364"><span class="linenos">364</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.add_reader-365"><a href="#DerivedFromUVLoop.add_reader-365"><span class="linenos">365</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.add_reader-366"><a href="#DerivedFromUVLoop.add_reader-366"><span class="linenos">366</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.add_reader-367"><a href="#DerivedFromUVLoop.add_reader-367"><span class="linenos">367</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.add_reader-368"><a href="#DerivedFromUVLoop.add_reader-368"><span class="linenos">368</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_reader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.add_reader(self, fileobj, callback, *args)
Add a reader callback.</p>
</div>


                            </div>
                            <div id="DerivedFromUVLoop.add_writer" class="classattr">
                                        <input id="DerivedFromUVLoop.add_writer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_writer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">fd</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.add_writer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.add_writer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.add_writer-370"><a href="#DerivedFromUVLoop.add_writer-370"><span class="linenos">370</span></a>    <span class="k">def</span> <span class="nf">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.add_writer-371"><a href="#DerivedFromUVLoop.add_writer-371"><span class="linenos">371</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.add_writer-372"><a href="#DerivedFromUVLoop.add_writer-372"><span class="linenos">372</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.add_writer-373"><a href="#DerivedFromUVLoop.add_writer-373"><span class="linenos">373</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.add_writer-374"><a href="#DerivedFromUVLoop.add_writer-374"><span class="linenos">374</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.add_writer-375"><a href="#DerivedFromUVLoop.add_writer-375"><span class="linenos">375</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fd</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.add_writer(self, fileobj, callback, *args)
Add a writer callback..</p>
</div>


                            </div>
                            <div id="DerivedFromUVLoop.add_signal_handler" class="classattr">
                                        <input id="DerivedFromUVLoop.add_signal_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_signal_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">sig</span>, </span><span class="param"><span class="n">callback</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DerivedFromUVLoop.add_signal_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DerivedFromUVLoop.add_signal_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DerivedFromUVLoop.add_signal_handler-379"><a href="#DerivedFromUVLoop.add_signal_handler-379"><span class="linenos">379</span></a>    <span class="k">def</span> <span class="nf">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="DerivedFromUVLoop.add_signal_handler-380"><a href="#DerivedFromUVLoop.add_signal_handler-380"><span class="linenos">380</span></a>        <span class="kn">from</span> <span class="nn">.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoop</span>
</span><span id="DerivedFromUVLoop.add_signal_handler-381"><a href="#DerivedFromUVLoop.add_signal_handler-381"><span class="linenos">381</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span>
</span><span id="DerivedFromUVLoop.add_signal_handler-382"><a href="#DerivedFromUVLoop.add_signal_handler-382"><span class="linenos">382</span></a>        <span class="n">service</span><span class="p">:</span> <span class="n">AsyncioLoop</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span>
</span><span id="DerivedFromUVLoop.add_signal_handler-383"><a href="#DerivedFromUVLoop.add_signal_handler-383"><span class="linenos">383</span></a>        <span class="n">service</span><span class="o">.</span><span class="n">register_new_asyncio_request</span><span class="p">()</span>
</span><span id="DerivedFromUVLoop.add_signal_handler-384"><a href="#DerivedFromUVLoop.add_signal_handler-384"><span class="linenos">384</span></a>        <span class="k">return</span> <span class="n">UVLoop</span><span class="o">.</span><span class="n">add_signal_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sig</span><span class="p">,</span> <span class="n">callback</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Loop.add_signal_handler(self, sig, callback, *args)
Add a handler for a signal.  UNIX only.</p>

<pre><code>    Raise ValueError if the signal number is invalid or uncatchable.
    Raise RuntimeError if there is a problem setting up the handler.
</code></pre>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>uvloop.loop.Loop</dt>
                                <dd id="DerivedFromUVLoop.__init__" class="function">Loop</dd>
                <dd id="DerivedFromUVLoop.run_forever" class="function">run_forever</dd>
                <dd id="DerivedFromUVLoop.run_until_complete" class="function">run_until_complete</dd>
                <dd id="DerivedFromUVLoop.stop" class="function">stop</dd>
                <dd id="DerivedFromUVLoop.is_running" class="function">is_running</dd>
                <dd id="DerivedFromUVLoop.is_closed" class="function">is_closed</dd>
                <dd id="DerivedFromUVLoop.close" class="function">close</dd>
                <dd id="DerivedFromUVLoop.shutdown_asyncgens" class="function">shutdown_asyncgens</dd>
                <dd id="DerivedFromUVLoop.time" class="function">time</dd>
                <dd id="DerivedFromUVLoop.create_future" class="function">create_future</dd>
                <dd id="DerivedFromUVLoop.set_default_executor" class="function">set_default_executor</dd>
                <dd id="DerivedFromUVLoop.getaddrinfo" class="function">getaddrinfo</dd>
                <dd id="DerivedFromUVLoop.getnameinfo" class="function">getnameinfo</dd>
                <dd id="DerivedFromUVLoop.create_connection" class="function">create_connection</dd>
                <dd id="DerivedFromUVLoop.create_server" class="function">create_server</dd>
                <dd id="DerivedFromUVLoop.start_tls" class="function">start_tls</dd>
                <dd id="DerivedFromUVLoop.create_unix_connection" class="function">create_unix_connection</dd>
                <dd id="DerivedFromUVLoop.create_unix_server" class="function">create_unix_server</dd>
                <dd id="DerivedFromUVLoop.create_datagram_endpoint" class="function">create_datagram_endpoint</dd>
                <dd id="DerivedFromUVLoop.connect_read_pipe" class="function">connect_read_pipe</dd>
                <dd id="DerivedFromUVLoop.connect_write_pipe" class="function">connect_write_pipe</dd>
                <dd id="DerivedFromUVLoop.subprocess_shell" class="function">subprocess_shell</dd>
                <dd id="DerivedFromUVLoop.subprocess_exec" class="function">subprocess_exec</dd>
                <dd id="DerivedFromUVLoop.remove_reader" class="function">remove_reader</dd>
                <dd id="DerivedFromUVLoop.remove_writer" class="function">remove_writer</dd>
                <dd id="DerivedFromUVLoop.sock_recv" class="function">sock_recv</dd>
                <dd id="DerivedFromUVLoop.sock_recv_into" class="function">sock_recv_into</dd>
                <dd id="DerivedFromUVLoop.sock_sendall" class="function">sock_sendall</dd>
                <dd id="DerivedFromUVLoop.sock_connect" class="function">sock_connect</dd>
                <dd id="DerivedFromUVLoop.sock_accept" class="function">sock_accept</dd>
                <dd id="DerivedFromUVLoop.remove_signal_handler" class="function">remove_signal_handler</dd>
                <dd id="DerivedFromUVLoop.set_task_factory" class="function">set_task_factory</dd>
                <dd id="DerivedFromUVLoop.get_task_factory" class="function">get_task_factory</dd>
                <dd id="DerivedFromUVLoop.get_exception_handler" class="function">get_exception_handler</dd>
                <dd id="DerivedFromUVLoop.set_exception_handler" class="function">set_exception_handler</dd>
                <dd id="DerivedFromUVLoop.default_exception_handler" class="function">default_exception_handler</dd>
                <dd id="DerivedFromUVLoop.call_exception_handler" class="function">call_exception_handler</dd>
                <dd id="DerivedFromUVLoop.get_debug" class="function">get_debug</dd>
                <dd id="DerivedFromUVLoop.set_debug" class="function">set_debug</dd>
                <dd id="DerivedFromUVLoop.sock_recvfrom" class="function">sock_recvfrom</dd>
                <dd id="DerivedFromUVLoop.sock_recvfrom_into" class="function">sock_recvfrom_into</dd>
                <dd id="DerivedFromUVLoop.sock_sendto" class="function">sock_sendto</dd>
                <dd id="DerivedFromUVLoop.connect_accepted_socket" class="function">connect_accepted_socket</dd>
                <dd id="DerivedFromUVLoop.shutdown_default_executor" class="function">shutdown_default_executor</dd>
                <dd id="DerivedFromUVLoop.print_debug_info" class="variable">print_debug_info</dd>
                <dd id="DerivedFromUVLoop.slow_callback_duration" class="variable">slow_callback_duration</dd>

            </div>
            <div><dt>asyncio.events.AbstractEventLoop</dt>
                                <dd id="DerivedFromUVLoop.sendfile" class="function">sendfile</dd>
                <dd id="DerivedFromUVLoop.sock_sendfile" class="function">sock_sendfile</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>