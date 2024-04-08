---
title: read_write_locker
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.read_write_locker<wbr>.versions<wbr>.v_0<wbr>.read_write_locker    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-read_write_locker-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-read_write_locker-view-source"><span>View Source</span></label>

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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.3&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>    <span class="s1">&#39;RWOperation&#39;</span><span class="p">,</span> <span class="s1">&#39;RWLockerRequest&#39;</span><span class="p">,</span> <span class="s1">&#39;RWLockerEntity&#39;</span><span class="p">,</span> <span class="s1">&#39;RWLockerContextManager&#39;</span><span class="p">,</span> <span class="s1">&#39;FakeRWLockerContextManager&#39;</span><span class="p">,</span> <span class="s1">&#39;UnknownLockerEntity&#39;</span><span class="p">,</span> <span class="s1">&#39;RWLocker&#39;</span><span class="p">,</span> <span class="s1">&#39;get_rw_lock&#39;</span><span class="p">,</span> <span class="s1">&#39;grwl&#39;</span><span class="p">,</span> <span class="s1">&#39;aget_rw_lock&#39;</span><span class="p">,</span> <span class="s1">&#39;agrwl&#39;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="p">]</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_tools.await_coro</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Set</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.repeat_for_a_time</span> <span class="kn">import</span> <span class="n">Tracer</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values.versions.v_1</span> <span class="kn">import</span> <span class="n">ValueExistence</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="kn">from</span> <span class="nn">async_generator</span> <span class="kn">import</span> <span class="n">asynccontextmanager</span><span class="p">,</span> <span class="n">async_generator</span><span class="p">,</span> <span class="n">yield_</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="k">class</span> <span class="nc">RWOperation</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="n">read</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="n">write</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="k">class</span> <span class="nc">RWLockerRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;RWLockerContextManager&#39;</span><span class="p">:</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">)</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="k">def</span> <span class="nf">deregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">safe</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">,</span> <span class="n">safe</span><span class="p">)</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    <span class="k">def</span> <span class="nf">wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="k">def</span> <span class="nf">wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="k">class</span> <span class="nc">RWLockerEntity</span><span class="p">:</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">recursive</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">service</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_writers_in_progress</span>  <span class="c1"># Must be edited directly from coroutine. In order to eliminate new writers arrived during the end of the current loop iteration</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_readers_in_progress</span>  <span class="c1"># Must be edited directly from coroutine. In order to eliminate new readers arrived during the end of the current loop iteration</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">:</span> <span class="n">RWOperation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>  <span class="c1"># Default is &#39;RWOperation.read&#39; in order to force &#39;write&#39; as a first operation among several first concurent operations</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">related_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="k">def</span> <span class="nf">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">increase_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>            
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="k">def</span> <span class="nf">decrease_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="nf">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">increase_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>            
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">decrease_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>    <span class="k">def</span> <span class="nf">try_write_lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">apply</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span><span class="p">:</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span> <span class="ow">and</span> <span class="p">(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>    <span class="k">def</span> <span class="nf">try_read_lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">apply</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span><span class="p">:</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span> <span class="ow">and</span> <span class="p">(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">test_remove</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_coroutines</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a><span class="k">class</span> <span class="nc">RWLockerContextManagerBase</span><span class="p">:</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">core</span><span class="p">:</span> <span class="n">RWLockerEntity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="p">:</span> <span class="n">RWLockerEntity</span> <span class="o">=</span> <span class="n">core</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RWOperation</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>    
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>    <span class="k">def</span> <span class="nf">lockable</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">operation</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RWOperation</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="k">if</span> <span class="n">operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>            <span class="n">operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="n">operation</span><span class="p">:</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_write_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_read_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="n">need_service_assistance</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>    
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>    <span class="k">def</span> <span class="nf">change_max_boundaries</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">max_writers_in_progress</span> <span class="o">=</span> <span class="n">max_writers_in_progress</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">max_readers_in_progress</span> <span class="o">=</span> <span class="n">max_readers_in_progress</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">operation</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RWOperation</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        <span class="k">if</span> <span class="n">operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>            <span class="n">operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">operation</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>    
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a><span class="k">class</span> <span class="nc">RWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerContextManagerBase</span><span class="p">):</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">core</span><span class="p">:</span> <span class="n">RWLockerEntity</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">core</span><span class="p">)</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>    
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_write_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            <span class="k">if</span> <span class="n">need_service_assistance</span><span class="p">:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">writers_pending</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_read_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>            <span class="k">if</span> <span class="n">need_service_assistance</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">readers_pending</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>        
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>    
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">)</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>        
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_write_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>            <span class="k">if</span> <span class="n">need_service_assistance</span><span class="p">:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">writers_pending</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_read_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>            <span class="k">if</span> <span class="n">need_service_assistance</span><span class="p">:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">readers_pending</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span>        
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>        
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">)</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">)</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>        
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a><span class="k">class</span> <span class="nc">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerContextManagerBase</span><span class="p">):</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">core</span><span class="p">:</span> <span class="n">RWLockerEntity</span><span class="p">):</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">core</span><span class="p">)</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>    
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>        
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">()</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">()</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_writers_in_progress</span><span class="p">()</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_readers_in_progress</span><span class="p">()</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>        
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">()</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">()</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_writers_in_progress</span><span class="p">()</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_readers_in_progress</span><span class="p">()</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a><span class="k">class</span> <span class="nc">UnknownLockerEntity</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>    <span class="k">pass</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a><span class="k">class</span> <span class="nc">RWLocker</span><span class="p">(</span><span class="n">Service</span><span class="p">,</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>        <span class="c1"># loop.add_global_on_coro_del_handler(self._on_coro_del_handler_global)  # Todo: switch to local coro del handler</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register</span><span class="p">,</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_deregister</span><span class="p">,</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_write</span><span class="p">,</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_read</span><span class="p">,</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        <span class="p">}</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">RWLockerEntity</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>            <span class="s1">&#39;locker entities num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">),</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>            <span class="s1">&#39;affected coroutines num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">),</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>            <span class="s1">&#39;waiting for write requests num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">),</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>            <span class="s1">&#39;waiting_for_read_requests num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">),</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="p">}</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RWLockerRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>        <span class="c1"># entities_waiting_for_remove</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>                <span class="k">continue</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>            
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">test_remove</span><span class="p">()</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>                <span class="k">continue</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>        <span class="c1"># entities_waiting_for_write</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">)</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>                <span class="k">continue</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>            
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">try_write_lock</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>                <span class="k">continue</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>                <span class="n">entity</span><span class="o">.</span><span class="n">writers_pending</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>                    <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>                
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>        
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>                    
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>        <span class="c1"># entities_waiting_for_read</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">)</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>                <span class="k">continue</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>            
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">try_read_lock</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>                <span class="k">continue</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>                <span class="n">entity</span><span class="o">.</span><span class="n">readers_pending</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>                    <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>                
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>        
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="c1"># general</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">):</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">)</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>    
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>    <span class="k">def</span> <span class="nf">get_locker_entity</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">):</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>    <span class="k">def</span> <span class="nf">_on_register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>        <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="n">entity</span><span class="p">:</span> <span class="n">RWLockerEntity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>        <span class="n">entity</span><span class="o">.</span><span class="n">related_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">:</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>        
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>        <span class="n">context_manager</span><span class="p">:</span> <span class="n">RWLockerContextManager</span> <span class="o">=</span> <span class="n">RWLockerContextManager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">interface</span><span class="p">)</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">context_manager</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>    <span class="k">def</span> <span class="nf">_on_deregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">safe</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>        <span class="k">if</span> <span class="n">safe</span><span class="p">:</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>                <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>                <span class="k">for</span> <span class="n">related_coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">related_coroutines</span><span class="p">:</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>                    <span class="n">coroutine_entities</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">related_coro_id</span><span class="p">]</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>                    <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="n">coroutine_entities</span><span class="p">:</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>                        <span class="n">coroutine_entities</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>                
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>            
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>    <span class="k">def</span> <span class="nf">_on_wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>        <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">()</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>        
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>        <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>    <span class="k">def</span> <span class="nf">_on_wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>        <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">()</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>        
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>        <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler_global</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">:</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>            <span class="n">entities</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>            <span class="k">for</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="n">entities</span><span class="p">:</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>                <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>                    <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>                    <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">related_coroutines</span><span class="p">:</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>                        <span class="n">entity</span><span class="o">.</span><span class="n">related_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>                    
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>                    <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>                        <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>        
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">:</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>        
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">:</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>        
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">:</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler_global</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a><span class="n">RWLockerRequest</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">RWLocker</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a><span class="k">def</span> <span class="nf">get_rw_lock</span><span class="p">(</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">RWLockerContextManager</span><span class="p">,</span> <span class="n">FakeRWLockerContextManager</span><span class="p">]:</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running from Service</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>    <span class="n">locker_entity</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">)</span><span class="o">.</span><span class="n">get_locker_entity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>    <span class="k">if</span> <span class="n">locker_entity</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">interface</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">))</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">RWLockerContextManager</span><span class="p">(</span><span class="n">locker_entity</span><span class="p">,</span> <span class="n">interface</span><span class="p">)</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>    
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>    <span class="k">return</span> <span class="n">lock</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a><span class="n">grwl</span> <span class="o">=</span> <span class="n">get_rw_lock</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_rw_lock</span><span class="p">(</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">RWLockerContextManager</span><span class="p">,</span> <span class="n">FakeRWLockerContextManager</span><span class="p">]:</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running from Service</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>    <span class="n">locker_entity</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">)</span><span class="o">.</span><span class="n">get_locker_entity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>    <span class="k">if</span> <span class="n">locker_entity</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="k">await</span> <span class="n">interface</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">))</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">RWLockerContextManager</span><span class="p">(</span><span class="n">locker_entity</span><span class="p">,</span> <span class="n">interface</span><span class="p">)</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>    
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>    <span class="k">return</span> <span class="n">lock</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a><span class="n">agrwl</span> <span class="o">=</span> <span class="n">aget_rw_lock</span>
</span></pre></div>


            </section>
                <section id="RWOperation">
                            <input id="RWOperation-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">RWOperation</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="RWOperation-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWOperation"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWOperation-52"><a href="#RWOperation-52"><span class="linenos">52</span></a><span class="k">class</span> <span class="nc">RWOperation</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="RWOperation-53"><a href="#RWOperation-53"><span class="linenos">53</span></a>    <span class="n">read</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWOperation-54"><a href="#RWOperation-54"><span class="linenos">54</span></a>    <span class="n">write</span> <span class="o">=</span> <span class="mi">1</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="RWOperation.read" class="classattr">
                                <div class="attr variable">
            <span class="name">read</span>        =
<span class="default_value">&lt;<a href="#RWOperation.read">RWOperation.read</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#RWOperation.read"></a>
    
    

                            </div>
                            <div id="RWOperation.write" class="classattr">
                                <div class="attr variable">
            <span class="name">write</span>        =
<span class="default_value">&lt;<a href="#RWOperation.write">RWOperation.write</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#RWOperation.write"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="RWOperation.name" class="variable">name</dd>
                <dd id="RWOperation.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="RWLockerRequest">
                            <input id="RWLockerRequest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">RWLockerRequest</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</span>):

                <label class="view-source-button" for="RWLockerRequest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerRequest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerRequest-57"><a href="#RWLockerRequest-57"><span class="linenos">57</span></a><span class="k">class</span> <span class="nc">RWLockerRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="RWLockerRequest-58"><a href="#RWLockerRequest-58"><span class="linenos">58</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;RWLockerContextManager&#39;</span><span class="p">:</span>
</span><span id="RWLockerRequest-59"><a href="#RWLockerRequest-59"><span class="linenos">59</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">)</span>
</span><span id="RWLockerRequest-60"><a href="#RWLockerRequest-60"><span class="linenos">60</span></a>
</span><span id="RWLockerRequest-61"><a href="#RWLockerRequest-61"><span class="linenos">61</span></a>    <span class="k">def</span> <span class="nf">deregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">safe</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerRequest-62"><a href="#RWLockerRequest-62"><span class="linenos">62</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">,</span> <span class="n">safe</span><span class="p">)</span>
</span><span id="RWLockerRequest-63"><a href="#RWLockerRequest-63"><span class="linenos">63</span></a>    
</span><span id="RWLockerRequest-64"><a href="#RWLockerRequest-64"><span class="linenos">64</span></a>    <span class="k">def</span> <span class="nf">wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RWLockerRequest-65"><a href="#RWLockerRequest-65"><span class="linenos">65</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="RWLockerRequest-66"><a href="#RWLockerRequest-66"><span class="linenos">66</span></a>    
</span><span id="RWLockerRequest-67"><a href="#RWLockerRequest-67"><span class="linenos">67</span></a>    <span class="k">def</span> <span class="nf">wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RWLockerRequest-68"><a href="#RWLockerRequest-68"><span class="linenos">68</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="RWLockerRequest.register" class="classattr">
                                        <input id="RWLockerRequest.register-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n"><a href="#RWLockerContextManager">RWLockerContextManager</a></span>:</span></span>

                <label class="view-source-button" for="RWLockerRequest.register-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerRequest.register"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerRequest.register-58"><a href="#RWLockerRequest.register-58"><span class="linenos">58</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;RWLockerContextManager&#39;</span><span class="p">:</span>
