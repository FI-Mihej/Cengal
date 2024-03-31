---
title: loop_yield
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.loop_yield<wbr>.versions<wbr>.v_0<wbr>.loop_yield    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-loop_yield-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-loop_yield-view-source"><span>View Source</span></label>

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
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>    <span class="s1">&#39;CoroPriority&#39;</span><span class="p">,</span> <span class="s1">&#39;ThisCoroWasRequestedToBeKilled&#39;</span><span class="p">,</span> <span class="s1">&#39;LoopYieldPrioritySchedulerRequest&#39;</span><span class="p">,</span> <span class="s1">&#39;LoopYieldManagedBase&#39;</span><span class="p">,</span> <span class="s1">&#39;LoopYieldManaged&#39;</span><span class="p">,</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>    <span class="s1">&#39;LoopYieldManagedAsync&#39;</span><span class="p">,</span> <span class="s1">&#39;FakeLoopYieldManaged&#39;</span><span class="p">,</span> <span class="s1">&#39;LoopYieldPriorityScheduler&#39;</span><span class="p">,</span> <span class="s1">&#39;get_loop_yield&#39;</span><span class="p">,</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>    <span class="s1">&#39;gly&#39;</span><span class="p">,</span> <span class="s1">&#39;aget_loop_yield&#39;</span><span class="p">,</span> <span class="s1">&#39;agly&#39;</span><span class="p">,</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">,</span> <span class="s1">&#39;FakeLoopYieldManagedAsync&#39;</span><span class="p">,</span> <span class="s1">&#39;external_aget_loop_yield&#39;</span><span class="p">,</span> <span class="s1">&#39;eagly&#39;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="p">]</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">asyncio.events</span> <span class="kn">import</span> <span class="n">Handle</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_tools.await_coro</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Hashable</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.repeat_for_a_time</span> <span class="kn">import</span> <span class="n">Tracer</span><span class="p">,</span> <span class="n">TimeLimitIsTooSmall</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values.versions.v_1</span> <span class="kn">import</span> <span class="n">ValueExistence</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="kn">from</span> <span class="nn">async_generator</span> <span class="kn">import</span> <span class="n">asynccontextmanager</span><span class="p">,</span> <span class="n">async_generator</span><span class="p">,</span> <span class="n">yield_</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="n">MIN_TIME</span> <span class="o">=</span> <span class="mf">0.000001</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="k">class</span> <span class="nc">CoroPriority</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="n">high</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="n">normal</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="n">low</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="k">class</span> <span class="nc">LoopYieldPrioritySchedulerRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedBase&#39;</span><span class="p">:</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>    <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">max_delay</span><span class="p">)</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="k">def</span> <span class="nf">change_priority</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">)</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedBase&#39;</span><span class="p">:</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="k">def</span> <span class="nf">register_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="k">def</span> <span class="nf">register_external_asyncio_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">:</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">task</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="k">def</span> <span class="nf">change_priority_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">)</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    <span class="k">def</span> <span class="nf">del_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">)</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    <span class="k">def</span> <span class="nf">request_coro_kill</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Make request for a coro kill asynchronously (immidiately returns). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it&#39;s next requests to LoopYield service</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a><span class="sd">        Args:</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a><span class="sd">            coro_id (CoroID): _description_</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="sd">        Returns:</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">def</span> <span class="nf">kill_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Make request for a coro kill synchronously (waits for next steps). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it&#39;s next requests to LoopYield service. After an exception was sent to the requested coro_id, current coro will receive an answer from the service (None).</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a><span class="sd">        Args:</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a><span class="sd">            coro_id (CoroID): _description_</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a><span class="sd">        Returns:</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a><span class="k">class</span> <span class="nc">LoopYieldManagedBase</span><span class="p">:</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="n">time_atom</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">service</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="nd">@property</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>    <span class="k">def</span> <span class="nf">interface</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    <span class="nd">@interface</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="k">class</span> <span class="nc">LoopYieldManaged</span><span class="p">(</span><span class="n">LoopYieldManagedBase</span><span class="p">):</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManaged</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">:</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">change_priority</span><span class="p">(</span><span class="n">priority</span><span class="p">,</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>                                                                                             <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">))</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="n">priority</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>        
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">ex</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>            <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">exception</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">exception</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>                <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="n">ex</span><span class="p">)</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>                
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">)</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="k">class</span> <span class="nc">LoopYieldManagedAsync</span><span class="p">(</span><span class="n">LoopYieldManagedBase</span><span class="p">):</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManagedAsync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">:</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">change_priority</span><span class="p">(</span><span class="n">priority</span><span class="p">,</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>                                                                                                   <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">))</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="n">priority</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">)</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a><span class="k">class</span> <span class="nc">LoopYieldManagedAsyncExternal</span><span class="p">(</span><span class="n">LoopYieldManagedBase</span><span class="p">):</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task_id</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">],</span> <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">):</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManagedAsyncExternal</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_id</span> <span class="o">=</span> <span class="n">task_id</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span> <span class="o">=</span> <span class="n">coro_scheduler</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_loop</span> <span class="o">=</span> <span class="n">asyncio_loop</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">:</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>            <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">,</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>                                  <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">change_priority_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">))</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="n">priority</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">)</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a><span class="k">class</span> <span class="nc">FakeLoopYieldManaged</span><span class="p">:</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">pass</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a><span class="k">class</span> <span class="nc">FakeLoopYieldManagedAsync</span><span class="p">:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="k">pass</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a><span class="k">class</span> <span class="nc">ThisCoroWasRequestedToBeKilled</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>    <span class="k">pass</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a><span class="k">class</span> <span class="nc">LoopYieldPriorityScheduler</span><span class="p">(</span><span class="n">TypedService</span><span class="p">[</span><span class="kc">None</span><span class="p">],</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="c1"># loop.add_global_on_coro_del_handler(self._on_coro_del_handler_global)  # Todo: switch to local coro del handler</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register</span><span class="p">,</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_setup</span><span class="p">,</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_change_priority</span><span class="p">,</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_external</span><span class="p">,</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_external_asyncio_task</span><span class="p">,</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_change_priority_external</span><span class="p">,</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_del_external</span><span class="p">,</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_coro_kill</span><span class="p">,</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kill_coro</span><span class="p">,</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="p">}</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="mf">0.6827</span><span class="p">,</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="mf">0.9545</span> <span class="o">-</span> <span class="mf">0.6827</span><span class="p">,</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="mf">1.0</span> <span class="o">-</span> <span class="mf">0.9545</span><span class="p">,</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="p">}</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">=</span> <span class="mf">0.01</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>        <span class="p">}</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">compute_delays</span><span class="p">()</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># type: Dict[CoroID, LoopYieldManagedBase]</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">get</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>            <span class="k">pass</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">:</span>   <span class="mi">0</span><span class="p">,</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">:</span>    <span class="mi">0</span><span class="p">,</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>        <span class="p">}</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">:</span>   <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">:</span>    <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">2</span><span class="p">]),</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="p">}</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>        <span class="n">coroutines_requested_to_be_killed</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>            <span class="s1">&#39;task counter&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>            <span class="s1">&#39;yields num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_num</span><span class="p">,</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>            <span class="s1">&#39;max_delay&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span><span class="p">,</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>            <span class="s1">&#39;max_delays&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">,</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>            <span class="s1">&#39;affected coroutines num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">),</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>            <span class="s1">&#39;coroutines num by priority&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>                <span class="s1">&#39;high&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">],</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>                <span class="s1">&#39;normal&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">],</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>                <span class="s1">&#39;low&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">],</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>            <span class="p">},</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>            <span class="s1">&#39;time atoms by priority&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>                <span class="s1">&#39;high&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span><span class="p">,</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>                <span class="s1">&#39;normal&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span><span class="p">,</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>                <span class="s1">&#39;low&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span><span class="p">,</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>            <span class="p">},</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>            <span class="s1">&#39;coroutines requested to be killed&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>                <span class="s1">&#39;num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">coroutines_requested_to_be_killed</span><span class="p">),</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>                <span class="s1">&#39;list&#39;</span><span class="p">:</span> <span class="n">coroutines_requested_to_be_killed</span><span class="p">,</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>            <span class="p">}</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="p">}</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span><span class="p">:</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>            <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>        
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">:</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>            <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>        
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>            <span class="k">if</span> <span class="n">coro_should_be_killed</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_del_external</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span><span class="p">[</span><span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">]):</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ThisCoroWasRequestedToBeKilled</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>                
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="k">if</span> <span class="n">coro_should_be_killed</span><span class="p">:</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ThisCoroWasRequestedToBeKilled</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">:</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">compute_time_atoms</span><span class="p">()</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>    <span class="k">def</span> <span class="nf">compute_time_atoms</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>            <span class="n">top_sigma</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]:</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]:</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="n">median_time_atom</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">)</span>  <span class="c1"># !!! Possible division by zero! Conditional must not be removed!</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>            <span class="k">if</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>            <span class="k">elif</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>                <span class="n">sigma_1_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]:</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>            <span class="k">elif</span> <span class="mi">3</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>                <span class="n">sigma_1_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>                <span class="n">sigma_2_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_2_time_atom</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">)</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>    <span class="k">def</span> <span class="nf">compute_delays</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>        <span class="p">}</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>    <span class="k">def</span> <span class="nf">_on_register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>        <span class="n">task_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>        <span class="k">if</span> <span class="n">task_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>            <span class="n">loop_yield</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>            <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">interface</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">InterfaceGreenlet</span><span class="p">):</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>                <span class="n">loop_yield</span> <span class="o">=</span> <span class="n">LoopYieldManaged</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>                                            <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">default_priority</span><span class="p">],</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>                                            <span class="n">default_priority</span><span class="p">,</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>                                            <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">InterfaceAsyncAwait</span><span class="p">):</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>                <span class="n">loop_yield</span> <span class="o">=</span> <span class="n">LoopYieldManagedAsync</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>                                                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">default_priority</span><span class="p">],</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>                                                <span class="n">default_priority</span><span class="p">,</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>                                                <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>                <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>            
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>            <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop_yield</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>        
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>    <span class="k">def</span> <span class="nf">_on_setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">=</span> <span class="n">max_delay</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">compute_delays</span><span class="p">()</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="c1"># self.compute_time_atoms()</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>    <span class="k">def</span> <span class="nf">_on_change_priority</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">old_priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">new_priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>        <span class="n">loop_yield</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>        <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">new_priority</span><span class="p">]</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>    <span class="k">def</span> <span class="nf">_on_get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">),</span> <span class="kc">None</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>    <span class="k">def</span> <span class="nf">get_yield_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">LoopYieldManagedBase</span><span class="p">:</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>    
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>    <span class="k">def</span> <span class="nf">_on_register_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>        <span class="n">task_id</span> <span class="o">=</span> <span class="o">-</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>        <span class="n">loop_yield</span> <span class="o">=</span> <span class="n">LoopYieldManagedAsyncExternal</span><span class="p">(</span><span class="n">task_id</span><span class="p">,</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>                                                   <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">default_priority</span><span class="p">],</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>                                                   <span class="n">default_priority</span><span class="p">,</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>                                                   <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>                                                   <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">,</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>                                                   <span class="n">asyncio_loop</span><span class="p">)</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>        <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop_yield</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>    
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>    <span class="k">def</span> <span class="nf">_on_register_external_asyncio_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>        <span class="n">asyncio_task_id</span> <span class="o">=</span> <span class="nb">id</span><span class="p">(</span><span class="n">task</span><span class="p">)</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>        <span class="k">if</span> <span class="n">asyncio_task_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">:</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">[</span><span class="n">asyncio_task_id</span><span class="p">]</span> <span class="o">=</span> <span class="o">-</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>            
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>        <span class="n">task_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">[</span><span class="n">asyncio_task_id</span><span class="p">]</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>        <span class="k">if</span> <span class="n">task_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>            <span class="n">loop_yield</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>            <span class="n">loop_yield</span> <span class="o">=</span> <span class="n">LoopYieldManagedAsyncExternal</span><span class="p">(</span><span class="n">task_id</span><span class="p">,</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>                                                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">default_priority</span><span class="p">],</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>                                                    <span class="n">default_priority</span><span class="p">,</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>                                                    <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>                                                    <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">,</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>                                                    <span class="n">asyncio_loop</span><span class="p">)</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>            <span class="k">def</span> <span class="nf">on_done_asyncio_coro</span><span class="p">(</span><span class="n">future</span><span class="p">):</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_on_del_external</span><span class="p">(</span><span class="n">loop_yield</span><span class="p">)</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>                <span class="n">task</span><span class="o">.</span><span class="n">remove_done_callback</span><span class="p">(</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span><span class="p">)</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>            
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>            <span class="n">loop_yield</span><span class="o">.</span><span class="n">asyncio_task</span> <span class="o">=</span> <span class="n">task</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>            <span class="n">loop_yield</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span> <span class="o">=</span> <span class="n">on_done_asyncio_coro</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>            <span class="n">task</span><span class="o">.</span><span class="n">add_done_callback</span><span class="p">(</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span><span class="p">)</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>            <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop_yield</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>        
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>    
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>    <span class="k">def</span> <span class="nf">_on_change_priority_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">old_priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">new_priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>        <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">new_priority</span><span class="p">]</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>    
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>    <span class="k">def</span> <span class="nf">_on_del_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span><span class="p">):</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>        <span class="n">task_id</span> <span class="o">=</span> <span class="n">loop_yield</span><span class="o">.</span><span class="n">task_id</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>        <span class="k">if</span> <span class="n">task_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span><span class="o">.</span><span class="n">priority</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>    
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>    <span class="k">def</span> <span class="nf">_request_coro_kill</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>    
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>    <span class="k">def</span> <span class="nf">_kill_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>        <span class="n">waiter_coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">:</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>        
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">waiter_coro_id</span><span class="p">)</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler_global</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">priority</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>        <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">priority</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a><span class="n">LoopYieldPrioritySchedulerRequest</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">LoopYieldPriorityScheduler</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a><span class="k">def</span> <span class="nf">get_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">LoopYieldManaged</span><span class="p">,</span> <span class="n">FakeLoopYieldManaged</span><span class="p">]:</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManaged</span><span class="p">()</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManaged</span><span class="p">()</span>  <span class="c1"># running from Service</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>    <span class="c1"># ly = interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().get())</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">)</span><span class="o">.</span><span class="n">get_yield_object</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>    <span class="k">if</span> <span class="n">ly</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">default_priority</span><span class="p">))</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>    
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>    <span class="k">return</span> <span class="n">ly</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a><span class="n">gly</span> <span class="o">=</span> <span class="n">get_loop_yield</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">LoopYieldManagedAsync</span><span class="p">,</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">]:</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">()</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">()</span>  <span class="c1"># running from Service</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>    <span class="c1"># ly = await interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().get())</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">)</span><span class="o">.</span><span class="n">get_yield_object</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>    <span class="k">if</span> <span class="n">ly</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="k">await</span> <span class="n">interface</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">default_priority</span><span class="p">))</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>    
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>    <span class="k">return</span> <span class="n">ly</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a><span class="n">agly</span> <span class="o">=</span> <span class="n">aget_loop_yield</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a><span class="nd">@asynccontextmanager</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a><span class="nd">@async_generator</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">external_aget_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>    <span class="k">if</span> <span class="n">coro_scheduler</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a>        <span class="n">coro_scheduler</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>    
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>    <span class="k">if</span> <span class="n">coro_scheduler</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>        <span class="k">await</span> <span class="n">yield_</span><span class="p">(</span><span class="n">FakeLoopYieldManagedAsync</span><span class="p">())</span>  <span class="c1"># can not determine coro scheduler loop</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>        <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>        
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>        <span class="k">if</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">:</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>            <span class="n">ly</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span> <span class="o">=</span> <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>                <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>                <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_external_asyncio_task</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">current_task</span><span class="p">(</span><span class="n">loop</span><span class="o">=</span><span class="n">asyncio_loop</span><span class="p">),</span> <span class="n">default_priority</span><span class="p">))</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>            <span class="n">ly</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span> <span class="o">=</span> <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>                <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>                <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_external</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">))</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>            <span class="k">await</span> <span class="n">yield_</span><span class="p">(</span><span class="n">ly</span><span class="p">)</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">:</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>                <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>                                    <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">del_external</span><span class="p">(</span><span class="n">ly</span><span class="p">))</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a><span class="n">eagly</span> <span class="o">=</span> <span class="n">external_aget_loop_yield</span>
</span></pre></div>


            </section>
                <section id="CoroPriority">
                            <input id="CoroPriority-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CoroPriority</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="CoroPriority-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroPriority"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroPriority-59"><a href="#CoroPriority-59"><span class="linenos">59</span></a><span class="k">class</span> <span class="nc">CoroPriority</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="CoroPriority-60"><a href="#CoroPriority-60"><span class="linenos">60</span></a>    <span class="n">high</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="CoroPriority-61"><a href="#CoroPriority-61"><span class="linenos">61</span></a>    <span class="n">normal</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="CoroPriority-62"><a href="#CoroPriority-62"><span class="linenos">62</span></a>    <span class="n">low</span> <span class="o">=</span> <span class="mi">2</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="CoroPriority.high" class="classattr">
                                <div class="attr variable">
            <span class="name">high</span>        =
