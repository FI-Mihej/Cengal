---
title: await_coro
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_tools<wbr>.await_coro<wbr>.versions<wbr>.v_0<wbr>.await_coro    </h1>

                
                        <input id="mod-await_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-await_coro-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;await_coro_fast&#39;</span><span class="p">,</span> <span class="s1">&#39;await_coro&#39;</span><span class="p">,</span> <span class="s1">&#39;await_coro_prim&#39;</span><span class="p">,</span> <span class="s1">&#39;asyncio_coro&#39;</span><span class="p">,</span> <span class="s1">&#39;await_task_fast&#39;</span><span class="p">,</span> <span class="s1">&#39;await_task&#39;</span><span class="p">,</span> <span class="s1">&#39;await_task_prim&#39;</span><span class="p">,</span> 
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a>           <span class="s1">&#39;cs_awaitable&#39;</span><span class="p">,</span> 
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>           <span class="s1">&#39;RunSchedulerInAsyncioLoop&#39;</span><span class="p">,</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>           <span class="s1">&#39;coro_interfaces_arg_manager&#39;</span><span class="p">,</span> <span class="s1">&#39;create_task&#39;</span><span class="p">,</span> <span class="s1">&#39;create_task_in_thread_pool&#39;</span><span class="p">,</span> <span class="s1">&#39;task_in_thread_pool&#39;</span><span class="p">]</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">inspect</span> <span class="kn">import</span> <span class="n">signature</span><span class="p">,</span> <span class="n">Signature</span><span class="p">,</span> <span class="n">Parameter</span><span class="p">,</span> <span class="n">isawaitable</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="c1"># from cengal.parallel_execution.coroutines.coro_standard_services import *</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.args_manager</span> <span class="kn">import</span> <span class="n">ArgsManager</span><span class="p">,</span> <span class="n">EArgs</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partial</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Coroutine</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.sleep_tools</span> <span class="kn">import</span> <span class="n">get_min_sleep_interval</span><span class="p">,</span> <span class="n">try_sleep</span><span class="p">,</span> <span class="n">get_usable_min_sleep_interval</span><span class="p">,</span> <span class="n">get_countable_delta_time</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span><span class="p">,</span> <span class="n">get_exception_tripple</span><span class="p">,</span> <span class="n">is_async</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.put_coro</span> <span class="kn">import</span> <span class="n">PutCoro</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">wraps</span><span class="p">,</span> <span class="n">update_wrapper</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="sd">Module Docstring</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="k">def</span> <span class="nf">_async_coro_wrapper</span><span class="p">(</span><span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">future</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="n">coro_worker_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ wrapper =&gt; </span><span class="si">{</span><span class="n">func_info</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="n">coro_worker_result</span> <span class="o">=</span> <span class="n">coro_worker</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="k">except</span><span class="p">:</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>        <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ wrapper (Exception) &lt;= </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">():</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>            <span class="n">ex_type</span><span class="p">,</span> <span class="n">ex_value</span><span class="p">,</span> <span class="n">ex_traceback</span> <span class="o">=</span> <span class="n">get_exception_tripple</span><span class="p">()</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>            <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="n">ex_type</span><span class="p">,</span> <span class="n">ex_value</span><span class="p">,</span> <span class="n">ex_traceback</span><span class="p">)</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>            <span class="n">ex_value</span> <span class="o">=</span> <span class="n">ex_value</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">ex_traceback</span><span class="p">)</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>            <span class="n">future</span><span class="o">.</span><span class="n">set_exception</span><span class="p">(</span><span class="n">ex_value</span><span class="p">)</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>        <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ wrapper &lt;= </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">():</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>            <span class="n">future</span><span class="o">.</span><span class="n">set_result</span><span class="p">(</span><span class="n">coro_worker_result</span><span class="p">)</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">_awaitable_async_coro_wrapper</span><span class="p">(</span><span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">future</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="n">coro_worker_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;aλ wrapper =&gt; </span><span class="si">{</span><span class="n">func_info</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>        
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="c1"># # TODO: fix required!</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="c1"># coro_worker_result = await interface(RunCoro, CoroType.awaitable, coro_worker, *args, **kwargs)</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>        <span class="c1"># TODO: possible fix:</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="n">coro_worker_result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">coro_worker</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    <span class="k">except</span><span class="p">:</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;aλ wrapper (Exception) &lt;= </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">():</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>            <span class="n">ex_type</span><span class="p">,</span> <span class="n">ex_value</span><span class="p">,</span> <span class="n">ex_traceback</span> <span class="o">=</span> <span class="n">get_exception_tripple</span><span class="p">()</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>            <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="n">ex_type</span><span class="p">,</span> <span class="n">ex_value</span><span class="p">,</span> <span class="n">ex_traceback</span><span class="p">)</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>            <span class="n">ex_value</span> <span class="o">=</span> <span class="n">ex_value</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">ex_traceback</span><span class="p">)</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>            <span class="n">future</span><span class="o">.</span><span class="n">set_exception</span><span class="p">(</span><span class="n">ex_value</span><span class="p">)</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;aλ wrapper &lt;= </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">():</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>            <span class="n">future</span><span class="o">.</span><span class="n">set_result</span><span class="p">(</span><span class="n">coro_worker_result</span><span class="p">)</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="k">def</span> <span class="nf">await_coro_fast</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>                    <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">coro_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroType</span><span class="p">],</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>                    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="n">coro_type</span> <span class="o">=</span> <span class="n">coro_type</span> <span class="ow">or</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">auto</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="k">if</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">auto</span> <span class="o">==</span> <span class="n">coro_type</span><span class="p">:</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="n">coro_type</span> <span class="o">=</span> <span class="n">find_coro_type</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="n">future</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>    <span class="k">if</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">awaitable</span> <span class="o">==</span> <span class="n">coro_type</span><span class="p">:</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="n">put_request_to_service_with_context</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="n">scheduler</span><span class="p">),</span> <span class="n">PutCoro</span><span class="p">,</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">coro_type</span><span class="p">,</span> <span class="n">_awaitable_async_coro_wrapper</span><span class="p">),</span> <span class="n">future</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">elif</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">greenlet</span> <span class="o">==</span> <span class="n">coro_type</span><span class="p">:</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="n">put_request_to_service_with_context</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="n">scheduler</span><span class="p">),</span> <span class="n">PutCoro</span><span class="p">,</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">coro_type</span><span class="p">,</span> <span class="n">_async_coro_wrapper</span><span class="p">),</span> <span class="n">future</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="k">return</span> <span class="n">future</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a><span class="k">def</span> <span class="nf">await_coro</span><span class="p">(</span><span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>    <span class="k">return</span> <span class="n">await_coro_fast</span><span class="p">(</span><span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">(),</span> <span class="n">scheduler</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="k">def</span> <span class="nf">await_coro_prim</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Tries to use primary coro scheduler (must be set before usage)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a><span class="sd">    Args:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="sd">        coro_worker (Worker): _description_</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="sd">    Returns:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="sd">        asyncio.Future: _description_</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    <span class="k">return</span> <span class="n">await_coro_fast</span><span class="p">(</span><span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">(),</span> <span class="n">available_coro_scheduler</span><span class="p">(),</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">auto</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="k">def</span> <span class="nf">asyncio_coro</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Coroutine</span><span class="p">:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Decorator. Without arguments. Gives an ability to await any decorated Cengal coroutine from the async code</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a><span class="sd">    Args:</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="sd">        coro_worker (Worker): _description_</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a><span class="sd">    Returns:</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a><span class="sd">        Coroutine: _description_</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">await_coro_prim</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="n">coro_worker_sign</span><span class="p">:</span> <span class="n">Signature</span> <span class="o">=</span> <span class="n">signature</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    <span class="n">wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">())[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="k">return</span> <span class="n">wrapper</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a><span class="k">def</span> <span class="nf">_async_task_runner_coro_worker</span><span class="p">(</span><span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>    <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ wrapper &lt;_async_task_runner_coro_worker&gt; =&gt; interface(</span><span class="si">{</span><span class="n">service_type</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="n">args</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="n">kwargs</span><span class="si">}</span><span class="s1">)&#39;</span><span class="p">)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">interface</span><span class="p">(</span><span class="n">service_type</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;λ wrapper &lt;_async_task_runner_coro_worker&gt; &lt;= interface(</span><span class="si">{</span><span class="n">service_type</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="n">args</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="n">kwargs</span><span class="si">}</span><span class="s1">): </span><span class="si">{</span><span class="n">result</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a><span class="k">def</span> <span class="nf">await_task_fast</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>                    <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>                    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>    <span class="n">future</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    <span class="n">put_request_to_service_with_context</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="n">scheduler</span><span class="p">),</span> <span class="n">PutCoro</span><span class="p">,</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">CoroType</span><span class="o">.</span><span class="n">greenlet</span><span class="p">,</span> <span class="n">_async_coro_wrapper</span><span class="p">),</span> <span class="n">future</span><span class="p">,</span> <span class="n">_async_task_runner_coro_worker</span><span class="p">,</span> <span class="n">service_type</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="k">return</span> <span class="n">future</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a><span class="k">def</span> <span class="nf">await_task</span><span class="p">(</span><span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>    <span class="k">return</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">(),</span> <span class="n">scheduler</span><span class="p">,</span> <span class="n">service_type</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a><span class="k">def</span> <span class="nf">await_task_prim</span><span class="p">(</span><span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Tries to use primary coro scheduler (must be set before usage)</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="sd">    Args:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="sd">        service_type (ServiceType): _description_</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="sd">    Returns:</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="sd">        asyncio.Future: _description_</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>    <span class="k">return</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">(),</span> <span class="n">available_coro_scheduler</span><span class="p">(),</span> <span class="n">service_type</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a><span class="k">def</span> <span class="nf">cs_awaitable</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Decorator. Without arguments. Makes any Cengal coro awaitable from the async code (like coroutines in asyncio)</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a><span class="sd">    Example:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_scheduler import cs_acoro</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="sd">        import asyncio</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a><span class="sd">        @cs_awaitable</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="sd">        def my_coro_g(a: str, b: str) -&gt; str:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a><span class="sd">            i(Sleep, 0.1)</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="sd">            return a + b</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a><span class="sd">        @cs_awaitable</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a><span class="sd">        async def my_coro_a(a: str, b: str) -&gt; str:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a><span class="sd">            await i(Sleep, 0.05)</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="sd">            await asyncio.sleep(0.05)</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a><span class="sd">            return a + b</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a><span class="sd">        @cs_acoro</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a><span class="sd">        async def my_coro_a_implicit(a: str, b: str) -&gt; str:</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a><span class="sd">            await i(Sleep, 0.05)</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="sd">            await asyncio.sleep(0.05)</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a><span class="sd">            return a + b</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a><span class="sd">        async def my_coro_a_explicit(i: Interface, a: str, b: str) -&gt; str:</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a><span class="sd">            await i(Sleep, 0.05)</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a><span class="sd">            await asyncio.sleep(0.05)</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a><span class="sd">            return a + b</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a><span class="sd">        </span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a><span class="sd">        async def my_coro_asyncio(a: str, b: str) -&gt; str:</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a><span class="sd">            await asyncio.sleep(0.1)</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a><span class="sd">            return a + b</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a><span class="sd">        </span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a><span class="sd">        @cs_awaitable</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a><span class="sd">        async def amain():</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a><span class="sd">            # await</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a><span class="sd">            print(await my_coro_g(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a><span class="sd">            print(await my_coro_a(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a><span class="sd">            print(await my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a><span class="sd">            print(await my_coro_a_explicit(i, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a><span class="sd">            print(await my_coro_asyncio(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a><span class="sd">            # RunCoro</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a><span class="sd">            print(await i(RunCoro, my_coro_g(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a><span class="sd">            print(await i(RunCoro, my_coro_g, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a><span class="sd">            print(await i(RunCoro, my_coro_a(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a><span class="sd">            print(await i(RunCoro, my_coro_a, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a><span class="sd">            </span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a><span class="sd">            print(await i(RunCoro, my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a><span class="sd">            print(await i(RunCoro, my_coro_a_implicit, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a><span class="sd">            </span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a><span class="sd">            print(await i(RunCoro, my_coro_a_explicit, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a><span class="sd">            </span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a><span class="sd">            print(await i(RunCoro, my_coro_asyncio(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a><span class="sd">            print(await i(RunCoro, cs_acoro(my_coro_asyncio), &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a><span class="sd">            # PutCoro</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a><span class="sd">            await i(PutCoro, my_coro_g(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a><span class="sd">            await i(PutCoro, my_coro_g, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a><span class="sd">            await i(PutCoro, my_coro_a(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a><span class="sd">            await i(PutCoro, my_coro_a, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a><span class="sd">            </span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a><span class="sd">            await i(PutCoro, my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a><span class="sd">            await i(PutCoro, my_coro_a_implicit, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a><span class="sd">            </span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a><span class="sd">            await i(PutCoro, my_coro_a_explicit, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a><span class="sd">            </span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a><span class="sd">            await i(PutCoro, my_coro_asyncio(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a><span class="sd">            await i(PutCoro, cs_acoro(my_coro_asyncio), &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a><span class="sd">        </span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a><span class="sd">        @cs_awaitable</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a><span class="sd">        def main():</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a><span class="sd">            # RunCoro</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a><span class="sd">            print(i(RunCoro, my_coro_g(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a><span class="sd">            print(i(RunCoro, my_coro_g, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a><span class="sd">            print(i(RunCoro, my_coro_a(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a><span class="sd">            print(i(RunCoro, my_coro_a, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a><span class="sd">            </span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a><span class="sd">            print(i(RunCoro, my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a><span class="sd">            print(i(RunCoro, my_coro_a_implicit, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a><span class="sd">            </span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a><span class="sd">            print(i(RunCoro, my_coro_a_explicit, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a><span class="sd">            </span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a><span class="sd">            print(i(RunCoro, my_coro_asyncio(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a><span class="sd">            print(i(RunCoro, cs_acoro(my_coro_asyncio), &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a><span class="sd">            # PutCoro</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a><span class="sd">            i(PutCoro, my_coro_g(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a><span class="sd">            i(PutCoro, my_coro_g, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a><span class="sd">            i(PutCoro, my_coro_a(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a><span class="sd">            i(PutCoro, my_coro_a, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a><span class="sd">            </span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a><span class="sd">            i(PutCoro, my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a><span class="sd">            i(PutCoro, my_coro_a_implicit, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a><span class="sd">            </span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a><span class="sd">            i(PutCoro, my_coro_a_explicit, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a><span class="sd">            </span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a><span class="sd">            i(PutCoro, my_coro_asyncio(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a><span class="sd">            i(PutCoro, cs_acoro(my_coro_asyncio), &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a><span class="sd">    Args:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a><span class="sd">        coro_worker (Worker): _description_</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a><span class="sd">    Returns:</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a><span class="sd">        Coroutine: _description_</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>    <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">):</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>        <span class="nd">@wraps</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>            <span class="k">if</span> <span class="n">isawaitable</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">):</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>                <span class="k">return</span> <span class="k">await</span> <span class="n">coro_worker</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>                <span class="k">return</span> <span class="k">await</span> <span class="n">coro_worker</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>        <span class="n">wrapper</span><span class="p">:</span> <span class="n">coro_worker</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>        <span class="k">return</span> <span class="n">wrapper</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>        <span class="nd">@wraps</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>            <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.run_coro</span> <span class="kn">import</span> <span class="n">RunCoro</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>            <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>            <span class="k">return</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>        
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="n">wrapper</span><span class="p">:</span> <span class="n">coro_worker</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="k">return</span> <span class="n">wrapper</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a><span class="k">def</span> <span class="nf">coro_interfaces_arg_manager</span><span class="p">(</span><span class="n">event_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>    <span class="n">acf</span> <span class="o">=</span> <span class="n">ArgsManager</span><span class="p">(</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="n">EArgs</span><span class="p">(</span><span class="n">event_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">auto</span><span class="p">),</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>    <span class="p">)</span><span class="o">.</span><span class="n">callable</span><span class="p">(</span><span class="n">await_coro_fast</span><span class="p">)</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>    <span class="n">atf</span> <span class="o">=</span> <span class="n">ArgsManager</span><span class="p">(</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>        <span class="n">EArgs</span><span class="p">(</span><span class="n">event_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">),</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>    <span class="p">)</span><span class="o">.</span><span class="n">callable</span><span class="p">(</span><span class="n">await_task_fast</span><span class="p">)</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>    
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>    <span class="k">return</span> <span class="n">EArgs</span><span class="p">(</span><span class="n">await_coro_fast</span><span class="o">=</span><span class="n">acf</span><span class="p">,</span> <span class="n">await_task_fast</span><span class="o">=</span><span class="n">atf</span><span class="p">)</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a><span class="k">class</span> <span class="nc">RunSchedulerInAsyncioLoop</span><span class="p">:</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">idle_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">execute_every_X_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span> <span class="o">=</span> <span class="n">scheduler</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">on_woke_up_callback</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_woke_up_callback</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="n">get_usable_min_sleep_interval</span><span class="p">()</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="o">=</span> <span class="n">get_min_sleep_interval</span><span class="p">()</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="n">get_min_sleep_interval</span><span class="p">())</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">min_sleep_interval</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">get_min_sleep_interval</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="ow">or</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">usable_idle_time</span> <span class="o">=</span> <span class="p">(</span><span class="n">get_min_sleep_interval</span><span class="p">()</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="n">get_min_sleep_interval</span><span class="p">()))</span> <span class="o">+</span> <span class="n">get_countable_delta_time</span><span class="p">()</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loop</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># type: Optional[asyncio.Handle]</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_idle_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="k">if</span> <span class="n">execute_every_X_iterations</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>            <span class="n">execute_every_X_iterations</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">execute_every_X_iterations</span> <span class="o">=</span> <span class="n">execute_every_X_iterations</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span> <span class="o">=</span> <span class="n">execute_every_X_iterations</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>    
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>    <span class="k">def</span> <span class="nf">on_woke_up_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span><span class="p">:</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cancel_handle</span><span class="p">()</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span><span class="p">:</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>            <span class="k">return</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">execute_every_X_iterations</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span><span class="p">:</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>            <span class="k">return</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        <span class="n">in_work</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">iteration</span><span class="p">()</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>        
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">in_work</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span><span class="p">:</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>            <span class="k">return</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        <span class="n">idle_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">next_event_after</span><span class="p">()</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="c1"># is_awake = self.scheduler.is_awake()</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>        <span class="n">is_idle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">is_idle</span><span class="p">()</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>        <span class="n">need_to_register</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_idle_when_possible</span><span class="p">:</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">is_idle</span><span class="p">:</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>                <span class="n">need_to_register</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>            <span class="n">need_to_register</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>        <span class="k">if</span> <span class="n">need_to_register</span><span class="p">:</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register_idle</span><span class="p">(</span><span class="n">idle_time</span><span class="p">)</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>    <span class="k">def</span> <span class="nf">ready_to_stop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="c1"># self.register_idle()</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>    <span class="k">def</span> <span class="nf">register_idle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">idle_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">usable_idle_time</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>        
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>        <span class="c1"># self.handle = self.loop.call_later(self.idle_time, self)</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">min_sleep_interval</span><span class="p">:</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>            <span class="c1"># self.handle = try_sleep(self.idle_time * (idle_time // self.idle_time), self.loop.call_later, self)</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>            <span class="c1"># # self.handle = try_sleep(0.001, self.loop.call_later, self)</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span><span class="p">))</span> <span class="o">+</span> <span class="n">get_countable_delta_time</span><span class="p">()</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="n">idle_time</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>    <span class="k">def</span> <span class="nf">cancel_handle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancel</span><span class="p">()</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancel</span><span class="p">()</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>    <span class="k">def</span> <span class="nf">stop_when_possible</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a><span class="c1"># def call_soon_future(loop: Optional[asyncio.AbstractEventLoop], awaitable_coro_obj: Awaitable):</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a><span class="c1">#     if __debug__: dlog(&#39;call_soon_future - start&#39;)</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a><span class="c1">#     loop = loop or asyncio.get_event_loop()</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a><span class="c1">#</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a><span class="c1">#     def handler():</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a><span class="c1">#         if __debug__: dlog(&#39;call_soon_future.handler - start&#39;)</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a><span class="c1">#         loop.create_task(awaitable_coro_obj)</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a><span class="c1">#         if __debug__: dlog(&#39;call_soon_future.handler - end&#39;)</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a><span class="c1">#</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a><span class="c1">#     loop.get_event_loop().call_soon(handler)</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a><span class="c1">#     if __debug__: dlog(&#39;call_soon_future - end&#39;)</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a><span class="k">def</span> <span class="nf">call_soon_future</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="n">awaitable_coro_obj</span><span class="p">:</span> <span class="n">Awaitable</span><span class="p">):</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>    <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="s1">&#39;call_soon_future - start&#39;</span><span class="p">)</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>    <span class="k">def</span> <span class="nf">handler</span><span class="p">():</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>        <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="s1">&#39;call_soon_future.handler - start&#39;</span><span class="p">)</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>        <span class="n">loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">awaitable_coro_obj</span><span class="p">)</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>        <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="s1">&#39;call_soon_future.handler - end&#39;</span><span class="p">)</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>    <span class="n">loop</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>    <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="s1">&#39;call_soon_future - end&#39;</span><span class="p">)</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a><span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="n">acoro</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span><span class="p">:</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>    <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="s1">&#39;call_soon_future - start&#39;</span><span class="p">)</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>    <span class="n">awaitable_coro_obj</span> <span class="o">=</span> <span class="n">acoro</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>    <span class="k">return</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">awaitable_coro_obj</span><span class="p">)</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a><span class="k">def</span> <span class="nf">create_task_in_thread_pool</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="n">joiner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">Any</span><span class="p">]],</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_handler</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">joiner</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>        <span class="n">worker_with_args</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">worker_with_args</span><span class="p">)</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>        <span class="k">if</span> <span class="n">joiner</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>            <span class="k">await</span> <span class="n">joiner</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>                        
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>    <span class="n">create_task</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">sync_handler</span><span class="p">,</span> <span class="n">loop</span><span class="p">,</span> <span class="n">joiner</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">task_in_thread_pool</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>    <span class="n">worker_with_args</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">worker_with_args</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="await_coro_fast">
                            <input id="await_coro_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">await_coro_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>,</span><span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="n">coro_type</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroType</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Future</span>:</span></span>

                <label class="view-source-button" for="await_coro_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#await_coro_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="await_coro_fast-98"><a href="#await_coro_fast-98"><span class="linenos"> 98</span></a><span class="k">def</span> <span class="nf">await_coro_fast</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span>