</span><span id="RWLockerRequest.register-59"><a href="#RWLockerRequest.register-59"><span class="linenos">59</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerRequest.deregister" class="classattr">
                                        <input id="RWLockerRequest.deregister-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">deregister</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span>, </span><span class="param"><span class="n">safe</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="RWLockerRequest.deregister-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerRequest.deregister"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerRequest.deregister-61"><a href="#RWLockerRequest.deregister-61"><span class="linenos">61</span></a>    <span class="k">def</span> <span class="nf">deregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">safe</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerRequest.deregister-62"><a href="#RWLockerRequest.deregister-62"><span class="linenos">62</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">,</span> <span class="n">safe</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerRequest.wait_for_write" class="classattr">
                                        <input id="RWLockerRequest.wait_for_write-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">wait_for_write</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="RWLockerRequest.wait_for_write-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerRequest.wait_for_write"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerRequest.wait_for_write-64"><a href="#RWLockerRequest.wait_for_write-64"><span class="linenos">64</span></a>    <span class="k">def</span> <span class="nf">wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RWLockerRequest.wait_for_write-65"><a href="#RWLockerRequest.wait_for_write-65"><span class="linenos">65</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerRequest.wait_for_read" class="classattr">
                                        <input id="RWLockerRequest.wait_for_read-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">wait_for_read</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="RWLockerRequest.wait_for_read-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerRequest.wait_for_read"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerRequest.wait_for_read-67"><a href="#RWLockerRequest.wait_for_read-67"><span class="linenos">67</span></a>    <span class="k">def</span> <span class="nf">wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RWLockerRequest.wait_for_read-68"><a href="#RWLockerRequest.wait_for_read-68"><span class="linenos">68</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerRequest.default_service_type" class="classattr">
                                <div class="attr variable">
            <span class="name">default_service_type</span><span class="annotation">: Union[type[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service], NoneType]</span>        =
<input id="RWLockerRequest.default_service_type-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="RWLockerRequest.default_service_type-view-value"></label><span class="default_value">&lt;class &#39;<a href="#RWLocker">RWLocker</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#RWLockerRequest.default_service_type"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</dt>
                                <dd id="RWLockerRequest.default__request__type__" class="variable">default__request__type__</dd>
                <dd id="RWLockerRequest.request_type" class="variable">request_type</dd>
                <dd id="RWLockerRequest.args" class="variable">args</dd>
                <dd id="RWLockerRequest.kwargs" class="variable">kwargs</dd>
                <dd id="RWLockerRequest.provide_to_request_handler" class="variable">provide_to_request_handler</dd>
                <dd id="RWLockerRequest.interface" class="function">interface</dd>
                <dd id="RWLockerRequest.i" class="function">i</dd>
                <dd id="RWLockerRequest.async_interface" class="function">async_interface</dd>
                <dd id="RWLockerRequest.ai" class="function">ai</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="RWLockerEntity">
                            <input id="RWLockerEntity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">RWLockerEntity</span>:

                <label class="view-source-button" for="RWLockerEntity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity-71"><a href="#RWLockerEntity-71"><span class="linenos"> 71</span></a><span class="k">class</span> <span class="nc">RWLockerEntity</span><span class="p">:</span>