<span class="default_value">&lt;<a href="#CoroPriority.high">CoroPriority.high</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#CoroPriority.high"></a>
    
    

                            </div>
                            <div id="CoroPriority.normal" class="classattr">
                                <div class="attr variable">
            <span class="name">normal</span>        =
<span class="default_value">&lt;<a href="#CoroPriority.normal">CoroPriority.normal</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#CoroPriority.normal"></a>
    
    

                            </div>
                            <div id="CoroPriority.low" class="classattr">
                                <div class="attr variable">
            <span class="name">low</span>        =
<span class="default_value">&lt;<a href="#CoroPriority.low">CoroPriority.low</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#CoroPriority.low"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="CoroPriority.name" class="variable">name</dd>
                <dd id="CoroPriority.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ThisCoroWasRequestedToBeKilled">
                            <input id="ThisCoroWasRequestedToBeKilled-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ThisCoroWasRequestedToBeKilled</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="ThisCoroWasRequestedToBeKilled-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ThisCoroWasRequestedToBeKilled"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ThisCoroWasRequestedToBeKilled-243"><a href="#ThisCoroWasRequestedToBeKilled-243"><span class="linenos">243</span></a><span class="k">class</span> <span class="nc">ThisCoroWasRequestedToBeKilled</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="ThisCoroWasRequestedToBeKilled-244"><a href="#ThisCoroWasRequestedToBeKilled-244"><span class="linenos">244</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="ThisCoroWasRequestedToBeKilled.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="ThisCoroWasRequestedToBeKilled.with_traceback" class="function">with_traceback</dd>
                <dd id="ThisCoroWasRequestedToBeKilled.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="LoopYieldPrioritySchedulerRequest">
                            <input id="LoopYieldPrioritySchedulerRequest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LoopYieldPrioritySchedulerRequest</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</span>):

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest-65"><a href="#LoopYieldPrioritySchedulerRequest-65"><span class="linenos"> 65</span></a><span class="k">class</span> <span class="nc">LoopYieldPrioritySchedulerRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="LoopYieldPrioritySchedulerRequest-66"><a href="#LoopYieldPrioritySchedulerRequest-66"><span class="linenos"> 66</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedBase&#39;</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-67"><a href="#LoopYieldPrioritySchedulerRequest-67"><span class="linenos"> 67</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-68"><a href="#LoopYieldPrioritySchedulerRequest-68"><span class="linenos"> 68</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-69"><a href="#LoopYieldPrioritySchedulerRequest-69"><span class="linenos"> 69</span></a>    <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-70"><a href="#LoopYieldPrioritySchedulerRequest-70"><span class="linenos"> 70</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">max_delay</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-71"><a href="#LoopYieldPrioritySchedulerRequest-71"><span class="linenos"> 71</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-72"><a href="#LoopYieldPrioritySchedulerRequest-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="nf">change_priority</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-73"><a href="#LoopYieldPrioritySchedulerRequest-73"><span class="linenos"> 73</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-74"><a href="#LoopYieldPrioritySchedulerRequest-74"><span class="linenos"> 74</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-75"><a href="#LoopYieldPrioritySchedulerRequest-75"><span class="linenos"> 75</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedBase&#39;</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-76"><a href="#LoopYieldPrioritySchedulerRequest-76"><span class="linenos"> 76</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-77"><a href="#LoopYieldPrioritySchedulerRequest-77"><span class="linenos"> 77</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-78"><a href="#LoopYieldPrioritySchedulerRequest-78"><span class="linenos"> 78</span></a>    <span class="k">def</span> <span class="nf">register_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-79"><a href="#LoopYieldPrioritySchedulerRequest-79"><span class="linenos"> 79</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-80"><a href="#LoopYieldPrioritySchedulerRequest-80"><span class="linenos"> 80</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-81"><a href="#LoopYieldPrioritySchedulerRequest-81"><span class="linenos"> 81</span></a>    <span class="k">def</span> <span class="nf">register_external_asyncio_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-82"><a href="#LoopYieldPrioritySchedulerRequest-82"><span class="linenos"> 82</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">task</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-83"><a href="#LoopYieldPrioritySchedulerRequest-83"><span class="linenos"> 83</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-84"><a href="#LoopYieldPrioritySchedulerRequest-84"><span class="linenos"> 84</span></a>    <span class="k">def</span> <span class="nf">change_priority_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-85"><a href="#LoopYieldPrioritySchedulerRequest-85"><span class="linenos"> 85</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-86"><a href="#LoopYieldPrioritySchedulerRequest-86"><span class="linenos"> 86</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-87"><a href="#LoopYieldPrioritySchedulerRequest-87"><span class="linenos"> 87</span></a>    <span class="k">def</span> <span class="nf">del_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-88"><a href="#LoopYieldPrioritySchedulerRequest-88"><span class="linenos"> 88</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-89"><a href="#LoopYieldPrioritySchedulerRequest-89"><span class="linenos"> 89</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-90"><a href="#LoopYieldPrioritySchedulerRequest-90"><span class="linenos"> 90</span></a>    <span class="k">def</span> <span class="nf">request_coro_kill</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-91"><a href="#LoopYieldPrioritySchedulerRequest-91"><span class="linenos"> 91</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Make request for a coro kill asynchronously (immidiately returns). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it&#39;s next requests to LoopYield service</span>
</span><span id="LoopYieldPrioritySchedulerRequest-92"><a href="#LoopYieldPrioritySchedulerRequest-92"><span class="linenos"> 92</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-93"><a href="#LoopYieldPrioritySchedulerRequest-93"><span class="linenos"> 93</span></a><span class="sd">        Args:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-94"><a href="#LoopYieldPrioritySchedulerRequest-94"><span class="linenos"> 94</span></a><span class="sd">            coro_id (CoroID): _description_</span>
</span><span id="LoopYieldPrioritySchedulerRequest-95"><a href="#LoopYieldPrioritySchedulerRequest-95"><span class="linenos"> 95</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-96"><a href="#LoopYieldPrioritySchedulerRequest-96"><span class="linenos"> 96</span></a><span class="sd">        Returns:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-97"><a href="#LoopYieldPrioritySchedulerRequest-97"><span class="linenos"> 97</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="LoopYieldPrioritySchedulerRequest-98"><a href="#LoopYieldPrioritySchedulerRequest-98"><span class="linenos"> 98</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="LoopYieldPrioritySchedulerRequest-99"><a href="#LoopYieldPrioritySchedulerRequest-99"><span class="linenos"> 99</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span><span id="LoopYieldPrioritySchedulerRequest-100"><a href="#LoopYieldPrioritySchedulerRequest-100"><span class="linenos">100</span></a>    
</span><span id="LoopYieldPrioritySchedulerRequest-101"><a href="#LoopYieldPrioritySchedulerRequest-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">kill_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-102"><a href="#LoopYieldPrioritySchedulerRequest-102"><span class="linenos">102</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Make request for a coro kill synchronously (waits for next steps). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it&#39;s next requests to LoopYield service. After an exception was sent to the requested coro_id, current coro will receive an answer from the service (None).</span>
</span><span id="LoopYieldPrioritySchedulerRequest-103"><a href="#LoopYieldPrioritySchedulerRequest-103"><span class="linenos">103</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-104"><a href="#LoopYieldPrioritySchedulerRequest-104"><span class="linenos">104</span></a><span class="sd">        Args:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-105"><a href="#LoopYieldPrioritySchedulerRequest-105"><span class="linenos">105</span></a><span class="sd">            coro_id (CoroID): _description_</span>
</span><span id="LoopYieldPrioritySchedulerRequest-106"><a href="#LoopYieldPrioritySchedulerRequest-106"><span class="linenos">106</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest-107"><a href="#LoopYieldPrioritySchedulerRequest-107"><span class="linenos">107</span></a><span class="sd">        Returns:</span>
</span><span id="LoopYieldPrioritySchedulerRequest-108"><a href="#LoopYieldPrioritySchedulerRequest-108"><span class="linenos">108</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="LoopYieldPrioritySchedulerRequest-109"><a href="#LoopYieldPrioritySchedulerRequest-109"><span class="linenos">109</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="LoopYieldPrioritySchedulerRequest-110"><a href="#LoopYieldPrioritySchedulerRequest-110"><span class="linenos">110</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="LoopYieldPrioritySchedulerRequest.register" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.register-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.register-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.register"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.register-66"><a href="#LoopYieldPrioritySchedulerRequest.register-66"><span class="linenos">66</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedBase&#39;</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.register-67"><a href="#LoopYieldPrioritySchedulerRequest.register-67"><span class="linenos">67</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.setup" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.setup-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">setup</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">max_delay</span><span class="p">:</span> <span class="nb">float</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.setup-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.setup"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.setup-69"><a href="#LoopYieldPrioritySchedulerRequest.setup-69"><span class="linenos">69</span></a>    <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.setup-70"><a href="#LoopYieldPrioritySchedulerRequest.setup-70"><span class="linenos">70</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">max_delay</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.change_priority" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.change_priority-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">change_priority</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">new_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span>,</span><span class="param">	<span class="n">old_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.change_priority-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.change_priority"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.change_priority-72"><a href="#LoopYieldPrioritySchedulerRequest.change_priority-72"><span class="linenos">72</span></a>    <span class="k">def</span> <span class="nf">change_priority</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.change_priority-73"><a href="#LoopYieldPrioritySchedulerRequest.change_priority-73"><span class="linenos">73</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.get" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.get-75"><a href="#LoopYieldPrioritySchedulerRequest.get-75"><span class="linenos">75</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedBase&#39;</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.get-76"><a href="#LoopYieldPrioritySchedulerRequest.get-76"><span class="linenos">76</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.register_external" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.register_external-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_external</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#LoopYieldManagedAsyncExternal">LoopYieldManagedAsyncExternal</a></span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.register_external-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.register_external"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.register_external-78"><a href="#LoopYieldPrioritySchedulerRequest.register_external-78"><span class="linenos">78</span></a>    <span class="k">def</span> <span class="nf">register_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.register_external-79"><a href="#LoopYieldPrioritySchedulerRequest.register_external-79"><span class="linenos">79</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.register_external_asyncio_task" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.register_external_asyncio_task-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_external_asyncio_task</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>,</span><span class="param">	<span class="n">task</span><span class="p">:</span> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Task</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#LoopYieldManagedAsyncExternal">LoopYieldManagedAsyncExternal</a></span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.register_external_asyncio_task-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.register_external_asyncio_task"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.register_external_asyncio_task-81"><a href="#LoopYieldPrioritySchedulerRequest.register_external_asyncio_task-81"><span class="linenos">81</span></a>    <span class="k">def</span> <span class="nf">register_external_asyncio_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.register_external_asyncio_task-82"><a href="#LoopYieldPrioritySchedulerRequest.register_external_asyncio_task-82"><span class="linenos">82</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">task</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.change_priority_external" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.change_priority_external-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">change_priority_external</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">loop_yield</span><span class="p">:</span> <span class="n"><a href="#LoopYieldManagedAsyncExternal">LoopYieldManagedAsyncExternal</a></span>,</span><span class="param">	<span class="n">new_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span>,</span><span class="param">	<span class="n">old_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.change_priority_external-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.change_priority_external"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.change_priority_external-84"><a href="#LoopYieldPrioritySchedulerRequest.change_priority_external-84"><span class="linenos">84</span></a>    <span class="k">def</span> <span class="nf">change_priority_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.change_priority_external-85"><a href="#LoopYieldPrioritySchedulerRequest.change_priority_external-85"><span class="linenos">85</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.del_external" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.del_external-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">del_external</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">loop_yield</span><span class="p">:</span> <span class="n"><a href="#LoopYieldManagedAsyncExternal">LoopYieldManagedAsyncExternal</a></span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.del_external-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.del_external"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.del_external-87"><a href="#LoopYieldPrioritySchedulerRequest.del_external-87"><span class="linenos">87</span></a>    <span class="k">def</span> <span class="nf">del_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="s1">&#39;LoopYieldManagedAsyncExternal&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.del_external-88"><a href="#LoopYieldPrioritySchedulerRequest.del_external-88"><span class="linenos">88</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.request_coro_kill" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.request_coro_kill-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">request_coro_kill</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.request_coro_kill-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.request_coro_kill"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-90"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-90"><span class="linenos">90</span></a>    <span class="k">def</span> <span class="nf">request_coro_kill</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-91"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-91"><span class="linenos">91</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Make request for a coro kill asynchronously (immidiately returns). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it&#39;s next requests to LoopYield service</span>
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-92"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-92"><span class="linenos">92</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-93"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-93"><span class="linenos">93</span></a><span class="sd">        Args:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-94"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-94"><span class="linenos">94</span></a><span class="sd">            coro_id (CoroID): _description_</span>
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-95"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-95"><span class="linenos">95</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-96"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-96"><span class="linenos">96</span></a><span class="sd">        Returns:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-97"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-97"><span class="linenos">97</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-98"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-98"><span class="linenos">98</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="LoopYieldPrioritySchedulerRequest.request_coro_kill-99"><a href="#LoopYieldPrioritySchedulerRequest.request_coro_kill-99"><span class="linenos">99</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Make request for a coro kill asynchronously (immidiately returns). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it's next requests to LoopYield service</p>

<p>Args:
    coro_id (CoroID): _description_</p>

<p>Returns:
    ServiceRequest: _description_</p>
</div>


                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.kill_coro" class="classattr">
                                        <input id="LoopYieldPrioritySchedulerRequest.kill_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">kill_coro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="LoopYieldPrioritySchedulerRequest.kill_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.kill_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-101"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">kill_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-102"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-102"><span class="linenos">102</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Make request for a coro kill synchronously (waits for next steps). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it&#39;s next requests to LoopYield service. After an exception was sent to the requested coro_id, current coro will receive an answer from the service (None).</span>
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-103"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-103"><span class="linenos">103</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-104"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-104"><span class="linenos">104</span></a><span class="sd">        Args:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-105"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-105"><span class="linenos">105</span></a><span class="sd">            coro_id (CoroID): _description_</span>
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-106"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-106"><span class="linenos">106</span></a>
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-107"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-107"><span class="linenos">107</span></a><span class="sd">        Returns:</span>
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-108"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-108"><span class="linenos">108</span></a><span class="sd">            ServiceRequest: _description_</span>
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-109"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-109"><span class="linenos">109</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="LoopYieldPrioritySchedulerRequest.kill_coro-110"><a href="#LoopYieldPrioritySchedulerRequest.kill_coro-110"><span class="linenos">110</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Make request for a coro kill synchronously (waits for next steps). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it's next requests to LoopYield service. After an exception was sent to the requested coro_id, current coro will receive an answer from the service (None).</p>

<p>Args:
    coro_id (CoroID): _description_</p>

<p>Returns:
    ServiceRequest: _description_</p>
</div>


                            </div>
                            <div id="LoopYieldPrioritySchedulerRequest.default_service_type" class="classattr">
                                <div class="attr variable">
            <span class="name">default_service_type</span><span class="annotation">: Union[type[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service], NoneType]</span>        =
<input id="LoopYieldPrioritySchedulerRequest.default_service_type-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="LoopYieldPrioritySchedulerRequest.default_service_type-view-value"></label><span class="default_value">&lt;class &#39;<a href="#LoopYieldPriorityScheduler">LoopYieldPriorityScheduler</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPrioritySchedulerRequest.default_service_type"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</dt>
                                <dd id="LoopYieldPrioritySchedulerRequest.default__request__type__" class="variable">default__request__type__</dd>
                <dd id="LoopYieldPrioritySchedulerRequest.request_type" class="variable">request_type</dd>
                <dd id="LoopYieldPrioritySchedulerRequest.args" class="variable">args</dd>
                <dd id="LoopYieldPrioritySchedulerRequest.kwargs" class="variable">kwargs</dd>
                <dd id="LoopYieldPrioritySchedulerRequest.provide_to_request_handler" class="variable">provide_to_request_handler</dd>
                <dd id="LoopYieldPrioritySchedulerRequest.interface" class="function">interface</dd>
                <dd id="LoopYieldPrioritySchedulerRequest.i" class="function">i</dd>
                <dd id="LoopYieldPrioritySchedulerRequest.async_interface" class="function">async_interface</dd>
                <dd id="LoopYieldPrioritySchedulerRequest.ai" class="function">ai</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="LoopYieldManagedBase">
                            <input id="LoopYieldManagedBase-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LoopYieldManagedBase</span>:

                <label class="view-source-button" for="LoopYieldManagedBase-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManagedBase"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManagedBase-113"><a href="#LoopYieldManagedBase-113"><span class="linenos">113</span></a><span class="k">class</span> <span class="nc">LoopYieldManagedBase</span><span class="p">:</span>