</span><span id="await_coro_fast-99"><a href="#await_coro_fast-99"><span class="linenos"> 99</span></a>                    <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">coro_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroType</span><span class="p">],</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
</span><span id="await_coro_fast-100"><a href="#await_coro_fast-100"><span class="linenos">100</span></a>                    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="await_coro_fast-101"><a href="#await_coro_fast-101"><span class="linenos">101</span></a>    <span class="n">coro_type</span> <span class="o">=</span> <span class="n">coro_type</span> <span class="ow">or</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">auto</span>
</span><span id="await_coro_fast-102"><a href="#await_coro_fast-102"><span class="linenos">102</span></a>    <span class="k">if</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">auto</span> <span class="o">==</span> <span class="n">coro_type</span><span class="p">:</span>
</span><span id="await_coro_fast-103"><a href="#await_coro_fast-103"><span class="linenos">103</span></a>        <span class="n">coro_type</span> <span class="o">=</span> <span class="n">find_coro_type</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="await_coro_fast-104"><a href="#await_coro_fast-104"><span class="linenos">104</span></a>    
</span><span id="await_coro_fast-105"><a href="#await_coro_fast-105"><span class="linenos">105</span></a>    <span class="n">future</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="await_coro_fast-106"><a href="#await_coro_fast-106"><span class="linenos">106</span></a>    <span class="k">if</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">awaitable</span> <span class="o">==</span> <span class="n">coro_type</span><span class="p">:</span>
</span><span id="await_coro_fast-107"><a href="#await_coro_fast-107"><span class="linenos">107</span></a>        <span class="n">put_request_to_service_with_context</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="n">scheduler</span><span class="p">),</span> <span class="n">PutCoro</span><span class="p">,</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">coro_type</span><span class="p">,</span> <span class="n">_awaitable_async_coro_wrapper</span><span class="p">),</span> <span class="n">future</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="await_coro_fast-108"><a href="#await_coro_fast-108"><span class="linenos">108</span></a>    <span class="k">elif</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">greenlet</span> <span class="o">==</span> <span class="n">coro_type</span><span class="p">:</span>
</span><span id="await_coro_fast-109"><a href="#await_coro_fast-109"><span class="linenos">109</span></a>        <span class="n">put_request_to_service_with_context</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="n">scheduler</span><span class="p">),</span> <span class="n">PutCoro</span><span class="p">,</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">coro_type</span><span class="p">,</span> <span class="n">_async_coro_wrapper</span><span class="p">),</span> <span class="n">future</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="await_coro_fast-110"><a href="#await_coro_fast-110"><span class="linenos">110</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="await_coro_fast-111"><a href="#await_coro_fast-111"><span class="linenos">111</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="await_coro_fast-112"><a href="#await_coro_fast-112"><span class="linenos">112</span></a>    
</span><span id="await_coro_fast-113"><a href="#await_coro_fast-113"><span class="linenos">113</span></a>    <span class="k">return</span> <span class="n">future</span>
</span></pre></div>


    

                </section>
                <section id="await_coro">
                            <input id="await_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">await_coro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Future</span>:</span></span>

                <label class="view-source-button" for="await_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#await_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="await_coro-116"><a href="#await_coro-116"><span class="linenos">116</span></a><span class="k">def</span> <span class="nf">await_coro</span><span class="p">(</span><span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="await_coro-117"><a href="#await_coro-117"><span class="linenos">117</span></a>    <span class="k">return</span> <span class="n">await_coro_fast</span><span class="p">(</span><span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">(),</span> <span class="n">scheduler</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="await_coro_prim">
                            <input id="await_coro_prim-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">await_coro_prim</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Future</span>:</span></span>

                <label class="view-source-button" for="await_coro_prim-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#await_coro_prim"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="await_coro_prim-120"><a href="#await_coro_prim-120"><span class="linenos">120</span></a><span class="k">def</span> <span class="nf">await_coro_prim</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="await_coro_prim-121"><a href="#await_coro_prim-121"><span class="linenos">121</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Tries to use primary coro scheduler (must be set before usage)</span>