</span><span id="RWLockerEntity-72"><a href="#RWLockerEntity-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="RWLockerEntity-73"><a href="#RWLockerEntity-73"><span class="linenos"> 73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="RWLockerEntity-74"><a href="#RWLockerEntity-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">recursive</span>
</span><span id="RWLockerEntity-75"><a href="#RWLockerEntity-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">service</span>
</span><span id="RWLockerEntity-76"><a href="#RWLockerEntity-76"><span class="linenos"> 76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity-77"><a href="#RWLockerEntity-77"><span class="linenos"> 77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLockerEntity-78"><a href="#RWLockerEntity-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity-79"><a href="#RWLockerEntity-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_writers_in_progress</span>  <span class="c1"># Must be edited directly from coroutine. In order to eliminate new writers arrived during the end of the current loop iteration</span>
</span><span id="RWLockerEntity-80"><a href="#RWLockerEntity-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity-81"><a href="#RWLockerEntity-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLockerEntity-82"><a href="#RWLockerEntity-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity-83"><a href="#RWLockerEntity-83"><span class="linenos"> 83</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_readers_in_progress</span>  <span class="c1"># Must be edited directly from coroutine. In order to eliminate new readers arrived during the end of the current loop iteration</span>
</span><span id="RWLockerEntity-84"><a href="#RWLockerEntity-84"><span class="linenos"> 84</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">:</span> <span class="n">RWOperation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>  <span class="c1"># Default is &#39;RWOperation.read&#39; in order to force &#39;write&#39; as a first operation among several first concurent operations</span>
</span><span id="RWLockerEntity-85"><a href="#RWLockerEntity-85"><span class="linenos"> 85</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLockerEntity-86"><a href="#RWLockerEntity-86"><span class="linenos"> 86</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">related_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLockerEntity-87"><a href="#RWLockerEntity-87"><span class="linenos"> 87</span></a>
</span><span id="RWLockerEntity-88"><a href="#RWLockerEntity-88"><span class="linenos"> 88</span></a>    <span class="k">def</span> <span class="nf">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity-89"><a href="#RWLockerEntity-89"><span class="linenos"> 89</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity-90"><a href="#RWLockerEntity-90"><span class="linenos"> 90</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span>
</span><span id="RWLockerEntity-91"><a href="#RWLockerEntity-91"><span class="linenos"> 91</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-92"><a href="#RWLockerEntity-92"><span class="linenos"> 92</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-93"><a href="#RWLockerEntity-93"><span class="linenos"> 93</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span>
</span><span id="RWLockerEntity-94"><a href="#RWLockerEntity-94"><span class="linenos"> 94</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-95"><a href="#RWLockerEntity-95"><span class="linenos"> 95</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-96"><a href="#RWLockerEntity-96"><span class="linenos"> 96</span></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span>
</span><span id="RWLockerEntity-97"><a href="#RWLockerEntity-97"><span class="linenos"> 97</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-98"><a href="#RWLockerEntity-98"><span class="linenos"> 98</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span>
</span><span id="RWLockerEntity-99"><a href="#RWLockerEntity-99"><span class="linenos"> 99</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-100"><a href="#RWLockerEntity-100"><span class="linenos">100</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-101"><a href="#RWLockerEntity-101"><span class="linenos">101</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span>
</span><span id="RWLockerEntity-102"><a href="#RWLockerEntity-102"><span class="linenos">102</span></a>    
</span><span id="RWLockerEntity-103"><a href="#RWLockerEntity-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">increase_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RWLockerEntity-104"><a href="#RWLockerEntity-104"><span class="linenos">104</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity-105"><a href="#RWLockerEntity-105"><span class="linenos">105</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span>
</span><span id="RWLockerEntity-106"><a href="#RWLockerEntity-106"><span class="linenos">106</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity-107"><a href="#RWLockerEntity-107"><span class="linenos">107</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-108"><a href="#RWLockerEntity-108"><span class="linenos">108</span></a>            
</span><span id="RWLockerEntity-109"><a href="#RWLockerEntity-109"><span class="linenos">109</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-110"><a href="#RWLockerEntity-110"><span class="linenos">110</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-111"><a href="#RWLockerEntity-111"><span class="linenos">111</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-112"><a href="#RWLockerEntity-112"><span class="linenos">112</span></a>    
</span><span id="RWLockerEntity-113"><a href="#RWLockerEntity-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="nf">decrease_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RWLockerEntity-114"><a href="#RWLockerEntity-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity-115"><a href="#RWLockerEntity-115"><span class="linenos">115</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-116"><a href="#RWLockerEntity-116"><span class="linenos">116</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="RWLockerEntity-117"><a href="#RWLockerEntity-117"><span class="linenos">117</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLockerEntity-118"><a href="#RWLockerEntity-118"><span class="linenos">118</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-119"><a href="#RWLockerEntity-119"><span class="linenos">119</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-120"><a href="#RWLockerEntity-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-121"><a href="#RWLockerEntity-121"><span class="linenos">121</span></a>
</span><span id="RWLockerEntity-122"><a href="#RWLockerEntity-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity-123"><a href="#RWLockerEntity-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity-124"><a href="#RWLockerEntity-124"><span class="linenos">124</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span>
</span><span id="RWLockerEntity-125"><a href="#RWLockerEntity-125"><span class="linenos">125</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-126"><a href="#RWLockerEntity-126"><span class="linenos">126</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-127"><a href="#RWLockerEntity-127"><span class="linenos">127</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span>
</span><span id="RWLockerEntity-128"><a href="#RWLockerEntity-128"><span class="linenos">128</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-129"><a href="#RWLockerEntity-129"><span class="linenos">129</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-130"><a href="#RWLockerEntity-130"><span class="linenos">130</span></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span>
</span><span id="RWLockerEntity-131"><a href="#RWLockerEntity-131"><span class="linenos">131</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-132"><a href="#RWLockerEntity-132"><span class="linenos">132</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span>
</span><span id="RWLockerEntity-133"><a href="#RWLockerEntity-133"><span class="linenos">133</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-134"><a href="#RWLockerEntity-134"><span class="linenos">134</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-135"><a href="#RWLockerEntity-135"><span class="linenos">135</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span>
</span><span id="RWLockerEntity-136"><a href="#RWLockerEntity-136"><span class="linenos">136</span></a>    
</span><span id="RWLockerEntity-137"><a href="#RWLockerEntity-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">increase_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RWLockerEntity-138"><a href="#RWLockerEntity-138"><span class="linenos">138</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity-139"><a href="#RWLockerEntity-139"><span class="linenos">139</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span>
</span><span id="RWLockerEntity-140"><a href="#RWLockerEntity-140"><span class="linenos">140</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity-141"><a href="#RWLockerEntity-141"><span class="linenos">141</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-142"><a href="#RWLockerEntity-142"><span class="linenos">142</span></a>            
</span><span id="RWLockerEntity-143"><a href="#RWLockerEntity-143"><span class="linenos">143</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-144"><a href="#RWLockerEntity-144"><span class="linenos">144</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-145"><a href="#RWLockerEntity-145"><span class="linenos">145</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-146"><a href="#RWLockerEntity-146"><span class="linenos">146</span></a>    
</span><span id="RWLockerEntity-147"><a href="#RWLockerEntity-147"><span class="linenos">147</span></a>    <span class="k">def</span> <span class="nf">decrease_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RWLockerEntity-148"><a href="#RWLockerEntity-148"><span class="linenos">148</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity-149"><a href="#RWLockerEntity-149"><span class="linenos">149</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-150"><a href="#RWLockerEntity-150"><span class="linenos">150</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="RWLockerEntity-151"><a href="#RWLockerEntity-151"><span class="linenos">151</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLockerEntity-152"><a href="#RWLockerEntity-152"><span class="linenos">152</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-153"><a href="#RWLockerEntity-153"><span class="linenos">153</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-154"><a href="#RWLockerEntity-154"><span class="linenos">154</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity-155"><a href="#RWLockerEntity-155"><span class="linenos">155</span></a>
</span><span id="RWLockerEntity-156"><a href="#RWLockerEntity-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">try_write_lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">apply</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity-157"><a href="#RWLockerEntity-157"><span class="linenos">157</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RWLockerEntity-158"><a href="#RWLockerEntity-158"><span class="linenos">158</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span><span class="p">:</span>
</span><span id="RWLockerEntity-159"><a href="#RWLockerEntity-159"><span class="linenos">159</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span> <span class="ow">and</span> <span class="p">(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="RWLockerEntity-160"><a href="#RWLockerEntity-160"><span class="linenos">160</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="RWLockerEntity-161"><a href="#RWLockerEntity-161"><span class="linenos">161</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerEntity-162"><a href="#RWLockerEntity-162"><span class="linenos">162</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="RWLockerEntity-163"><a href="#RWLockerEntity-163"><span class="linenos">163</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-164"><a href="#RWLockerEntity-164"><span class="linenos">164</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-165"><a href="#RWLockerEntity-165"><span class="linenos">165</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-166"><a href="#RWLockerEntity-166"><span class="linenos">166</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="RWLockerEntity-167"><a href="#RWLockerEntity-167"><span class="linenos">167</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="RWLockerEntity-168"><a href="#RWLockerEntity-168"><span class="linenos">168</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerEntity-169"><a href="#RWLockerEntity-169"><span class="linenos">169</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="RWLockerEntity-170"><a href="#RWLockerEntity-170"><span class="linenos">170</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-171"><a href="#RWLockerEntity-171"><span class="linenos">171</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-172"><a href="#RWLockerEntity-172"><span class="linenos">172</span></a>        
</span><span id="RWLockerEntity-173"><a href="#RWLockerEntity-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span><span id="RWLockerEntity-174"><a href="#RWLockerEntity-174"><span class="linenos">174</span></a>
</span><span id="RWLockerEntity-175"><a href="#RWLockerEntity-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">try_read_lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">apply</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity-176"><a href="#RWLockerEntity-176"><span class="linenos">176</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RWLockerEntity-177"><a href="#RWLockerEntity-177"><span class="linenos">177</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span><span class="p">:</span>
</span><span id="RWLockerEntity-178"><a href="#RWLockerEntity-178"><span class="linenos">178</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span> <span class="ow">and</span> <span class="p">(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="RWLockerEntity-179"><a href="#RWLockerEntity-179"><span class="linenos">179</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="RWLockerEntity-180"><a href="#RWLockerEntity-180"><span class="linenos">180</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerEntity-181"><a href="#RWLockerEntity-181"><span class="linenos">181</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="RWLockerEntity-182"><a href="#RWLockerEntity-182"><span class="linenos">182</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-183"><a href="#RWLockerEntity-183"><span class="linenos">183</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-184"><a href="#RWLockerEntity-184"><span class="linenos">184</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-185"><a href="#RWLockerEntity-185"><span class="linenos">185</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="RWLockerEntity-186"><a href="#RWLockerEntity-186"><span class="linenos">186</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="RWLockerEntity-187"><a href="#RWLockerEntity-187"><span class="linenos">187</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerEntity-188"><a href="#RWLockerEntity-188"><span class="linenos">188</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="RWLockerEntity-189"><a href="#RWLockerEntity-189"><span class="linenos">189</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity-190"><a href="#RWLockerEntity-190"><span class="linenos">190</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLockerEntity-191"><a href="#RWLockerEntity-191"><span class="linenos">191</span></a>        
</span><span id="RWLockerEntity-192"><a href="#RWLockerEntity-192"><span class="linenos">192</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span><span id="RWLockerEntity-193"><a href="#RWLockerEntity-193"><span class="linenos">193</span></a>    
</span><span id="RWLockerEntity-194"><a href="#RWLockerEntity-194"><span class="linenos">194</span></a>    <span class="k">def</span> <span class="nf">test_remove</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity-195"><a href="#RWLockerEntity-195"><span class="linenos">195</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_coroutines</span>
</span><span id="RWLockerEntity-196"><a href="#RWLockerEntity-196"><span class="linenos">196</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span></pre></div>


    

                            <div id="RWLockerEntity.__init__" class="classattr">
                                        <input id="RWLockerEntity.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">RWLockerEntity</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span>,</span><span class="param">	<span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Service</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="RWLockerEntity.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.__init__-72"><a href="#RWLockerEntity.__init__-72"><span class="linenos">72</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">service</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Service</span><span class="p">]):</span>
</span><span id="RWLockerEntity.__init__-73"><a href="#RWLockerEntity.__init__-73"><span class="linenos">73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="RWLockerEntity.__init__-74"><a href="#RWLockerEntity.__init__-74"><span class="linenos">74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">recursive</span>
</span><span id="RWLockerEntity.__init__-75"><a href="#RWLockerEntity.__init__-75"><span class="linenos">75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">service</span> <span class="o">=</span> <span class="n">service</span>
</span><span id="RWLockerEntity.__init__-76"><a href="#RWLockerEntity.__init__-76"><span class="linenos">76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity.__init__-77"><a href="#RWLockerEntity.__init__-77"><span class="linenos">77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLockerEntity.__init__-78"><a href="#RWLockerEntity.__init__-78"><span class="linenos">78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity.__init__-79"><a href="#RWLockerEntity.__init__-79"><span class="linenos">79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_writers_in_progress</span>  <span class="c1"># Must be edited directly from coroutine. In order to eliminate new writers arrived during the end of the current loop iteration</span>
</span><span id="RWLockerEntity.__init__-80"><a href="#RWLockerEntity.__init__-80"><span class="linenos">80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity.__init__-81"><a href="#RWLockerEntity.__init__-81"><span class="linenos">81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLockerEntity.__init__-82"><a href="#RWLockerEntity.__init__-82"><span class="linenos">82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity.__init__-83"><a href="#RWLockerEntity.__init__-83"><span class="linenos">83</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_readers_in_progress</span>  <span class="c1"># Must be edited directly from coroutine. In order to eliminate new readers arrived during the end of the current loop iteration</span>
</span><span id="RWLockerEntity.__init__-84"><a href="#RWLockerEntity.__init__-84"><span class="linenos">84</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">:</span> <span class="n">RWOperation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>  <span class="c1"># Default is &#39;RWOperation.read&#39; in order to force &#39;write&#39; as a first operation among several first concurent operations</span>
</span><span id="RWLockerEntity.__init__-85"><a href="#RWLockerEntity.__init__-85"><span class="linenos">85</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLockerEntity.__init__-86"><a href="#RWLockerEntity.__init__-86"><span class="linenos">86</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">related_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.entity_id" class="classattr">
                                <div class="attr variable">
            <span class="name">entity_id</span><span class="annotation">: Hashable</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.entity_id"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.recursive" class="classattr">
                                <div class="attr variable">
            <span class="name">recursive</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.recursive"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.service" class="classattr">
                                <div class="attr variable">
            <span class="name">service</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.service"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.writers_pending" class="classattr">
                                <div class="attr variable">
            <span class="name">writers_pending</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.writers_pending"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.writers_in_progress_dict" class="classattr">
                                <div class="attr variable">
            <span class="name">writers_in_progress_dict</span><span class="annotation">: Dict[int, int]</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.writers_in_progress_dict"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.writers_in_progress" class="classattr">
                                <div class="attr variable">
            <span class="name">writers_in_progress</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.writers_in_progress"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.max_writers_in_progress" class="classattr">
                                <div class="attr variable">
            <span class="name">max_writers_in_progress</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.max_writers_in_progress"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.readers_pending" class="classattr">
                                <div class="attr variable">
            <span class="name">readers_pending</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.readers_pending"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.readers_in_progress_dict" class="classattr">
                                <div class="attr variable">
            <span class="name">readers_in_progress_dict</span><span class="annotation">: Dict[int, int]</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.readers_in_progress_dict"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.readers_in_progress" class="classattr">
                                <div class="attr variable">
            <span class="name">readers_in_progress</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.readers_in_progress"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.max_readers_in_progress" class="classattr">
                                <div class="attr variable">
            <span class="name">max_readers_in_progress</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.max_readers_in_progress"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.last_operation" class="classattr">
                                <div class="attr variable">
            <span class="name">last_operation</span><span class="annotation">: <a href="#RWOperation">RWOperation</a></span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.last_operation"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.waiting_coroutines" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_coroutines</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.waiting_coroutines"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.related_coroutines" class="classattr">
                                <div class="attr variable">
            <span class="name">related_coroutines</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#RWLockerEntity.related_coroutines"></a>
    
    

                            </div>
                            <div id="RWLockerEntity.check_writers_in_progress_boundaries" class="classattr">
                                        <input id="RWLockerEntity.check_writers_in_progress_boundaries-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_writers_in_progress_boundaries</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="RWLockerEntity.check_writers_in_progress_boundaries-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.check_writers_in_progress_boundaries"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.check_writers_in_progress_boundaries-88"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-88"><span class="linenos"> 88</span></a>    <span class="k">def</span> <span class="nf">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-89"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-89"><span class="linenos"> 89</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-90"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-90"><span class="linenos"> 90</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-91"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-91"><span class="linenos"> 91</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-92"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-92"><span class="linenos"> 92</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-93"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-93"><span class="linenos"> 93</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-94"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-94"><span class="linenos"> 94</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-95"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-95"><span class="linenos"> 95</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-96"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-96"><span class="linenos"> 96</span></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-97"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-97"><span class="linenos"> 97</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-98"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-98"><span class="linenos"> 98</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-99"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-99"><span class="linenos"> 99</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-100"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-100"><span class="linenos">100</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_writers_in_progress_boundaries-101"><a href="#RWLockerEntity.check_writers_in_progress_boundaries-101"><span class="linenos">101</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.increase_writers_in_progress" class="classattr">
                                        <input id="RWLockerEntity.increase_writers_in_progress-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">increase_writers_in_progress</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RWLockerEntity.increase_writers_in_progress-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.increase_writers_in_progress"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.increase_writers_in_progress-103"><a href="#RWLockerEntity.increase_writers_in_progress-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">increase_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RWLockerEntity.increase_writers_in_progress-104"><a href="#RWLockerEntity.increase_writers_in_progress-104"><span class="linenos">104</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity.increase_writers_in_progress-105"><a href="#RWLockerEntity.increase_writers_in_progress-105"><span class="linenos">105</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">:</span>
</span><span id="RWLockerEntity.increase_writers_in_progress-106"><a href="#RWLockerEntity.increase_writers_in_progress-106"><span class="linenos">106</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity.increase_writers_in_progress-107"><a href="#RWLockerEntity.increase_writers_in_progress-107"><span class="linenos">107</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity.increase_writers_in_progress-108"><a href="#RWLockerEntity.increase_writers_in_progress-108"><span class="linenos">108</span></a>            
</span><span id="RWLockerEntity.increase_writers_in_progress-109"><a href="#RWLockerEntity.increase_writers_in_progress-109"><span class="linenos">109</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity.increase_writers_in_progress-110"><a href="#RWLockerEntity.increase_writers_in_progress-110"><span class="linenos">110</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.increase_writers_in_progress-111"><a href="#RWLockerEntity.increase_writers_in_progress-111"><span class="linenos">111</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.decrease_writers_in_progress" class="classattr">
                                        <input id="RWLockerEntity.decrease_writers_in_progress-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">decrease_writers_in_progress</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RWLockerEntity.decrease_writers_in_progress-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.decrease_writers_in_progress"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.decrease_writers_in_progress-113"><a href="#RWLockerEntity.decrease_writers_in_progress-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="nf">decrease_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RWLockerEntity.decrease_writers_in_progress-114"><a href="#RWLockerEntity.decrease_writers_in_progress-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity.decrease_writers_in_progress-115"><a href="#RWLockerEntity.decrease_writers_in_progress-115"><span class="linenos">115</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity.decrease_writers_in_progress-116"><a href="#RWLockerEntity.decrease_writers_in_progress-116"><span class="linenos">116</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="RWLockerEntity.decrease_writers_in_progress-117"><a href="#RWLockerEntity.decrease_writers_in_progress-117"><span class="linenos">117</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLockerEntity.decrease_writers_in_progress-118"><a href="#RWLockerEntity.decrease_writers_in_progress-118"><span class="linenos">118</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity.decrease_writers_in_progress-119"><a href="#RWLockerEntity.decrease_writers_in_progress-119"><span class="linenos">119</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.decrease_writers_in_progress-120"><a href="#RWLockerEntity.decrease_writers_in_progress-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.check_readers_in_progress_boundaries" class="classattr">
                                        <input id="RWLockerEntity.check_readers_in_progress_boundaries-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_readers_in_progress_boundaries</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="RWLockerEntity.check_readers_in_progress_boundaries-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.check_readers_in_progress_boundaries"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.check_readers_in_progress_boundaries-122"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-123"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-124"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-124"><span class="linenos">124</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-125"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-125"><span class="linenos">125</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-126"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-126"><span class="linenos">126</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-127"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-127"><span class="linenos">127</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-128"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-128"><span class="linenos">128</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-129"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-129"><span class="linenos">129</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-130"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-130"><span class="linenos">130</span></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-131"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-131"><span class="linenos">131</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-132"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-132"><span class="linenos">132</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-133"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-133"><span class="linenos">133</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-134"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-134"><span class="linenos">134</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.check_readers_in_progress_boundaries-135"><a href="#RWLockerEntity.check_readers_in_progress_boundaries-135"><span class="linenos">135</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.increase_readers_in_progress" class="classattr">
                                        <input id="RWLockerEntity.increase_readers_in_progress-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">increase_readers_in_progress</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RWLockerEntity.increase_readers_in_progress-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.increase_readers_in_progress"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.increase_readers_in_progress-137"><a href="#RWLockerEntity.increase_readers_in_progress-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">increase_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RWLockerEntity.increase_readers_in_progress-138"><a href="#RWLockerEntity.increase_readers_in_progress-138"><span class="linenos">138</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity.increase_readers_in_progress-139"><a href="#RWLockerEntity.increase_readers_in_progress-139"><span class="linenos">139</span></a>            <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">:</span>
</span><span id="RWLockerEntity.increase_readers_in_progress-140"><a href="#RWLockerEntity.increase_readers_in_progress-140"><span class="linenos">140</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RWLockerEntity.increase_readers_in_progress-141"><a href="#RWLockerEntity.increase_readers_in_progress-141"><span class="linenos">141</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity.increase_readers_in_progress-142"><a href="#RWLockerEntity.increase_readers_in_progress-142"><span class="linenos">142</span></a>            
</span><span id="RWLockerEntity.increase_readers_in_progress-143"><a href="#RWLockerEntity.increase_readers_in_progress-143"><span class="linenos">143</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity.increase_readers_in_progress-144"><a href="#RWLockerEntity.increase_readers_in_progress-144"><span class="linenos">144</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.increase_readers_in_progress-145"><a href="#RWLockerEntity.increase_readers_in_progress-145"><span class="linenos">145</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">+=</span> <span class="mi">1</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.decrease_readers_in_progress" class="classattr">
                                        <input id="RWLockerEntity.decrease_readers_in_progress-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">decrease_readers_in_progress</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RWLockerEntity.decrease_readers_in_progress-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.decrease_readers_in_progress"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.decrease_readers_in_progress-147"><a href="#RWLockerEntity.decrease_readers_in_progress-147"><span class="linenos">147</span></a>    <span class="k">def</span> <span class="nf">decrease_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="RWLockerEntity.decrease_readers_in_progress-148"><a href="#RWLockerEntity.decrease_readers_in_progress-148"><span class="linenos">148</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive</span><span class="p">:</span>
</span><span id="RWLockerEntity.decrease_readers_in_progress-149"><a href="#RWLockerEntity.decrease_readers_in_progress-149"><span class="linenos">149</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity.decrease_readers_in_progress-150"><a href="#RWLockerEntity.decrease_readers_in_progress-150"><span class="linenos">150</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]:</span>
</span><span id="RWLockerEntity.decrease_readers_in_progress-151"><a href="#RWLockerEntity.decrease_readers_in_progress-151"><span class="linenos">151</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress_dict</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLockerEntity.decrease_readers_in_progress-152"><a href="#RWLockerEntity.decrease_readers_in_progress-152"><span class="linenos">152</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLockerEntity.decrease_readers_in_progress-153"><a href="#RWLockerEntity.decrease_readers_in_progress-153"><span class="linenos">153</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.decrease_readers_in_progress-154"><a href="#RWLockerEntity.decrease_readers_in_progress-154"><span class="linenos">154</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="o">-=</span> <span class="mi">1</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.try_write_lock" class="classattr">
                                        <input id="RWLockerEntity.try_write_lock-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">try_write_lock</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>, </span><span class="param"><span class="n">apply</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="RWLockerEntity.try_write_lock-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.try_write_lock"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.try_write_lock-156"><a href="#RWLockerEntity.try_write_lock-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">try_write_lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">apply</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_write_lock-157"><a href="#RWLockerEntity.try_write_lock-157"><span class="linenos">157</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RWLockerEntity.try_write_lock-158"><a href="#RWLockerEntity.try_write_lock-158"><span class="linenos">158</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_write_lock-159"><a href="#RWLockerEntity.try_write_lock-159"><span class="linenos">159</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_in_progress</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">readers_pending</span> <span class="ow">and</span> <span class="p">(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="RWLockerEntity.try_write_lock-160"><a href="#RWLockerEntity.try_write_lock-160"><span class="linenos">160</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_write_lock-161"><a href="#RWLockerEntity.try_write_lock-161"><span class="linenos">161</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerEntity.try_write_lock-162"><a href="#RWLockerEntity.try_write_lock-162"><span class="linenos">162</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="RWLockerEntity.try_write_lock-163"><a href="#RWLockerEntity.try_write_lock-163"><span class="linenos">163</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_write_lock-164"><a href="#RWLockerEntity.try_write_lock-164"><span class="linenos">164</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.try_write_lock-165"><a href="#RWLockerEntity.try_write_lock-165"><span class="linenos">165</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_write_lock-166"><a href="#RWLockerEntity.try_write_lock-166"><span class="linenos">166</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_writers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="RWLockerEntity.try_write_lock-167"><a href="#RWLockerEntity.try_write_lock-167"><span class="linenos">167</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_write_lock-168"><a href="#RWLockerEntity.try_write_lock-168"><span class="linenos">168</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerEntity.try_write_lock-169"><a href="#RWLockerEntity.try_write_lock-169"><span class="linenos">169</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="RWLockerEntity.try_write_lock-170"><a href="#RWLockerEntity.try_write_lock-170"><span class="linenos">170</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_write_lock-171"><a href="#RWLockerEntity.try_write_lock-171"><span class="linenos">171</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.try_write_lock-172"><a href="#RWLockerEntity.try_write_lock-172"><span class="linenos">172</span></a>        
</span><span id="RWLockerEntity.try_write_lock-173"><a href="#RWLockerEntity.try_write_lock-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.try_read_lock" class="classattr">
                                        <input id="RWLockerEntity.try_read_lock-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">try_read_lock</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">coro_id</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>, </span><span class="param"><span class="n">apply</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="RWLockerEntity.try_read_lock-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.try_read_lock"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.try_read_lock-175"><a href="#RWLockerEntity.try_read_lock-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">try_read_lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">apply</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_read_lock-176"><a href="#RWLockerEntity.try_read_lock-176"><span class="linenos">176</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RWLockerEntity.try_read_lock-177"><a href="#RWLockerEntity.try_read_lock-177"><span class="linenos">177</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_read_lock-178"><a href="#RWLockerEntity.try_read_lock-178"><span class="linenos">178</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_in_progress</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">writers_pending</span> <span class="ow">and</span> <span class="p">(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="RWLockerEntity.try_read_lock-179"><a href="#RWLockerEntity.try_read_lock-179"><span class="linenos">179</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_read_lock-180"><a href="#RWLockerEntity.try_read_lock-180"><span class="linenos">180</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerEntity.try_read_lock-181"><a href="#RWLockerEntity.try_read_lock-181"><span class="linenos">181</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="RWLockerEntity.try_read_lock-182"><a href="#RWLockerEntity.try_read_lock-182"><span class="linenos">182</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_read_lock-183"><a href="#RWLockerEntity.try_read_lock-183"><span class="linenos">183</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.try_read_lock-184"><a href="#RWLockerEntity.try_read_lock-184"><span class="linenos">184</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_read_lock-185"><a href="#RWLockerEntity.try_read_lock-185"><span class="linenos">185</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_readers_in_progress_boundaries</span><span class="p">(</span><span class="n">coro_id</span><span class="p">):</span>
</span><span id="RWLockerEntity.try_read_lock-186"><a href="#RWLockerEntity.try_read_lock-186"><span class="linenos">186</span></a>                <span class="k">if</span> <span class="n">apply</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_read_lock-187"><a href="#RWLockerEntity.try_read_lock-187"><span class="linenos">187</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerEntity.try_read_lock-188"><a href="#RWLockerEntity.try_read_lock-188"><span class="linenos">188</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="RWLockerEntity.try_read_lock-189"><a href="#RWLockerEntity.try_read_lock-189"><span class="linenos">189</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerEntity.try_read_lock-190"><a href="#RWLockerEntity.try_read_lock-190"><span class="linenos">190</span></a>                <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLockerEntity.try_read_lock-191"><a href="#RWLockerEntity.try_read_lock-191"><span class="linenos">191</span></a>        
</span><span id="RWLockerEntity.try_read_lock-192"><a href="#RWLockerEntity.try_read_lock-192"><span class="linenos">192</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLockerEntity.test_remove" class="classattr">
                                        <input id="RWLockerEntity.test_remove-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">test_remove</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="RWLockerEntity.test_remove-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerEntity.test_remove"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerEntity.test_remove-194"><a href="#RWLockerEntity.test_remove-194"><span class="linenos">194</span></a>    <span class="k">def</span> <span class="nf">test_remove</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLockerEntity.test_remove-195"><a href="#RWLockerEntity.test_remove-195"><span class="linenos">195</span></a>        <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_coroutines</span>
</span><span id="RWLockerEntity.test_remove-196"><a href="#RWLockerEntity.test_remove-196"><span class="linenos">196</span></a>        <span class="k">return</span> <span class="n">need_to_try_later</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="RWLockerContextManager">
                            <input id="RWLockerContextManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">RWLockerContextManager</span><wbr>(<span class="base"><a href="#RWLockerContextManagerBase">RWLockerContextManagerBase</a></span>):

                <label class="view-source-button" for="RWLockerContextManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerContextManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerContextManager-227"><a href="#RWLockerContextManager-227"><span class="linenos">227</span></a><span class="k">class</span> <span class="nc">RWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerContextManagerBase</span><span class="p">):</span>
</span><span id="RWLockerContextManager-228"><a href="#RWLockerContextManager-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">core</span><span class="p">:</span> <span class="n">RWLockerEntity</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="RWLockerContextManager-229"><a href="#RWLockerContextManager-229"><span class="linenos">229</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">core</span><span class="p">)</span>
</span><span id="RWLockerContextManager-230"><a href="#RWLockerContextManager-230"><span class="linenos">230</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="RWLockerContextManager-231"><a href="#RWLockerContextManager-231"><span class="linenos">231</span></a>    
</span><span id="RWLockerContextManager-232"><a href="#RWLockerContextManager-232"><span class="linenos">232</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RWLockerContextManager-233"><a href="#RWLockerContextManager-233"><span class="linenos">233</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RWLockerContextManager-234"><a href="#RWLockerContextManager-234"><span class="linenos">234</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="RWLockerContextManager-235"><a href="#RWLockerContextManager-235"><span class="linenos">235</span></a>        
</span><span id="RWLockerContextManager-236"><a href="#RWLockerContextManager-236"><span class="linenos">236</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="RWLockerContextManager-237"><a href="#RWLockerContextManager-237"><span class="linenos">237</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_write_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerContextManager-238"><a href="#RWLockerContextManager-238"><span class="linenos">238</span></a>            <span class="k">if</span> <span class="n">need_service_assistance</span><span class="p">:</span>
</span><span id="RWLockerContextManager-239"><a href="#RWLockerContextManager-239"><span class="linenos">239</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">writers_pending</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerContextManager-240"><a href="#RWLockerContextManager-240"><span class="linenos">240</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span>
</span><span id="RWLockerContextManager-241"><a href="#RWLockerContextManager-241"><span class="linenos">241</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerContextManager-242"><a href="#RWLockerContextManager-242"><span class="linenos">242</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_read_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerContextManager-243"><a href="#RWLockerContextManager-243"><span class="linenos">243</span></a>            <span class="k">if</span> <span class="n">need_service_assistance</span><span class="p">:</span>
</span><span id="RWLockerContextManager-244"><a href="#RWLockerContextManager-244"><span class="linenos">244</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">readers_pending</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerContextManager-245"><a href="#RWLockerContextManager-245"><span class="linenos">245</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span>
</span><span id="RWLockerContextManager-246"><a href="#RWLockerContextManager-246"><span class="linenos">246</span></a>        
</span><span id="RWLockerContextManager-247"><a href="#RWLockerContextManager-247"><span class="linenos">247</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="RWLockerContextManager-248"><a href="#RWLockerContextManager-248"><span class="linenos">248</span></a>    
</span><span id="RWLockerContextManager-249"><a href="#RWLockerContextManager-249"><span class="linenos">249</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="RWLockerContextManager-250"><a href="#RWLockerContextManager-250"><span class="linenos">250</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="RWLockerContextManager-251"><a href="#RWLockerContextManager-251"><span class="linenos">251</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">)</span>
</span><span id="RWLockerContextManager-252"><a href="#RWLockerContextManager-252"><span class="linenos">252</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerContextManager-253"><a href="#RWLockerContextManager-253"><span class="linenos">253</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">)</span>
</span><span id="RWLockerContextManager-254"><a href="#RWLockerContextManager-254"><span class="linenos">254</span></a>        
</span><span id="RWLockerContextManager-255"><a href="#RWLockerContextManager-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="RWLockerContextManager-256"><a href="#RWLockerContextManager-256"><span class="linenos">256</span></a>
</span><span id="RWLockerContextManager-257"><a href="#RWLockerContextManager-257"><span class="linenos">257</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RWLockerContextManager-258"><a href="#RWLockerContextManager-258"><span class="linenos">258</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RWLockerContextManager-259"><a href="#RWLockerContextManager-259"><span class="linenos">259</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="RWLockerContextManager-260"><a href="#RWLockerContextManager-260"><span class="linenos">260</span></a>        
</span><span id="RWLockerContextManager-261"><a href="#RWLockerContextManager-261"><span class="linenos">261</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="RWLockerContextManager-262"><a href="#RWLockerContextManager-262"><span class="linenos">262</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_write_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerContextManager-263"><a href="#RWLockerContextManager-263"><span class="linenos">263</span></a>            <span class="k">if</span> <span class="n">need_service_assistance</span><span class="p">:</span>
</span><span id="RWLockerContextManager-264"><a href="#RWLockerContextManager-264"><span class="linenos">264</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">writers_pending</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerContextManager-265"><a href="#RWLockerContextManager-265"><span class="linenos">265</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span>
</span><span id="RWLockerContextManager-266"><a href="#RWLockerContextManager-266"><span class="linenos">266</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerContextManager-267"><a href="#RWLockerContextManager-267"><span class="linenos">267</span></a>            <span class="n">need_service_assistance</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">try_read_lock</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="o">.</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLockerContextManager-268"><a href="#RWLockerContextManager-268"><span class="linenos">268</span></a>            <span class="k">if</span> <span class="n">need_service_assistance</span><span class="p">:</span>
</span><span id="RWLockerContextManager-269"><a href="#RWLockerContextManager-269"><span class="linenos">269</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">readers_pending</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="RWLockerContextManager-270"><a href="#RWLockerContextManager-270"><span class="linenos">270</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">service</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span>        
</span><span id="RWLockerContextManager-271"><a href="#RWLockerContextManager-271"><span class="linenos">271</span></a>        
</span><span id="RWLockerContextManager-272"><a href="#RWLockerContextManager-272"><span class="linenos">272</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="RWLockerContextManager-273"><a href="#RWLockerContextManager-273"><span class="linenos">273</span></a>
</span><span id="RWLockerContextManager-274"><a href="#RWLockerContextManager-274"><span class="linenos">274</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="RWLockerContextManager-275"><a href="#RWLockerContextManager-275"><span class="linenos">275</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="RWLockerContextManager-276"><a href="#RWLockerContextManager-276"><span class="linenos">276</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_writers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">)</span>
</span><span id="RWLockerContextManager-277"><a href="#RWLockerContextManager-277"><span class="linenos">277</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLockerContextManager-278"><a href="#RWLockerContextManager-278"><span class="linenos">278</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_readers_in_progress</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_interface</span><span class="p">)</span>
</span><span id="RWLockerContextManager-279"><a href="#RWLockerContextManager-279"><span class="linenos">279</span></a>        
</span><span id="RWLockerContextManager-280"><a href="#RWLockerContextManager-280"><span class="linenos">280</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            <div id="RWLockerContextManager.__init__" class="classattr">
                                        <input id="RWLockerContextManager.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">RWLockerContextManager</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">core</span><span class="p">:</span> <span class="n"><a href="#RWLockerEntity">RWLockerEntity</a></span>,</span><span class="param">	<span class="n">interface</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span></span>)</span>

                <label class="view-source-button" for="RWLockerContextManager.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLockerContextManager.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLockerContextManager.__init__-228"><a href="#RWLockerContextManager.__init__-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">core</span><span class="p">:</span> <span class="n">RWLockerEntity</span><span class="p">,</span> <span class="n">interface</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="RWLockerContextManager.__init__-229"><a href="#RWLockerContextManager.__init__-229"><span class="linenos">229</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">core</span><span class="p">)</span>
</span><span id="RWLockerContextManager.__init__-230"><a href="#RWLockerContextManager.__init__-230"><span class="linenos">230</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_interface</span> <span class="o">=</span> <span class="n">interface</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#RWLockerContextManagerBase">RWLockerContextManagerBase</a></dt>
                                <dd id="RWLockerContextManager.core" class="variable"><a href="#RWLockerContextManagerBase.core">core</a></dd>
                <dd id="RWLockerContextManager.current_context_operation" class="variable"><a href="#RWLockerContextManagerBase.current_context_operation">current_context_operation</a></dd>
                <dd id="RWLockerContextManager.lockable" class="function"><a href="#RWLockerContextManagerBase.lockable">lockable</a></dd>
                <dd id="RWLockerContextManager.change_max_boundaries" class="function"><a href="#RWLockerContextManagerBase.change_max_boundaries">change_max_boundaries</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="FakeRWLockerContextManager">
                            <input id="FakeRWLockerContextManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">FakeRWLockerContextManager</span><wbr>(<span class="base"><a href="#RWLockerContextManagerBase">RWLockerContextManagerBase</a></span>):

                <label class="view-source-button" for="FakeRWLockerContextManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FakeRWLockerContextManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FakeRWLockerContextManager-283"><a href="#FakeRWLockerContextManager-283"><span class="linenos">283</span></a><span class="k">class</span> <span class="nc">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerContextManagerBase</span><span class="p">):</span>