</span><span id="LoopYieldManagedBase-114"><a href="#LoopYieldManagedBase-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="LoopYieldManagedBase-115"><a href="#LoopYieldManagedBase-115"><span class="linenos">115</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="LoopYieldManagedBase-116"><a href="#LoopYieldManagedBase-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedBase-117"><a href="#LoopYieldManagedBase-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="LoopYieldManagedBase-118"><a href="#LoopYieldManagedBase-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="n">time_atom</span>
</span><span id="LoopYieldManagedBase-119"><a href="#LoopYieldManagedBase-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="LoopYieldManagedBase-120"><a href="#LoopYieldManagedBase-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="LoopYieldManagedBase-121"><a href="#LoopYieldManagedBase-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">service</span>
</span><span id="LoopYieldManagedBase-122"><a href="#LoopYieldManagedBase-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedBase-123"><a href="#LoopYieldManagedBase-123"><span class="linenos">123</span></a>
</span><span id="LoopYieldManagedBase-124"><a href="#LoopYieldManagedBase-124"><span class="linenos">124</span></a>    <span class="nd">@property</span>
</span><span id="LoopYieldManagedBase-125"><a href="#LoopYieldManagedBase-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">interface</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldManagedBase-126"><a href="#LoopYieldManagedBase-126"><span class="linenos">126</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManagedBase-127"><a href="#LoopYieldManagedBase-127"><span class="linenos">127</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="LoopYieldManagedBase-128"><a href="#LoopYieldManagedBase-128"><span class="linenos">128</span></a>        
</span><span id="LoopYieldManagedBase-129"><a href="#LoopYieldManagedBase-129"><span class="linenos">129</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span>
</span><span id="LoopYieldManagedBase-130"><a href="#LoopYieldManagedBase-130"><span class="linenos">130</span></a>
</span><span id="LoopYieldManagedBase-131"><a href="#LoopYieldManagedBase-131"><span class="linenos">131</span></a>    <span class="nd">@interface</span><span class="o">.</span><span class="n">setter</span>
</span><span id="LoopYieldManagedBase-132"><a href="#LoopYieldManagedBase-132"><span class="linenos">132</span></a>    <span class="k">def</span> <span class="nf">interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
</span><span id="LoopYieldManagedBase-133"><a href="#LoopYieldManagedBase-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">value</span>
</span></pre></div>


    

                            <div id="LoopYieldManagedBase.__init__" class="classattr">
                                        <input id="LoopYieldManagedBase.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LoopYieldManagedBase</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">interface</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="n">time_atom</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_1</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span>,</span><span class="param">	<span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="LoopYieldManagedBase.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManagedBase.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManagedBase.__init__-114"><a href="#LoopYieldManagedBase.__init__-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="LoopYieldManagedBase.__init__-115"><a href="#LoopYieldManagedBase.__init__-115"><span class="linenos">115</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="LoopYieldManagedBase.__init__-116"><a href="#LoopYieldManagedBase.__init__-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedBase.__init__-117"><a href="#LoopYieldManagedBase.__init__-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="LoopYieldManagedBase.__init__-118"><a href="#LoopYieldManagedBase.__init__-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="n">time_atom</span>
</span><span id="LoopYieldManagedBase.__init__-119"><a href="#LoopYieldManagedBase.__init__-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="LoopYieldManagedBase.__init__-120"><a href="#LoopYieldManagedBase.__init__-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="LoopYieldManagedBase.__init__-121"><a href="#LoopYieldManagedBase.__init__-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">service</span>
</span><span id="LoopYieldManagedBase.__init__-122"><a href="#LoopYieldManagedBase.__init__-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldManagedBase.interface" class="classattr">
                                        <input id="LoopYieldManagedBase.interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">interface</span>

                <label class="view-source-button" for="LoopYieldManagedBase.interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManagedBase.interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManagedBase.interface-124"><a href="#LoopYieldManagedBase.interface-124"><span class="linenos">124</span></a>    <span class="nd">@property</span>
</span><span id="LoopYieldManagedBase.interface-125"><a href="#LoopYieldManagedBase.interface-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">interface</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldManagedBase.interface-126"><a href="#LoopYieldManagedBase.interface-126"><span class="linenos">126</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManagedBase.interface-127"><a href="#LoopYieldManagedBase.interface-127"><span class="linenos">127</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="LoopYieldManagedBase.interface-128"><a href="#LoopYieldManagedBase.interface-128"><span class="linenos">128</span></a>        
</span><span id="LoopYieldManagedBase.interface-129"><a href="#LoopYieldManagedBase.interface-129"><span class="linenos">129</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldManagedBase.time_atom" class="classattr">
                                <div class="attr variable">
            <span class="name">time_atom</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedBase.time_atom"></a>
    
    

                            </div>
                            <div id="LoopYieldManagedBase.default_priority" class="classattr">
                                <div class="attr variable">
            <span class="name">default_priority</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedBase.default_priority"></a>
    
    

                            </div>
                            <div id="LoopYieldManagedBase.priority" class="classattr">
                                <div class="attr variable">
            <span class="name">priority</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedBase.priority"></a>
    
    

                            </div>
                            <div id="LoopYieldManagedBase.service" class="classattr">
                                <div class="attr variable">
            <span class="name">service</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedBase.service"></a>
    
    

                            </div>
                            <div id="LoopYieldManagedBase.tracer" class="classattr">
                                <div class="attr variable">
            <span class="name">tracer</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedBase.tracer"></a>
    
    

                            </div>
                </section>
                <section id="LoopYieldManaged">
                            <input id="LoopYieldManaged-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LoopYieldManaged</span><wbr>(<span class="base"><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></span>):

                <label class="view-source-button" for="LoopYieldManaged-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManaged"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManaged-136"><a href="#LoopYieldManaged-136"><span class="linenos">136</span></a><span class="k">class</span> <span class="nc">LoopYieldManaged</span><span class="p">(</span><span class="n">LoopYieldManagedBase</span><span class="p">):</span>
</span><span id="LoopYieldManaged-137"><a href="#LoopYieldManaged-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="LoopYieldManaged-138"><a href="#LoopYieldManaged-138"><span class="linenos">138</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="LoopYieldManaged-139"><a href="#LoopYieldManaged-139"><span class="linenos">139</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManaged</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span><span id="LoopYieldManaged-140"><a href="#LoopYieldManaged-140"><span class="linenos">140</span></a>
</span><span id="LoopYieldManaged-141"><a href="#LoopYieldManaged-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="LoopYieldManaged-142"><a href="#LoopYieldManaged-142"><span class="linenos">142</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManaged-143"><a href="#LoopYieldManaged-143"><span class="linenos">143</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="LoopYieldManaged-144"><a href="#LoopYieldManaged-144"><span class="linenos">144</span></a>        
</span><span id="LoopYieldManaged-145"><a href="#LoopYieldManaged-145"><span class="linenos">145</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">:</span>
</span><span id="LoopYieldManaged-146"><a href="#LoopYieldManaged-146"><span class="linenos">146</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManaged-147"><a href="#LoopYieldManaged-147"><span class="linenos">147</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">change_priority</span><span class="p">(</span><span class="n">priority</span><span class="p">,</span>
</span><span id="LoopYieldManaged-148"><a href="#LoopYieldManaged-148"><span class="linenos">148</span></a>                                                                                             <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">))</span>
</span><span id="LoopYieldManaged-149"><a href="#LoopYieldManaged-149"><span class="linenos">149</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="n">priority</span>
</span><span id="LoopYieldManaged-150"><a href="#LoopYieldManaged-150"><span class="linenos">150</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="LoopYieldManaged-151"><a href="#LoopYieldManaged-151"><span class="linenos">151</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="LoopYieldManaged-152"><a href="#LoopYieldManaged-152"><span class="linenos">152</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="LoopYieldManaged-153"><a href="#LoopYieldManaged-153"><span class="linenos">153</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="LoopYieldManaged-154"><a href="#LoopYieldManaged-154"><span class="linenos">154</span></a>        
</span><span id="LoopYieldManaged-155"><a href="#LoopYieldManaged-155"><span class="linenos">155</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManaged-156"><a href="#LoopYieldManaged-156"><span class="linenos">156</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManaged-157"><a href="#LoopYieldManaged-157"><span class="linenos">157</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="LoopYieldManaged-158"><a href="#LoopYieldManaged-158"><span class="linenos">158</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="LoopYieldManaged-159"><a href="#LoopYieldManaged-159"><span class="linenos">159</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="LoopYieldManaged-160"><a href="#LoopYieldManaged-160"><span class="linenos">160</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">ex</span>
</span><span id="LoopYieldManaged-161"><a href="#LoopYieldManaged-161"><span class="linenos">161</span></a>
</span><span id="LoopYieldManaged-162"><a href="#LoopYieldManaged-162"><span class="linenos">162</span></a>            <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManaged-163"><a href="#LoopYieldManaged-163"><span class="linenos">163</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="LoopYieldManaged-164"><a href="#LoopYieldManaged-164"><span class="linenos">164</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">exception</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">exception</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="LoopYieldManaged-165"><a href="#LoopYieldManaged-165"><span class="linenos">165</span></a>                <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="LoopYieldManaged-166"><a href="#LoopYieldManaged-166"><span class="linenos">166</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="n">ex</span><span class="p">)</span>
</span><span id="LoopYieldManaged-167"><a href="#LoopYieldManaged-167"><span class="linenos">167</span></a>                
</span><span id="LoopYieldManaged-168"><a href="#LoopYieldManaged-168"><span class="linenos">168</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManaged-169"><a href="#LoopYieldManaged-169"><span class="linenos">169</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="LoopYieldManaged-170"><a href="#LoopYieldManaged-170"><span class="linenos">170</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManaged-171"><a href="#LoopYieldManaged-171"><span class="linenos">171</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManaged-172"><a href="#LoopYieldManaged-172"><span class="linenos">172</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="LoopYieldManaged.__init__" class="classattr">
                                        <input id="LoopYieldManaged.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LoopYieldManaged</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">interface</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="n">time_atom</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_1</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span>,</span><span class="param">	<span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="LoopYieldManaged.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManaged.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManaged.__init__-137"><a href="#LoopYieldManaged.__init__-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="LoopYieldManaged.__init__-138"><a href="#LoopYieldManaged.__init__-138"><span class="linenos">138</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="LoopYieldManaged.__init__-139"><a href="#LoopYieldManaged.__init__-139"><span class="linenos">139</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManaged</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></dt>
                                <dd id="LoopYieldManaged.interface" class="variable"><a href="#LoopYieldManagedBase.interface">interface</a></dd>
                <dd id="LoopYieldManaged.time_atom" class="variable"><a href="#LoopYieldManagedBase.time_atom">time_atom</a></dd>
                <dd id="LoopYieldManaged.default_priority" class="variable"><a href="#LoopYieldManagedBase.default_priority">default_priority</a></dd>
                <dd id="LoopYieldManaged.priority" class="variable"><a href="#LoopYieldManagedBase.priority">priority</a></dd>
                <dd id="LoopYieldManaged.service" class="variable"><a href="#LoopYieldManagedBase.service">service</a></dd>
                <dd id="LoopYieldManaged.tracer" class="variable"><a href="#LoopYieldManagedBase.tracer">tracer</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="LoopYieldManagedAsync">
                            <input id="LoopYieldManagedAsync-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LoopYieldManagedAsync</span><wbr>(<span class="base"><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></span>):

                <label class="view-source-button" for="LoopYieldManagedAsync-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManagedAsync"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManagedAsync-175"><a href="#LoopYieldManagedAsync-175"><span class="linenos">175</span></a><span class="k">class</span> <span class="nc">LoopYieldManagedAsync</span><span class="p">(</span><span class="n">LoopYieldManagedBase</span><span class="p">):</span>
</span><span id="LoopYieldManagedAsync-176"><a href="#LoopYieldManagedAsync-176"><span class="linenos">176</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="LoopYieldManagedAsync-177"><a href="#LoopYieldManagedAsync-177"><span class="linenos">177</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="LoopYieldManagedAsync-178"><a href="#LoopYieldManagedAsync-178"><span class="linenos">178</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManagedAsync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsync-179"><a href="#LoopYieldManagedAsync-179"><span class="linenos">179</span></a>
</span><span id="LoopYieldManagedAsync-180"><a href="#LoopYieldManagedAsync-180"><span class="linenos">180</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="LoopYieldManagedAsync-181"><a href="#LoopYieldManagedAsync-181"><span class="linenos">181</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsync-182"><a href="#LoopYieldManagedAsync-182"><span class="linenos">182</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="LoopYieldManagedAsync-183"><a href="#LoopYieldManagedAsync-183"><span class="linenos">183</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsync-184"><a href="#LoopYieldManagedAsync-184"><span class="linenos">184</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedAsync-185"><a href="#LoopYieldManagedAsync-185"><span class="linenos">185</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">change_priority</span><span class="p">(</span><span class="n">priority</span><span class="p">,</span>
</span><span id="LoopYieldManagedAsync-186"><a href="#LoopYieldManagedAsync-186"><span class="linenos">186</span></a>                                                                                                   <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">))</span>
</span><span id="LoopYieldManagedAsync-187"><a href="#LoopYieldManagedAsync-187"><span class="linenos">187</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="n">priority</span>
</span><span id="LoopYieldManagedAsync-188"><a href="#LoopYieldManagedAsync-188"><span class="linenos">188</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsync-189"><a href="#LoopYieldManagedAsync-189"><span class="linenos">189</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsync-190"><a href="#LoopYieldManagedAsync-190"><span class="linenos">190</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsync-191"><a href="#LoopYieldManagedAsync-191"><span class="linenos">191</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsync-192"><a href="#LoopYieldManagedAsync-192"><span class="linenos">192</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsync-193"><a href="#LoopYieldManagedAsync-193"><span class="linenos">193</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsync-194"><a href="#LoopYieldManagedAsync-194"><span class="linenos">194</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsync-195"><a href="#LoopYieldManagedAsync-195"><span class="linenos">195</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsync-196"><a href="#LoopYieldManagedAsync-196"><span class="linenos">196</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsync-197"><a href="#LoopYieldManagedAsync-197"><span class="linenos">197</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="LoopYieldManagedAsync-198"><a href="#LoopYieldManagedAsync-198"><span class="linenos">198</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedAsync-199"><a href="#LoopYieldManagedAsync-199"><span class="linenos">199</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedAsync-200"><a href="#LoopYieldManagedAsync-200"><span class="linenos">200</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="LoopYieldManagedAsync.__init__" class="classattr">
                                        <input id="LoopYieldManagedAsync.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LoopYieldManagedAsync</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">interface</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span>,</span><span class="param">	<span class="n">time_atom</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_1</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span>,</span><span class="param">	<span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="LoopYieldManagedAsync.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManagedAsync.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManagedAsync.__init__-176"><a href="#LoopYieldManagedAsync.__init__-176"><span class="linenos">176</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="LoopYieldManagedAsync.__init__-177"><a href="#LoopYieldManagedAsync.__init__-177"><span class="linenos">177</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="LoopYieldManagedAsync.__init__-178"><a href="#LoopYieldManagedAsync.__init__-178"><span class="linenos">178</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManagedAsync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></dt>
                                <dd id="LoopYieldManagedAsync.interface" class="variable"><a href="#LoopYieldManagedBase.interface">interface</a></dd>
                <dd id="LoopYieldManagedAsync.time_atom" class="variable"><a href="#LoopYieldManagedBase.time_atom">time_atom</a></dd>
                <dd id="LoopYieldManagedAsync.default_priority" class="variable"><a href="#LoopYieldManagedBase.default_priority">default_priority</a></dd>
                <dd id="LoopYieldManagedAsync.priority" class="variable"><a href="#LoopYieldManagedBase.priority">priority</a></dd>
                <dd id="LoopYieldManagedAsync.service" class="variable"><a href="#LoopYieldManagedBase.service">service</a></dd>
                <dd id="LoopYieldManagedAsync.tracer" class="variable"><a href="#LoopYieldManagedBase.tracer">tracer</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="FakeLoopYieldManaged">
                            <input id="FakeLoopYieldManaged-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">FakeLoopYieldManaged</span>:

                <label class="view-source-button" for="FakeLoopYieldManaged-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FakeLoopYieldManaged"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FakeLoopYieldManaged-234"><a href="#FakeLoopYieldManaged-234"><span class="linenos">234</span></a><span class="k">class</span> <span class="nc">FakeLoopYieldManaged</span><span class="p">:</span>