</span><span id="await_coro_prim-122"><a href="#await_coro_prim-122"><span class="linenos">122</span></a>
</span><span id="await_coro_prim-123"><a href="#await_coro_prim-123"><span class="linenos">123</span></a><span class="sd">    Args:</span>
</span><span id="await_coro_prim-124"><a href="#await_coro_prim-124"><span class="linenos">124</span></a><span class="sd">        coro_worker (Worker): _description_</span>
</span><span id="await_coro_prim-125"><a href="#await_coro_prim-125"><span class="linenos">125</span></a>
</span><span id="await_coro_prim-126"><a href="#await_coro_prim-126"><span class="linenos">126</span></a><span class="sd">    Returns:</span>
</span><span id="await_coro_prim-127"><a href="#await_coro_prim-127"><span class="linenos">127</span></a><span class="sd">        asyncio.Future: _description_</span>
</span><span id="await_coro_prim-128"><a href="#await_coro_prim-128"><span class="linenos">128</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="await_coro_prim-129"><a href="#await_coro_prim-129"><span class="linenos">129</span></a>    <span class="k">return</span> <span class="n">await_coro_fast</span><span class="p">(</span><span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">(),</span> <span class="n">available_coro_scheduler</span><span class="p">(),</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">auto</span><span class="p">,</span> <span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Tries to use primary coro scheduler (must be set before usage)</p>

<p>Args:
    coro_worker (Worker): _description_</p>

<p>Returns:
    asyncio.Future: _description_</p>
</div>


                </section>
                <section id="asyncio_coro">
                            <input id="asyncio_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">asyncio_coro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">coro_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">]]]</span></span><span class="return-annotation">) -> <span class="n">Coroutine</span>:</span></span>

                <label class="view-source-button" for="asyncio_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#asyncio_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="asyncio_coro-132"><a href="#asyncio_coro-132"><span class="linenos">132</span></a><span class="k">def</span> <span class="nf">asyncio_coro</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">:</span> <span class="n">Worker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Coroutine</span><span class="p">:</span>
</span><span id="asyncio_coro-133"><a href="#asyncio_coro-133"><span class="linenos">133</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Decorator. Without arguments. Gives an ability to await any decorated Cengal coroutine from the async code</span>
</span><span id="asyncio_coro-134"><a href="#asyncio_coro-134"><span class="linenos">134</span></a>
</span><span id="asyncio_coro-135"><a href="#asyncio_coro-135"><span class="linenos">135</span></a><span class="sd">    Args:</span>
</span><span id="asyncio_coro-136"><a href="#asyncio_coro-136"><span class="linenos">136</span></a><span class="sd">        coro_worker (Worker): _description_</span>
</span><span id="asyncio_coro-137"><a href="#asyncio_coro-137"><span class="linenos">137</span></a>
</span><span id="asyncio_coro-138"><a href="#asyncio_coro-138"><span class="linenos">138</span></a><span class="sd">    Returns:</span>
</span><span id="asyncio_coro-139"><a href="#asyncio_coro-139"><span class="linenos">139</span></a><span class="sd">        Coroutine: _description_</span>
</span><span id="asyncio_coro-140"><a href="#asyncio_coro-140"><span class="linenos">140</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="asyncio_coro-141"><a href="#asyncio_coro-141"><span class="linenos">141</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="asyncio_coro-142"><a href="#asyncio_coro-142"><span class="linenos">142</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">await_coro_prim</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="asyncio_coro-143"><a href="#asyncio_coro-143"><span class="linenos">143</span></a>    
</span><span id="asyncio_coro-144"><a href="#asyncio_coro-144"><span class="linenos">144</span></a>    <span class="n">coro_worker_sign</span><span class="p">:</span> <span class="n">Signature</span> <span class="o">=</span> <span class="n">signature</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="asyncio_coro-145"><a href="#asyncio_coro-145"><span class="linenos">145</span></a>    <span class="n">wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">())[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="asyncio_coro-146"><a href="#asyncio_coro-146"><span class="linenos">146</span></a>    <span class="k">return</span> <span class="n">wrapper</span>
</span></pre></div>


            <div class="docstring"><p>Decorator. Without arguments. Gives an ability to await any decorated Cengal coroutine from the async code</p>

<p>Args:
    coro_worker (Worker): _description_</p>

<p>Returns:
    Coroutine: _description_</p>
</div>


                </section>
                <section id="await_task_fast">
                            <input id="await_task_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">await_task_fast</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span>,</span><span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="n">service_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Future</span>:</span></span>

                <label class="view-source-button" for="await_task_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#await_task_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="await_task_fast-156"><a href="#await_task_fast-156"><span class="linenos">156</span></a><span class="k">def</span> <span class="nf">await_task_fast</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span>