</span><span id="FakeRWLockerContextManager-284"><a href="#FakeRWLockerContextManager-284"><span class="linenos">284</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">core</span><span class="p">:</span> <span class="n">RWLockerEntity</span><span class="p">):</span>
</span><span id="FakeRWLockerContextManager-285"><a href="#FakeRWLockerContextManager-285"><span class="linenos">285</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">core</span><span class="p">)</span>
</span><span id="FakeRWLockerContextManager-286"><a href="#FakeRWLockerContextManager-286"><span class="linenos">286</span></a>    
</span><span id="FakeRWLockerContextManager-287"><a href="#FakeRWLockerContextManager-287"><span class="linenos">287</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FakeRWLockerContextManager-288"><a href="#FakeRWLockerContextManager-288"><span class="linenos">288</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-289"><a href="#FakeRWLockerContextManager-289"><span class="linenos">289</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="FakeRWLockerContextManager-290"><a href="#FakeRWLockerContextManager-290"><span class="linenos">290</span></a>        
</span><span id="FakeRWLockerContextManager-291"><a href="#FakeRWLockerContextManager-291"><span class="linenos">291</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-292"><a href="#FakeRWLockerContextManager-292"><span class="linenos">292</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">()</span>
</span><span id="FakeRWLockerContextManager-293"><a href="#FakeRWLockerContextManager-293"><span class="linenos">293</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="FakeRWLockerContextManager-294"><a href="#FakeRWLockerContextManager-294"><span class="linenos">294</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-295"><a href="#FakeRWLockerContextManager-295"><span class="linenos">295</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">()</span>
</span><span id="FakeRWLockerContextManager-296"><a href="#FakeRWLockerContextManager-296"><span class="linenos">296</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="FakeRWLockerContextManager-297"><a href="#FakeRWLockerContextManager-297"><span class="linenos">297</span></a>        
</span><span id="FakeRWLockerContextManager-298"><a href="#FakeRWLockerContextManager-298"><span class="linenos">298</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="FakeRWLockerContextManager-299"><a href="#FakeRWLockerContextManager-299"><span class="linenos">299</span></a>    
</span><span id="FakeRWLockerContextManager-300"><a href="#FakeRWLockerContextManager-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="FakeRWLockerContextManager-301"><a href="#FakeRWLockerContextManager-301"><span class="linenos">301</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-302"><a href="#FakeRWLockerContextManager-302"><span class="linenos">302</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_writers_in_progress</span><span class="p">()</span>
</span><span id="FakeRWLockerContextManager-303"><a href="#FakeRWLockerContextManager-303"><span class="linenos">303</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-304"><a href="#FakeRWLockerContextManager-304"><span class="linenos">304</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_readers_in_progress</span><span class="p">()</span>
</span><span id="FakeRWLockerContextManager-305"><a href="#FakeRWLockerContextManager-305"><span class="linenos">305</span></a>        
</span><span id="FakeRWLockerContextManager-306"><a href="#FakeRWLockerContextManager-306"><span class="linenos">306</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="FakeRWLockerContextManager-307"><a href="#FakeRWLockerContextManager-307"><span class="linenos">307</span></a>
</span><span id="FakeRWLockerContextManager-308"><a href="#FakeRWLockerContextManager-308"><span class="linenos">308</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FakeRWLockerContextManager-309"><a href="#FakeRWLockerContextManager-309"><span class="linenos">309</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-310"><a href="#FakeRWLockerContextManager-310"><span class="linenos">310</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="FakeRWLockerContextManager-311"><a href="#FakeRWLockerContextManager-311"><span class="linenos">311</span></a>        
</span><span id="FakeRWLockerContextManager-312"><a href="#FakeRWLockerContextManager-312"><span class="linenos">312</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-313"><a href="#FakeRWLockerContextManager-313"><span class="linenos">313</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">increase_writers_in_progress</span><span class="p">()</span>
</span><span id="FakeRWLockerContextManager-314"><a href="#FakeRWLockerContextManager-314"><span class="linenos">314</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span>
</span><span id="FakeRWLockerContextManager-315"><a href="#FakeRWLockerContextManager-315"><span class="linenos">315</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-316"><a href="#FakeRWLockerContextManager-316"><span class="linenos">316</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">increase_readers_in_progress</span><span class="p">()</span>
</span><span id="FakeRWLockerContextManager-317"><a href="#FakeRWLockerContextManager-317"><span class="linenos">317</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">last_operation</span> <span class="o">=</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span>
</span><span id="FakeRWLockerContextManager-318"><a href="#FakeRWLockerContextManager-318"><span class="linenos">318</span></a>        
</span><span id="FakeRWLockerContextManager-319"><a href="#FakeRWLockerContextManager-319"><span class="linenos">319</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="FakeRWLockerContextManager-320"><a href="#FakeRWLockerContextManager-320"><span class="linenos">320</span></a>
</span><span id="FakeRWLockerContextManager-321"><a href="#FakeRWLockerContextManager-321"><span class="linenos">321</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
</span><span id="FakeRWLockerContextManager-322"><a href="#FakeRWLockerContextManager-322"><span class="linenos">322</span></a>        <span class="k">if</span> <span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-323"><a href="#FakeRWLockerContextManager-323"><span class="linenos">323</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_writers_in_progress</span><span class="p">()</span>
</span><span id="FakeRWLockerContextManager-324"><a href="#FakeRWLockerContextManager-324"><span class="linenos">324</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="FakeRWLockerContextManager-325"><a href="#FakeRWLockerContextManager-325"><span class="linenos">325</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">decrease_readers_in_progress</span><span class="p">()</span>
</span><span id="FakeRWLockerContextManager-326"><a href="#FakeRWLockerContextManager-326"><span class="linenos">326</span></a>        
</span><span id="FakeRWLockerContextManager-327"><a href="#FakeRWLockerContextManager-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_context_operation</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            <div id="FakeRWLockerContextManager.__init__" class="classattr">
                                        <input id="FakeRWLockerContextManager.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">FakeRWLockerContextManager</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">core</span><span class="p">:</span> <span class="n"><a href="#RWLockerEntity">RWLockerEntity</a></span></span>)</span>

                <label class="view-source-button" for="FakeRWLockerContextManager.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FakeRWLockerContextManager.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FakeRWLockerContextManager.__init__-284"><a href="#FakeRWLockerContextManager.__init__-284"><span class="linenos">284</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">core</span><span class="p">:</span> <span class="n">RWLockerEntity</span><span class="p">):</span>