</span><span id="FakeLoopYieldManaged-235"><a href="#FakeLoopYieldManaged-235"><span class="linenos">235</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="FakeLoopYieldManaged-236"><a href="#FakeLoopYieldManaged-236"><span class="linenos">236</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                </section>
                <section id="LoopYieldPriorityScheduler">
                            <input id="LoopYieldPriorityScheduler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LoopYieldPriorityScheduler</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.TypedService[NoneType]</span>, <span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</span>):

                <label class="view-source-button" for="LoopYieldPriorityScheduler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPriorityScheduler-247"><a href="#LoopYieldPriorityScheduler-247"><span class="linenos">247</span></a><span class="k">class</span> <span class="nc">LoopYieldPriorityScheduler</span><span class="p">(</span><span class="n">TypedService</span><span class="p">[</span><span class="kc">None</span><span class="p">],</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-248"><a href="#LoopYieldPriorityScheduler-248"><span class="linenos">248</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-249"><a href="#LoopYieldPriorityScheduler-249"><span class="linenos">249</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-250"><a href="#LoopYieldPriorityScheduler-250"><span class="linenos">250</span></a>
</span><span id="LoopYieldPriorityScheduler-251"><a href="#LoopYieldPriorityScheduler-251"><span class="linenos">251</span></a>        <span class="c1"># loop.add_global_on_coro_del_handler(self._on_coro_del_handler_global)  # Todo: switch to local coro del handler</span>
</span><span id="LoopYieldPriorityScheduler-252"><a href="#LoopYieldPriorityScheduler-252"><span class="linenos">252</span></a>
</span><span id="LoopYieldPriorityScheduler-253"><a href="#LoopYieldPriorityScheduler-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-254"><a href="#LoopYieldPriorityScheduler-254"><span class="linenos">254</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-255"><a href="#LoopYieldPriorityScheduler-255"><span class="linenos">255</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_setup</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-256"><a href="#LoopYieldPriorityScheduler-256"><span class="linenos">256</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_change_priority</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-257"><a href="#LoopYieldPriorityScheduler-257"><span class="linenos">257</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-258"><a href="#LoopYieldPriorityScheduler-258"><span class="linenos">258</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_external</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-259"><a href="#LoopYieldPriorityScheduler-259"><span class="linenos">259</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_external_asyncio_task</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-260"><a href="#LoopYieldPriorityScheduler-260"><span class="linenos">260</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_change_priority_external</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-261"><a href="#LoopYieldPriorityScheduler-261"><span class="linenos">261</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_del_external</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-262"><a href="#LoopYieldPriorityScheduler-262"><span class="linenos">262</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_coro_kill</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-263"><a href="#LoopYieldPriorityScheduler-263"><span class="linenos">263</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kill_coro</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-264"><a href="#LoopYieldPriorityScheduler-264"><span class="linenos">264</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler-265"><a href="#LoopYieldPriorityScheduler-265"><span class="linenos">265</span></a>
</span><span id="LoopYieldPriorityScheduler-266"><a href="#LoopYieldPriorityScheduler-266"><span class="linenos">266</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-267"><a href="#LoopYieldPriorityScheduler-267"><span class="linenos">267</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="mf">0.6827</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-268"><a href="#LoopYieldPriorityScheduler-268"><span class="linenos">268</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="mf">0.9545</span> <span class="o">-</span> <span class="mf">0.6827</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-269"><a href="#LoopYieldPriorityScheduler-269"><span class="linenos">269</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="mf">1.0</span> <span class="o">-</span> <span class="mf">0.9545</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-270"><a href="#LoopYieldPriorityScheduler-270"><span class="linenos">270</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler-271"><a href="#LoopYieldPriorityScheduler-271"><span class="linenos">271</span></a>
</span><span id="LoopYieldPriorityScheduler-272"><a href="#LoopYieldPriorityScheduler-272"><span class="linenos">272</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">=</span> <span class="mf">0.01</span>
</span><span id="LoopYieldPriorityScheduler-273"><a href="#LoopYieldPriorityScheduler-273"><span class="linenos">273</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-274"><a href="#LoopYieldPriorityScheduler-274"><span class="linenos">274</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-275"><a href="#LoopYieldPriorityScheduler-275"><span class="linenos">275</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-276"><a href="#LoopYieldPriorityScheduler-276"><span class="linenos">276</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-277"><a href="#LoopYieldPriorityScheduler-277"><span class="linenos">277</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler-278"><a href="#LoopYieldPriorityScheduler-278"><span class="linenos">278</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">compute_delays</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-279"><a href="#LoopYieldPriorityScheduler-279"><span class="linenos">279</span></a>
</span><span id="LoopYieldPriorityScheduler-280"><a href="#LoopYieldPriorityScheduler-280"><span class="linenos">280</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># type: Dict[CoroID, LoopYieldManagedBase]</span>
</span><span id="LoopYieldPriorityScheduler-281"><a href="#LoopYieldPriorityScheduler-281"><span class="linenos">281</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-282"><a href="#LoopYieldPriorityScheduler-282"><span class="linenos">282</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">get</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-283"><a href="#LoopYieldPriorityScheduler-283"><span class="linenos">283</span></a>            <span class="k">pass</span>
</span><span id="LoopYieldPriorityScheduler-284"><a href="#LoopYieldPriorityScheduler-284"><span class="linenos">284</span></a>        
</span><span id="LoopYieldPriorityScheduler-285"><a href="#LoopYieldPriorityScheduler-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="LoopYieldPriorityScheduler-286"><a href="#LoopYieldPriorityScheduler-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-287"><a href="#LoopYieldPriorityScheduler-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-288"><a href="#LoopYieldPriorityScheduler-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-289"><a href="#LoopYieldPriorityScheduler-289"><span class="linenos">289</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-290"><a href="#LoopYieldPriorityScheduler-290"><span class="linenos">290</span></a>
</span><span id="LoopYieldPriorityScheduler-291"><a href="#LoopYieldPriorityScheduler-291"><span class="linenos">291</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-292"><a href="#LoopYieldPriorityScheduler-292"><span class="linenos">292</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">:</span>   <span class="mi">0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-293"><a href="#LoopYieldPriorityScheduler-293"><span class="linenos">293</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-294"><a href="#LoopYieldPriorityScheduler-294"><span class="linenos">294</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">:</span>    <span class="mi">0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-295"><a href="#LoopYieldPriorityScheduler-295"><span class="linenos">295</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler-296"><a href="#LoopYieldPriorityScheduler-296"><span class="linenos">296</span></a>
</span><span id="LoopYieldPriorityScheduler-297"><a href="#LoopYieldPriorityScheduler-297"><span class="linenos">297</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-298"><a href="#LoopYieldPriorityScheduler-298"><span class="linenos">298</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">:</span>   <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
</span><span id="LoopYieldPriorityScheduler-299"><a href="#LoopYieldPriorityScheduler-299"><span class="linenos">299</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
</span><span id="LoopYieldPriorityScheduler-300"><a href="#LoopYieldPriorityScheduler-300"><span class="linenos">300</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">:</span>    <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">2</span><span class="p">]),</span>
</span><span id="LoopYieldPriorityScheduler-301"><a href="#LoopYieldPriorityScheduler-301"><span class="linenos">301</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler-302"><a href="#LoopYieldPriorityScheduler-302"><span class="linenos">302</span></a>
</span><span id="LoopYieldPriorityScheduler-303"><a href="#LoopYieldPriorityScheduler-303"><span class="linenos">303</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="LoopYieldPriorityScheduler-304"><a href="#LoopYieldPriorityScheduler-304"><span class="linenos">304</span></a>        <span class="n">coroutines_requested_to_be_killed</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="LoopYieldPriorityScheduler-305"><a href="#LoopYieldPriorityScheduler-305"><span class="linenos">305</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-306"><a href="#LoopYieldPriorityScheduler-306"><span class="linenos">306</span></a>            <span class="s1">&#39;task counter&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-307"><a href="#LoopYieldPriorityScheduler-307"><span class="linenos">307</span></a>            <span class="s1">&#39;yields num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_num</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-308"><a href="#LoopYieldPriorityScheduler-308"><span class="linenos">308</span></a>            <span class="s1">&#39;max_delay&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-309"><a href="#LoopYieldPriorityScheduler-309"><span class="linenos">309</span></a>            <span class="s1">&#39;max_delays&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-310"><a href="#LoopYieldPriorityScheduler-310"><span class="linenos">310</span></a>            <span class="s1">&#39;affected coroutines num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">),</span>
</span><span id="LoopYieldPriorityScheduler-311"><a href="#LoopYieldPriorityScheduler-311"><span class="linenos">311</span></a>            <span class="s1">&#39;coroutines num by priority&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-312"><a href="#LoopYieldPriorityScheduler-312"><span class="linenos">312</span></a>                <span class="s1">&#39;high&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-313"><a href="#LoopYieldPriorityScheduler-313"><span class="linenos">313</span></a>                <span class="s1">&#39;normal&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-314"><a href="#LoopYieldPriorityScheduler-314"><span class="linenos">314</span></a>                <span class="s1">&#39;low&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-315"><a href="#LoopYieldPriorityScheduler-315"><span class="linenos">315</span></a>            <span class="p">},</span>
</span><span id="LoopYieldPriorityScheduler-316"><a href="#LoopYieldPriorityScheduler-316"><span class="linenos">316</span></a>            <span class="s1">&#39;time atoms by priority&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-317"><a href="#LoopYieldPriorityScheduler-317"><span class="linenos">317</span></a>                <span class="s1">&#39;high&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-318"><a href="#LoopYieldPriorityScheduler-318"><span class="linenos">318</span></a>                <span class="s1">&#39;normal&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-319"><a href="#LoopYieldPriorityScheduler-319"><span class="linenos">319</span></a>                <span class="s1">&#39;low&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-320"><a href="#LoopYieldPriorityScheduler-320"><span class="linenos">320</span></a>            <span class="p">},</span>
</span><span id="LoopYieldPriorityScheduler-321"><a href="#LoopYieldPriorityScheduler-321"><span class="linenos">321</span></a>            <span class="s1">&#39;coroutines requested to be killed&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-322"><a href="#LoopYieldPriorityScheduler-322"><span class="linenos">322</span></a>                <span class="s1">&#39;num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">coroutines_requested_to_be_killed</span><span class="p">),</span>
</span><span id="LoopYieldPriorityScheduler-323"><a href="#LoopYieldPriorityScheduler-323"><span class="linenos">323</span></a>                <span class="s1">&#39;list&#39;</span><span class="p">:</span> <span class="n">coroutines_requested_to_be_killed</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-324"><a href="#LoopYieldPriorityScheduler-324"><span class="linenos">324</span></a>            <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler-325"><a href="#LoopYieldPriorityScheduler-325"><span class="linenos">325</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler-326"><a href="#LoopYieldPriorityScheduler-326"><span class="linenos">326</span></a>
</span><span id="LoopYieldPriorityScheduler-327"><a href="#LoopYieldPriorityScheduler-327"><span class="linenos">327</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-328"><a href="#LoopYieldPriorityScheduler-328"><span class="linenos">328</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler-329"><a href="#LoopYieldPriorityScheduler-329"><span class="linenos">329</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-330"><a href="#LoopYieldPriorityScheduler-330"><span class="linenos">330</span></a>        <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="LoopYieldPriorityScheduler-331"><a href="#LoopYieldPriorityScheduler-331"><span class="linenos">331</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="LoopYieldPriorityScheduler-332"><a href="#LoopYieldPriorityScheduler-332"><span class="linenos">332</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-333"><a href="#LoopYieldPriorityScheduler-333"><span class="linenos">333</span></a>            <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="LoopYieldPriorityScheduler-334"><a href="#LoopYieldPriorityScheduler-334"><span class="linenos">334</span></a>        
</span><span id="LoopYieldPriorityScheduler-335"><a href="#LoopYieldPriorityScheduler-335"><span class="linenos">335</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-336"><a href="#LoopYieldPriorityScheduler-336"><span class="linenos">336</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-337"><a href="#LoopYieldPriorityScheduler-337"><span class="linenos">337</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-338"><a href="#LoopYieldPriorityScheduler-338"><span class="linenos">338</span></a>            <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="LoopYieldPriorityScheduler-339"><a href="#LoopYieldPriorityScheduler-339"><span class="linenos">339</span></a>        
</span><span id="LoopYieldPriorityScheduler-340"><a href="#LoopYieldPriorityScheduler-340"><span class="linenos">340</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-341"><a href="#LoopYieldPriorityScheduler-341"><span class="linenos">341</span></a>            <span class="k">if</span> <span class="n">coro_should_be_killed</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_del_external</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span><span class="p">[</span><span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">]):</span>
</span><span id="LoopYieldPriorityScheduler-342"><a href="#LoopYieldPriorityScheduler-342"><span class="linenos">342</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ThisCoroWasRequestedToBeKilled</span>
</span><span id="LoopYieldPriorityScheduler-343"><a href="#LoopYieldPriorityScheduler-343"><span class="linenos">343</span></a>                
</span><span id="LoopYieldPriorityScheduler-344"><a href="#LoopYieldPriorityScheduler-344"><span class="linenos">344</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-345"><a href="#LoopYieldPriorityScheduler-345"><span class="linenos">345</span></a>
</span><span id="LoopYieldPriorityScheduler-346"><a href="#LoopYieldPriorityScheduler-346"><span class="linenos">346</span></a>        <span class="k">if</span> <span class="n">coro_should_be_killed</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-347"><a href="#LoopYieldPriorityScheduler-347"><span class="linenos">347</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ThisCoroWasRequestedToBeKilled</span>
</span><span id="LoopYieldPriorityScheduler-348"><a href="#LoopYieldPriorityScheduler-348"><span class="linenos">348</span></a>        
</span><span id="LoopYieldPriorityScheduler-349"><a href="#LoopYieldPriorityScheduler-349"><span class="linenos">349</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-350"><a href="#LoopYieldPriorityScheduler-350"><span class="linenos">350</span></a>
</span><span id="LoopYieldPriorityScheduler-351"><a href="#LoopYieldPriorityScheduler-351"><span class="linenos">351</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-352"><a href="#LoopYieldPriorityScheduler-352"><span class="linenos">352</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-353"><a href="#LoopYieldPriorityScheduler-353"><span class="linenos">353</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-354"><a href="#LoopYieldPriorityScheduler-354"><span class="linenos">354</span></a>        
</span><span id="LoopYieldPriorityScheduler-355"><a href="#LoopYieldPriorityScheduler-355"><span class="linenos">355</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">compute_time_atoms</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-356"><a href="#LoopYieldPriorityScheduler-356"><span class="linenos">356</span></a>
</span><span id="LoopYieldPriorityScheduler-357"><a href="#LoopYieldPriorityScheduler-357"><span class="linenos">357</span></a>    <span class="k">def</span> <span class="nf">compute_time_atoms</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-358"><a href="#LoopYieldPriorityScheduler-358"><span class="linenos">358</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-359"><a href="#LoopYieldPriorityScheduler-359"><span class="linenos">359</span></a>            <span class="n">top_sigma</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="LoopYieldPriorityScheduler-360"><a href="#LoopYieldPriorityScheduler-360"><span class="linenos">360</span></a>
</span><span id="LoopYieldPriorityScheduler-361"><a href="#LoopYieldPriorityScheduler-361"><span class="linenos">361</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler-362"><a href="#LoopYieldPriorityScheduler-362"><span class="linenos">362</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-363"><a href="#LoopYieldPriorityScheduler-363"><span class="linenos">363</span></a>
</span><span id="LoopYieldPriorityScheduler-364"><a href="#LoopYieldPriorityScheduler-364"><span class="linenos">364</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler-365"><a href="#LoopYieldPriorityScheduler-365"><span class="linenos">365</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-366"><a href="#LoopYieldPriorityScheduler-366"><span class="linenos">366</span></a>
</span><span id="LoopYieldPriorityScheduler-367"><a href="#LoopYieldPriorityScheduler-367"><span class="linenos">367</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler-368"><a href="#LoopYieldPriorityScheduler-368"><span class="linenos">368</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-369"><a href="#LoopYieldPriorityScheduler-369"><span class="linenos">369</span></a>
</span><span id="LoopYieldPriorityScheduler-370"><a href="#LoopYieldPriorityScheduler-370"><span class="linenos">370</span></a>            <span class="n">median_time_atom</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">)</span>  <span class="c1"># !!! Possible division by zero! Conditional must not be removed!</span>
</span><span id="LoopYieldPriorityScheduler-371"><a href="#LoopYieldPriorityScheduler-371"><span class="linenos">371</span></a>            <span class="k">if</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-372"><a href="#LoopYieldPriorityScheduler-372"><span class="linenos">372</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler-373"><a href="#LoopYieldPriorityScheduler-373"><span class="linenos">373</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-374"><a href="#LoopYieldPriorityScheduler-374"><span class="linenos">374</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-375"><a href="#LoopYieldPriorityScheduler-375"><span class="linenos">375</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-376"><a href="#LoopYieldPriorityScheduler-376"><span class="linenos">376</span></a>            <span class="k">elif</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-377"><a href="#LoopYieldPriorityScheduler-377"><span class="linenos">377</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler-378"><a href="#LoopYieldPriorityScheduler-378"><span class="linenos">378</span></a>                <span class="n">sigma_1_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler-379"><a href="#LoopYieldPriorityScheduler-379"><span class="linenos">379</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler-380"><a href="#LoopYieldPriorityScheduler-380"><span class="linenos">380</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-381"><a href="#LoopYieldPriorityScheduler-381"><span class="linenos">381</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-382"><a href="#LoopYieldPriorityScheduler-382"><span class="linenos">382</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-383"><a href="#LoopYieldPriorityScheduler-383"><span class="linenos">383</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-384"><a href="#LoopYieldPriorityScheduler-384"><span class="linenos">384</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-385"><a href="#LoopYieldPriorityScheduler-385"><span class="linenos">385</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-386"><a href="#LoopYieldPriorityScheduler-386"><span class="linenos">386</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-387"><a href="#LoopYieldPriorityScheduler-387"><span class="linenos">387</span></a>            <span class="k">elif</span> <span class="mi">3</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-388"><a href="#LoopYieldPriorityScheduler-388"><span class="linenos">388</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler-389"><a href="#LoopYieldPriorityScheduler-389"><span class="linenos">389</span></a>                <span class="n">sigma_1_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler-390"><a href="#LoopYieldPriorityScheduler-390"><span class="linenos">390</span></a>                <span class="n">sigma_2_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler-391"><a href="#LoopYieldPriorityScheduler-391"><span class="linenos">391</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-392"><a href="#LoopYieldPriorityScheduler-392"><span class="linenos">392</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-393"><a href="#LoopYieldPriorityScheduler-393"><span class="linenos">393</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_2_time_atom</span>
</span><span id="LoopYieldPriorityScheduler-394"><a href="#LoopYieldPriorityScheduler-394"><span class="linenos">394</span></a>        
</span><span id="LoopYieldPriorityScheduler-395"><a href="#LoopYieldPriorityScheduler-395"><span class="linenos">395</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-396"><a href="#LoopYieldPriorityScheduler-396"><span class="linenos">396</span></a>
</span><span id="LoopYieldPriorityScheduler-397"><a href="#LoopYieldPriorityScheduler-397"><span class="linenos">397</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-398"><a href="#LoopYieldPriorityScheduler-398"><span class="linenos">398</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-399"><a href="#LoopYieldPriorityScheduler-399"><span class="linenos">399</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-400"><a href="#LoopYieldPriorityScheduler-400"><span class="linenos">400</span></a>
</span><span id="LoopYieldPriorityScheduler-401"><a href="#LoopYieldPriorityScheduler-401"><span class="linenos">401</span></a>    <span class="k">def</span> <span class="nf">compute_delays</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-402"><a href="#LoopYieldPriorityScheduler-402"><span class="linenos">402</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler-403"><a href="#LoopYieldPriorityScheduler-403"><span class="linenos">403</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-404"><a href="#LoopYieldPriorityScheduler-404"><span class="linenos">404</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-405"><a href="#LoopYieldPriorityScheduler-405"><span class="linenos">405</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-406"><a href="#LoopYieldPriorityScheduler-406"><span class="linenos">406</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler-407"><a href="#LoopYieldPriorityScheduler-407"><span class="linenos">407</span></a>
</span><span id="LoopYieldPriorityScheduler-408"><a href="#LoopYieldPriorityScheduler-408"><span class="linenos">408</span></a>    <span class="k">def</span> <span class="nf">_on_register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-409"><a href="#LoopYieldPriorityScheduler-409"><span class="linenos">409</span></a>        <span class="n">task_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="LoopYieldPriorityScheduler-410"><a href="#LoopYieldPriorityScheduler-410"><span class="linenos">410</span></a>        <span class="k">if</span> <span class="n">task_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-411"><a href="#LoopYieldPriorityScheduler-411"><span class="linenos">411</span></a>            <span class="n">loop_yield</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-412"><a href="#LoopYieldPriorityScheduler-412"><span class="linenos">412</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-413"><a href="#LoopYieldPriorityScheduler-413"><span class="linenos">413</span></a>            <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">interface</span>
</span><span id="LoopYieldPriorityScheduler-414"><a href="#LoopYieldPriorityScheduler-414"><span class="linenos">414</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">InterfaceGreenlet</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-415"><a href="#LoopYieldPriorityScheduler-415"><span class="linenos">415</span></a>                <span class="n">loop_yield</span> <span class="o">=</span> <span class="n">LoopYieldManaged</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-416"><a href="#LoopYieldPriorityScheduler-416"><span class="linenos">416</span></a>                                            <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">default_priority</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-417"><a href="#LoopYieldPriorityScheduler-417"><span class="linenos">417</span></a>                                            <span class="n">default_priority</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-418"><a href="#LoopYieldPriorityScheduler-418"><span class="linenos">418</span></a>                                            <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="LoopYieldPriorityScheduler-419"><a href="#LoopYieldPriorityScheduler-419"><span class="linenos">419</span></a>            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">InterfaceAsyncAwait</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-420"><a href="#LoopYieldPriorityScheduler-420"><span class="linenos">420</span></a>                <span class="n">loop_yield</span> <span class="o">=</span> <span class="n">LoopYieldManagedAsync</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-421"><a href="#LoopYieldPriorityScheduler-421"><span class="linenos">421</span></a>                                                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">default_priority</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-422"><a href="#LoopYieldPriorityScheduler-422"><span class="linenos">422</span></a>                                                <span class="n">default_priority</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-423"><a href="#LoopYieldPriorityScheduler-423"><span class="linenos">423</span></a>                                                <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="LoopYieldPriorityScheduler-424"><a href="#LoopYieldPriorityScheduler-424"><span class="linenos">424</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-425"><a href="#LoopYieldPriorityScheduler-425"><span class="linenos">425</span></a>                <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="LoopYieldPriorityScheduler-426"><a href="#LoopYieldPriorityScheduler-426"><span class="linenos">426</span></a>            
</span><span id="LoopYieldPriorityScheduler-427"><a href="#LoopYieldPriorityScheduler-427"><span class="linenos">427</span></a>            <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-428"><a href="#LoopYieldPriorityScheduler-428"><span class="linenos">428</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop_yield</span>
</span><span id="LoopYieldPriorityScheduler-429"><a href="#LoopYieldPriorityScheduler-429"><span class="linenos">429</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-430"><a href="#LoopYieldPriorityScheduler-430"><span class="linenos">430</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-431"><a href="#LoopYieldPriorityScheduler-431"><span class="linenos">431</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-432"><a href="#LoopYieldPriorityScheduler-432"><span class="linenos">432</span></a>        
</span><span id="LoopYieldPriorityScheduler-433"><a href="#LoopYieldPriorityScheduler-433"><span class="linenos">433</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-434"><a href="#LoopYieldPriorityScheduler-434"><span class="linenos">434</span></a>
</span><span id="LoopYieldPriorityScheduler-435"><a href="#LoopYieldPriorityScheduler-435"><span class="linenos">435</span></a>    <span class="k">def</span> <span class="nf">_on_setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_delay</span><span class="p">:</span> <span class="nb">float</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-436"><a href="#LoopYieldPriorityScheduler-436"><span class="linenos">436</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">=</span> <span class="n">max_delay</span>
</span><span id="LoopYieldPriorityScheduler-437"><a href="#LoopYieldPriorityScheduler-437"><span class="linenos">437</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">compute_delays</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-438"><a href="#LoopYieldPriorityScheduler-438"><span class="linenos">438</span></a>        <span class="c1"># self.compute_time_atoms()</span>
</span><span id="LoopYieldPriorityScheduler-439"><a href="#LoopYieldPriorityScheduler-439"><span class="linenos">439</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-440"><a href="#LoopYieldPriorityScheduler-440"><span class="linenos">440</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-441"><a href="#LoopYieldPriorityScheduler-441"><span class="linenos">441</span></a>
</span><span id="LoopYieldPriorityScheduler-442"><a href="#LoopYieldPriorityScheduler-442"><span class="linenos">442</span></a>    <span class="k">def</span> <span class="nf">_on_change_priority</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-443"><a href="#LoopYieldPriorityScheduler-443"><span class="linenos">443</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">old_priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-444"><a href="#LoopYieldPriorityScheduler-444"><span class="linenos">444</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">new_priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-445"><a href="#LoopYieldPriorityScheduler-445"><span class="linenos">445</span></a>        <span class="n">loop_yield</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-446"><a href="#LoopYieldPriorityScheduler-446"><span class="linenos">446</span></a>        <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">new_priority</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-447"><a href="#LoopYieldPriorityScheduler-447"><span class="linenos">447</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-448"><a href="#LoopYieldPriorityScheduler-448"><span class="linenos">448</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-449"><a href="#LoopYieldPriorityScheduler-449"><span class="linenos">449</span></a>
</span><span id="LoopYieldPriorityScheduler-450"><a href="#LoopYieldPriorityScheduler-450"><span class="linenos">450</span></a>    <span class="k">def</span> <span class="nf">_on_get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-451"><a href="#LoopYieldPriorityScheduler-451"><span class="linenos">451</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">),</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-452"><a href="#LoopYieldPriorityScheduler-452"><span class="linenos">452</span></a>
</span><span id="LoopYieldPriorityScheduler-453"><a href="#LoopYieldPriorityScheduler-453"><span class="linenos">453</span></a>    <span class="k">def</span> <span class="nf">get_yield_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">LoopYieldManagedBase</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-454"><a href="#LoopYieldPriorityScheduler-454"><span class="linenos">454</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-455"><a href="#LoopYieldPriorityScheduler-455"><span class="linenos">455</span></a>    
</span><span id="LoopYieldPriorityScheduler-456"><a href="#LoopYieldPriorityScheduler-456"><span class="linenos">456</span></a>    <span class="k">def</span> <span class="nf">_on_register_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-457"><a href="#LoopYieldPriorityScheduler-457"><span class="linenos">457</span></a>        <span class="n">task_id</span> <span class="o">=</span> <span class="o">-</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="LoopYieldPriorityScheduler-458"><a href="#LoopYieldPriorityScheduler-458"><span class="linenos">458</span></a>        <span class="n">loop_yield</span> <span class="o">=</span> <span class="n">LoopYieldManagedAsyncExternal</span><span class="p">(</span><span class="n">task_id</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-459"><a href="#LoopYieldPriorityScheduler-459"><span class="linenos">459</span></a>                                                   <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">default_priority</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-460"><a href="#LoopYieldPriorityScheduler-460"><span class="linenos">460</span></a>                                                   <span class="n">default_priority</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-461"><a href="#LoopYieldPriorityScheduler-461"><span class="linenos">461</span></a>                                                   <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span>
</span><span id="LoopYieldPriorityScheduler-462"><a href="#LoopYieldPriorityScheduler-462"><span class="linenos">462</span></a>                                                   <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-463"><a href="#LoopYieldPriorityScheduler-463"><span class="linenos">463</span></a>                                                   <span class="n">asyncio_loop</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-464"><a href="#LoopYieldPriorityScheduler-464"><span class="linenos">464</span></a>        <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-465"><a href="#LoopYieldPriorityScheduler-465"><span class="linenos">465</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop_yield</span>
</span><span id="LoopYieldPriorityScheduler-466"><a href="#LoopYieldPriorityScheduler-466"><span class="linenos">466</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-467"><a href="#LoopYieldPriorityScheduler-467"><span class="linenos">467</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-468"><a href="#LoopYieldPriorityScheduler-468"><span class="linenos">468</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-469"><a href="#LoopYieldPriorityScheduler-469"><span class="linenos">469</span></a>    
</span><span id="LoopYieldPriorityScheduler-470"><a href="#LoopYieldPriorityScheduler-470"><span class="linenos">470</span></a>    <span class="k">def</span> <span class="nf">_on_register_external_asyncio_task</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">task</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-471"><a href="#LoopYieldPriorityScheduler-471"><span class="linenos">471</span></a>        <span class="n">asyncio_task_id</span> <span class="o">=</span> <span class="nb">id</span><span class="p">(</span><span class="n">task</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-472"><a href="#LoopYieldPriorityScheduler-472"><span class="linenos">472</span></a>        <span class="k">if</span> <span class="n">asyncio_task_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-473"><a href="#LoopYieldPriorityScheduler-473"><span class="linenos">473</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">[</span><span class="n">asyncio_task_id</span><span class="p">]</span> <span class="o">=</span> <span class="o">-</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="LoopYieldPriorityScheduler-474"><a href="#LoopYieldPriorityScheduler-474"><span class="linenos">474</span></a>            
</span><span id="LoopYieldPriorityScheduler-475"><a href="#LoopYieldPriorityScheduler-475"><span class="linenos">475</span></a>        <span class="n">task_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">[</span><span class="n">asyncio_task_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-476"><a href="#LoopYieldPriorityScheduler-476"><span class="linenos">476</span></a>        <span class="k">if</span> <span class="n">task_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-477"><a href="#LoopYieldPriorityScheduler-477"><span class="linenos">477</span></a>            <span class="n">loop_yield</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-478"><a href="#LoopYieldPriorityScheduler-478"><span class="linenos">478</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-479"><a href="#LoopYieldPriorityScheduler-479"><span class="linenos">479</span></a>            <span class="n">loop_yield</span> <span class="o">=</span> <span class="n">LoopYieldManagedAsyncExternal</span><span class="p">(</span><span class="n">task_id</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-480"><a href="#LoopYieldPriorityScheduler-480"><span class="linenos">480</span></a>                                                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">default_priority</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler-481"><a href="#LoopYieldPriorityScheduler-481"><span class="linenos">481</span></a>                                                    <span class="n">default_priority</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-482"><a href="#LoopYieldPriorityScheduler-482"><span class="linenos">482</span></a>                                                    <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span>
</span><span id="LoopYieldPriorityScheduler-483"><a href="#LoopYieldPriorityScheduler-483"><span class="linenos">483</span></a>                                                    <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler-484"><a href="#LoopYieldPriorityScheduler-484"><span class="linenos">484</span></a>                                                    <span class="n">asyncio_loop</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-485"><a href="#LoopYieldPriorityScheduler-485"><span class="linenos">485</span></a>            <span class="k">def</span> <span class="nf">on_done_asyncio_coro</span><span class="p">(</span><span class="n">future</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-486"><a href="#LoopYieldPriorityScheduler-486"><span class="linenos">486</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_on_del_external</span><span class="p">(</span><span class="n">loop_yield</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-487"><a href="#LoopYieldPriorityScheduler-487"><span class="linenos">487</span></a>                <span class="n">task</span><span class="o">.</span><span class="n">remove_done_callback</span><span class="p">(</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-488"><a href="#LoopYieldPriorityScheduler-488"><span class="linenos">488</span></a>            
</span><span id="LoopYieldPriorityScheduler-489"><a href="#LoopYieldPriorityScheduler-489"><span class="linenos">489</span></a>            <span class="n">loop_yield</span><span class="o">.</span><span class="n">asyncio_task</span> <span class="o">=</span> <span class="n">task</span>
</span><span id="LoopYieldPriorityScheduler-490"><a href="#LoopYieldPriorityScheduler-490"><span class="linenos">490</span></a>            <span class="n">loop_yield</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span> <span class="o">=</span> <span class="n">on_done_asyncio_coro</span>
</span><span id="LoopYieldPriorityScheduler-491"><a href="#LoopYieldPriorityScheduler-491"><span class="linenos">491</span></a>            <span class="n">task</span><span class="o">.</span><span class="n">add_done_callback</span><span class="p">(</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-492"><a href="#LoopYieldPriorityScheduler-492"><span class="linenos">492</span></a>            <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-493"><a href="#LoopYieldPriorityScheduler-493"><span class="linenos">493</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop_yield</span>
</span><span id="LoopYieldPriorityScheduler-494"><a href="#LoopYieldPriorityScheduler-494"><span class="linenos">494</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-495"><a href="#LoopYieldPriorityScheduler-495"><span class="linenos">495</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-496"><a href="#LoopYieldPriorityScheduler-496"><span class="linenos">496</span></a>        
</span><span id="LoopYieldPriorityScheduler-497"><a href="#LoopYieldPriorityScheduler-497"><span class="linenos">497</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-498"><a href="#LoopYieldPriorityScheduler-498"><span class="linenos">498</span></a>    
</span><span id="LoopYieldPriorityScheduler-499"><a href="#LoopYieldPriorityScheduler-499"><span class="linenos">499</span></a>    <span class="k">def</span> <span class="nf">_on_change_priority_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span><span class="p">,</span> <span class="n">new_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">old_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-500"><a href="#LoopYieldPriorityScheduler-500"><span class="linenos">500</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">old_priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-501"><a href="#LoopYieldPriorityScheduler-501"><span class="linenos">501</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">new_priority</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-502"><a href="#LoopYieldPriorityScheduler-502"><span class="linenos">502</span></a>        <span class="n">loop_yield</span><span class="o">.</span><span class="n">time_atom</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">new_priority</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-503"><a href="#LoopYieldPriorityScheduler-503"><span class="linenos">503</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-504"><a href="#LoopYieldPriorityScheduler-504"><span class="linenos">504</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-505"><a href="#LoopYieldPriorityScheduler-505"><span class="linenos">505</span></a>    
</span><span id="LoopYieldPriorityScheduler-506"><a href="#LoopYieldPriorityScheduler-506"><span class="linenos">506</span></a>    <span class="k">def</span> <span class="nf">_on_del_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop_yield</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler-507"><a href="#LoopYieldPriorityScheduler-507"><span class="linenos">507</span></a>        <span class="n">task_id</span> <span class="o">=</span> <span class="n">loop_yield</span><span class="o">.</span><span class="n">task_id</span>
</span><span id="LoopYieldPriorityScheduler-508"><a href="#LoopYieldPriorityScheduler-508"><span class="linenos">508</span></a>        <span class="k">if</span> <span class="n">task_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-509"><a href="#LoopYieldPriorityScheduler-509"><span class="linenos">509</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span><span class="o">.</span><span class="n">priority</span>
</span><span id="LoopYieldPriorityScheduler-510"><a href="#LoopYieldPriorityScheduler-510"><span class="linenos">510</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">task_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-511"><a href="#LoopYieldPriorityScheduler-511"><span class="linenos">511</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-512"><a href="#LoopYieldPriorityScheduler-512"><span class="linenos">512</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-513"><a href="#LoopYieldPriorityScheduler-513"><span class="linenos">513</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-514"><a href="#LoopYieldPriorityScheduler-514"><span class="linenos">514</span></a>    
</span><span id="LoopYieldPriorityScheduler-515"><a href="#LoopYieldPriorityScheduler-515"><span class="linenos">515</span></a>    <span class="k">def</span> <span class="nf">_request_coro_kill</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-516"><a href="#LoopYieldPriorityScheduler-516"><span class="linenos">516</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-517"><a href="#LoopYieldPriorityScheduler-517"><span class="linenos">517</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-518"><a href="#LoopYieldPriorityScheduler-518"><span class="linenos">518</span></a>    
</span><span id="LoopYieldPriorityScheduler-519"><a href="#LoopYieldPriorityScheduler-519"><span class="linenos">519</span></a>    <span class="k">def</span> <span class="nf">_kill_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-520"><a href="#LoopYieldPriorityScheduler-520"><span class="linenos">520</span></a>        <span class="n">waiter_coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span>
</span><span id="LoopYieldPriorityScheduler-521"><a href="#LoopYieldPriorityScheduler-521"><span class="linenos">521</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-522"><a href="#LoopYieldPriorityScheduler-522"><span class="linenos">522</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-523"><a href="#LoopYieldPriorityScheduler-523"><span class="linenos">523</span></a>        
</span><span id="LoopYieldPriorityScheduler-524"><a href="#LoopYieldPriorityScheduler-524"><span class="linenos">524</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">waiter_coro_id</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler-525"><a href="#LoopYieldPriorityScheduler-525"><span class="linenos">525</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler-526"><a href="#LoopYieldPriorityScheduler-526"><span class="linenos">526</span></a>
</span><span id="LoopYieldPriorityScheduler-527"><a href="#LoopYieldPriorityScheduler-527"><span class="linenos">527</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler_global</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-528"><a href="#LoopYieldPriorityScheduler-528"><span class="linenos">528</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="LoopYieldPriorityScheduler-529"><a href="#LoopYieldPriorityScheduler-529"><span class="linenos">529</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-530"><a href="#LoopYieldPriorityScheduler-530"><span class="linenos">530</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">priority</span>
</span><span id="LoopYieldPriorityScheduler-531"><a href="#LoopYieldPriorityScheduler-531"><span class="linenos">531</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-532"><a href="#LoopYieldPriorityScheduler-532"><span class="linenos">532</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-533"><a href="#LoopYieldPriorityScheduler-533"><span class="linenos">533</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-534"><a href="#LoopYieldPriorityScheduler-534"><span class="linenos">534</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="LoopYieldPriorityScheduler-535"><a href="#LoopYieldPriorityScheduler-535"><span class="linenos">535</span></a>
</span><span id="LoopYieldPriorityScheduler-536"><a href="#LoopYieldPriorityScheduler-536"><span class="linenos">536</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler-537"><a href="#LoopYieldPriorityScheduler-537"><span class="linenos">537</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="LoopYieldPriorityScheduler-538"><a href="#LoopYieldPriorityScheduler-538"><span class="linenos">538</span></a>        <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">priority</span>
</span><span id="LoopYieldPriorityScheduler-539"><a href="#LoopYieldPriorityScheduler-539"><span class="linenos">539</span></a>        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler-540"><a href="#LoopYieldPriorityScheduler-540"><span class="linenos">540</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">priority</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler-541"><a href="#LoopYieldPriorityScheduler-541"><span class="linenos">541</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler-542"><a href="#LoopYieldPriorityScheduler-542"><span class="linenos">542</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="LoopYieldPriorityScheduler.__init__" class="classattr">
                                        <input id="LoopYieldPriorityScheduler.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LoopYieldPriorityScheduler</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="LoopYieldPriorityScheduler.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPriorityScheduler.__init__-248"><a href="#LoopYieldPriorityScheduler.__init__-248"><span class="linenos">248</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler.__init__-249"><a href="#LoopYieldPriorityScheduler.__init__-249"><span class="linenos">249</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler.__init__-250"><a href="#LoopYieldPriorityScheduler.__init__-250"><span class="linenos">250</span></a>
</span><span id="LoopYieldPriorityScheduler.__init__-251"><a href="#LoopYieldPriorityScheduler.__init__-251"><span class="linenos">251</span></a>        <span class="c1"># loop.add_global_on_coro_del_handler(self._on_coro_del_handler_global)  # Todo: switch to local coro del handler</span>
</span><span id="LoopYieldPriorityScheduler.__init__-252"><a href="#LoopYieldPriorityScheduler.__init__-252"><span class="linenos">252</span></a>
</span><span id="LoopYieldPriorityScheduler.__init__-253"><a href="#LoopYieldPriorityScheduler.__init__-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler.__init__-254"><a href="#LoopYieldPriorityScheduler.__init__-254"><span class="linenos">254</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-255"><a href="#LoopYieldPriorityScheduler.__init__-255"><span class="linenos">255</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_setup</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-256"><a href="#LoopYieldPriorityScheduler.__init__-256"><span class="linenos">256</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_change_priority</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-257"><a href="#LoopYieldPriorityScheduler.__init__-257"><span class="linenos">257</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-258"><a href="#LoopYieldPriorityScheduler.__init__-258"><span class="linenos">258</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_external</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-259"><a href="#LoopYieldPriorityScheduler.__init__-259"><span class="linenos">259</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register_external_asyncio_task</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-260"><a href="#LoopYieldPriorityScheduler.__init__-260"><span class="linenos">260</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_change_priority_external</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-261"><a href="#LoopYieldPriorityScheduler.__init__-261"><span class="linenos">261</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_del_external</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-262"><a href="#LoopYieldPriorityScheduler.__init__-262"><span class="linenos">262</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_coro_kill</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-263"><a href="#LoopYieldPriorityScheduler.__init__-263"><span class="linenos">263</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kill_coro</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-264"><a href="#LoopYieldPriorityScheduler.__init__-264"><span class="linenos">264</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler.__init__-265"><a href="#LoopYieldPriorityScheduler.__init__-265"><span class="linenos">265</span></a>
</span><span id="LoopYieldPriorityScheduler.__init__-266"><a href="#LoopYieldPriorityScheduler.__init__-266"><span class="linenos">266</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler.__init__-267"><a href="#LoopYieldPriorityScheduler.__init__-267"><span class="linenos">267</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="mf">0.6827</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-268"><a href="#LoopYieldPriorityScheduler.__init__-268"><span class="linenos">268</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="mf">0.9545</span> <span class="o">-</span> <span class="mf">0.6827</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-269"><a href="#LoopYieldPriorityScheduler.__init__-269"><span class="linenos">269</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="mf">1.0</span> <span class="o">-</span> <span class="mf">0.9545</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-270"><a href="#LoopYieldPriorityScheduler.__init__-270"><span class="linenos">270</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler.__init__-271"><a href="#LoopYieldPriorityScheduler.__init__-271"><span class="linenos">271</span></a>
</span><span id="LoopYieldPriorityScheduler.__init__-272"><a href="#LoopYieldPriorityScheduler.__init__-272"><span class="linenos">272</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">=</span> <span class="mf">0.01</span>
</span><span id="LoopYieldPriorityScheduler.__init__-273"><a href="#LoopYieldPriorityScheduler.__init__-273"><span class="linenos">273</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler.__init__-274"><a href="#LoopYieldPriorityScheduler.__init__-274"><span class="linenos">274</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-275"><a href="#LoopYieldPriorityScheduler.__init__-275"><span class="linenos">275</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-276"><a href="#LoopYieldPriorityScheduler.__init__-276"><span class="linenos">276</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="mf">0.0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-277"><a href="#LoopYieldPriorityScheduler.__init__-277"><span class="linenos">277</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler.__init__-278"><a href="#LoopYieldPriorityScheduler.__init__-278"><span class="linenos">278</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">compute_delays</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler.__init__-279"><a href="#LoopYieldPriorityScheduler.__init__-279"><span class="linenos">279</span></a>
</span><span id="LoopYieldPriorityScheduler.__init__-280"><a href="#LoopYieldPriorityScheduler.__init__-280"><span class="linenos">280</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># type: Dict[CoroID, LoopYieldManagedBase]</span>
</span><span id="LoopYieldPriorityScheduler.__init__-281"><a href="#LoopYieldPriorityScheduler.__init__-281"><span class="linenos">281</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler.__init__-282"><a href="#LoopYieldPriorityScheduler.__init__-282"><span class="linenos">282</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">task_counter</span><span class="o">.</span><span class="n">get</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.__init__-283"><a href="#LoopYieldPriorityScheduler.__init__-283"><span class="linenos">283</span></a>            <span class="k">pass</span>
</span><span id="LoopYieldPriorityScheduler.__init__-284"><a href="#LoopYieldPriorityScheduler.__init__-284"><span class="linenos">284</span></a>        
</span><span id="LoopYieldPriorityScheduler.__init__-285"><a href="#LoopYieldPriorityScheduler.__init__-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="LoopYieldPriorityScheduler.__init__-286"><a href="#LoopYieldPriorityScheduler.__init__-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler.__init__-287"><a href="#LoopYieldPriorityScheduler.__init__-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler.__init__-288"><a href="#LoopYieldPriorityScheduler.__init__-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler.__init__-289"><a href="#LoopYieldPriorityScheduler.__init__-289"><span class="linenos">289</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task_ids</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler.__init__-290"><a href="#LoopYieldPriorityScheduler.__init__-290"><span class="linenos">290</span></a>
</span><span id="LoopYieldPriorityScheduler.__init__-291"><a href="#LoopYieldPriorityScheduler.__init__-291"><span class="linenos">291</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler.__init__-292"><a href="#LoopYieldPriorityScheduler.__init__-292"><span class="linenos">292</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">:</span>   <span class="mi">0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-293"><a href="#LoopYieldPriorityScheduler.__init__-293"><span class="linenos">293</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-294"><a href="#LoopYieldPriorityScheduler.__init__-294"><span class="linenos">294</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">:</span>    <span class="mi">0</span><span class="p">,</span>
</span><span id="LoopYieldPriorityScheduler.__init__-295"><a href="#LoopYieldPriorityScheduler.__init__-295"><span class="linenos">295</span></a>        <span class="p">}</span>
</span><span id="LoopYieldPriorityScheduler.__init__-296"><a href="#LoopYieldPriorityScheduler.__init__-296"><span class="linenos">296</span></a>
</span><span id="LoopYieldPriorityScheduler.__init__-297"><a href="#LoopYieldPriorityScheduler.__init__-297"><span class="linenos">297</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler.__init__-298"><a href="#LoopYieldPriorityScheduler.__init__-298"><span class="linenos">298</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">:</span>   <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
</span><span id="LoopYieldPriorityScheduler.__init__-299"><a href="#LoopYieldPriorityScheduler.__init__-299"><span class="linenos">299</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
</span><span id="LoopYieldPriorityScheduler.__init__-300"><a href="#LoopYieldPriorityScheduler.__init__-300"><span class="linenos">300</span></a>            <span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">:</span>    <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">2</span><span class="p">]),</span>
</span><span id="LoopYieldPriorityScheduler.__init__-301"><a href="#LoopYieldPriorityScheduler.__init__-301"><span class="linenos">301</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPriorityScheduler.sigma" class="classattr">
                                <div class="attr variable">
            <span class="name">sigma</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.sigma"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.max_delay" class="classattr">
                                <div class="attr variable">
            <span class="name">max_delay</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.max_delay"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.max_delays" class="classattr">
                                <div class="attr variable">
            <span class="name">max_delays</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.max_delays"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.all_yield_objects" class="classattr">
                                <div class="attr variable">
            <span class="name">all_yield_objects</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.all_yield_objects"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.task_counter" class="classattr">
                                <div class="attr variable">
            <span class="name">task_counter</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.task_counter"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.yields_num" class="classattr">
                                <div class="attr variable">
            <span class="name">yields_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.yields_num"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.coroutines_requested_to_be_deleted" class="classattr">
                                <div class="attr variable">
            <span class="name">coroutines_requested_to_be_deleted</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.coroutines_requested_to_be_deleted"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.coroutines_requested_to_be_deleted_by_waiters" class="classattr">
                                <div class="attr variable">
            <span class="name">coroutines_requested_to_be_deleted_by_waiters</span><span class="annotation">: Dict[int, Set[int]]</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.coroutines_requested_to_be_deleted_by_waiters"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.finished_waiters_for_coro_kill" class="classattr">
                                <div class="attr variable">
            <span class="name">finished_waiters_for_coro_kill</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.finished_waiters_for_coro_kill"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.asyncio_task_ids" class="classattr">
                                <div class="attr variable">
            <span class="name">asyncio_task_ids</span><span class="annotation">: Dict[Hashable, int]</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.asyncio_task_ids"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.yields_by_priority" class="classattr">
                                <div class="attr variable">
            <span class="name">yields_by_priority</span><span class="annotation">: Dict[<a href="#CoroPriority">CoroPriority</a>, int]</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.yields_by_priority"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.time_atom_by_priority" class="classattr">
                                <div class="attr variable">
            <span class="name">time_atom_by_priority</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.time_atom_by_priority"></a>
    
    

                            </div>
                            <div id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#LoopYieldPrioritySchedulerRequest">LoopYieldPrioritySchedulerRequest</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-327"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-327"><span class="linenos">327</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-328"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-328"><span class="linenos">328</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-329"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-329"><span class="linenos">329</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">yields_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-330"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-330"><span class="linenos">330</span></a>        <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-331"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-331"><span class="linenos">331</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-332"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-332"><span class="linenos">332</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-333"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-333"><span class="linenos">333</span></a>            <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-334"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-334"><span class="linenos">334</span></a>        
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-335"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-335"><span class="linenos">335</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-336"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-336"><span class="linenos">336</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span> <span class="o">|=</span> <span class="bp">self</span><span class="o">.</span><span class="n">coroutines_requested_to_be_deleted_by_waiters</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-337"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-337"><span class="linenos">337</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-338"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-338"><span class="linenos">338</span></a>            <span class="n">coro_should_be_killed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-339"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-339"><span class="linenos">339</span></a>        
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-340"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-340"><span class="linenos">340</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-341"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-341"><span class="linenos">341</span></a>            <span class="k">if</span> <span class="n">coro_should_be_killed</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_del_external</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span><span class="p">[</span><span class="n">request</span><span class="o">.</span><span class="n">request_type</span><span class="p">]):</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-342"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-342"><span class="linenos">342</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ThisCoroWasRequestedToBeKilled</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-343"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-343"><span class="linenos">343</span></a>                
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-344"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-344"><span class="linenos">344</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-345"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-345"><span class="linenos">345</span></a>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-346"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-346"><span class="linenos">346</span></a>        <span class="k">if</span> <span class="n">coro_should_be_killed</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-347"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-347"><span class="linenos">347</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ThisCoroWasRequestedToBeKilled</span>
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-348"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-348"><span class="linenos">348</span></a>        
</span><span id="LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-349"><a href="#LoopYieldPriorityScheduler.single_task_registration_or_immediate_processing-349"><span class="linenos">349</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPriorityScheduler.full_processing_iteration" class="classattr">
                                        <input id="LoopYieldPriorityScheduler.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="LoopYieldPriorityScheduler.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPriorityScheduler.full_processing_iteration-351"><a href="#LoopYieldPriorityScheduler.full_processing_iteration-351"><span class="linenos">351</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler.full_processing_iteration-352"><a href="#LoopYieldPriorityScheduler.full_processing_iteration-352"><span class="linenos">352</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.full_processing_iteration-353"><a href="#LoopYieldPriorityScheduler.full_processing_iteration-353"><span class="linenos">353</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler.full_processing_iteration-354"><a href="#LoopYieldPriorityScheduler.full_processing_iteration-354"><span class="linenos">354</span></a>        