</span><span id="await_task_fast-157"><a href="#await_task_fast-157"><span class="linenos">157</span></a>                    <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
</span><span id="await_task_fast-158"><a href="#await_task_fast-158"><span class="linenos">158</span></a>                    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="await_task_fast-159"><a href="#await_task_fast-159"><span class="linenos">159</span></a>    <span class="n">future</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="await_task_fast-160"><a href="#await_task_fast-160"><span class="linenos">160</span></a>    <span class="n">put_request_to_service_with_context</span><span class="p">(</span><span class="n">get_interface_and_loop_with_explicit_loop</span><span class="p">(</span><span class="n">scheduler</span><span class="p">),</span> <span class="n">PutCoro</span><span class="p">,</span> <span class="n">ExplicitWorker</span><span class="p">(</span><span class="n">CoroType</span><span class="o">.</span><span class="n">greenlet</span><span class="p">,</span> <span class="n">_async_coro_wrapper</span><span class="p">),</span> <span class="n">future</span><span class="p">,</span> <span class="n">_async_task_runner_coro_worker</span><span class="p">,</span> <span class="n">service_type</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="await_task_fast-161"><a href="#await_task_fast-161"><span class="linenos">161</span></a>    <span class="k">return</span> <span class="n">future</span>
</span></pre></div>


    

                </section>
                <section id="await_task">
                            <input id="await_task-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">await_task</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="n">service_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Future</span>:</span></span>

                <label class="view-source-button" for="await_task-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#await_task"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="await_task-164"><a href="#await_task-164"><span class="linenos">164</span></a><span class="k">def</span> <span class="nf">await_task</span><span class="p">(</span><span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="await_task-165"><a href="#await_task-165"><span class="linenos">165</span></a>    <span class="k">return</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">(),</span> <span class="n">scheduler</span><span class="p">,</span> <span class="n">service_type</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="await_task_prim">
                            <input id="await_task_prim-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">await_task_prim</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">service_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Future</span>:</span></span>

                <label class="view-source-button" for="await_task_prim-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#await_task_prim"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="await_task_prim-168"><a href="#await_task_prim-168"><span class="linenos">168</span></a><span class="k">def</span> <span class="nf">await_task_prim</span><span class="p">(</span><span class="n">service_type</span><span class="p">:</span> <span class="n">ServiceType</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Future</span><span class="p">:</span>
</span><span id="await_task_prim-169"><a href="#await_task_prim-169"><span class="linenos">169</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Tries to use primary coro scheduler (must be set before usage)</span>
</span><span id="await_task_prim-170"><a href="#await_task_prim-170"><span class="linenos">170</span></a>
</span><span id="await_task_prim-171"><a href="#await_task_prim-171"><span class="linenos">171</span></a><span class="sd">    Args:</span>
</span><span id="await_task_prim-172"><a href="#await_task_prim-172"><span class="linenos">172</span></a><span class="sd">        service_type (ServiceType): _description_</span>
</span><span id="await_task_prim-173"><a href="#await_task_prim-173"><span class="linenos">173</span></a>
</span><span id="await_task_prim-174"><a href="#await_task_prim-174"><span class="linenos">174</span></a><span class="sd">    Returns:</span>
</span><span id="await_task_prim-175"><a href="#await_task_prim-175"><span class="linenos">175</span></a><span class="sd">        asyncio.Future: _description_</span>
</span><span id="await_task_prim-176"><a href="#await_task_prim-176"><span class="linenos">176</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="await_task_prim-177"><a href="#await_task_prim-177"><span class="linenos">177</span></a>    <span class="k">return</span> <span class="n">await_task_fast</span><span class="p">(</span><span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">(),</span> <span class="n">available_coro_scheduler</span><span class="p">(),</span> <span class="n">service_type</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Tries to use primary coro scheduler (must be set before usage)</p>

<p>Args:
    service_type (ServiceType): _description_</p>

<p>Returns:
    asyncio.Future: _description_</p>
</div>


                </section>
                <section id="cs_awaitable">
                            <input id="cs_awaitable-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cs_awaitable</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">coro_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="cs_awaitable-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cs_awaitable"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cs_awaitable-180"><a href="#cs_awaitable-180"><span class="linenos">180</span></a><span class="k">def</span> <span class="nf">cs_awaitable</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="cs_awaitable-181"><a href="#cs_awaitable-181"><span class="linenos">181</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Decorator. Without arguments. Makes any Cengal coro awaitable from the async code (like coroutines in asyncio)</span>
</span><span id="cs_awaitable-182"><a href="#cs_awaitable-182"><span class="linenos">182</span></a><span class="sd">    Example:</span>
</span><span id="cs_awaitable-183"><a href="#cs_awaitable-183"><span class="linenos">183</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_scheduler import cs_acoro</span>
</span><span id="cs_awaitable-184"><a href="#cs_awaitable-184"><span class="linenos">184</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro</span>
</span><span id="cs_awaitable-185"><a href="#cs_awaitable-185"><span class="linenos">185</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro</span>
</span><span id="cs_awaitable-186"><a href="#cs_awaitable-186"><span class="linenos">186</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep</span>
</span><span id="cs_awaitable-187"><a href="#cs_awaitable-187"><span class="linenos">187</span></a><span class="sd">        import asyncio</span>
</span><span id="cs_awaitable-188"><a href="#cs_awaitable-188"><span class="linenos">188</span></a>
</span><span id="cs_awaitable-189"><a href="#cs_awaitable-189"><span class="linenos">189</span></a><span class="sd">        @cs_awaitable</span>
</span><span id="cs_awaitable-190"><a href="#cs_awaitable-190"><span class="linenos">190</span></a><span class="sd">        def my_coro_g(a: str, b: str) -&gt; str:</span>
</span><span id="cs_awaitable-191"><a href="#cs_awaitable-191"><span class="linenos">191</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="cs_awaitable-192"><a href="#cs_awaitable-192"><span class="linenos">192</span></a><span class="sd">            i(Sleep, 0.1)</span>
</span><span id="cs_awaitable-193"><a href="#cs_awaitable-193"><span class="linenos">193</span></a>
</span><span id="cs_awaitable-194"><a href="#cs_awaitable-194"><span class="linenos">194</span></a><span class="sd">            return a + b</span>
</span><span id="cs_awaitable-195"><a href="#cs_awaitable-195"><span class="linenos">195</span></a>
</span><span id="cs_awaitable-196"><a href="#cs_awaitable-196"><span class="linenos">196</span></a><span class="sd">        @cs_awaitable</span>
</span><span id="cs_awaitable-197"><a href="#cs_awaitable-197"><span class="linenos">197</span></a><span class="sd">        async def my_coro_a(a: str, b: str) -&gt; str:</span>
</span><span id="cs_awaitable-198"><a href="#cs_awaitable-198"><span class="linenos">198</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="cs_awaitable-199"><a href="#cs_awaitable-199"><span class="linenos">199</span></a><span class="sd">            await i(Sleep, 0.05)</span>
</span><span id="cs_awaitable-200"><a href="#cs_awaitable-200"><span class="linenos">200</span></a>
</span><span id="cs_awaitable-201"><a href="#cs_awaitable-201"><span class="linenos">201</span></a><span class="sd">            await asyncio.sleep(0.05)</span>
</span><span id="cs_awaitable-202"><a href="#cs_awaitable-202"><span class="linenos">202</span></a>
</span><span id="cs_awaitable-203"><a href="#cs_awaitable-203"><span class="linenos">203</span></a><span class="sd">            return a + b</span>
</span><span id="cs_awaitable-204"><a href="#cs_awaitable-204"><span class="linenos">204</span></a>
</span><span id="cs_awaitable-205"><a href="#cs_awaitable-205"><span class="linenos">205</span></a><span class="sd">        @cs_acoro</span>
</span><span id="cs_awaitable-206"><a href="#cs_awaitable-206"><span class="linenos">206</span></a><span class="sd">        async def my_coro_a_implicit(a: str, b: str) -&gt; str:</span>
</span><span id="cs_awaitable-207"><a href="#cs_awaitable-207"><span class="linenos">207</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="cs_awaitable-208"><a href="#cs_awaitable-208"><span class="linenos">208</span></a><span class="sd">            await i(Sleep, 0.05)</span>
</span><span id="cs_awaitable-209"><a href="#cs_awaitable-209"><span class="linenos">209</span></a>
</span><span id="cs_awaitable-210"><a href="#cs_awaitable-210"><span class="linenos">210</span></a><span class="sd">            await asyncio.sleep(0.05)</span>
</span><span id="cs_awaitable-211"><a href="#cs_awaitable-211"><span class="linenos">211</span></a>
</span><span id="cs_awaitable-212"><a href="#cs_awaitable-212"><span class="linenos">212</span></a><span class="sd">            return a + b</span>
</span><span id="cs_awaitable-213"><a href="#cs_awaitable-213"><span class="linenos">213</span></a>
</span><span id="cs_awaitable-214"><a href="#cs_awaitable-214"><span class="linenos">214</span></a><span class="sd">        async def my_coro_a_explicit(i: Interface, a: str, b: str) -&gt; str:</span>
</span><span id="cs_awaitable-215"><a href="#cs_awaitable-215"><span class="linenos">215</span></a><span class="sd">            await i(Sleep, 0.05)</span>
</span><span id="cs_awaitable-216"><a href="#cs_awaitable-216"><span class="linenos">216</span></a>
</span><span id="cs_awaitable-217"><a href="#cs_awaitable-217"><span class="linenos">217</span></a><span class="sd">            await asyncio.sleep(0.05)</span>
</span><span id="cs_awaitable-218"><a href="#cs_awaitable-218"><span class="linenos">218</span></a>
</span><span id="cs_awaitable-219"><a href="#cs_awaitable-219"><span class="linenos">219</span></a><span class="sd">            return a + b</span>
</span><span id="cs_awaitable-220"><a href="#cs_awaitable-220"><span class="linenos">220</span></a><span class="sd">        </span>
</span><span id="cs_awaitable-221"><a href="#cs_awaitable-221"><span class="linenos">221</span></a><span class="sd">        async def my_coro_asyncio(a: str, b: str) -&gt; str:</span>
</span><span id="cs_awaitable-222"><a href="#cs_awaitable-222"><span class="linenos">222</span></a><span class="sd">            await asyncio.sleep(0.1)</span>
</span><span id="cs_awaitable-223"><a href="#cs_awaitable-223"><span class="linenos">223</span></a>
</span><span id="cs_awaitable-224"><a href="#cs_awaitable-224"><span class="linenos">224</span></a><span class="sd">            return a + b</span>
</span><span id="cs_awaitable-225"><a href="#cs_awaitable-225"><span class="linenos">225</span></a><span class="sd">        </span>
</span><span id="cs_awaitable-226"><a href="#cs_awaitable-226"><span class="linenos">226</span></a><span class="sd">        @cs_awaitable</span>
</span><span id="cs_awaitable-227"><a href="#cs_awaitable-227"><span class="linenos">227</span></a><span class="sd">        async def amain():</span>
</span><span id="cs_awaitable-228"><a href="#cs_awaitable-228"><span class="linenos">228</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="cs_awaitable-229"><a href="#cs_awaitable-229"><span class="linenos">229</span></a>
</span><span id="cs_awaitable-230"><a href="#cs_awaitable-230"><span class="linenos">230</span></a><span class="sd">            # await</span>
</span><span id="cs_awaitable-231"><a href="#cs_awaitable-231"><span class="linenos">231</span></a>
</span><span id="cs_awaitable-232"><a href="#cs_awaitable-232"><span class="linenos">232</span></a><span class="sd">            print(await my_coro_g(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-233"><a href="#cs_awaitable-233"><span class="linenos">233</span></a><span class="sd">            print(await my_coro_a(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-234"><a href="#cs_awaitable-234"><span class="linenos">234</span></a><span class="sd">            print(await my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-235"><a href="#cs_awaitable-235"><span class="linenos">235</span></a><span class="sd">            print(await my_coro_a_explicit(i, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-236"><a href="#cs_awaitable-236"><span class="linenos">236</span></a><span class="sd">            print(await my_coro_asyncio(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-237"><a href="#cs_awaitable-237"><span class="linenos">237</span></a>
</span><span id="cs_awaitable-238"><a href="#cs_awaitable-238"><span class="linenos">238</span></a><span class="sd">            # RunCoro</span>
</span><span id="cs_awaitable-239"><a href="#cs_awaitable-239"><span class="linenos">239</span></a>
</span><span id="cs_awaitable-240"><a href="#cs_awaitable-240"><span class="linenos">240</span></a><span class="sd">            print(await i(RunCoro, my_coro_g(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="cs_awaitable-241"><a href="#cs_awaitable-241"><span class="linenos">241</span></a><span class="sd">            print(await i(RunCoro, my_coro_g, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-242"><a href="#cs_awaitable-242"><span class="linenos">242</span></a>
</span><span id="cs_awaitable-243"><a href="#cs_awaitable-243"><span class="linenos">243</span></a><span class="sd">            print(await i(RunCoro, my_coro_a(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="cs_awaitable-244"><a href="#cs_awaitable-244"><span class="linenos">244</span></a><span class="sd">            print(await i(RunCoro, my_coro_a, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-245"><a href="#cs_awaitable-245"><span class="linenos">245</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-246"><a href="#cs_awaitable-246"><span class="linenos">246</span></a><span class="sd">            print(await i(RunCoro, my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="cs_awaitable-247"><a href="#cs_awaitable-247"><span class="linenos">247</span></a><span class="sd">            print(await i(RunCoro, my_coro_a_implicit, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-248"><a href="#cs_awaitable-248"><span class="linenos">248</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-249"><a href="#cs_awaitable-249"><span class="linenos">249</span></a><span class="sd">            print(await i(RunCoro, my_coro_a_explicit, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-250"><a href="#cs_awaitable-250"><span class="linenos">250</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-251"><a href="#cs_awaitable-251"><span class="linenos">251</span></a><span class="sd">            print(await i(RunCoro, my_coro_asyncio(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="cs_awaitable-252"><a href="#cs_awaitable-252"><span class="linenos">252</span></a><span class="sd">            print(await i(RunCoro, cs_acoro(my_coro_asyncio), &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-253"><a href="#cs_awaitable-253"><span class="linenos">253</span></a>
</span><span id="cs_awaitable-254"><a href="#cs_awaitable-254"><span class="linenos">254</span></a><span class="sd">            # PutCoro</span>
</span><span id="cs_awaitable-255"><a href="#cs_awaitable-255"><span class="linenos">255</span></a>
</span><span id="cs_awaitable-256"><a href="#cs_awaitable-256"><span class="linenos">256</span></a><span class="sd">            await i(PutCoro, my_coro_g(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-257"><a href="#cs_awaitable-257"><span class="linenos">257</span></a><span class="sd">            await i(PutCoro, my_coro_g, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-258"><a href="#cs_awaitable-258"><span class="linenos">258</span></a>
</span><span id="cs_awaitable-259"><a href="#cs_awaitable-259"><span class="linenos">259</span></a><span class="sd">            await i(PutCoro, my_coro_a(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-260"><a href="#cs_awaitable-260"><span class="linenos">260</span></a><span class="sd">            await i(PutCoro, my_coro_a, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-261"><a href="#cs_awaitable-261"><span class="linenos">261</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-262"><a href="#cs_awaitable-262"><span class="linenos">262</span></a><span class="sd">            await i(PutCoro, my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-263"><a href="#cs_awaitable-263"><span class="linenos">263</span></a><span class="sd">            await i(PutCoro, my_coro_a_implicit, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-264"><a href="#cs_awaitable-264"><span class="linenos">264</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-265"><a href="#cs_awaitable-265"><span class="linenos">265</span></a><span class="sd">            await i(PutCoro, my_coro_a_explicit, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-266"><a href="#cs_awaitable-266"><span class="linenos">266</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-267"><a href="#cs_awaitable-267"><span class="linenos">267</span></a><span class="sd">            await i(PutCoro, my_coro_asyncio(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-268"><a href="#cs_awaitable-268"><span class="linenos">268</span></a><span class="sd">            await i(PutCoro, cs_acoro(my_coro_asyncio), &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-269"><a href="#cs_awaitable-269"><span class="linenos">269</span></a><span class="sd">        </span>
</span><span id="cs_awaitable-270"><a href="#cs_awaitable-270"><span class="linenos">270</span></a><span class="sd">        @cs_awaitable</span>
</span><span id="cs_awaitable-271"><a href="#cs_awaitable-271"><span class="linenos">271</span></a><span class="sd">        def main():</span>
</span><span id="cs_awaitable-272"><a href="#cs_awaitable-272"><span class="linenos">272</span></a><span class="sd">            i: Interface = current_interface()</span>
</span><span id="cs_awaitable-273"><a href="#cs_awaitable-273"><span class="linenos">273</span></a>
</span><span id="cs_awaitable-274"><a href="#cs_awaitable-274"><span class="linenos">274</span></a><span class="sd">            # RunCoro</span>
</span><span id="cs_awaitable-275"><a href="#cs_awaitable-275"><span class="linenos">275</span></a>
</span><span id="cs_awaitable-276"><a href="#cs_awaitable-276"><span class="linenos">276</span></a><span class="sd">            print(i(RunCoro, my_coro_g(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="cs_awaitable-277"><a href="#cs_awaitable-277"><span class="linenos">277</span></a><span class="sd">            print(i(RunCoro, my_coro_g, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-278"><a href="#cs_awaitable-278"><span class="linenos">278</span></a>
</span><span id="cs_awaitable-279"><a href="#cs_awaitable-279"><span class="linenos">279</span></a><span class="sd">            print(i(RunCoro, my_coro_a(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="cs_awaitable-280"><a href="#cs_awaitable-280"><span class="linenos">280</span></a><span class="sd">            print(i(RunCoro, my_coro_a, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-281"><a href="#cs_awaitable-281"><span class="linenos">281</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-282"><a href="#cs_awaitable-282"><span class="linenos">282</span></a><span class="sd">            print(i(RunCoro, my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="cs_awaitable-283"><a href="#cs_awaitable-283"><span class="linenos">283</span></a><span class="sd">            print(i(RunCoro, my_coro_a_implicit, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-284"><a href="#cs_awaitable-284"><span class="linenos">284</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-285"><a href="#cs_awaitable-285"><span class="linenos">285</span></a><span class="sd">            print(i(RunCoro, my_coro_a_explicit, &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-286"><a href="#cs_awaitable-286"><span class="linenos">286</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-287"><a href="#cs_awaitable-287"><span class="linenos">287</span></a><span class="sd">            print(i(RunCoro, my_coro_asyncio(&#39;a&#39;, &#39;b&#39;)))</span>
</span><span id="cs_awaitable-288"><a href="#cs_awaitable-288"><span class="linenos">288</span></a><span class="sd">            print(i(RunCoro, cs_acoro(my_coro_asyncio), &#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-289"><a href="#cs_awaitable-289"><span class="linenos">289</span></a>
</span><span id="cs_awaitable-290"><a href="#cs_awaitable-290"><span class="linenos">290</span></a><span class="sd">            # PutCoro</span>
</span><span id="cs_awaitable-291"><a href="#cs_awaitable-291"><span class="linenos">291</span></a>
</span><span id="cs_awaitable-292"><a href="#cs_awaitable-292"><span class="linenos">292</span></a><span class="sd">            i(PutCoro, my_coro_g(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-293"><a href="#cs_awaitable-293"><span class="linenos">293</span></a><span class="sd">            i(PutCoro, my_coro_g, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-294"><a href="#cs_awaitable-294"><span class="linenos">294</span></a>
</span><span id="cs_awaitable-295"><a href="#cs_awaitable-295"><span class="linenos">295</span></a><span class="sd">            i(PutCoro, my_coro_a(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-296"><a href="#cs_awaitable-296"><span class="linenos">296</span></a><span class="sd">            i(PutCoro, my_coro_a, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-297"><a href="#cs_awaitable-297"><span class="linenos">297</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-298"><a href="#cs_awaitable-298"><span class="linenos">298</span></a><span class="sd">            i(PutCoro, my_coro_a_implicit(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-299"><a href="#cs_awaitable-299"><span class="linenos">299</span></a><span class="sd">            i(PutCoro, my_coro_a_implicit, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-300"><a href="#cs_awaitable-300"><span class="linenos">300</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-301"><a href="#cs_awaitable-301"><span class="linenos">301</span></a><span class="sd">            i(PutCoro, my_coro_a_explicit, &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-302"><a href="#cs_awaitable-302"><span class="linenos">302</span></a><span class="sd">            </span>
</span><span id="cs_awaitable-303"><a href="#cs_awaitable-303"><span class="linenos">303</span></a><span class="sd">            i(PutCoro, my_coro_asyncio(&#39;a&#39;, &#39;b&#39;))</span>
</span><span id="cs_awaitable-304"><a href="#cs_awaitable-304"><span class="linenos">304</span></a><span class="sd">            i(PutCoro, cs_acoro(my_coro_asyncio), &#39;a&#39;, &#39;b&#39;)</span>
</span><span id="cs_awaitable-305"><a href="#cs_awaitable-305"><span class="linenos">305</span></a>
</span><span id="cs_awaitable-306"><a href="#cs_awaitable-306"><span class="linenos">306</span></a><span class="sd">    Args:</span>
</span><span id="cs_awaitable-307"><a href="#cs_awaitable-307"><span class="linenos">307</span></a><span class="sd">        coro_worker (Worker): _description_</span>
</span><span id="cs_awaitable-308"><a href="#cs_awaitable-308"><span class="linenos">308</span></a>
</span><span id="cs_awaitable-309"><a href="#cs_awaitable-309"><span class="linenos">309</span></a><span class="sd">    Returns:</span>
</span><span id="cs_awaitable-310"><a href="#cs_awaitable-310"><span class="linenos">310</span></a><span class="sd">        Coroutine: _description_</span>
</span><span id="cs_awaitable-311"><a href="#cs_awaitable-311"><span class="linenos">311</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="cs_awaitable-312"><a href="#cs_awaitable-312"><span class="linenos">312</span></a>    <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">):</span>
</span><span id="cs_awaitable-313"><a href="#cs_awaitable-313"><span class="linenos">313</span></a>        <span class="nd">@wraps</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="cs_awaitable-314"><a href="#cs_awaitable-314"><span class="linenos">314</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cs_awaitable-315"><a href="#cs_awaitable-315"><span class="linenos">315</span></a>            <span class="k">if</span> <span class="n">isawaitable</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">):</span>
</span><span id="cs_awaitable-316"><a href="#cs_awaitable-316"><span class="linenos">316</span></a>                <span class="k">return</span> <span class="k">await</span> <span class="n">coro_worker</span>
</span><span id="cs_awaitable-317"><a href="#cs_awaitable-317"><span class="linenos">317</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="cs_awaitable-318"><a href="#cs_awaitable-318"><span class="linenos">318</span></a>                <span class="k">return</span> <span class="k">await</span> <span class="n">coro_worker</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="cs_awaitable-319"><a href="#cs_awaitable-319"><span class="linenos">319</span></a>        
</span><span id="cs_awaitable-320"><a href="#cs_awaitable-320"><span class="linenos">320</span></a>        <span class="n">wrapper</span><span class="p">:</span> <span class="n">coro_worker</span>
</span><span id="cs_awaitable-321"><a href="#cs_awaitable-321"><span class="linenos">321</span></a>        <span class="k">return</span> <span class="n">wrapper</span>
</span><span id="cs_awaitable-322"><a href="#cs_awaitable-322"><span class="linenos">322</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="cs_awaitable-323"><a href="#cs_awaitable-323"><span class="linenos">323</span></a>        <span class="nd">@wraps</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">)</span>
</span><span id="cs_awaitable-324"><a href="#cs_awaitable-324"><span class="linenos">324</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cs_awaitable-325"><a href="#cs_awaitable-325"><span class="linenos">325</span></a>            <span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.run_coro</span> <span class="kn">import</span> <span class="n">RunCoro</span>
</span><span id="cs_awaitable-326"><a href="#cs_awaitable-326"><span class="linenos">326</span></a>            <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="cs_awaitable-327"><a href="#cs_awaitable-327"><span class="linenos">327</span></a>            <span class="k">return</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">coro_worker</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="cs_awaitable-328"><a href="#cs_awaitable-328"><span class="linenos">328</span></a>        
</span><span id="cs_awaitable-329"><a href="#cs_awaitable-329"><span class="linenos">329</span></a>        <span class="n">wrapper</span><span class="p">:</span> <span class="n">coro_worker</span>
</span><span id="cs_awaitable-330"><a href="#cs_awaitable-330"><span class="linenos">330</span></a>        <span class="k">return</span> <span class="n">wrapper</span>
</span></pre></div>


            <div class="docstring"><p>Decorator. Without arguments. Makes any Cengal coro awaitable from the async code (like coroutines in asyncio)
Example:
    from cengal.parallel_execution.coroutines.coro_scheduler import cs_acoro
    from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
    from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
    from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
    import asyncio</p>

<pre><code>@cs_awaitable
def my_coro_g(a: str, b: str) -&gt; str:
    i: Interface = current_interface()
    i(Sleep, 0.1)

    return a + b

@cs_awaitable
async def my_coro_a(a: str, b: str) -&gt; str:
    i: Interface = current_interface()
    await i(Sleep, 0.05)

    await asyncio.sleep(0.05)

    return a + b

@cs_acoro
async def my_coro_a_implicit(a: str, b: str) -&gt; str:
    i: Interface = current_interface()
    await i(Sleep, 0.05)

    await asyncio.sleep(0.05)

    return a + b

async def my_coro_a_explicit(i: Interface, a: str, b: str) -&gt; str:
    await i(Sleep, 0.05)

    await asyncio.sleep(0.05)

    return a + b

async def my_coro_asyncio(a: str, b: str) -&gt; str:
    await asyncio.sleep(0.1)

    return a + b

@cs_awaitable
async def amain():
    i: Interface = current_interface()

    # await

    print(await my_coro_g('a', 'b'))
    print(await my_coro_a('a', 'b'))
    print(await my_coro_a_implicit('a', 'b'))
    print(await my_coro_a_explicit(i, 'a', 'b'))
    print(await my_coro_asyncio('a', 'b'))

    # RunCoro

    print(await i(RunCoro, my_coro_g('a', 'b')))
    print(await i(RunCoro, my_coro_g, 'a', 'b'))

    print(await i(RunCoro, my_coro_a('a', 'b')))
    print(await i(RunCoro, my_coro_a, 'a', 'b'))

    print(await i(RunCoro, my_coro_a_implicit('a', 'b')))
    print(await i(RunCoro, my_coro_a_implicit, 'a', 'b'))

    print(await i(RunCoro, my_coro_a_explicit, 'a', 'b'))

    print(await i(RunCoro, my_coro_asyncio('a', 'b')))
    print(await i(RunCoro, cs_acoro(my_coro_asyncio), 'a', 'b'))

    # PutCoro

    await i(PutCoro, my_coro_g('a', 'b'))
    await i(PutCoro, my_coro_g, 'a', 'b')

    await i(PutCoro, my_coro_a('a', 'b'))
    await i(PutCoro, my_coro_a, 'a', 'b')

    await i(PutCoro, my_coro_a_implicit('a', 'b'))
    await i(PutCoro, my_coro_a_implicit, 'a', 'b')

    await i(PutCoro, my_coro_a_explicit, 'a', 'b')

    await i(PutCoro, my_coro_asyncio('a', 'b'))
    await i(PutCoro, cs_acoro(my_coro_asyncio), 'a', 'b')

@cs_awaitable
def main():
    i: Interface = current_interface()

    # RunCoro

    print(i(RunCoro, my_coro_g('a', 'b')))
    print(i(RunCoro, my_coro_g, 'a', 'b'))

    print(i(RunCoro, my_coro_a('a', 'b')))
    print(i(RunCoro, my_coro_a, 'a', 'b'))

    print(i(RunCoro, my_coro_a_implicit('a', 'b')))
    print(i(RunCoro, my_coro_a_implicit, 'a', 'b'))

    print(i(RunCoro, my_coro_a_explicit, 'a', 'b'))

    print(i(RunCoro, my_coro_asyncio('a', 'b')))
    print(i(RunCoro, cs_acoro(my_coro_asyncio), 'a', 'b'))

    # PutCoro

    i(PutCoro, my_coro_g('a', 'b'))
    i(PutCoro, my_coro_g, 'a', 'b')

    i(PutCoro, my_coro_a('a', 'b'))
    i(PutCoro, my_coro_a, 'a', 'b')

    i(PutCoro, my_coro_a_implicit('a', 'b'))
    i(PutCoro, my_coro_a_implicit, 'a', 'b')

    i(PutCoro, my_coro_a_explicit, 'a', 'b')

    i(PutCoro, my_coro_asyncio('a', 'b'))
    i(PutCoro, cs_acoro(my_coro_asyncio), 'a', 'b')
</code></pre>

<p>Args:
    coro_worker (Worker): _description_</p>

<p>Returns:
    Coroutine: _description_</p>
</div>


                </section>
                <section id="RunSchedulerInAsyncioLoop">
                            <input id="RunSchedulerInAsyncioLoop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">RunSchedulerInAsyncioLoop</span>:

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop-344"><a href="#RunSchedulerInAsyncioLoop-344"><span class="linenos">344</span></a><span class="k">class</span> <span class="nc">RunSchedulerInAsyncioLoop</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-345"><a href="#RunSchedulerInAsyncioLoop-345"><span class="linenos">345</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">idle_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">execute_every_X_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop-346"><a href="#RunSchedulerInAsyncioLoop-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span> <span class="o">=</span> <span class="n">scheduler</span>
</span><span id="RunSchedulerInAsyncioLoop-347"><a href="#RunSchedulerInAsyncioLoop-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">on_woke_up_callback</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_woke_up_callback</span>
</span><span id="RunSchedulerInAsyncioLoop-348"><a href="#RunSchedulerInAsyncioLoop-348"><span class="linenos">348</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-349"><a href="#RunSchedulerInAsyncioLoop-349"><span class="linenos">349</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="n">get_usable_min_sleep_interval</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-350"><a href="#RunSchedulerInAsyncioLoop-350"><span class="linenos">350</span></a>        
</span><span id="RunSchedulerInAsyncioLoop-351"><a href="#RunSchedulerInAsyncioLoop-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="o">=</span> <span class="n">get_min_sleep_interval</span><span class="p">()</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="n">get_min_sleep_interval</span><span class="p">())</span>
</span><span id="RunSchedulerInAsyncioLoop-352"><a href="#RunSchedulerInAsyncioLoop-352"><span class="linenos">352</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">min_sleep_interval</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">get_min_sleep_interval</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="ow">or</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="RunSchedulerInAsyncioLoop-353"><a href="#RunSchedulerInAsyncioLoop-353"><span class="linenos">353</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">usable_idle_time</span> <span class="o">=</span> <span class="p">(</span><span class="n">get_min_sleep_interval</span><span class="p">()</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="n">get_min_sleep_interval</span><span class="p">()))</span> <span class="o">+</span> <span class="n">get_countable_delta_time</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-354"><a href="#RunSchedulerInAsyncioLoop-354"><span class="linenos">354</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loop</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-355"><a href="#RunSchedulerInAsyncioLoop-355"><span class="linenos">355</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># type: Optional[asyncio.Handle]</span>
</span><span id="RunSchedulerInAsyncioLoop-356"><a href="#RunSchedulerInAsyncioLoop-356"><span class="linenos">356</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_idle_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-357"><a href="#RunSchedulerInAsyncioLoop-357"><span class="linenos">357</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-358"><a href="#RunSchedulerInAsyncioLoop-358"><span class="linenos">358</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-359"><a href="#RunSchedulerInAsyncioLoop-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-360"><a href="#RunSchedulerInAsyncioLoop-360"><span class="linenos">360</span></a>        <span class="k">if</span> <span class="n">execute_every_X_iterations</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-361"><a href="#RunSchedulerInAsyncioLoop-361"><span class="linenos">361</span></a>            <span class="n">execute_every_X_iterations</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="RunSchedulerInAsyncioLoop-362"><a href="#RunSchedulerInAsyncioLoop-362"><span class="linenos">362</span></a>        
</span><span id="RunSchedulerInAsyncioLoop-363"><a href="#RunSchedulerInAsyncioLoop-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">execute_every_X_iterations</span> <span class="o">=</span> <span class="n">execute_every_X_iterations</span>
</span><span id="RunSchedulerInAsyncioLoop-364"><a href="#RunSchedulerInAsyncioLoop-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span> <span class="o">=</span> <span class="n">execute_every_X_iterations</span>
</span><span id="RunSchedulerInAsyncioLoop-365"><a href="#RunSchedulerInAsyncioLoop-365"><span class="linenos">365</span></a>    
</span><span id="RunSchedulerInAsyncioLoop-366"><a href="#RunSchedulerInAsyncioLoop-366"><span class="linenos">366</span></a>    <span class="k">def</span> <span class="nf">on_woke_up_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop-367"><a href="#RunSchedulerInAsyncioLoop-367"><span class="linenos">367</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-368"><a href="#RunSchedulerInAsyncioLoop-368"><span class="linenos">368</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cancel_handle</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-369"><a href="#RunSchedulerInAsyncioLoop-369"><span class="linenos">369</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-370"><a href="#RunSchedulerInAsyncioLoop-370"><span class="linenos">370</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-371"><a href="#RunSchedulerInAsyncioLoop-371"><span class="linenos">371</span></a>
</span><span id="RunSchedulerInAsyncioLoop-372"><a href="#RunSchedulerInAsyncioLoop-372"><span class="linenos">372</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop-373"><a href="#RunSchedulerInAsyncioLoop-373"><span class="linenos">373</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RunSchedulerInAsyncioLoop-374"><a href="#RunSchedulerInAsyncioLoop-374"><span class="linenos">374</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-375"><a href="#RunSchedulerInAsyncioLoop-375"><span class="linenos">375</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-376"><a href="#RunSchedulerInAsyncioLoop-376"><span class="linenos">376</span></a>            <span class="k">return</span>
</span><span id="RunSchedulerInAsyncioLoop-377"><a href="#RunSchedulerInAsyncioLoop-377"><span class="linenos">377</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-378"><a href="#RunSchedulerInAsyncioLoop-378"><span class="linenos">378</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">execute_every_X_iterations</span>
</span><span id="RunSchedulerInAsyncioLoop-379"><a href="#RunSchedulerInAsyncioLoop-379"><span class="linenos">379</span></a>        
</span><span id="RunSchedulerInAsyncioLoop-380"><a href="#RunSchedulerInAsyncioLoop-380"><span class="linenos">380</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="RunSchedulerInAsyncioLoop-381"><a href="#RunSchedulerInAsyncioLoop-381"><span class="linenos">381</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-382"><a href="#RunSchedulerInAsyncioLoop-382"><span class="linenos">382</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-383"><a href="#RunSchedulerInAsyncioLoop-383"><span class="linenos">383</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-384"><a href="#RunSchedulerInAsyncioLoop-384"><span class="linenos">384</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-385"><a href="#RunSchedulerInAsyncioLoop-385"><span class="linenos">385</span></a>            <span class="k">return</span>
</span><span id="RunSchedulerInAsyncioLoop-386"><a href="#RunSchedulerInAsyncioLoop-386"><span class="linenos">386</span></a>
</span><span id="RunSchedulerInAsyncioLoop-387"><a href="#RunSchedulerInAsyncioLoop-387"><span class="linenos">387</span></a>        <span class="n">in_work</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">iteration</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-388"><a href="#RunSchedulerInAsyncioLoop-388"><span class="linenos">388</span></a>        
</span><span id="RunSchedulerInAsyncioLoop-389"><a href="#RunSchedulerInAsyncioLoop-389"><span class="linenos">389</span></a>        <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">in_work</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-390"><a href="#RunSchedulerInAsyncioLoop-390"><span class="linenos">390</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-391"><a href="#RunSchedulerInAsyncioLoop-391"><span class="linenos">391</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-392"><a href="#RunSchedulerInAsyncioLoop-392"><span class="linenos">392</span></a>            <span class="k">return</span>
</span><span id="RunSchedulerInAsyncioLoop-393"><a href="#RunSchedulerInAsyncioLoop-393"><span class="linenos">393</span></a>
</span><span id="RunSchedulerInAsyncioLoop-394"><a href="#RunSchedulerInAsyncioLoop-394"><span class="linenos">394</span></a>        <span class="n">idle_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">next_event_after</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-395"><a href="#RunSchedulerInAsyncioLoop-395"><span class="linenos">395</span></a>        <span class="c1"># is_awake = self.scheduler.is_awake()</span>
</span><span id="RunSchedulerInAsyncioLoop-396"><a href="#RunSchedulerInAsyncioLoop-396"><span class="linenos">396</span></a>        <span class="n">is_idle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">is_idle</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-397"><a href="#RunSchedulerInAsyncioLoop-397"><span class="linenos">397</span></a>        <span class="n">need_to_register</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop-398"><a href="#RunSchedulerInAsyncioLoop-398"><span class="linenos">398</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_idle_when_possible</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-399"><a href="#RunSchedulerInAsyncioLoop-399"><span class="linenos">399</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">is_idle</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-400"><a href="#RunSchedulerInAsyncioLoop-400"><span class="linenos">400</span></a>                <span class="n">need_to_register</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RunSchedulerInAsyncioLoop-401"><a href="#RunSchedulerInAsyncioLoop-401"><span class="linenos">401</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-402"><a href="#RunSchedulerInAsyncioLoop-402"><span class="linenos">402</span></a>            <span class="n">need_to_register</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RunSchedulerInAsyncioLoop-403"><a href="#RunSchedulerInAsyncioLoop-403"><span class="linenos">403</span></a>
</span><span id="RunSchedulerInAsyncioLoop-404"><a href="#RunSchedulerInAsyncioLoop-404"><span class="linenos">404</span></a>        <span class="k">if</span> <span class="n">need_to_register</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-405"><a href="#RunSchedulerInAsyncioLoop-405"><span class="linenos">405</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-406"><a href="#RunSchedulerInAsyncioLoop-406"><span class="linenos">406</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-407"><a href="#RunSchedulerInAsyncioLoop-407"><span class="linenos">407</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register_idle</span><span class="p">(</span><span class="n">idle_time</span><span class="p">)</span>
</span><span id="RunSchedulerInAsyncioLoop-408"><a href="#RunSchedulerInAsyncioLoop-408"><span class="linenos">408</span></a>
</span><span id="RunSchedulerInAsyncioLoop-409"><a href="#RunSchedulerInAsyncioLoop-409"><span class="linenos">409</span></a>    <span class="k">def</span> <span class="nf">ready_to_stop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-410"><a href="#RunSchedulerInAsyncioLoop-410"><span class="linenos">410</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-411"><a href="#RunSchedulerInAsyncioLoop-411"><span class="linenos">411</span></a>
</span><span id="RunSchedulerInAsyncioLoop-412"><a href="#RunSchedulerInAsyncioLoop-412"><span class="linenos">412</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop-413"><a href="#RunSchedulerInAsyncioLoop-413"><span class="linenos">413</span></a>        <span class="c1"># self.register_idle()</span>
</span><span id="RunSchedulerInAsyncioLoop-414"><a href="#RunSchedulerInAsyncioLoop-414"><span class="linenos">414</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="RunSchedulerInAsyncioLoop-415"><a href="#RunSchedulerInAsyncioLoop-415"><span class="linenos">415</span></a>
</span><span id="RunSchedulerInAsyncioLoop-416"><a href="#RunSchedulerInAsyncioLoop-416"><span class="linenos">416</span></a>    <span class="k">def</span> <span class="nf">register_idle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">idle_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop-417"><a href="#RunSchedulerInAsyncioLoop-417"><span class="linenos">417</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-418"><a href="#RunSchedulerInAsyncioLoop-418"><span class="linenos">418</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">usable_idle_time</span>
</span><span id="RunSchedulerInAsyncioLoop-419"><a href="#RunSchedulerInAsyncioLoop-419"><span class="linenos">419</span></a>        
</span><span id="RunSchedulerInAsyncioLoop-420"><a href="#RunSchedulerInAsyncioLoop-420"><span class="linenos">420</span></a>        <span class="c1"># self.handle = self.loop.call_later(self.idle_time, self)</span>
</span><span id="RunSchedulerInAsyncioLoop-421"><a href="#RunSchedulerInAsyncioLoop-421"><span class="linenos">421</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">min_sleep_interval</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-422"><a href="#RunSchedulerInAsyncioLoop-422"><span class="linenos">422</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-423"><a href="#RunSchedulerInAsyncioLoop-423"><span class="linenos">423</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop-424"><a href="#RunSchedulerInAsyncioLoop-424"><span class="linenos">424</span></a>            <span class="c1"># self.handle = try_sleep(self.idle_time * (idle_time // self.idle_time), self.loop.call_later, self)</span>
</span><span id="RunSchedulerInAsyncioLoop-425"><a href="#RunSchedulerInAsyncioLoop-425"><span class="linenos">425</span></a>            <span class="c1"># # self.handle = try_sleep(0.001, self.loop.call_later, self)</span>
</span><span id="RunSchedulerInAsyncioLoop-426"><a href="#RunSchedulerInAsyncioLoop-426"><span class="linenos">426</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RunSchedulerInAsyncioLoop-427"><a href="#RunSchedulerInAsyncioLoop-427"><span class="linenos">427</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span><span class="p">))</span> <span class="o">+</span> <span class="n">get_countable_delta_time</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-428"><a href="#RunSchedulerInAsyncioLoop-428"><span class="linenos">428</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="n">idle_time</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="RunSchedulerInAsyncioLoop-429"><a href="#RunSchedulerInAsyncioLoop-429"><span class="linenos">429</span></a>
</span><span id="RunSchedulerInAsyncioLoop-430"><a href="#RunSchedulerInAsyncioLoop-430"><span class="linenos">430</span></a>    <span class="k">def</span> <span class="nf">cancel_handle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop-431"><a href="#RunSchedulerInAsyncioLoop-431"><span class="linenos">431</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="RunSchedulerInAsyncioLoop-432"><a href="#RunSchedulerInAsyncioLoop-432"><span class="linenos">432</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancel</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-433"><a href="#RunSchedulerInAsyncioLoop-433"><span class="linenos">433</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="RunSchedulerInAsyncioLoop-434"><a href="#RunSchedulerInAsyncioLoop-434"><span class="linenos">434</span></a>
</span><span id="RunSchedulerInAsyncioLoop-435"><a href="#RunSchedulerInAsyncioLoop-435"><span class="linenos">435</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop-436"><a href="#RunSchedulerInAsyncioLoop-436"><span class="linenos">436</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="RunSchedulerInAsyncioLoop-437"><a href="#RunSchedulerInAsyncioLoop-437"><span class="linenos">437</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RunSchedulerInAsyncioLoop-438"><a href="#RunSchedulerInAsyncioLoop-438"><span class="linenos">438</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancel</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop-439"><a href="#RunSchedulerInAsyncioLoop-439"><span class="linenos">439</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="RunSchedulerInAsyncioLoop-440"><a href="#RunSchedulerInAsyncioLoop-440"><span class="linenos">440</span></a>
</span><span id="RunSchedulerInAsyncioLoop-441"><a href="#RunSchedulerInAsyncioLoop-441"><span class="linenos">441</span></a>    <span class="k">def</span> <span class="nf">stop_when_possible</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop-442"><a href="#RunSchedulerInAsyncioLoop-442"><span class="linenos">442</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            <div id="RunSchedulerInAsyncioLoop.__init__" class="classattr">
                                        <input id="RunSchedulerInAsyncioLoop.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">RunSchedulerInAsyncioLoop</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span>,</span><span class="param">	<span class="n">idle_time</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">execute_every_X_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span></span>)</span>

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop.__init__-345"><a href="#RunSchedulerInAsyncioLoop.__init__-345"><span class="linenos">345</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">idle_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">execute_every_X_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-346"><a href="#RunSchedulerInAsyncioLoop.__init__-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span> <span class="o">=</span> <span class="n">scheduler</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-347"><a href="#RunSchedulerInAsyncioLoop.__init__-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">on_woke_up_callback</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_woke_up_callback</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-348"><a href="#RunSchedulerInAsyncioLoop.__init__-348"><span class="linenos">348</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-349"><a href="#RunSchedulerInAsyncioLoop.__init__-349"><span class="linenos">349</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="n">get_usable_min_sleep_interval</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-350"><a href="#RunSchedulerInAsyncioLoop.__init__-350"><span class="linenos">350</span></a>        
</span><span id="RunSchedulerInAsyncioLoop.__init__-351"><a href="#RunSchedulerInAsyncioLoop.__init__-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="o">=</span> <span class="n">get_min_sleep_interval</span><span class="p">()</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="n">get_min_sleep_interval</span><span class="p">())</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-352"><a href="#RunSchedulerInAsyncioLoop.__init__-352"><span class="linenos">352</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">min_sleep_interval</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">get_min_sleep_interval</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="ow">or</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-353"><a href="#RunSchedulerInAsyncioLoop.__init__-353"><span class="linenos">353</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">usable_idle_time</span> <span class="o">=</span> <span class="p">(</span><span class="n">get_min_sleep_interval</span><span class="p">()</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="n">get_min_sleep_interval</span><span class="p">()))</span> <span class="o">+</span> <span class="n">get_countable_delta_time</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-354"><a href="#RunSchedulerInAsyncioLoop.__init__-354"><span class="linenos">354</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loop</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-355"><a href="#RunSchedulerInAsyncioLoop.__init__-355"><span class="linenos">355</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># type: Optional[asyncio.Handle]</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-356"><a href="#RunSchedulerInAsyncioLoop.__init__-356"><span class="linenos">356</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_idle_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-357"><a href="#RunSchedulerInAsyncioLoop.__init__-357"><span class="linenos">357</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-358"><a href="#RunSchedulerInAsyncioLoop.__init__-358"><span class="linenos">358</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-359"><a href="#RunSchedulerInAsyncioLoop.__init__-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-360"><a href="#RunSchedulerInAsyncioLoop.__init__-360"><span class="linenos">360</span></a>        <span class="k">if</span> <span class="n">execute_every_X_iterations</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-361"><a href="#RunSchedulerInAsyncioLoop.__init__-361"><span class="linenos">361</span></a>            <span class="n">execute_every_X_iterations</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-362"><a href="#RunSchedulerInAsyncioLoop.__init__-362"><span class="linenos">362</span></a>        
</span><span id="RunSchedulerInAsyncioLoop.__init__-363"><a href="#RunSchedulerInAsyncioLoop.__init__-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">execute_every_X_iterations</span> <span class="o">=</span> <span class="n">execute_every_X_iterations</span>
</span><span id="RunSchedulerInAsyncioLoop.__init__-364"><a href="#RunSchedulerInAsyncioLoop.__init__-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_iteration</span> <span class="o">=</span> <span class="n">execute_every_X_iterations</span>
</span></pre></div>


    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.scheduler" class="classattr">
                                <div class="attr variable">
            <span class="name">scheduler</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.scheduler"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.idle_time" class="classattr">
                                <div class="attr variable">
            <span class="name">idle_time</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.idle_time"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.min_sleep_interval" class="classattr">
                                <div class="attr variable">
            <span class="name">min_sleep_interval</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.min_sleep_interval"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.usable_idle_time" class="classattr">
                                <div class="attr variable">
            <span class="name">usable_idle_time</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.usable_idle_time"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.loop" class="classattr">
                                <div class="attr variable">
            <span class="name">loop</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.loop"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.handle" class="classattr">
                                <div class="attr variable">
            <span class="name">handle</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.handle"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.make_idle_when_possible" class="classattr">
                                <div class="attr variable">
            <span class="name">make_idle_when_possible</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.make_idle_when_possible"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.need_to_stop_when_possible" class="classattr">
                                <div class="attr variable">
            <span class="name">need_to_stop_when_possible</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.need_to_stop_when_possible"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.need_to_stop_now" class="classattr">
                                <div class="attr variable">
            <span class="name">need_to_stop_now</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.need_to_stop_now"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.in_idle_state" class="classattr">
                                <div class="attr variable">
            <span class="name">in_idle_state</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.in_idle_state"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.execute_every_X_iterations" class="classattr">
                                <div class="attr variable">
            <span class="name">execute_every_X_iterations</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.execute_every_X_iterations"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.current_iteration" class="classattr">
                                <div class="attr variable">
            <span class="name">current_iteration</span>

        
    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.current_iteration"></a>
    
    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.on_woke_up_callback" class="classattr">
                                        <input id="RunSchedulerInAsyncioLoop.on_woke_up_callback-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_woke_up_callback</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop.on_woke_up_callback-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.on_woke_up_callback"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop.on_woke_up_callback-366"><a href="#RunSchedulerInAsyncioLoop.on_woke_up_callback-366"><span class="linenos">366</span></a>    <span class="k">def</span> <span class="nf">on_woke_up_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop.on_woke_up_callback-367"><a href="#RunSchedulerInAsyncioLoop.on_woke_up_callback-367"><span class="linenos">367</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop.on_woke_up_callback-368"><a href="#RunSchedulerInAsyncioLoop.on_woke_up_callback-368"><span class="linenos">368</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cancel_handle</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop.on_woke_up_callback-369"><a href="#RunSchedulerInAsyncioLoop.on_woke_up_callback-369"><span class="linenos">369</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RunSchedulerInAsyncioLoop.on_woke_up_callback-370"><a href="#RunSchedulerInAsyncioLoop.on_woke_up_callback-370"><span class="linenos">370</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.ready_to_stop" class="classattr">
                                        <input id="RunSchedulerInAsyncioLoop.ready_to_stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ready_to_stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop.ready_to_stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.ready_to_stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop.ready_to_stop-409"><a href="#RunSchedulerInAsyncioLoop.ready_to_stop-409"><span class="linenos">409</span></a>    <span class="k">def</span> <span class="nf">ready_to_stop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop.ready_to_stop-410"><a href="#RunSchedulerInAsyncioLoop.ready_to_stop-410"><span class="linenos">410</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="o">.</span><span class="n">in_work</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.register" class="classattr">
                                        <input id="RunSchedulerInAsyncioLoop.register-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop.register-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.register"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop.register-412"><a href="#RunSchedulerInAsyncioLoop.register-412"><span class="linenos">412</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop.register-413"><a href="#RunSchedulerInAsyncioLoop.register-413"><span class="linenos">413</span></a>        <span class="c1"># self.register_idle()</span>
</span><span id="RunSchedulerInAsyncioLoop.register-414"><a href="#RunSchedulerInAsyncioLoop.register-414"><span class="linenos">414</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">call_soon</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.register_idle" class="classattr">
                                        <input id="RunSchedulerInAsyncioLoop.register_idle-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_idle</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">idle_time</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop.register_idle-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.register_idle"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop.register_idle-416"><a href="#RunSchedulerInAsyncioLoop.register_idle-416"><span class="linenos">416</span></a>    <span class="k">def</span> <span class="nf">register_idle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">idle_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-417"><a href="#RunSchedulerInAsyncioLoop.register_idle-417"><span class="linenos">417</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-418"><a href="#RunSchedulerInAsyncioLoop.register_idle-418"><span class="linenos">418</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">usable_idle_time</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-419"><a href="#RunSchedulerInAsyncioLoop.register_idle-419"><span class="linenos">419</span></a>        
</span><span id="RunSchedulerInAsyncioLoop.register_idle-420"><a href="#RunSchedulerInAsyncioLoop.register_idle-420"><span class="linenos">420</span></a>        <span class="c1"># self.handle = self.loop.call_later(self.idle_time, self)</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-421"><a href="#RunSchedulerInAsyncioLoop.register_idle-421"><span class="linenos">421</span></a>        <span class="k">if</span> <span class="n">idle_time</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">min_sleep_interval</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-422"><a href="#RunSchedulerInAsyncioLoop.register_idle-422"><span class="linenos">422</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-423"><a href="#RunSchedulerInAsyncioLoop.register_idle-423"><span class="linenos">423</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-424"><a href="#RunSchedulerInAsyncioLoop.register_idle-424"><span class="linenos">424</span></a>            <span class="c1"># self.handle = try_sleep(self.idle_time * (idle_time // self.idle_time), self.loop.call_later, self)</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-425"><a href="#RunSchedulerInAsyncioLoop.register_idle-425"><span class="linenos">425</span></a>            <span class="c1"># # self.handle = try_sleep(0.001, self.loop.call_later, self)</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-426"><a href="#RunSchedulerInAsyncioLoop.register_idle-426"><span class="linenos">426</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">in_idle_state</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-427"><a href="#RunSchedulerInAsyncioLoop.register_idle-427"><span class="linenos">427</span></a>            <span class="n">idle_time</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span> <span class="o">*</span> <span class="p">(</span><span class="n">idle_time</span> <span class="o">//</span> <span class="bp">self</span><span class="o">.</span><span class="n">idle_time</span><span class="p">))</span> <span class="o">+</span> <span class="n">get_countable_delta_time</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop.register_idle-428"><a href="#RunSchedulerInAsyncioLoop.register_idle-428"><span class="linenos">428</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">call_later</span><span class="p">(</span><span class="n">idle_time</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.cancel_handle" class="classattr">
                                        <input id="RunSchedulerInAsyncioLoop.cancel_handle-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cancel_handle</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop.cancel_handle-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.cancel_handle"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop.cancel_handle-430"><a href="#RunSchedulerInAsyncioLoop.cancel_handle-430"><span class="linenos">430</span></a>    <span class="k">def</span> <span class="nf">cancel_handle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop.cancel_handle-431"><a href="#RunSchedulerInAsyncioLoop.cancel_handle-431"><span class="linenos">431</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="RunSchedulerInAsyncioLoop.cancel_handle-432"><a href="#RunSchedulerInAsyncioLoop.cancel_handle-432"><span class="linenos">432</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancel</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop.cancel_handle-433"><a href="#RunSchedulerInAsyncioLoop.cancel_handle-433"><span class="linenos">433</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.stop" class="classattr">
                                        <input id="RunSchedulerInAsyncioLoop.stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop.stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop.stop-435"><a href="#RunSchedulerInAsyncioLoop.stop-435"><span class="linenos">435</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop.stop-436"><a href="#RunSchedulerInAsyncioLoop.stop-436"><span class="linenos">436</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="RunSchedulerInAsyncioLoop.stop-437"><a href="#RunSchedulerInAsyncioLoop.stop-437"><span class="linenos">437</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_now</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RunSchedulerInAsyncioLoop.stop-438"><a href="#RunSchedulerInAsyncioLoop.stop-438"><span class="linenos">438</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="o">.</span><span class="n">cancel</span><span class="p">()</span>
</span><span id="RunSchedulerInAsyncioLoop.stop-439"><a href="#RunSchedulerInAsyncioLoop.stop-439"><span class="linenos">439</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">handle</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="RunSchedulerInAsyncioLoop.stop_when_possible" class="classattr">
                                        <input id="RunSchedulerInAsyncioLoop.stop_when_possible-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop_when_possible</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RunSchedulerInAsyncioLoop.stop_when_possible-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RunSchedulerInAsyncioLoop.stop_when_possible"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RunSchedulerInAsyncioLoop.stop_when_possible-441"><a href="#RunSchedulerInAsyncioLoop.stop_when_possible-441"><span class="linenos">441</span></a>    <span class="k">def</span> <span class="nf">stop_when_possible</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RunSchedulerInAsyncioLoop.stop_when_possible-442"><a href="#RunSchedulerInAsyncioLoop.stop_when_possible-442"><span class="linenos">442</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_to_stop_when_possible</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="coro_interfaces_arg_manager">
                            <input id="coro_interfaces_arg_manager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">coro_interfaces_arg_manager</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">event_loop</span>,</span><span class="param">	<span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="coro_interfaces_arg_manager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#coro_interfaces_arg_manager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="coro_interfaces_arg_manager-333"><a href="#coro_interfaces_arg_manager-333"><span class="linenos">333</span></a><span class="k">def</span> <span class="nf">coro_interfaces_arg_manager</span><span class="p">(</span><span class="n">event_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="coro_interfaces_arg_manager-334"><a href="#coro_interfaces_arg_manager-334"><span class="linenos">334</span></a>    <span class="n">acf</span> <span class="o">=</span> <span class="n">ArgsManager</span><span class="p">(</span>
</span><span id="coro_interfaces_arg_manager-335"><a href="#coro_interfaces_arg_manager-335"><span class="linenos">335</span></a>        <span class="n">EArgs</span><span class="p">(</span><span class="n">event_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">,</span> <span class="n">CoroType</span><span class="o">.</span><span class="n">auto</span><span class="p">),</span>
</span><span id="coro_interfaces_arg_manager-336"><a href="#coro_interfaces_arg_manager-336"><span class="linenos">336</span></a>    <span class="p">)</span><span class="o">.</span><span class="n">callable</span><span class="p">(</span><span class="n">await_coro_fast</span><span class="p">)</span>
</span><span id="coro_interfaces_arg_manager-337"><a href="#coro_interfaces_arg_manager-337"><span class="linenos">337</span></a>    <span class="n">atf</span> <span class="o">=</span> <span class="n">ArgsManager</span><span class="p">(</span>
</span><span id="coro_interfaces_arg_manager-338"><a href="#coro_interfaces_arg_manager-338"><span class="linenos">338</span></a>        <span class="n">EArgs</span><span class="p">(</span><span class="n">event_loop</span><span class="p">,</span> <span class="n">coro_scheduler</span><span class="p">),</span>
</span><span id="coro_interfaces_arg_manager-339"><a href="#coro_interfaces_arg_manager-339"><span class="linenos">339</span></a>    <span class="p">)</span><span class="o">.</span><span class="n">callable</span><span class="p">(</span><span class="n">await_task_fast</span><span class="p">)</span>
</span><span id="coro_interfaces_arg_manager-340"><a href="#coro_interfaces_arg_manager-340"><span class="linenos">340</span></a>    
</span><span id="coro_interfaces_arg_manager-341"><a href="#coro_interfaces_arg_manager-341"><span class="linenos">341</span></a>    <span class="k">return</span> <span class="n">EArgs</span><span class="p">(</span><span class="n">await_coro_fast</span><span class="o">=</span><span class="n">acf</span><span class="p">,</span> <span class="n">await_task_fast</span><span class="o">=</span><span class="n">atf</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="create_task">
                            <input id="create_task-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">create_task</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">acoro</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">_asyncio</span><span class="o">.</span><span class="n">Task</span>:</span></span>

                <label class="view-source-button" for="create_task-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#create_task"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="create_task-471"><a href="#create_task-471"><span class="linenos">471</span></a><span class="k">def</span> <span class="nf">create_task</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="n">acoro</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">Task</span><span class="p">:</span>
</span><span id="create_task-472"><a href="#create_task-472"><span class="linenos">472</span></a>    <span class="k">if</span> <span class="n">__debug__</span><span class="p">:</span> <span class="n">dlog</span><span class="p">(</span><span class="s1">&#39;call_soon_future - start&#39;</span><span class="p">)</span>
</span><span id="create_task-473"><a href="#create_task-473"><span class="linenos">473</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="create_task-474"><a href="#create_task-474"><span class="linenos">474</span></a>    <span class="n">awaitable_coro_obj</span> <span class="o">=</span> <span class="n">acoro</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="create_task-475"><a href="#create_task-475"><span class="linenos">475</span></a>    <span class="k">return</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">awaitable_coro_obj</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="create_task_in_thread_pool">
                            <input id="create_task_in_thread_pool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">create_task_in_thread_pool</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">joiner</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="create_task_in_thread_pool-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#create_task_in_thread_pool"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="create_task_in_thread_pool-478"><a href="#create_task_in_thread_pool-478"><span class="linenos">478</span></a><span class="k">def</span> <span class="nf">create_task_in_thread_pool</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="n">joiner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Awaitable</span><span class="p">[</span><span class="n">Any</span><span class="p">]],</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="create_task_in_thread_pool-479"><a href="#create_task_in_thread_pool-479"><span class="linenos">479</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_handler</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">joiner</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="create_task_in_thread_pool-480"><a href="#create_task_in_thread_pool-480"><span class="linenos">480</span></a>        <span class="n">worker_with_args</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="create_task_in_thread_pool-481"><a href="#create_task_in_thread_pool-481"><span class="linenos">481</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">worker_with_args</span><span class="p">)</span>
</span><span id="create_task_in_thread_pool-482"><a href="#create_task_in_thread_pool-482"><span class="linenos">482</span></a>        <span class="k">if</span> <span class="n">joiner</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="create_task_in_thread_pool-483"><a href="#create_task_in_thread_pool-483"><span class="linenos">483</span></a>            <span class="k">await</span> <span class="n">joiner</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="create_task_in_thread_pool-484"><a href="#create_task_in_thread_pool-484"><span class="linenos">484</span></a>                        
</span><span id="create_task_in_thread_pool-485"><a href="#create_task_in_thread_pool-485"><span class="linenos">485</span></a>    <span class="n">create_task</span><span class="p">(</span><span class="n">loop</span><span class="p">,</span> <span class="n">sync_handler</span><span class="p">,</span> <span class="n">loop</span><span class="p">,</span> <span class="n">joiner</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="task_in_thread_pool">
                            <input id="task_in_thread_pool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">task_in_thread_pool</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="task_in_thread_pool-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#task_in_thread_pool"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="task_in_thread_pool-488"><a href="#task_in_thread_pool-488"><span class="linenos">488</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">task_in_thread_pool</span><span class="p">(</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">],</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="task_in_thread_pool-489"><a href="#task_in_thread_pool-489"><span class="linenos">489</span></a>    <span class="n">worker_with_args</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="task_in_thread_pool-490"><a href="#task_in_thread_pool-490"><span class="linenos">490</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">worker_with_args</span><span class="p">)</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>