</span><span id="FakeRWLockerContextManager.__init__-285"><a href="#FakeRWLockerContextManager.__init__-285"><span class="linenos">285</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">core</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#RWLockerContextManagerBase">RWLockerContextManagerBase</a></dt>
                                <dd id="FakeRWLockerContextManager.core" class="variable"><a href="#RWLockerContextManagerBase.core">core</a></dd>
                <dd id="FakeRWLockerContextManager.current_context_operation" class="variable"><a href="#RWLockerContextManagerBase.current_context_operation">current_context_operation</a></dd>
                <dd id="FakeRWLockerContextManager.lockable" class="function"><a href="#RWLockerContextManagerBase.lockable">lockable</a></dd>
                <dd id="FakeRWLockerContextManager.change_max_boundaries" class="function"><a href="#RWLockerContextManagerBase.change_max_boundaries">change_max_boundaries</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="UnknownLockerEntity">
                            <input id="UnknownLockerEntity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UnknownLockerEntity</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="UnknownLockerEntity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UnknownLockerEntity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UnknownLockerEntity-330"><a href="#UnknownLockerEntity-330"><span class="linenos">330</span></a><span class="k">class</span> <span class="nc">UnknownLockerEntity</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="UnknownLockerEntity-331"><a href="#UnknownLockerEntity-331"><span class="linenos">331</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="UnknownLockerEntity.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="UnknownLockerEntity.with_traceback" class="function">with_traceback</dd>
                <dd id="UnknownLockerEntity.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="RWLocker">
                            <input id="RWLocker-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">RWLocker</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</span>, <span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</span>):

                <label class="view-source-button" for="RWLocker-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLocker"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLocker-334"><a href="#RWLocker-334"><span class="linenos">334</span></a><span class="k">class</span> <span class="nc">RWLocker</span><span class="p">(</span><span class="n">Service</span><span class="p">,</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="RWLocker-335"><a href="#RWLocker-335"><span class="linenos">335</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="RWLocker-336"><a href="#RWLocker-336"><span class="linenos">336</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="RWLocker-337"><a href="#RWLocker-337"><span class="linenos">337</span></a>