</span><span id="LoopYieldPriorityScheduler.full_processing_iteration-355"><a href="#LoopYieldPriorityScheduler.full_processing_iteration-355"><span class="linenos">355</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">compute_time_atoms</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPriorityScheduler.compute_time_atoms" class="classattr">
                                        <input id="LoopYieldPriorityScheduler.compute_time_atoms-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">compute_time_atoms</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="LoopYieldPriorityScheduler.compute_time_atoms-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.compute_time_atoms"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPriorityScheduler.compute_time_atoms-357"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-357"><span class="linenos">357</span></a>    <span class="k">def</span> <span class="nf">compute_time_atoms</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-358"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-358"><span class="linenos">358</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-359"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-359"><span class="linenos">359</span></a>            <span class="n">top_sigma</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-360"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-360"><span class="linenos">360</span></a>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-361"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-361"><span class="linenos">361</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-362"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-362"><span class="linenos">362</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-363"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-363"><span class="linenos">363</span></a>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-364"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-364"><span class="linenos">364</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-365"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-365"><span class="linenos">365</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-366"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-366"><span class="linenos">366</span></a>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-367"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-367"><span class="linenos">367</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-368"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-368"><span class="linenos">368</span></a>                <span class="n">top_sigma</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-369"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-369"><span class="linenos">369</span></a>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-370"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-370"><span class="linenos">370</span></a>            <span class="n">median_time_atom</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">)</span>  <span class="c1"># !!! Possible division by zero! Conditional must not be removed!</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-371"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-371"><span class="linenos">371</span></a>            <span class="k">if</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-372"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-372"><span class="linenos">372</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-373"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-373"><span class="linenos">373</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-374"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-374"><span class="linenos">374</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-375"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-375"><span class="linenos">375</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-376"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-376"><span class="linenos">376</span></a>            <span class="k">elif</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-377"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-377"><span class="linenos">377</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-378"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-378"><span class="linenos">378</span></a>                <span class="n">sigma_1_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-379"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-379"><span class="linenos">379</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">yields_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-380"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-380"><span class="linenos">380</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-381"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-381"><span class="linenos">381</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-382"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-382"><span class="linenos">382</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-383"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-383"><span class="linenos">383</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-384"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-384"><span class="linenos">384</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-385"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-385"><span class="linenos">385</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-386"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-386"><span class="linenos">386</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-387"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-387"><span class="linenos">387</span></a>            <span class="k">elif</span> <span class="mi">3</span> <span class="o">==</span> <span class="n">top_sigma</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-388"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-388"><span class="linenos">388</span></a>                <span class="n">sigma_0_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-389"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-389"><span class="linenos">389</span></a>                <span class="n">sigma_1_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-390"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-390"><span class="linenos">390</span></a>                <span class="n">sigma_2_time_atom</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">median_time_atom</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-391"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-391"><span class="linenos">391</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_0_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-392"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-392"><span class="linenos">392</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_1_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-393"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-393"><span class="linenos">393</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">time_atom_by_priority</span><span class="p">[</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">]</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">sigma_2_time_atom</span>
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-394"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-394"><span class="linenos">394</span></a>        
</span><span id="LoopYieldPriorityScheduler.compute_time_atoms-395"><a href="#LoopYieldPriorityScheduler.compute_time_atoms-395"><span class="linenos">395</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPriorityScheduler.in_work" class="classattr">
                                        <input id="LoopYieldPriorityScheduler.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="LoopYieldPriorityScheduler.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPriorityScheduler.in_work-397"><a href="#LoopYieldPriorityScheduler.in_work-397"><span class="linenos">397</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.in_work-398"><a href="#LoopYieldPriorityScheduler.in_work-398"><span class="linenos">398</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">finished_waiters_for_coro_kill</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="p">)</span>
</span><span id="LoopYieldPriorityScheduler.in_work-399"><a href="#LoopYieldPriorityScheduler.in_work-399"><span class="linenos">399</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="LoopYieldPriorityScheduler.compute_delays" class="classattr">
                                        <input id="LoopYieldPriorityScheduler.compute_delays-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">compute_delays</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="LoopYieldPriorityScheduler.compute_delays-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.compute_delays"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPriorityScheduler.compute_delays-401"><a href="#LoopYieldPriorityScheduler.compute_delays-401"><span class="linenos">401</span></a>    <span class="k">def</span> <span class="nf">compute_delays</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="LoopYieldPriorityScheduler.compute_delays-402"><a href="#LoopYieldPriorityScheduler.compute_delays-402"><span class="linenos">402</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_delays</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="LoopYieldPriorityScheduler.compute_delays-403"><a href="#LoopYieldPriorityScheduler.compute_delays-403"><span class="linenos">403</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler.compute_delays-404"><a href="#LoopYieldPriorityScheduler.compute_delays-404"><span class="linenos">404</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler.compute_delays-405"><a href="#LoopYieldPriorityScheduler.compute_delays-405"><span class="linenos">405</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_delay</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigma</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
</span><span id="LoopYieldPriorityScheduler.compute_delays-406"><a href="#LoopYieldPriorityScheduler.compute_delays-406"><span class="linenos">406</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldPriorityScheduler.get_yield_object" class="classattr">
                                        <input id="LoopYieldPriorityScheduler.get_yield_object-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_yield_object</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro_id</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="n"><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></span>:</span></span>

                <label class="view-source-button" for="LoopYieldPriorityScheduler.get_yield_object-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldPriorityScheduler.get_yield_object"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldPriorityScheduler.get_yield_object-453"><a href="#LoopYieldPriorityScheduler.get_yield_object-453"><span class="linenos">453</span></a>    <span class="k">def</span> <span class="nf">get_yield_object</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">LoopYieldManagedBase</span><span class="p">:</span>
</span><span id="LoopYieldPriorityScheduler.get_yield_object-454"><a href="#LoopYieldPriorityScheduler.get_yield_object-454"><span class="linenos">454</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_yield_objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</dt>
                                <dd id="LoopYieldPriorityScheduler.StatsLevel" class="class">StatsLevel</dd>
                <dd id="LoopYieldPriorityScheduler.get_entity_stats" class="function">get_entity_stats</dd>

            </div>
            <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="LoopYieldPriorityScheduler.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="LoopYieldPriorityScheduler.iteration" class="function">iteration</dd>
                <dd id="LoopYieldPriorityScheduler.make_response" class="function">make_response</dd>
                <dd id="LoopYieldPriorityScheduler.register_response" class="function">register_response</dd>
                <dd id="LoopYieldPriorityScheduler.put_task" class="function">put_task</dd>
                <dd id="LoopYieldPriorityScheduler.resolve_request" class="function">resolve_request</dd>
                <dd id="LoopYieldPriorityScheduler.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="LoopYieldPriorityScheduler.in_forground_work" class="function">in_forground_work</dd>
                <dd id="LoopYieldPriorityScheduler.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="LoopYieldPriorityScheduler.time_left_before_next_event" class="function">time_left_before_next_event</dd>
                <dd id="LoopYieldPriorityScheduler.is_low_latency" class="function">is_low_latency</dd>
                <dd id="LoopYieldPriorityScheduler.make_live" class="function">make_live</dd>
                <dd id="LoopYieldPriorityScheduler.make_dead" class="function">make_dead</dd>
                <dd id="LoopYieldPriorityScheduler.service_id_impl" class="function">service_id_impl</dd>
                <dd id="LoopYieldPriorityScheduler.service_id" class="function">service_id</dd>
                <dd id="LoopYieldPriorityScheduler.destroy" class="function">destroy</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="get_loop_yield">
                            <input id="get_loop_yield-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_loop_yield</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#CoroPriority.normal">CoroPriority.normal</a></span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#LoopYieldManaged">LoopYieldManaged</a></span><span class="p">,</span> <span class="n"><a href="#FakeLoopYieldManaged">FakeLoopYieldManaged</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="get_loop_yield-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_loop_yield"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_loop_yield-548"><a href="#get_loop_yield-548"><span class="linenos">548</span></a><span class="k">def</span> <span class="nf">get_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">LoopYieldManaged</span><span class="p">,</span> <span class="n">FakeLoopYieldManaged</span><span class="p">]:</span>
</span><span id="get_loop_yield-549"><a href="#get_loop_yield-549"><span class="linenos">549</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="get_loop_yield-550"><a href="#get_loop_yield-550"><span class="linenos">550</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_loop_yield-551"><a href="#get_loop_yield-551"><span class="linenos">551</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManaged</span><span class="p">()</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="get_loop_yield-552"><a href="#get_loop_yield-552"><span class="linenos">552</span></a>
</span><span id="get_loop_yield-553"><a href="#get_loop_yield-553"><span class="linenos">553</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="get_loop_yield-554"><a href="#get_loop_yield-554"><span class="linenos">554</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_loop_yield-555"><a href="#get_loop_yield-555"><span class="linenos">555</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManaged</span><span class="p">()</span>  <span class="c1"># running from Service</span>
</span><span id="get_loop_yield-556"><a href="#get_loop_yield-556"><span class="linenos">556</span></a>
</span><span id="get_loop_yield-557"><a href="#get_loop_yield-557"><span class="linenos">557</span></a>    <span class="c1"># ly = interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().get())</span>
</span><span id="get_loop_yield-558"><a href="#get_loop_yield-558"><span class="linenos">558</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">)</span><span class="o">.</span><span class="n">get_yield_object</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="get_loop_yield-559"><a href="#get_loop_yield-559"><span class="linenos">559</span></a>    <span class="k">if</span> <span class="n">ly</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_loop_yield-560"><a href="#get_loop_yield-560"><span class="linenos">560</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">default_priority</span><span class="p">))</span>
</span><span id="get_loop_yield-561"><a href="#get_loop_yield-561"><span class="linenos">561</span></a>    
</span><span id="get_loop_yield-562"><a href="#get_loop_yield-562"><span class="linenos">562</span></a>    <span class="k">return</span> <span class="n">ly</span>
</span></pre></div>


    

                </section>
                <section id="gly">
                            <input id="gly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gly</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#CoroPriority.normal">CoroPriority.normal</a></span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#LoopYieldManaged">LoopYieldManaged</a></span><span class="p">,</span> <span class="n"><a href="#FakeLoopYieldManaged">FakeLoopYieldManaged</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="gly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gly-548"><a href="#gly-548"><span class="linenos">548</span></a><span class="k">def</span> <span class="nf">get_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">LoopYieldManaged</span><span class="p">,</span> <span class="n">FakeLoopYieldManaged</span><span class="p">]:</span>
</span><span id="gly-549"><a href="#gly-549"><span class="linenos">549</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="gly-550"><a href="#gly-550"><span class="linenos">550</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="gly-551"><a href="#gly-551"><span class="linenos">551</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManaged</span><span class="p">()</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="gly-552"><a href="#gly-552"><span class="linenos">552</span></a>
</span><span id="gly-553"><a href="#gly-553"><span class="linenos">553</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="gly-554"><a href="#gly-554"><span class="linenos">554</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="gly-555"><a href="#gly-555"><span class="linenos">555</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManaged</span><span class="p">()</span>  <span class="c1"># running from Service</span>
</span><span id="gly-556"><a href="#gly-556"><span class="linenos">556</span></a>
</span><span id="gly-557"><a href="#gly-557"><span class="linenos">557</span></a>    <span class="c1"># ly = interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().get())</span>
</span><span id="gly-558"><a href="#gly-558"><span class="linenos">558</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">)</span><span class="o">.</span><span class="n">get_yield_object</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="gly-559"><a href="#gly-559"><span class="linenos">559</span></a>    <span class="k">if</span> <span class="n">ly</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="gly-560"><a href="#gly-560"><span class="linenos">560</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">default_priority</span><span class="p">))</span>
</span><span id="gly-561"><a href="#gly-561"><span class="linenos">561</span></a>    
</span><span id="gly-562"><a href="#gly-562"><span class="linenos">562</span></a>    <span class="k">return</span> <span class="n">ly</span>
</span></pre></div>


    

                </section>
                <section id="aget_loop_yield">
                            <input id="aget_loop_yield-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aget_loop_yield</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#CoroPriority.normal">CoroPriority.normal</a></span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#LoopYieldManagedAsync">LoopYieldManagedAsync</a></span><span class="p">,</span> <span class="n"><a href="#FakeLoopYieldManagedAsync">FakeLoopYieldManagedAsync</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="aget_loop_yield-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#aget_loop_yield"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="aget_loop_yield-568"><a href="#aget_loop_yield-568"><span class="linenos">568</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">LoopYieldManagedAsync</span><span class="p">,</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">]:</span>
</span><span id="aget_loop_yield-569"><a href="#aget_loop_yield-569"><span class="linenos">569</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="aget_loop_yield-570"><a href="#aget_loop_yield-570"><span class="linenos">570</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="aget_loop_yield-571"><a href="#aget_loop_yield-571"><span class="linenos">571</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">()</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="aget_loop_yield-572"><a href="#aget_loop_yield-572"><span class="linenos">572</span></a>
</span><span id="aget_loop_yield-573"><a href="#aget_loop_yield-573"><span class="linenos">573</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="aget_loop_yield-574"><a href="#aget_loop_yield-574"><span class="linenos">574</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="aget_loop_yield-575"><a href="#aget_loop_yield-575"><span class="linenos">575</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">()</span>  <span class="c1"># running from Service</span>
</span><span id="aget_loop_yield-576"><a href="#aget_loop_yield-576"><span class="linenos">576</span></a>
</span><span id="aget_loop_yield-577"><a href="#aget_loop_yield-577"><span class="linenos">577</span></a>    <span class="c1"># ly = await interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().get())</span>
</span><span id="aget_loop_yield-578"><a href="#aget_loop_yield-578"><span class="linenos">578</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">)</span><span class="o">.</span><span class="n">get_yield_object</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="aget_loop_yield-579"><a href="#aget_loop_yield-579"><span class="linenos">579</span></a>    <span class="k">if</span> <span class="n">ly</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="aget_loop_yield-580"><a href="#aget_loop_yield-580"><span class="linenos">580</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="k">await</span> <span class="n">interface</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">default_priority</span><span class="p">))</span>
</span><span id="aget_loop_yield-581"><a href="#aget_loop_yield-581"><span class="linenos">581</span></a>    
</span><span id="aget_loop_yield-582"><a href="#aget_loop_yield-582"><span class="linenos">582</span></a>    <span class="k">return</span> <span class="n">ly</span>
</span></pre></div>


    

                </section>
                <section id="agly">
                            <input id="agly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">agly</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#CoroPriority.normal">CoroPriority.normal</a></span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#LoopYieldManagedAsync">LoopYieldManagedAsync</a></span><span class="p">,</span> <span class="n"><a href="#FakeLoopYieldManagedAsync">FakeLoopYieldManagedAsync</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="agly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#agly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="agly-568"><a href="#agly-568"><span class="linenos">568</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">LoopYieldManagedAsync</span><span class="p">,</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">]:</span>
</span><span id="agly-569"><a href="#agly-569"><span class="linenos">569</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="agly-570"><a href="#agly-570"><span class="linenos">570</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="agly-571"><a href="#agly-571"><span class="linenos">571</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">()</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="agly-572"><a href="#agly-572"><span class="linenos">572</span></a>
</span><span id="agly-573"><a href="#agly-573"><span class="linenos">573</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="agly-574"><a href="#agly-574"><span class="linenos">574</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="agly-575"><a href="#agly-575"><span class="linenos">575</span></a>        <span class="k">return</span> <span class="n">FakeLoopYieldManagedAsync</span><span class="p">()</span>  <span class="c1"># running from Service</span>
</span><span id="agly-576"><a href="#agly-576"><span class="linenos">576</span></a>
</span><span id="agly-577"><a href="#agly-577"><span class="linenos">577</span></a>    <span class="c1"># ly = await interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().get())</span>
</span><span id="agly-578"><a href="#agly-578"><span class="linenos">578</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">)</span><span class="o">.</span><span class="n">get_yield_object</span><span class="p">(</span><span class="n">interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="agly-579"><a href="#agly-579"><span class="linenos">579</span></a>    <span class="k">if</span> <span class="n">ly</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="agly-580"><a href="#agly-580"><span class="linenos">580</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="k">await</span> <span class="n">interface</span><span class="p">(</span><span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span> <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">default_priority</span><span class="p">))</span>
</span><span id="agly-581"><a href="#agly-581"><span class="linenos">581</span></a>    
</span><span id="agly-582"><a href="#agly-582"><span class="linenos">582</span></a>    <span class="k">return</span> <span class="n">ly</span>
</span></pre></div>


    

                </section>
                <section id="LoopYieldManagedAsyncExternal">
                            <input id="LoopYieldManagedAsyncExternal-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LoopYieldManagedAsyncExternal</span><wbr>(<span class="base"><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></span>):

                <label class="view-source-button" for="LoopYieldManagedAsyncExternal-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManagedAsyncExternal"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManagedAsyncExternal-203"><a href="#LoopYieldManagedAsyncExternal-203"><span class="linenos">203</span></a><span class="k">class</span> <span class="nc">LoopYieldManagedAsyncExternal</span><span class="p">(</span><span class="n">LoopYieldManagedBase</span><span class="p">):</span>
</span><span id="LoopYieldManagedAsyncExternal-204"><a href="#LoopYieldManagedAsyncExternal-204"><span class="linenos">204</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task_id</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="LoopYieldManagedAsyncExternal-205"><a href="#LoopYieldManagedAsyncExternal-205"><span class="linenos">205</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">],</span> <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">):</span>
</span><span id="LoopYieldManagedAsyncExternal-206"><a href="#LoopYieldManagedAsyncExternal-206"><span class="linenos">206</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManagedAsyncExternal</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsyncExternal-207"><a href="#LoopYieldManagedAsyncExternal-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_id</span> <span class="o">=</span> <span class="n">task_id</span>
</span><span id="LoopYieldManagedAsyncExternal-208"><a href="#LoopYieldManagedAsyncExternal-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span> <span class="o">=</span> <span class="n">coro_scheduler</span>
</span><span id="LoopYieldManagedAsyncExternal-209"><a href="#LoopYieldManagedAsyncExternal-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_loop</span> <span class="o">=</span> <span class="n">asyncio_loop</span>
</span><span id="LoopYieldManagedAsyncExternal-210"><a href="#LoopYieldManagedAsyncExternal-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedAsyncExternal-211"><a href="#LoopYieldManagedAsyncExternal-211"><span class="linenos">211</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedAsyncExternal-212"><a href="#LoopYieldManagedAsyncExternal-212"><span class="linenos">212</span></a>
</span><span id="LoopYieldManagedAsyncExternal-213"><a href="#LoopYieldManagedAsyncExternal-213"><span class="linenos">213</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="LoopYieldManagedAsyncExternal-214"><a href="#LoopYieldManagedAsyncExternal-214"><span class="linenos">214</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsyncExternal-215"><a href="#LoopYieldManagedAsyncExternal-215"><span class="linenos">215</span></a>            <span class="n">priority</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="LoopYieldManagedAsyncExternal-216"><a href="#LoopYieldManagedAsyncExternal-216"><span class="linenos">216</span></a>        <span class="k">if</span> <span class="n">priority</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsyncExternal-217"><a href="#LoopYieldManagedAsyncExternal-217"><span class="linenos">217</span></a>            <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">,</span>
</span><span id="LoopYieldManagedAsyncExternal-218"><a href="#LoopYieldManagedAsyncExternal-218"><span class="linenos">218</span></a>                                  <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">change_priority_external</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">priority</span><span class="p">))</span>
</span><span id="LoopYieldManagedAsyncExternal-219"><a href="#LoopYieldManagedAsyncExternal-219"><span class="linenos">219</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">priority</span> <span class="o">=</span> <span class="n">priority</span>
</span><span id="LoopYieldManagedAsyncExternal-220"><a href="#LoopYieldManagedAsyncExternal-220"><span class="linenos">220</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsyncExternal-221"><a href="#LoopYieldManagedAsyncExternal-221"><span class="linenos">221</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsyncExternal-222"><a href="#LoopYieldManagedAsyncExternal-222"><span class="linenos">222</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsyncExternal-223"><a href="#LoopYieldManagedAsyncExternal-223"><span class="linenos">223</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsyncExternal-224"><a href="#LoopYieldManagedAsyncExternal-224"><span class="linenos">224</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsyncExternal-225"><a href="#LoopYieldManagedAsyncExternal-225"><span class="linenos">225</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsyncExternal-226"><a href="#LoopYieldManagedAsyncExternal-226"><span class="linenos">226</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">time_atom</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsyncExternal-227"><a href="#LoopYieldManagedAsyncExternal-227"><span class="linenos">227</span></a>            <span class="k">except</span> <span class="n">TimeLimitIsTooSmall</span> <span class="k">as</span> <span class="n">ex</span><span class="p">:</span>
</span><span id="LoopYieldManagedAsyncExternal-228"><a href="#LoopYieldManagedAsyncExternal-228"><span class="linenos">228</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="k">if</span> <span class="n">ex</span><span class="o">.</span><span class="n">min_time</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">MIN_TIME</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsyncExternal-229"><a href="#LoopYieldManagedAsyncExternal-229"><span class="linenos">229</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="LoopYieldManagedAsyncExternal-230"><a href="#LoopYieldManagedAsyncExternal-230"><span class="linenos">230</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedAsyncExternal-231"><a href="#LoopYieldManagedAsyncExternal-231"><span class="linenos">231</span></a>            <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">service</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="LoopYieldManagedAsyncExternal.__init__" class="classattr">
                                        <input id="LoopYieldManagedAsyncExternal.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LoopYieldManagedAsyncExternal</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">task_id</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">time_atom</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_1</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueExistence</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span>,</span><span class="param">	<span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span><span class="p">]</span>,</span><span class="param">	<span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span></span>)</span>

                <label class="view-source-button" for="LoopYieldManagedAsyncExternal.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LoopYieldManagedAsyncExternal.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LoopYieldManagedAsyncExternal.__init__-204"><a href="#LoopYieldManagedAsyncExternal.__init__-204"><span class="linenos">204</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">task_id</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">:</span> <span class="n">ValueExistence</span><span class="p">,</span>