</span><span id="RWLocker-338"><a href="#RWLocker-338"><span class="linenos">338</span></a>        <span class="c1"># loop.add_global_on_coro_del_handler(self._on_coro_del_handler_global)  # Todo: switch to local coro del handler</span>
</span><span id="RWLocker-339"><a href="#RWLocker-339"><span class="linenos">339</span></a>
</span><span id="RWLocker-340"><a href="#RWLocker-340"><span class="linenos">340</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="RWLocker-341"><a href="#RWLocker-341"><span class="linenos">341</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register</span><span class="p">,</span>
</span><span id="RWLocker-342"><a href="#RWLocker-342"><span class="linenos">342</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_deregister</span><span class="p">,</span>
</span><span id="RWLocker-343"><a href="#RWLocker-343"><span class="linenos">343</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_write</span><span class="p">,</span>
</span><span id="RWLocker-344"><a href="#RWLocker-344"><span class="linenos">344</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_read</span><span class="p">,</span>
</span><span id="RWLocker-345"><a href="#RWLocker-345"><span class="linenos">345</span></a>        <span class="p">}</span>
</span><span id="RWLocker-346"><a href="#RWLocker-346"><span class="linenos">346</span></a>        
</span><span id="RWLocker-347"><a href="#RWLocker-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">RWLockerEntity</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker-348"><a href="#RWLocker-348"><span class="linenos">348</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker-349"><a href="#RWLocker-349"><span class="linenos">349</span></a>        
</span><span id="RWLocker-350"><a href="#RWLocker-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker-351"><a href="#RWLocker-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker-352"><a href="#RWLocker-352"><span class="linenos">352</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker-353"><a href="#RWLocker-353"><span class="linenos">353</span></a>
</span><span id="RWLocker-354"><a href="#RWLocker-354"><span class="linenos">354</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="RWLocker-355"><a href="#RWLocker-355"><span class="linenos">355</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="RWLocker-356"><a href="#RWLocker-356"><span class="linenos">356</span></a>            <span class="s1">&#39;locker entities num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">),</span>
</span><span id="RWLocker-357"><a href="#RWLocker-357"><span class="linenos">357</span></a>            <span class="s1">&#39;affected coroutines num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">),</span>
</span><span id="RWLocker-358"><a href="#RWLocker-358"><span class="linenos">358</span></a>            <span class="s1">&#39;waiting for write requests num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">),</span>
</span><span id="RWLocker-359"><a href="#RWLocker-359"><span class="linenos">359</span></a>            <span class="s1">&#39;waiting_for_read_requests num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">),</span>
</span><span id="RWLocker-360"><a href="#RWLocker-360"><span class="linenos">360</span></a>        <span class="p">}</span>
</span><span id="RWLocker-361"><a href="#RWLocker-361"><span class="linenos">361</span></a>
</span><span id="RWLocker-362"><a href="#RWLocker-362"><span class="linenos">362</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RWLockerRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="RWLocker-363"><a href="#RWLocker-363"><span class="linenos">363</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="RWLocker-364"><a href="#RWLocker-364"><span class="linenos">364</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RWLocker-365"><a href="#RWLocker-365"><span class="linenos">365</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="RWLocker-366"><a href="#RWLocker-366"><span class="linenos">366</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="RWLocker-367"><a href="#RWLocker-367"><span class="linenos">367</span></a>
</span><span id="RWLocker-368"><a href="#RWLocker-368"><span class="linenos">368</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RWLocker-369"><a href="#RWLocker-369"><span class="linenos">369</span></a>        <span class="c1"># entities_waiting_for_remove</span>
</span><span id="RWLocker-370"><a href="#RWLocker-370"><span class="linenos">370</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLocker-371"><a href="#RWLocker-371"><span class="linenos">371</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="RWLocker-372"><a href="#RWLocker-372"><span class="linenos">372</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker-373"><a href="#RWLocker-373"><span class="linenos">373</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="RWLocker-374"><a href="#RWLocker-374"><span class="linenos">374</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-375"><a href="#RWLocker-375"><span class="linenos">375</span></a>                <span class="k">continue</span>
</span><span id="RWLocker-376"><a href="#RWLocker-376"><span class="linenos">376</span></a>            
</span><span id="RWLocker-377"><a href="#RWLocker-377"><span class="linenos">377</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-378"><a href="#RWLocker-378"><span class="linenos">378</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">test_remove</span><span class="p">()</span>
</span><span id="RWLocker-379"><a href="#RWLocker-379"><span class="linenos">379</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="RWLocker-380"><a href="#RWLocker-380"><span class="linenos">380</span></a>                <span class="k">continue</span>
</span><span id="RWLocker-381"><a href="#RWLocker-381"><span class="linenos">381</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLocker-382"><a href="#RWLocker-382"><span class="linenos">382</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-383"><a href="#RWLocker-383"><span class="linenos">383</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-384"><a href="#RWLocker-384"><span class="linenos">384</span></a>        
</span><span id="RWLocker-385"><a href="#RWLocker-385"><span class="linenos">385</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="RWLocker-386"><a href="#RWLocker-386"><span class="linenos">386</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker-387"><a href="#RWLocker-387"><span class="linenos">387</span></a>        
</span><span id="RWLocker-388"><a href="#RWLocker-388"><span class="linenos">388</span></a>        <span class="c1"># entities_waiting_for_write</span>
</span><span id="RWLocker-389"><a href="#RWLocker-389"><span class="linenos">389</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLocker-390"><a href="#RWLocker-390"><span class="linenos">390</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="RWLocker-391"><a href="#RWLocker-391"><span class="linenos">391</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker-392"><a href="#RWLocker-392"><span class="linenos">392</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">)</span>
</span><span id="RWLocker-393"><a href="#RWLocker-393"><span class="linenos">393</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-394"><a href="#RWLocker-394"><span class="linenos">394</span></a>                <span class="k">continue</span>
</span><span id="RWLocker-395"><a href="#RWLocker-395"><span class="linenos">395</span></a>            
</span><span id="RWLocker-396"><a href="#RWLocker-396"><span class="linenos">396</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-397"><a href="#RWLocker-397"><span class="linenos">397</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">try_write_lock</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-398"><a href="#RWLocker-398"><span class="linenos">398</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="RWLocker-399"><a href="#RWLocker-399"><span class="linenos">399</span></a>                <span class="k">continue</span>
</span><span id="RWLocker-400"><a href="#RWLocker-400"><span class="linenos">400</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLocker-401"><a href="#RWLocker-401"><span class="linenos">401</span></a>                <span class="n">entity</span><span class="o">.</span><span class="n">writers_pending</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLocker-402"><a href="#RWLocker-402"><span class="linenos">402</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span>
</span><span id="RWLocker-403"><a href="#RWLocker-403"><span class="linenos">403</span></a>                    <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-404"><a href="#RWLocker-404"><span class="linenos">404</span></a>                
</span><span id="RWLocker-405"><a href="#RWLocker-405"><span class="linenos">405</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="RWLocker-406"><a href="#RWLocker-406"><span class="linenos">406</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-407"><a href="#RWLocker-407"><span class="linenos">407</span></a>        
</span><span id="RWLocker-408"><a href="#RWLocker-408"><span class="linenos">408</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="RWLocker-409"><a href="#RWLocker-409"><span class="linenos">409</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker-410"><a href="#RWLocker-410"><span class="linenos">410</span></a>                    
</span><span id="RWLocker-411"><a href="#RWLocker-411"><span class="linenos">411</span></a>        <span class="c1"># entities_waiting_for_read</span>
</span><span id="RWLocker-412"><a href="#RWLocker-412"><span class="linenos">412</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLocker-413"><a href="#RWLocker-413"><span class="linenos">413</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="RWLocker-414"><a href="#RWLocker-414"><span class="linenos">414</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker-415"><a href="#RWLocker-415"><span class="linenos">415</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">)</span>
</span><span id="RWLocker-416"><a href="#RWLocker-416"><span class="linenos">416</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-417"><a href="#RWLocker-417"><span class="linenos">417</span></a>                <span class="k">continue</span>
</span><span id="RWLocker-418"><a href="#RWLocker-418"><span class="linenos">418</span></a>            
</span><span id="RWLocker-419"><a href="#RWLocker-419"><span class="linenos">419</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-420"><a href="#RWLocker-420"><span class="linenos">420</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">try_read_lock</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-421"><a href="#RWLocker-421"><span class="linenos">421</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="RWLocker-422"><a href="#RWLocker-422"><span class="linenos">422</span></a>                <span class="k">continue</span>
</span><span id="RWLocker-423"><a href="#RWLocker-423"><span class="linenos">423</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLocker-424"><a href="#RWLocker-424"><span class="linenos">424</span></a>                <span class="n">entity</span><span class="o">.</span><span class="n">readers_pending</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLocker-425"><a href="#RWLocker-425"><span class="linenos">425</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span>
</span><span id="RWLocker-426"><a href="#RWLocker-426"><span class="linenos">426</span></a>                    <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-427"><a href="#RWLocker-427"><span class="linenos">427</span></a>                
</span><span id="RWLocker-428"><a href="#RWLocker-428"><span class="linenos">428</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="RWLocker-429"><a href="#RWLocker-429"><span class="linenos">429</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-430"><a href="#RWLocker-430"><span class="linenos">430</span></a>        
</span><span id="RWLocker-431"><a href="#RWLocker-431"><span class="linenos">431</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="RWLocker-432"><a href="#RWLocker-432"><span class="linenos">432</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker-433"><a href="#RWLocker-433"><span class="linenos">433</span></a>        
</span><span id="RWLocker-434"><a href="#RWLocker-434"><span class="linenos">434</span></a>        <span class="c1"># general</span>
</span><span id="RWLocker-435"><a href="#RWLocker-435"><span class="linenos">435</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">):</span>
</span><span id="RWLocker-436"><a href="#RWLocker-436"><span class="linenos">436</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="RWLocker-437"><a href="#RWLocker-437"><span class="linenos">437</span></a>
</span><span id="RWLocker-438"><a href="#RWLocker-438"><span class="linenos">438</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLocker-439"><a href="#RWLocker-439"><span class="linenos">439</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">)</span>
</span><span id="RWLocker-440"><a href="#RWLocker-440"><span class="linenos">440</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="RWLocker-441"><a href="#RWLocker-441"><span class="linenos">441</span></a>    
</span><span id="RWLocker-442"><a href="#RWLocker-442"><span class="linenos">442</span></a>    <span class="k">def</span> <span class="nf">get_locker_entity</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">):</span>
</span><span id="RWLocker-443"><a href="#RWLocker-443"><span class="linenos">443</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="RWLocker-444"><a href="#RWLocker-444"><span class="linenos">444</span></a>
</span><span id="RWLocker-445"><a href="#RWLocker-445"><span class="linenos">445</span></a>    <span class="k">def</span> <span class="nf">_on_register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="RWLocker-446"><a href="#RWLocker-446"><span class="linenos">446</span></a>        <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker-447"><a href="#RWLocker-447"><span class="linenos">447</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="RWLocker-448"><a href="#RWLocker-448"><span class="linenos">448</span></a>        <span class="n">entity</span><span class="p">:</span> <span class="n">RWLockerEntity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-449"><a href="#RWLocker-449"><span class="linenos">449</span></a>        
</span><span id="RWLocker-450"><a href="#RWLocker-450"><span class="linenos">450</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="RWLocker-451"><a href="#RWLocker-451"><span class="linenos">451</span></a>        <span class="n">entity</span><span class="o">.</span><span class="n">related_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-452"><a href="#RWLocker-452"><span class="linenos">452</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">:</span>
</span><span id="RWLocker-453"><a href="#RWLocker-453"><span class="linenos">453</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLocker-454"><a href="#RWLocker-454"><span class="linenos">454</span></a>        
</span><span id="RWLocker-455"><a href="#RWLocker-455"><span class="linenos">455</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="RWLocker-456"><a href="#RWLocker-456"><span class="linenos">456</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="RWLocker-457"><a href="#RWLocker-457"><span class="linenos">457</span></a>        <span class="n">context_manager</span><span class="p">:</span> <span class="n">RWLockerContextManager</span> <span class="o">=</span> <span class="n">RWLockerContextManager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">interface</span><span class="p">)</span>
</span><span id="RWLocker-458"><a href="#RWLocker-458"><span class="linenos">458</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">context_manager</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="RWLocker-459"><a href="#RWLocker-459"><span class="linenos">459</span></a>
</span><span id="RWLocker-460"><a href="#RWLocker-460"><span class="linenos">460</span></a>    <span class="k">def</span> <span class="nf">_on_deregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">safe</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="RWLocker-461"><a href="#RWLocker-461"><span class="linenos">461</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="RWLocker-462"><a href="#RWLocker-462"><span class="linenos">462</span></a>        <span class="k">if</span> <span class="n">safe</span><span class="p">:</span>
</span><span id="RWLocker-463"><a href="#RWLocker-463"><span class="linenos">463</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="RWLocker-464"><a href="#RWLocker-464"><span class="linenos">464</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="RWLocker-465"><a href="#RWLocker-465"><span class="linenos">465</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="RWLocker-466"><a href="#RWLocker-466"><span class="linenos">466</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="RWLocker-467"><a href="#RWLocker-467"><span class="linenos">467</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="RWLocker-468"><a href="#RWLocker-468"><span class="linenos">468</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker-469"><a href="#RWLocker-469"><span class="linenos">469</span></a>                <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-470"><a href="#RWLocker-470"><span class="linenos">470</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-471"><a href="#RWLocker-471"><span class="linenos">471</span></a>                <span class="k">for</span> <span class="n">related_coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">related_coroutines</span><span class="p">:</span>
</span><span id="RWLocker-472"><a href="#RWLocker-472"><span class="linenos">472</span></a>                    <span class="n">coroutine_entities</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">related_coro_id</span><span class="p">]</span>
</span><span id="RWLocker-473"><a href="#RWLocker-473"><span class="linenos">473</span></a>                    <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="n">coroutine_entities</span><span class="p">:</span>
</span><span id="RWLocker-474"><a href="#RWLocker-474"><span class="linenos">474</span></a>                        <span class="n">coroutine_entities</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="RWLocker-475"><a href="#RWLocker-475"><span class="linenos">475</span></a>                
</span><span id="RWLocker-476"><a href="#RWLocker-476"><span class="linenos">476</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="RWLocker-477"><a href="#RWLocker-477"><span class="linenos">477</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLocker-478"><a href="#RWLocker-478"><span class="linenos">478</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="RWLocker-479"><a href="#RWLocker-479"><span class="linenos">479</span></a>            
</span><span id="RWLocker-480"><a href="#RWLocker-480"><span class="linenos">480</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="RWLocker-481"><a href="#RWLocker-481"><span class="linenos">481</span></a>
</span><span id="RWLocker-482"><a href="#RWLocker-482"><span class="linenos">482</span></a>    <span class="k">def</span> <span class="nf">_on_wait_for_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="RWLocker-483"><a href="#RWLocker-483"><span class="linenos">483</span></a>        <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker-484"><a href="#RWLocker-484"><span class="linenos">484</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">()</span>
</span><span id="RWLocker-485"><a href="#RWLocker-485"><span class="linenos">485</span></a>        
</span><span id="RWLocker-486"><a href="#RWLocker-486"><span class="linenos">486</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="RWLocker-487"><a href="#RWLocker-487"><span class="linenos">487</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="RWLocker-488"><a href="#RWLocker-488"><span class="linenos">488</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="RWLocker-489"><a href="#RWLocker-489"><span class="linenos">489</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-490"><a href="#RWLocker-490"><span class="linenos">490</span></a>        <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-491"><a href="#RWLocker-491"><span class="linenos">491</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="RWLocker-492"><a href="#RWLocker-492"><span class="linenos">492</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="RWLocker-493"><a href="#RWLocker-493"><span class="linenos">493</span></a>
</span><span id="RWLocker-494"><a href="#RWLocker-494"><span class="linenos">494</span></a>    <span class="k">def</span> <span class="nf">_on_wait_for_read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="RWLocker-495"><a href="#RWLocker-495"><span class="linenos">495</span></a>        <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker-496"><a href="#RWLocker-496"><span class="linenos">496</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">()</span>
</span><span id="RWLocker-497"><a href="#RWLocker-497"><span class="linenos">497</span></a>        
</span><span id="RWLocker-498"><a href="#RWLocker-498"><span class="linenos">498</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="RWLocker-499"><a href="#RWLocker-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="RWLocker-500"><a href="#RWLocker-500"><span class="linenos">500</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro</span><span class="o">.</span><span class="n">add_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler</span><span class="p">)</span>
</span><span id="RWLocker-501"><a href="#RWLocker-501"><span class="linenos">501</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-502"><a href="#RWLocker-502"><span class="linenos">502</span></a>        <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-503"><a href="#RWLocker-503"><span class="linenos">503</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="RWLocker-504"><a href="#RWLocker-504"><span class="linenos">504</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="RWLocker-505"><a href="#RWLocker-505"><span class="linenos">505</span></a>
</span><span id="RWLocker-506"><a href="#RWLocker-506"><span class="linenos">506</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler_global</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLocker-507"><a href="#RWLocker-507"><span class="linenos">507</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="RWLocker-508"><a href="#RWLocker-508"><span class="linenos">508</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">:</span>
</span><span id="RWLocker-509"><a href="#RWLocker-509"><span class="linenos">509</span></a>            <span class="n">entities</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker-510"><a href="#RWLocker-510"><span class="linenos">510</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker-511"><a href="#RWLocker-511"><span class="linenos">511</span></a>            <span class="k">for</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="n">entities</span><span class="p">:</span>
</span><span id="RWLocker-512"><a href="#RWLocker-512"><span class="linenos">512</span></a>                <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker-513"><a href="#RWLocker-513"><span class="linenos">513</span></a>                    <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker-514"><a href="#RWLocker-514"><span class="linenos">514</span></a>                    <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">related_coroutines</span><span class="p">:</span>
</span><span id="RWLocker-515"><a href="#RWLocker-515"><span class="linenos">515</span></a>                        <span class="n">entity</span><span class="o">.</span><span class="n">related_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-516"><a href="#RWLocker-516"><span class="linenos">516</span></a>                    
</span><span id="RWLocker-517"><a href="#RWLocker-517"><span class="linenos">517</span></a>                    <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span>
</span><span id="RWLocker-518"><a href="#RWLocker-518"><span class="linenos">518</span></a>                        <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker-519"><a href="#RWLocker-519"><span class="linenos">519</span></a>        
</span><span id="RWLocker-520"><a href="#RWLocker-520"><span class="linenos">520</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">:</span>
</span><span id="RWLocker-521"><a href="#RWLocker-521"><span class="linenos">521</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker-522"><a href="#RWLocker-522"><span class="linenos">522</span></a>        
</span><span id="RWLocker-523"><a href="#RWLocker-523"><span class="linenos">523</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">:</span>
</span><span id="RWLocker-524"><a href="#RWLocker-524"><span class="linenos">524</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker-525"><a href="#RWLocker-525"><span class="linenos">525</span></a>        
</span><span id="RWLocker-526"><a href="#RWLocker-526"><span class="linenos">526</span></a>        <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">:</span>
</span><span id="RWLocker-527"><a href="#RWLocker-527"><span class="linenos">527</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker-528"><a href="#RWLocker-528"><span class="linenos">528</span></a>
</span><span id="RWLocker-529"><a href="#RWLocker-529"><span class="linenos">529</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="RWLocker-530"><a href="#RWLocker-530"><span class="linenos">530</span></a>
</span><span id="RWLocker-531"><a href="#RWLocker-531"><span class="linenos">531</span></a>    <span class="k">def</span> <span class="nf">_on_coro_del_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLocker-532"><a href="#RWLocker-532"><span class="linenos">532</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_coro_del_handler_global</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="RWLocker.__init__" class="classattr">
                                        <input id="RWLocker.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">RWLocker</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="RWLocker.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLocker.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLocker.__init__-335"><a href="#RWLocker.__init__-335"><span class="linenos">335</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="RWLocker.__init__-336"><a href="#RWLocker.__init__-336"><span class="linenos">336</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="RWLocker.__init__-337"><a href="#RWLocker.__init__-337"><span class="linenos">337</span></a>