</span><span id="LoopYieldManagedAsyncExternal.__init__-205"><a href="#LoopYieldManagedAsyncExternal.__init__-205"><span class="linenos">205</span></a>                 <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">],</span> <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">):</span>
</span><span id="LoopYieldManagedAsyncExternal.__init__-206"><a href="#LoopYieldManagedAsyncExternal.__init__-206"><span class="linenos">206</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">LoopYieldManagedAsyncExternal</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">time_atom</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">,</span> <span class="n">service</span><span class="p">)</span>
</span><span id="LoopYieldManagedAsyncExternal.__init__-207"><a href="#LoopYieldManagedAsyncExternal.__init__-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">task_id</span> <span class="o">=</span> <span class="n">task_id</span>
</span><span id="LoopYieldManagedAsyncExternal.__init__-208"><a href="#LoopYieldManagedAsyncExternal.__init__-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span> <span class="o">=</span> <span class="n">coro_scheduler</span>
</span><span id="LoopYieldManagedAsyncExternal.__init__-209"><a href="#LoopYieldManagedAsyncExternal.__init__-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_loop</span> <span class="o">=</span> <span class="n">asyncio_loop</span>
</span><span id="LoopYieldManagedAsyncExternal.__init__-210"><a href="#LoopYieldManagedAsyncExternal.__init__-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">asyncio_task</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LoopYieldManagedAsyncExternal.__init__-211"><a href="#LoopYieldManagedAsyncExternal.__init__-211"><span class="linenos">211</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_done_asyncio_coro</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="LoopYieldManagedAsyncExternal.task_id" class="classattr">
                                <div class="attr variable">
            <span class="name">task_id</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedAsyncExternal.task_id"></a>
    
    

                            </div>
                            <div id="LoopYieldManagedAsyncExternal.coro_scheduler" class="classattr">
                                <div class="attr variable">
            <span class="name">coro_scheduler</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedAsyncExternal.coro_scheduler"></a>
    
    

                            </div>
                            <div id="LoopYieldManagedAsyncExternal.asyncio_loop" class="classattr">
                                <div class="attr variable">
            <span class="name">asyncio_loop</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedAsyncExternal.asyncio_loop"></a>
    
    

                            </div>
                            <div id="LoopYieldManagedAsyncExternal.asyncio_task" class="classattr">
                                <div class="attr variable">
            <span class="name">asyncio_task</span><span class="annotation">: _asyncio.Task</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedAsyncExternal.asyncio_task"></a>
    
    

                            </div>
                            <div id="LoopYieldManagedAsyncExternal.on_done_asyncio_coro" class="classattr">
                                <div class="attr variable">
            <span class="name">on_done_asyncio_coro</span><span class="annotation">: Callable</span>

        
    </div>
    <a class="headerlink" href="#LoopYieldManagedAsyncExternal.on_done_asyncio_coro"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#LoopYieldManagedBase">LoopYieldManagedBase</a></dt>
                                <dd id="LoopYieldManagedAsyncExternal.interface" class="variable"><a href="#LoopYieldManagedBase.interface">interface</a></dd>
                <dd id="LoopYieldManagedAsyncExternal.time_atom" class="variable"><a href="#LoopYieldManagedBase.time_atom">time_atom</a></dd>
                <dd id="LoopYieldManagedAsyncExternal.default_priority" class="variable"><a href="#LoopYieldManagedBase.default_priority">default_priority</a></dd>
                <dd id="LoopYieldManagedAsyncExternal.priority" class="variable"><a href="#LoopYieldManagedBase.priority">priority</a></dd>
                <dd id="LoopYieldManagedAsyncExternal.service" class="variable"><a href="#LoopYieldManagedBase.service">service</a></dd>
                <dd id="LoopYieldManagedAsyncExternal.tracer" class="variable"><a href="#LoopYieldManagedBase.tracer">tracer</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="FakeLoopYieldManagedAsync">
                            <input id="FakeLoopYieldManagedAsync-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">FakeLoopYieldManagedAsync</span>:

                <label class="view-source-button" for="FakeLoopYieldManagedAsync-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FakeLoopYieldManagedAsync"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FakeLoopYieldManagedAsync-238"><a href="#FakeLoopYieldManagedAsync-238"><span class="linenos">238</span></a><span class="k">class</span> <span class="nc">FakeLoopYieldManagedAsync</span><span class="p">:</span>