</span><span id="RWLocker.__init__-338"><a href="#RWLocker.__init__-338"><span class="linenos">338</span></a>        <span class="c1"># loop.add_global_on_coro_del_handler(self._on_coro_del_handler_global)  # Todo: switch to local coro del handler</span>
</span><span id="RWLocker.__init__-339"><a href="#RWLocker.__init__-339"><span class="linenos">339</span></a>
</span><span id="RWLocker.__init__-340"><a href="#RWLocker.__init__-340"><span class="linenos">340</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="RWLocker.__init__-341"><a href="#RWLocker.__init__-341"><span class="linenos">341</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_register</span><span class="p">,</span>
</span><span id="RWLocker.__init__-342"><a href="#RWLocker.__init__-342"><span class="linenos">342</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_deregister</span><span class="p">,</span>
</span><span id="RWLocker.__init__-343"><a href="#RWLocker.__init__-343"><span class="linenos">343</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_write</span><span class="p">,</span>
</span><span id="RWLocker.__init__-344"><a href="#RWLocker.__init__-344"><span class="linenos">344</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_wait_for_read</span><span class="p">,</span>
</span><span id="RWLocker.__init__-345"><a href="#RWLocker.__init__-345"><span class="linenos">345</span></a>        <span class="p">}</span>
</span><span id="RWLocker.__init__-346"><a href="#RWLocker.__init__-346"><span class="linenos">346</span></a>        
</span><span id="RWLocker.__init__-347"><a href="#RWLocker.__init__-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">RWLockerEntity</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker.__init__-348"><a href="#RWLocker.__init__-348"><span class="linenos">348</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker.__init__-349"><a href="#RWLocker.__init__-349"><span class="linenos">349</span></a>        
</span><span id="RWLocker.__init__-350"><a href="#RWLocker.__init__-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker.__init__-351"><a href="#RWLocker.__init__-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="RWLocker.__init__-352"><a href="#RWLocker.__init__-352"><span class="linenos">352</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLocker.locker_entities" class="classattr">
                                <div class="attr variable">
            <span class="name">locker_entities</span><span class="annotation">: Dict[Hashable, <a href="#RWLockerEntity">RWLockerEntity</a>]</span>

        
    </div>
    <a class="headerlink" href="#RWLocker.locker_entities"></a>
    
    

                            </div>
                            <div id="RWLocker.entities_by_coroutine" class="classattr">
                                <div class="attr variable">
            <span class="name">entities_by_coroutine</span><span class="annotation">: Dict[int, Set[Hashable]]</span>

        
    </div>
    <a class="headerlink" href="#RWLocker.entities_by_coroutine"></a>
    
    

                            </div>
                            <div id="RWLocker.remove_entity_requests" class="classattr">
                                <div class="attr variable">
            <span class="name">remove_entity_requests</span><span class="annotation">: Dict[int, Hashable]</span>

        
    </div>
    <a class="headerlink" href="#RWLocker.remove_entity_requests"></a>
    
    

                            </div>
                            <div id="RWLocker.waiting_for_write_requests" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_for_write_requests</span><span class="annotation">: Dict[int, Hashable]</span>

        
    </div>
    <a class="headerlink" href="#RWLocker.waiting_for_write_requests"></a>
    
    

                            </div>
                            <div id="RWLocker.waiting_for_read_requests" class="classattr">
                                <div class="attr variable">
            <span class="name">waiting_for_read_requests</span><span class="annotation">: Dict[int, Hashable]</span>

        
    </div>
    <a class="headerlink" href="#RWLocker.waiting_for_read_requests"></a>
    
    

                            </div>
                            <div id="RWLocker.get_entity_stats" class="classattr">
                                        <input id="RWLocker.get_entity_stats-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_entity_stats</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">stats_level</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="RWLocker.get_entity_stats-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLocker.get_entity_stats"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLocker.get_entity_stats-354"><a href="#RWLocker.get_entity_stats-354"><span class="linenos">354</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="RWLocker.get_entity_stats-355"><a href="#RWLocker.get_entity_stats-355"><span class="linenos">355</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="RWLocker.get_entity_stats-356"><a href="#RWLocker.get_entity_stats-356"><span class="linenos">356</span></a>            <span class="s1">&#39;locker entities num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">),</span>
</span><span id="RWLocker.get_entity_stats-357"><a href="#RWLocker.get_entity_stats-357"><span class="linenos">357</span></a>            <span class="s1">&#39;affected coroutines num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entities_by_coroutine</span><span class="p">),</span>
</span><span id="RWLocker.get_entity_stats-358"><a href="#RWLocker.get_entity_stats-358"><span class="linenos">358</span></a>            <span class="s1">&#39;waiting for write requests num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">),</span>
</span><span id="RWLocker.get_entity_stats-359"><a href="#RWLocker.get_entity_stats-359"><span class="linenos">359</span></a>            <span class="s1">&#39;waiting_for_read_requests num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">),</span>
</span><span id="RWLocker.get_entity_stats-360"><a href="#RWLocker.get_entity_stats-360"><span class="linenos">360</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLocker.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="RWLocker.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#RWLockerRequest">RWLockerRequest</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="RWLocker.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLocker.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLocker.single_task_registration_or_immediate_processing-362"><a href="#RWLocker.single_task_registration_or_immediate_processing-362"><span class="linenos">362</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RWLockerRequest</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span>
</span><span id="RWLocker.single_task_registration_or_immediate_processing-363"><a href="#RWLocker.single_task_registration_or_immediate_processing-363"><span class="linenos">363</span></a>                                                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="RWLocker.single_task_registration_or_immediate_processing-364"><a href="#RWLocker.single_task_registration_or_immediate_processing-364"><span class="linenos">364</span></a>        <span class="k">if</span> <span class="n">request</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="RWLocker.single_task_registration_or_immediate_processing-365"><a href="#RWLocker.single_task_registration_or_immediate_processing-365"><span class="linenos">365</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">resolve_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="RWLocker.single_task_registration_or_immediate_processing-366"><a href="#RWLocker.single_task_registration_or_immediate_processing-366"><span class="linenos">366</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLocker.full_processing_iteration" class="classattr">
                                        <input id="RWLocker.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RWLocker.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLocker.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLocker.full_processing_iteration-368"><a href="#RWLocker.full_processing_iteration-368"><span class="linenos">368</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="RWLocker.full_processing_iteration-369"><a href="#RWLocker.full_processing_iteration-369"><span class="linenos">369</span></a>        <span class="c1"># entities_waiting_for_remove</span>