</span><span id="FakeLoopYieldManagedAsync-239"><a href="#FakeLoopYieldManagedAsync-239"><span class="linenos">239</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroPriority</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="FakeLoopYieldManagedAsync-240"><a href="#FakeLoopYieldManagedAsync-240"><span class="linenos">240</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                </section>
                <section id="external_aget_loop_yield">
                            <input id="external_aget_loop_yield-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@asynccontextmanager</div>
        <div class="decorator">@async_generator</div>

        <span class="def">def</span>
        <span class="name">external_aget_loop_yield</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#CoroPriority.normal">CoroPriority.normal</a></span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="external_aget_loop_yield-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#external_aget_loop_yield"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="external_aget_loop_yield-588"><a href="#external_aget_loop_yield-588"><span class="linenos">588</span></a><span class="nd">@asynccontextmanager</span>
</span><span id="external_aget_loop_yield-589"><a href="#external_aget_loop_yield-589"><span class="linenos">589</span></a><span class="nd">@async_generator</span>
</span><span id="external_aget_loop_yield-590"><a href="#external_aget_loop_yield-590"><span class="linenos">590</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">external_aget_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="external_aget_loop_yield-591"><a href="#external_aget_loop_yield-591"><span class="linenos">591</span></a>    <span class="k">if</span> <span class="n">coro_scheduler</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-592"><a href="#external_aget_loop_yield-592"><span class="linenos">592</span></a>        <span class="n">coro_scheduler</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="external_aget_loop_yield-593"><a href="#external_aget_loop_yield-593"><span class="linenos">593</span></a>    
</span><span id="external_aget_loop_yield-594"><a href="#external_aget_loop_yield-594"><span class="linenos">594</span></a>    <span class="k">if</span> <span class="n">coro_scheduler</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-595"><a href="#external_aget_loop_yield-595"><span class="linenos">595</span></a>        <span class="k">await</span> <span class="n">yield_</span><span class="p">(</span><span class="n">FakeLoopYieldManagedAsync</span><span class="p">())</span>  <span class="c1"># can not determine coro scheduler loop</span>
</span><span id="external_aget_loop_yield-596"><a href="#external_aget_loop_yield-596"><span class="linenos">596</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-597"><a href="#external_aget_loop_yield-597"><span class="linenos">597</span></a>        <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-598"><a href="#external_aget_loop_yield-598"><span class="linenos">598</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="external_aget_loop_yield-599"><a href="#external_aget_loop_yield-599"><span class="linenos">599</span></a>        
</span><span id="external_aget_loop_yield-600"><a href="#external_aget_loop_yield-600"><span class="linenos">600</span></a>        <span class="k">if</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-601"><a href="#external_aget_loop_yield-601"><span class="linenos">601</span></a>            <span class="n">ly</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span> <span class="o">=</span> <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span>
</span><span id="external_aget_loop_yield-602"><a href="#external_aget_loop_yield-602"><span class="linenos">602</span></a>                <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="external_aget_loop_yield-603"><a href="#external_aget_loop_yield-603"><span class="linenos">603</span></a>                <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_external_asyncio_task</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">current_task</span><span class="p">(</span><span class="n">loop</span><span class="o">=</span><span class="n">asyncio_loop</span><span class="p">),</span> <span class="n">default_priority</span><span class="p">))</span>
</span><span id="external_aget_loop_yield-604"><a href="#external_aget_loop_yield-604"><span class="linenos">604</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-605"><a href="#external_aget_loop_yield-605"><span class="linenos">605</span></a>            <span class="n">ly</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span> <span class="o">=</span> <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span>
</span><span id="external_aget_loop_yield-606"><a href="#external_aget_loop_yield-606"><span class="linenos">606</span></a>                <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="external_aget_loop_yield-607"><a href="#external_aget_loop_yield-607"><span class="linenos">607</span></a>                <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_external</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">))</span>
</span><span id="external_aget_loop_yield-608"><a href="#external_aget_loop_yield-608"><span class="linenos">608</span></a>
</span><span id="external_aget_loop_yield-609"><a href="#external_aget_loop_yield-609"><span class="linenos">609</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-610"><a href="#external_aget_loop_yield-610"><span class="linenos">610</span></a>            <span class="k">await</span> <span class="n">yield_</span><span class="p">(</span><span class="n">ly</span><span class="p">)</span>
</span><span id="external_aget_loop_yield-611"><a href="#external_aget_loop_yield-611"><span class="linenos">611</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-612"><a href="#external_aget_loop_yield-612"><span class="linenos">612</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">:</span>
</span><span id="external_aget_loop_yield-613"><a href="#external_aget_loop_yield-613"><span class="linenos">613</span></a>                <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="external_aget_loop_yield-614"><a href="#external_aget_loop_yield-614"><span class="linenos">614</span></a>                                    <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">del_external</span><span class="p">(</span><span class="n">ly</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="eagly">
                            <input id="eagly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@asynccontextmanager</div>
        <div class="decorator">@async_generator</div>

        <span class="def">def</span>
        <span class="name">eagly</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#CoroPriority.normal">CoroPriority.normal</a></span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="eagly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#eagly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="eagly-588"><a href="#eagly-588"><span class="linenos">588</span></a><span class="nd">@asynccontextmanager</span>
</span><span id="eagly-589"><a href="#eagly-589"><span class="linenos">589</span></a><span class="nd">@async_generator</span>
</span><span id="eagly-590"><a href="#eagly-590"><span class="linenos">590</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">external_aget_loop_yield</span><span class="p">(</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="eagly-591"><a href="#eagly-591"><span class="linenos">591</span></a>    <span class="k">if</span> <span class="n">coro_scheduler</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="eagly-592"><a href="#eagly-592"><span class="linenos">592</span></a>        <span class="n">coro_scheduler</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="eagly-593"><a href="#eagly-593"><span class="linenos">593</span></a>    
</span><span id="eagly-594"><a href="#eagly-594"><span class="linenos">594</span></a>    <span class="k">if</span> <span class="n">coro_scheduler</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="eagly-595"><a href="#eagly-595"><span class="linenos">595</span></a>        <span class="k">await</span> <span class="n">yield_</span><span class="p">(</span><span class="n">FakeLoopYieldManagedAsync</span><span class="p">())</span>  <span class="c1"># can not determine coro scheduler loop</span>
</span><span id="eagly-596"><a href="#eagly-596"><span class="linenos">596</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="eagly-597"><a href="#eagly-597"><span class="linenos">597</span></a>        <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="eagly-598"><a href="#eagly-598"><span class="linenos">598</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="eagly-599"><a href="#eagly-599"><span class="linenos">599</span></a>        
</span><span id="eagly-600"><a href="#eagly-600"><span class="linenos">600</span></a>        <span class="k">if</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">:</span>
</span><span id="eagly-601"><a href="#eagly-601"><span class="linenos">601</span></a>            <span class="n">ly</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span> <span class="o">=</span> <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span>
</span><span id="eagly-602"><a href="#eagly-602"><span class="linenos">602</span></a>                <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="eagly-603"><a href="#eagly-603"><span class="linenos">603</span></a>                <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_external_asyncio_task</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">current_task</span><span class="p">(</span><span class="n">loop</span><span class="o">=</span><span class="n">asyncio_loop</span><span class="p">),</span> <span class="n">default_priority</span><span class="p">))</span>
</span><span id="eagly-604"><a href="#eagly-604"><span class="linenos">604</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="eagly-605"><a href="#eagly-605"><span class="linenos">605</span></a>            <span class="n">ly</span><span class="p">:</span> <span class="n">LoopYieldManagedAsyncExternal</span> <span class="o">=</span> <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span>
</span><span id="eagly-606"><a href="#eagly-606"><span class="linenos">606</span></a>                <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="eagly-607"><a href="#eagly-607"><span class="linenos">607</span></a>                <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_external</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">))</span>
</span><span id="eagly-608"><a href="#eagly-608"><span class="linenos">608</span></a>
</span><span id="eagly-609"><a href="#eagly-609"><span class="linenos">609</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="eagly-610"><a href="#eagly-610"><span class="linenos">610</span></a>            <span class="k">await</span> <span class="n">yield_</span><span class="p">(</span><span class="n">ly</span><span class="p">)</span>
</span><span id="eagly-611"><a href="#eagly-611"><span class="linenos">611</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="eagly-612"><a href="#eagly-612"><span class="linenos">612</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">:</span>
</span><span id="eagly-613"><a href="#eagly-613"><span class="linenos">613</span></a>                <span class="k">await</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">LoopYieldPriorityScheduler</span><span class="p">,</span>
</span><span id="eagly-614"><a href="#eagly-614"><span class="linenos">614</span></a>                                    <span class="n">LoopYieldPrioritySchedulerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">del_external</span><span class="p">(</span><span class="n">ly</span><span class="p">))</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>