</span><span id="RWLocker.full_processing_iteration-370"><a href="#RWLocker.full_processing_iteration-370"><span class="linenos">370</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLocker.full_processing_iteration-371"><a href="#RWLocker.full_processing_iteration-371"><span class="linenos">371</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="RWLocker.full_processing_iteration-372"><a href="#RWLocker.full_processing_iteration-372"><span class="linenos">372</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-373"><a href="#RWLocker.full_processing_iteration-373"><span class="linenos">373</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-374"><a href="#RWLocker.full_processing_iteration-374"><span class="linenos">374</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-375"><a href="#RWLocker.full_processing_iteration-375"><span class="linenos">375</span></a>                <span class="k">continue</span>
</span><span id="RWLocker.full_processing_iteration-376"><a href="#RWLocker.full_processing_iteration-376"><span class="linenos">376</span></a>            
</span><span id="RWLocker.full_processing_iteration-377"><a href="#RWLocker.full_processing_iteration-377"><span class="linenos">377</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker.full_processing_iteration-378"><a href="#RWLocker.full_processing_iteration-378"><span class="linenos">378</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">test_remove</span><span class="p">()</span>
</span><span id="RWLocker.full_processing_iteration-379"><a href="#RWLocker.full_processing_iteration-379"><span class="linenos">379</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-380"><a href="#RWLocker.full_processing_iteration-380"><span class="linenos">380</span></a>                <span class="k">continue</span>
</span><span id="RWLocker.full_processing_iteration-381"><a href="#RWLocker.full_processing_iteration-381"><span class="linenos">381</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-382"><a href="#RWLocker.full_processing_iteration-382"><span class="linenos">382</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker.full_processing_iteration-383"><a href="#RWLocker.full_processing_iteration-383"><span class="linenos">383</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-384"><a href="#RWLocker.full_processing_iteration-384"><span class="linenos">384</span></a>        
</span><span id="RWLocker.full_processing_iteration-385"><a href="#RWLocker.full_processing_iteration-385"><span class="linenos">385</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-386"><a href="#RWLocker.full_processing_iteration-386"><span class="linenos">386</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker.full_processing_iteration-387"><a href="#RWLocker.full_processing_iteration-387"><span class="linenos">387</span></a>        
</span><span id="RWLocker.full_processing_iteration-388"><a href="#RWLocker.full_processing_iteration-388"><span class="linenos">388</span></a>        <span class="c1"># entities_waiting_for_write</span>
</span><span id="RWLocker.full_processing_iteration-389"><a href="#RWLocker.full_processing_iteration-389"><span class="linenos">389</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLocker.full_processing_iteration-390"><a href="#RWLocker.full_processing_iteration-390"><span class="linenos">390</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="RWLocker.full_processing_iteration-391"><a href="#RWLocker.full_processing_iteration-391"><span class="linenos">391</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-392"><a href="#RWLocker.full_processing_iteration-392"><span class="linenos">392</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-393"><a href="#RWLocker.full_processing_iteration-393"><span class="linenos">393</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-394"><a href="#RWLocker.full_processing_iteration-394"><span class="linenos">394</span></a>                <span class="k">continue</span>
</span><span id="RWLocker.full_processing_iteration-395"><a href="#RWLocker.full_processing_iteration-395"><span class="linenos">395</span></a>            
</span><span id="RWLocker.full_processing_iteration-396"><a href="#RWLocker.full_processing_iteration-396"><span class="linenos">396</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker.full_processing_iteration-397"><a href="#RWLocker.full_processing_iteration-397"><span class="linenos">397</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">try_write_lock</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-398"><a href="#RWLocker.full_processing_iteration-398"><span class="linenos">398</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-399"><a href="#RWLocker.full_processing_iteration-399"><span class="linenos">399</span></a>                <span class="k">continue</span>
</span><span id="RWLocker.full_processing_iteration-400"><a href="#RWLocker.full_processing_iteration-400"><span class="linenos">400</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-401"><a href="#RWLocker.full_processing_iteration-401"><span class="linenos">401</span></a>                <span class="n">entity</span><span class="o">.</span><span class="n">writers_pending</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLocker.full_processing_iteration-402"><a href="#RWLocker.full_processing_iteration-402"><span class="linenos">402</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-403"><a href="#RWLocker.full_processing_iteration-403"><span class="linenos">403</span></a>                    <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-404"><a href="#RWLocker.full_processing_iteration-404"><span class="linenos">404</span></a>                
</span><span id="RWLocker.full_processing_iteration-405"><a href="#RWLocker.full_processing_iteration-405"><span class="linenos">405</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-406"><a href="#RWLocker.full_processing_iteration-406"><span class="linenos">406</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-407"><a href="#RWLocker.full_processing_iteration-407"><span class="linenos">407</span></a>        
</span><span id="RWLocker.full_processing_iteration-408"><a href="#RWLocker.full_processing_iteration-408"><span class="linenos">408</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-409"><a href="#RWLocker.full_processing_iteration-409"><span class="linenos">409</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker.full_processing_iteration-410"><a href="#RWLocker.full_processing_iteration-410"><span class="linenos">410</span></a>                    
</span><span id="RWLocker.full_processing_iteration-411"><a href="#RWLocker.full_processing_iteration-411"><span class="linenos">411</span></a>        <span class="c1"># entities_waiting_for_read</span>
</span><span id="RWLocker.full_processing_iteration-412"><a href="#RWLocker.full_processing_iteration-412"><span class="linenos">412</span></a>        <span class="n">processed_coro_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="RWLocker.full_processing_iteration-413"><a href="#RWLocker.full_processing_iteration-413"><span class="linenos">413</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">entity_id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="RWLocker.full_processing_iteration-414"><a href="#RWLocker.full_processing_iteration-414"><span class="linenos">414</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-415"><a href="#RWLocker.full_processing_iteration-415"><span class="linenos">415</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">UnknownLockerEntity</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-416"><a href="#RWLocker.full_processing_iteration-416"><span class="linenos">416</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-417"><a href="#RWLocker.full_processing_iteration-417"><span class="linenos">417</span></a>                <span class="k">continue</span>
</span><span id="RWLocker.full_processing_iteration-418"><a href="#RWLocker.full_processing_iteration-418"><span class="linenos">418</span></a>            
</span><span id="RWLocker.full_processing_iteration-419"><a href="#RWLocker.full_processing_iteration-419"><span class="linenos">419</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="p">[</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="RWLocker.full_processing_iteration-420"><a href="#RWLocker.full_processing_iteration-420"><span class="linenos">420</span></a>            <span class="n">need_to_try_later</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">try_read_lock</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-421"><a href="#RWLocker.full_processing_iteration-421"><span class="linenos">421</span></a>            <span class="k">if</span> <span class="n">need_to_try_later</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-422"><a href="#RWLocker.full_processing_iteration-422"><span class="linenos">422</span></a>                <span class="k">continue</span>
</span><span id="RWLocker.full_processing_iteration-423"><a href="#RWLocker.full_processing_iteration-423"><span class="linenos">423</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-424"><a href="#RWLocker.full_processing_iteration-424"><span class="linenos">424</span></a>                <span class="n">entity</span><span class="o">.</span><span class="n">readers_pending</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="RWLocker.full_processing_iteration-425"><a href="#RWLocker.full_processing_iteration-425"><span class="linenos">425</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-426"><a href="#RWLocker.full_processing_iteration-426"><span class="linenos">426</span></a>                    <span class="n">entity</span><span class="o">.</span><span class="n">waiting_coroutines</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-427"><a href="#RWLocker.full_processing_iteration-427"><span class="linenos">427</span></a>                
</span><span id="RWLocker.full_processing_iteration-428"><a href="#RWLocker.full_processing_iteration-428"><span class="linenos">428</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-429"><a href="#RWLocker.full_processing_iteration-429"><span class="linenos">429</span></a>                <span class="n">processed_coro_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="RWLocker.full_processing_iteration-430"><a href="#RWLocker.full_processing_iteration-430"><span class="linenos">430</span></a>        
</span><span id="RWLocker.full_processing_iteration-431"><a href="#RWLocker.full_processing_iteration-431"><span class="linenos">431</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coro_ids</span><span class="p">:</span>
</span><span id="RWLocker.full_processing_iteration-432"><a href="#RWLocker.full_processing_iteration-432"><span class="linenos">432</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span>
</span><span id="RWLocker.full_processing_iteration-433"><a href="#RWLocker.full_processing_iteration-433"><span class="linenos">433</span></a>        
</span><span id="RWLocker.full_processing_iteration-434"><a href="#RWLocker.full_processing_iteration-434"><span class="linenos">434</span></a>        <span class="c1"># general</span>
</span><span id="RWLocker.full_processing_iteration-435"><a href="#RWLocker.full_processing_iteration-435"><span class="linenos">435</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">):</span>
</span><span id="RWLocker.full_processing_iteration-436"><a href="#RWLocker.full_processing_iteration-436"><span class="linenos">436</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="RWLocker.in_work" class="classattr">
                                        <input id="RWLocker.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="RWLocker.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLocker.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLocker.in_work-438"><a href="#RWLocker.in_work-438"><span class="linenos">438</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="RWLocker.in_work-439"><a href="#RWLocker.in_work-439"><span class="linenos">439</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">remove_entity_requests</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_write_requests</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">waiting_for_read_requests</span><span class="p">)</span>
</span><span id="RWLocker.in_work-440"><a href="#RWLocker.in_work-440"><span class="linenos">440</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="RWLocker.get_locker_entity" class="classattr">
                                        <input id="RWLocker.get_locker_entity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_locker_entity</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="RWLocker.get_locker_entity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RWLocker.get_locker_entity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RWLocker.get_locker_entity-442"><a href="#RWLocker.get_locker_entity-442"><span class="linenos">442</span></a>    <span class="k">def</span> <span class="nf">get_locker_entity</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">):</span>
</span><span id="RWLocker.get_locker_entity-443"><a href="#RWLocker.get_locker_entity-443"><span class="linenos">443</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">locker_entities</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="RWLocker.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="RWLocker.iteration" class="function">iteration</dd>
                <dd id="RWLocker.make_response" class="function">make_response</dd>
                <dd id="RWLocker.register_response" class="function">register_response</dd>
                <dd id="RWLocker.put_task" class="function">put_task</dd>
                <dd id="RWLocker.resolve_request" class="function">resolve_request</dd>
                <dd id="RWLocker.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="RWLocker.in_forground_work" class="function">in_forground_work</dd>
                <dd id="RWLocker.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="RWLocker.time_left_before_next_event" class="function">time_left_before_next_event</dd>
                <dd id="RWLocker.is_low_latency" class="function">is_low_latency</dd>
                <dd id="RWLocker.make_live" class="function">make_live</dd>
                <dd id="RWLocker.make_dead" class="function">make_dead</dd>
                <dd id="RWLocker.service_id_impl" class="function">service_id_impl</dd>
                <dd id="RWLocker.service_id" class="function">service_id</dd>
                <dd id="RWLocker.destroy" class="function">destroy</dd>

            </div>
            <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</dt>
                                <dd id="RWLocker.StatsLevel" class="class">StatsLevel</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="get_rw_lock">
                            <input id="get_rw_lock-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_rw_lock</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#RWLockerContextManager">RWLockerContextManager</a></span><span class="p">,</span> <span class="n"><a href="#FakeRWLockerContextManager">FakeRWLockerContextManager</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="get_rw_lock-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_rw_lock"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_rw_lock-538"><a href="#get_rw_lock-538"><span class="linenos">538</span></a><span class="k">def</span> <span class="nf">get_rw_lock</span><span class="p">(</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">RWLockerContextManager</span><span class="p">,</span> <span class="n">FakeRWLockerContextManager</span><span class="p">]:</span>
</span><span id="get_rw_lock-539"><a href="#get_rw_lock-539"><span class="linenos">539</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="get_rw_lock-540"><a href="#get_rw_lock-540"><span class="linenos">540</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_rw_lock-541"><a href="#get_rw_lock-541"><span class="linenos">541</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="get_rw_lock-542"><a href="#get_rw_lock-542"><span class="linenos">542</span></a>
</span><span id="get_rw_lock-543"><a href="#get_rw_lock-543"><span class="linenos">543</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="get_rw_lock-544"><a href="#get_rw_lock-544"><span class="linenos">544</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_rw_lock-545"><a href="#get_rw_lock-545"><span class="linenos">545</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running from Service</span>
</span><span id="get_rw_lock-546"><a href="#get_rw_lock-546"><span class="linenos">546</span></a>
</span><span id="get_rw_lock-547"><a href="#get_rw_lock-547"><span class="linenos">547</span></a>    <span class="n">locker_entity</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">)</span><span class="o">.</span><span class="n">get_locker_entity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="get_rw_lock-548"><a href="#get_rw_lock-548"><span class="linenos">548</span></a>    <span class="k">if</span> <span class="n">locker_entity</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_rw_lock-549"><a href="#get_rw_lock-549"><span class="linenos">549</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">interface</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">))</span>
</span><span id="get_rw_lock-550"><a href="#get_rw_lock-550"><span class="linenos">550</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="get_rw_lock-551"><a href="#get_rw_lock-551"><span class="linenos">551</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">RWLockerContextManager</span><span class="p">(</span><span class="n">locker_entity</span><span class="p">,</span> <span class="n">interface</span><span class="p">)</span>
</span><span id="get_rw_lock-552"><a href="#get_rw_lock-552"><span class="linenos">552</span></a>    
</span><span id="get_rw_lock-553"><a href="#get_rw_lock-553"><span class="linenos">553</span></a>    <span class="k">return</span> <span class="n">lock</span>
</span></pre></div>


    

                </section>
                <section id="grwl">
                            <input id="grwl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">grwl</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#RWLockerContextManager">RWLockerContextManager</a></span><span class="p">,</span> <span class="n"><a href="#FakeRWLockerContextManager">FakeRWLockerContextManager</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="grwl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#grwl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="grwl-538"><a href="#grwl-538"><span class="linenos">538</span></a><span class="k">def</span> <span class="nf">get_rw_lock</span><span class="p">(</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">RWLockerContextManager</span><span class="p">,</span> <span class="n">FakeRWLockerContextManager</span><span class="p">]:</span>
</span><span id="grwl-539"><a href="#grwl-539"><span class="linenos">539</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="grwl-540"><a href="#grwl-540"><span class="linenos">540</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="grwl-541"><a href="#grwl-541"><span class="linenos">541</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="grwl-542"><a href="#grwl-542"><span class="linenos">542</span></a>
</span><span id="grwl-543"><a href="#grwl-543"><span class="linenos">543</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="grwl-544"><a href="#grwl-544"><span class="linenos">544</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="grwl-545"><a href="#grwl-545"><span class="linenos">545</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running from Service</span>
</span><span id="grwl-546"><a href="#grwl-546"><span class="linenos">546</span></a>
</span><span id="grwl-547"><a href="#grwl-547"><span class="linenos">547</span></a>    <span class="n">locker_entity</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">)</span><span class="o">.</span><span class="n">get_locker_entity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="grwl-548"><a href="#grwl-548"><span class="linenos">548</span></a>    <span class="k">if</span> <span class="n">locker_entity</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="grwl-549"><a href="#grwl-549"><span class="linenos">549</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">interface</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">))</span>
</span><span id="grwl-550"><a href="#grwl-550"><span class="linenos">550</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="grwl-551"><a href="#grwl-551"><span class="linenos">551</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">RWLockerContextManager</span><span class="p">(</span><span class="n">locker_entity</span><span class="p">,</span> <span class="n">interface</span><span class="p">)</span>
</span><span id="grwl-552"><a href="#grwl-552"><span class="linenos">552</span></a>    
</span><span id="grwl-553"><a href="#grwl-553"><span class="linenos">553</span></a>    <span class="k">return</span> <span class="n">lock</span>
</span></pre></div>


    

                </section>
                <section id="aget_rw_lock">
                            <input id="aget_rw_lock-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aget_rw_lock</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#RWLockerContextManager">RWLockerContextManager</a></span><span class="p">,</span> <span class="n"><a href="#FakeRWLockerContextManager">FakeRWLockerContextManager</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="aget_rw_lock-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#aget_rw_lock"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="aget_rw_lock-559"><a href="#aget_rw_lock-559"><span class="linenos">559</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_rw_lock</span><span class="p">(</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">RWLockerContextManager</span><span class="p">,</span> <span class="n">FakeRWLockerContextManager</span><span class="p">]:</span>
</span><span id="aget_rw_lock-560"><a href="#aget_rw_lock-560"><span class="linenos">560</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="aget_rw_lock-561"><a href="#aget_rw_lock-561"><span class="linenos">561</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="aget_rw_lock-562"><a href="#aget_rw_lock-562"><span class="linenos">562</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="aget_rw_lock-563"><a href="#aget_rw_lock-563"><span class="linenos">563</span></a>
</span><span id="aget_rw_lock-564"><a href="#aget_rw_lock-564"><span class="linenos">564</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="aget_rw_lock-565"><a href="#aget_rw_lock-565"><span class="linenos">565</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="aget_rw_lock-566"><a href="#aget_rw_lock-566"><span class="linenos">566</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running from Service</span>
</span><span id="aget_rw_lock-567"><a href="#aget_rw_lock-567"><span class="linenos">567</span></a>
</span><span id="aget_rw_lock-568"><a href="#aget_rw_lock-568"><span class="linenos">568</span></a>    <span class="n">locker_entity</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">)</span><span class="o">.</span><span class="n">get_locker_entity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="aget_rw_lock-569"><a href="#aget_rw_lock-569"><span class="linenos">569</span></a>    <span class="k">if</span> <span class="n">locker_entity</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="aget_rw_lock-570"><a href="#aget_rw_lock-570"><span class="linenos">570</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="k">await</span> <span class="n">interface</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">))</span>
</span><span id="aget_rw_lock-571"><a href="#aget_rw_lock-571"><span class="linenos">571</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="aget_rw_lock-572"><a href="#aget_rw_lock-572"><span class="linenos">572</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">RWLockerContextManager</span><span class="p">(</span><span class="n">locker_entity</span><span class="p">,</span> <span class="n">interface</span><span class="p">)</span>
</span><span id="aget_rw_lock-573"><a href="#aget_rw_lock-573"><span class="linenos">573</span></a>    
</span><span id="aget_rw_lock-574"><a href="#aget_rw_lock-574"><span class="linenos">574</span></a>    <span class="k">return</span> <span class="n">lock</span>
</span></pre></div>


    

                </section>
                <section id="agrwl">
                            <input id="agrwl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">agrwl</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#RWLockerContextManager">RWLockerContextManager</a></span><span class="p">,</span> <span class="n"><a href="#FakeRWLockerContextManager">FakeRWLockerContextManager</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="agrwl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#agrwl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="agrwl-559"><a href="#agrwl-559"><span class="linenos">559</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_rw_lock</span><span class="p">(</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">recursive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">RWLockerContextManager</span><span class="p">,</span> <span class="n">FakeRWLockerContextManager</span><span class="p">]:</span>
</span><span id="agrwl-560"><a href="#agrwl-560"><span class="linenos">560</span></a>    <span class="n">loop</span> <span class="o">=</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="agrwl-561"><a href="#agrwl-561"><span class="linenos">561</span></a>    <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="agrwl-562"><a href="#agrwl-562"><span class="linenos">562</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running not from inside the loop</span>
</span><span id="agrwl-563"><a href="#agrwl-563"><span class="linenos">563</span></a>
</span><span id="agrwl-564"><a href="#agrwl-564"><span class="linenos">564</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">loop</span><span class="o">.</span><span class="n">current_interface</span><span class="p">()</span>
</span><span id="agrwl-565"><a href="#agrwl-565"><span class="linenos">565</span></a>    <span class="k">if</span> <span class="n">interface</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="agrwl-566"><a href="#agrwl-566"><span class="linenos">566</span></a>        <span class="k">return</span> <span class="n">FakeRWLockerContextManager</span><span class="p">(</span><span class="n">RWLockerEntity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">,</span> <span class="n">RWLocker</span><span class="p">))</span>  <span class="c1"># running from Service</span>
</span><span id="agrwl-567"><a href="#agrwl-567"><span class="linenos">567</span></a>
</span><span id="agrwl-568"><a href="#agrwl-568"><span class="linenos">568</span></a>    <span class="n">locker_entity</span> <span class="o">=</span> <span class="n">interface</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">)</span><span class="o">.</span><span class="n">get_locker_entity</span><span class="p">(</span><span class="n">entity_id</span><span class="p">)</span>
</span><span id="agrwl-569"><a href="#agrwl-569"><span class="linenos">569</span></a>    <span class="k">if</span> <span class="n">locker_entity</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="agrwl-570"><a href="#agrwl-570"><span class="linenos">570</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="k">await</span> <span class="n">interface</span><span class="p">(</span><span class="n">RWLocker</span><span class="p">,</span> <span class="n">RWLockerRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="n">recursive</span><span class="p">))</span>
</span><span id="agrwl-571"><a href="#agrwl-571"><span class="linenos">571</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="agrwl-572"><a href="#agrwl-572"><span class="linenos">572</span></a>        <span class="n">lock</span> <span class="o">=</span> <span class="n">RWLockerContextManager</span><span class="p">(</span><span class="n">locker_entity</span><span class="p">,</span> <span class="n">interface</span><span class="p">)</span>
</span><span id="agrwl-573"><a href="#agrwl-573"><span class="linenos">573</span></a>    
</span><span id="agrwl-574"><a href="#agrwl-574"><span class="linenos">574</span></a>    <span class="k">return</span> <span class="n">lock</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>