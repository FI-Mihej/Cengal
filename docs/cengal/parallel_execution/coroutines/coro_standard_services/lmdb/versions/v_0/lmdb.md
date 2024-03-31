---
title: lmdb
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.lmdb<wbr>.versions<wbr>.v_0<wbr>.lmdb    </h1>

                
                        <input id="mod-lmdb-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-lmdb-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Lmdb&#39;</span><span class="p">,</span> <span class="s1">&#39;LmdbRequest&#39;</span><span class="p">,</span> <span class="s1">&#39;KeyType&#39;</span><span class="p">,</span> <span class="s1">&#39;RawKeyType&#39;</span><span class="p">,</span> <span class="s1">&#39;ValueType&#39;</span><span class="p">,</span> <span class="s1">&#39;RawValueType&#39;</span><span class="p">,</span> <span class="s1">&#39;DbId&#39;</span><span class="p">,</span> <span class="s1">&#39;DbName&#39;</span><span class="p">,</span> <span class="s1">&#39;DbKeyError&#39;</span><span class="p">]</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_tools.await_coro</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="n">CoroPriority</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.put_coro</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.file_manager</span> <span class="kn">import</span> <span class="n">path_relative_to_current_dir</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.load_best_timer</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.serialization</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Callable</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="kn">import</span> <span class="nn">os</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>    <span class="kn">import</span> <span class="nn">lmdb</span> <span class="k">as</span> <span class="nn">lmdb_lib</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>    <span class="kn">from</span> <span class="nn">warnings</span> <span class="kn">import</span> <span class="n">warn</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>    <span class="n">warn</span><span class="p">(</span><span class="s1">&#39;&#39;&#39;WARNING: `lmdb` library is not installed. Lmdb service will not work.</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="s1">         To install `lmdb` use: `pip install lmdb`&#39;&#39;&#39;</span><span class="p">)</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>    <span class="k">raise</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="sd">Module Docstring</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.2.0&quot;</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="n">KeyType</span> <span class="o">=</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="n">RawKeyType</span> <span class="o">=</span> <span class="nb">bytes</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="n">ValueType</span> <span class="o">=</span> <span class="n">Any</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="n">RawValueType</span> <span class="o">=</span> <span class="nb">bytes</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="n">DbId</span> <span class="o">=</span> <span class="n">Hashable</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="n">DbName</span> <span class="o">=</span> <span class="nb">bytes</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="k">class</span> <span class="nc">LmdbRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="k">def</span> <span class="nf">set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="nf">open_databases</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">DbId</span><span class="p">,</span> <span class="n">DbName</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">db_names</span><span class="p">)</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="k">def</span> <span class="nf">drop_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">,</span> <span class="n">delete</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">db_id</span><span class="p">,</span> <span class="n">delete</span><span class="p">)</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="k">def</span> <span class="nf">sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>    <span class="k">def</span> <span class="nf">get_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">keys</span><span class="p">)</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="k">def</span> <span class="nf">get_all_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>    
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    <span class="k">def</span> <span class="nf">put_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>    
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">def</span> <span class="nf">delete_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">open_db_environment</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">11</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>    
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a><span class="k">def</span> <span class="nf">make_key_frozen</span><span class="p">(</span><span class="n">key</span><span class="p">):</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="nb">list</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="nb">set</span><span class="p">):</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="n">new_key</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">key</span><span class="p">:</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>            <span class="n">new_key</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">make_key_frozen</span><span class="p">(</span><span class="n">item</span><span class="p">))</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="n">key</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">new_key</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    <span class="k">return</span> <span class="n">key</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>    
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a><span class="k">class</span> <span class="nc">Lmdb</span><span class="p">(</span><span class="n">Service</span><span class="p">,</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Lmdb</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_db_name</span><span class="p">:</span> <span class="n">DbName</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;__default__&#39;</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">RawKeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">],</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">],</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_relative_to_current_dir</span><span class="p">(</span><span class="s1">&#39;lmdb.db&#39;</span><span class="p">)</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">DbId</span><span class="p">,</span> <span class="n">DbName</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>        <span class="c1"># self.serializer = best_serializer_for_standard_data((DataFormats.binary,</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="c1">#                                    Tags.can_use_bytes,</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="c1">#                                    Tags.decode_str_as_str,</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="c1">#                                    Tags.decode_list_as_list,</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="c1">#                                    Tags.decode_bytes_as_bytes,</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="c1">#                                    Tags.superficial,</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="c1">#                                    Tags.current_platform,</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="c1">#                                    Tags.multi_platform),</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="c1">#                                   TestDataType.small,</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="c1">#                                   0.1)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_db_environment_path</span><span class="p">,</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_open_databases</span><span class="p">,</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_drop_db</span><span class="p">,</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_sync</span><span class="p">,</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get_items</span><span class="p">,</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get_all_items</span><span class="p">,</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put</span><span class="p">,</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put_items</span><span class="p">,</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_delete</span><span class="p">,</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="mi">10</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_delete_items</span><span class="p">,</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>            <span class="mi">11</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_open_db_environment</span><span class="p">,</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="p">}</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>            <span class="s1">&#39;db_names&#39;</span><span class="p">:</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_names</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>            <span class="s1">&#39;writes num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span><span class="p">,</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>            <span class="s1">&#39;reads num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span><span class="p">,</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>            <span class="s1">&#39;deletes num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span><span class="p">,</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>            <span class="s1">&#39;db drops num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span><span class="p">,</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="p">}</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">try_resolve_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>        
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>        <span class="n">data_cache_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">data_cache_buff</span><span class="p">)()</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="n">read_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">read_queue_buff</span><span class="p">)()</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="n">massive_read_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">massive_read_queue_buff</span><span class="p">)()</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="n">deletion_cache_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">deletion_cache_buff</span><span class="p">)()</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="n">get_all_items_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">get_all_items_queue_buff</span><span class="p">)()</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="c1"># put</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="k">def</span> <span class="nf">put_handler</span><span class="p">(</span><span class="n">db_environment</span><span class="p">,</span> <span class="n">databases</span><span class="p">):</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>            <span class="n">db_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>                <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>                    <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">data_cache_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>                        <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>                        <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">],</span> <span class="n">dupdata</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>            <span class="k">except</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">MapFullError</span><span class="p">:</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>                <span class="k">raise</span> <span class="n">DBError</span><span class="o">.</span><span class="n">from_exception</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">,</span> <span class="n">put_handler</span><span class="p">)</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="c1"># delete</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">deletion_cache_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>                <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>                <span class="n">txn</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="c1"># drop</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>        <span class="n">drop_db_requests_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">drop_db_requests_buff</span><span class="p">)()</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="n">dropped_databases</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>        <span class="n">processed_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">def</span> <span class="nf">drop_handler</span><span class="p">(</span><span class="n">db_environment</span><span class="p">,</span> <span class="n">databases</span><span class="p">):</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">request</span> <span class="ow">in</span> <span class="n">drop_db_requests_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coroutines</span><span class="p">:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                    <span class="k">continue</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>                
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>                <span class="n">db_id</span><span class="p">,</span> <span class="n">delete_db</span> <span class="o">=</span> <span class="n">request</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>                <span class="k">if</span> <span class="n">db_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">dropped_databases</span><span class="p">:</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>                        <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>                            <span class="n">txn</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">],</span> <span class="n">delete</span><span class="o">=</span><span class="n">delete_db</span><span class="p">)</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>                        
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>                    <span class="k">except</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">MapFullError</span><span class="p">:</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>                        <span class="k">raise</span> <span class="n">DBError</span><span class="o">.</span><span class="n">from_exception</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>                    
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>                    <span class="n">dropped_databases</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>                
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>                <span class="n">processed_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>                    
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">,</span> <span class="n">drop_handler</span><span class="p">)</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="c1"># get</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="k">def</span> <span class="nf">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]:</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>            <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>            <span class="k">if</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">data_cache_buff</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>                <span class="n">value</span> <span class="o">=</span> <span class="n">data_cache_buff</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>                <span class="n">value</span> <span class="o">=</span> <span class="n">txn</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>            
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>                <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>                    <span class="n">exception</span> <span class="o">=</span> <span class="n">DbKeyError</span><span class="p">(</span><span class="n">key_info</span><span class="p">)</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>                    <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>            
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>            <span class="k">return</span> <span class="n">value</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">()</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">read_queue_buff</span><span class="p">:</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>                <span class="n">value</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>            
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">set_of_key_info</span> <span class="ow">in</span> <span class="n">massive_read_queue_buff</span><span class="p">:</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>                <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>                <span class="k">for</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">set_of_key_info</span><span class="p">:</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>                    <span class="n">items</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">items</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="c1"># get all items</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">db_id</span> <span class="ow">in</span> <span class="n">get_all_items_queue_buff</span><span class="p">:</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>                    <span class="c1"># for k, v in txn.cursor(db=self.databases[db_id]):</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>                    <span class="c1">#     key = make_key_frozen(self.serializer.loads(k))</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>                    <span class="c1">#     value = self.serializer.loads(v)</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>                    <span class="c1">#     result[key] = value</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="p">{</span><span class="n">make_key_frozen</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">k</span><span class="p">)):</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])}</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>                    <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>                
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>        
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        <span class="c1"># sync</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>        
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span><span class="p">))</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="ow">or</span> <span class="p">((</span><span class="ow">not</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">))</span> <span class="ow">and</span> <span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span><span class="p">))</span> <span class="ow">and</span> <span class="p">((</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">)))</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>    
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        <span class="n">time_since_last_sync_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">&gt;</span> <span class="n">time_since_last_sync_time</span><span class="p">:</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">-</span> <span class="n">time_since_last_sync_time</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="mi">0</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>    <span class="k">def</span> <span class="nf">_init_db</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;self.path_to_db_environment: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="o">=</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span><span class="p">,</span> <span class="n">map_size</span><span class="o">=</span><span class="mi">20</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="n">writemap</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_dbs</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>                                        <span class="n">map_async</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">lock</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">metasync</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">sync</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">meminit</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="kc">None</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_db_name</span><span class="p">)</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>    
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>    <span class="k">def</span> <span class="nf">_open_db_environment</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>    <span class="k">def</span> <span class="nf">_on_set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">:</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>        
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_to_db_environment</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>    
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>    <span class="k">def</span> <span class="nf">_on_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">:</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>            <span class="c1"># self.db_environment.sync(True)</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>        
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>    
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>    <span class="k">def</span> <span class="nf">_on_get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>        
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="k">if</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">:</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">],</span> <span class="kc">None</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">key_info</span><span class="p">))</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>    
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="nf">_on_get_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>        
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="n">raw_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="ow">in</span> <span class="n">keys</span><span class="p">:</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>            <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>            
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>            <span class="n">raw_keys</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">))</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>        
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">raw_keys</span><span class="p">))</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>    
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>    <span class="k">def</span> <span class="nf">_on_get_all_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">db_id</span><span class="p">))</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>    
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>    <span class="k">def</span> <span class="nf">_on_put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>        <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>        
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>        <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>    
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>    <span class="k">def</span> <span class="nf">_on_put_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">ValueType</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>        <span class="n">result_items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>        <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">items</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>            <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>            <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>            
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>            <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>            
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>            <span class="n">result_items</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>        
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result_items</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>    
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>    <span class="k">def</span> <span class="nf">_on_delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>        <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>        
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>        <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>        
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>    
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>    <span class="k">def</span> <span class="nf">_on_delete_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">ValueType</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>        <span class="n">result_items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">items</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>            <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>            <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>            
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>            <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>            
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>            <span class="n">result_items</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>        
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result_items</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>    
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>    <span class="k">def</span> <span class="nf">_open_databases</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">DbId</span><span class="p">,</span> <span class="n">DbName</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>        <span class="k">for</span> <span class="n">db_id</span><span class="p">,</span> <span class="n">db_name</span> <span class="ow">in</span> <span class="n">db_names</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="n">db_name</span><span class="p">)</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">db_names</span><span class="p">[</span><span class="n">db_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">db_name</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>        
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>    
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>    <span class="k">def</span> <span class="nf">_drop_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">,</span> <span class="n">delete</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">db_id</span><span class="p">,</span> <span class="n">delete</span><span class="p">)</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>    
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>    <span class="k">def</span> <span class="nf">sync_in_thread_pool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db_coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>            <span class="k">if</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>                <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">,</span> <span class="kc">True</span><span class="p">))</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>                <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>                    <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>            
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>            <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">):</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>                <span class="k">def</span> <span class="nf">sync_worker</span><span class="p">():</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>                
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>                <span class="k">await</span> <span class="n">task_in_thread_pool</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">sync_worker</span><span class="p">)</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">)))</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>            <span class="k">def</span> <span class="nf">make_service_live_for_a_next_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>            
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">,</span> <span class="n">make_service_live_for_a_next_sync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>        <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>        <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span><span class="o">.</span><span class="n">inline_get</span><span class="p">()</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>        <span class="k">except</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>            <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>        <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">sync_db_coro</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">)</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a><span class="n">LmdbRequest</span><span class="o">.</span><span class="n">default_service_type</span> <span class="o">=</span> <span class="n">Lmdb</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a><span class="k">class</span> <span class="nc">DbKeyError</span><span class="p">(</span><span class="ne">KeyError</span><span class="p">):</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key_info</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">key_info</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a><span class="k">class</span> <span class="nc">DBError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">,</span> <span class="n">original_exception</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="n">db_id</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_exception</span> <span class="o">=</span> <span class="n">original_exception</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>    
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>    <span class="k">def</span> <span class="nf">from_exception</span><span class="p">(</span><span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;DBError&#39;</span><span class="p">:</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>        <span class="k">return</span> <span class="n">DBError</span><span class="p">(</span><span class="n">db_id</span><span class="p">,</span> <span class="n">get_exception</span><span class="p">())</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a><span class="k">def</span> <span class="nf">lmdb_reapplier</span><span class="p">(</span><span class="n">environment</span><span class="p">:</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">Environment</span><span class="p">,</span> <span class="n">databases</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">):</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>    <span class="n">failed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>    <span class="k">while</span> <span class="n">failed</span><span class="p">:</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>        <span class="n">need_to_resize</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>            <span class="n">handler</span><span class="p">(</span><span class="n">environment</span><span class="p">,</span> <span class="n">databases</span><span class="p">)</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>            <span class="n">failed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>        <span class="k">except</span> <span class="n">DBError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">err</span><span class="o">.</span><span class="n">original_exception</span><span class="p">,</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">MapFullError</span><span class="p">):</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>                <span class="n">need_to_resize</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>        
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>        <span class="k">if</span> <span class="n">need_to_resize</span><span class="p">:</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>            <span class="n">environment</span><span class="o">.</span><span class="n">set_mapsize</span><span class="p">(</span><span class="n">environment</span><span class="o">.</span><span class="n">info</span><span class="p">()[</span><span class="s1">&#39;map_size&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">2</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="Lmdb">
                            <input id="Lmdb-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Lmdb</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</span>, <span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</span>):

                <label class="view-source-button" for="Lmdb-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Lmdb"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Lmdb-119"><a href="#Lmdb-119"><span class="linenos">119</span></a><span class="k">class</span> <span class="nc">Lmdb</span><span class="p">(</span><span class="n">Service</span><span class="p">,</span> <span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="Lmdb-120"><a href="#Lmdb-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="Lmdb-121"><a href="#Lmdb-121"><span class="linenos">121</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Lmdb</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="Lmdb-122"><a href="#Lmdb-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_db_name</span><span class="p">:</span> <span class="n">DbName</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;__default__&#39;</span>
</span><span id="Lmdb-123"><a href="#Lmdb-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-124"><a href="#Lmdb-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">RawKeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Lmdb-125"><a href="#Lmdb-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Lmdb-126"><a href="#Lmdb-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">],</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-127"><a href="#Lmdb-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">],</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-128"><a href="#Lmdb-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Lmdb-129"><a href="#Lmdb-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_relative_to_current_dir</span><span class="p">(</span><span class="s1">&#39;lmdb.db&#39;</span><span class="p">)</span>
</span><span id="Lmdb-130"><a href="#Lmdb-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-131"><a href="#Lmdb-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-132"><a href="#Lmdb-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">DbId</span><span class="p">,</span> <span class="n">DbName</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-133"><a href="#Lmdb-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-134"><a href="#Lmdb-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="Lmdb-135"><a href="#Lmdb-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Lmdb-136"><a href="#Lmdb-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb-137"><a href="#Lmdb-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb-138"><a href="#Lmdb-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Lmdb-139"><a href="#Lmdb-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Lmdb-140"><a href="#Lmdb-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Lmdb-141"><a href="#Lmdb-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Lmdb-142"><a href="#Lmdb-142"><span class="linenos">142</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-143"><a href="#Lmdb-143"><span class="linenos">143</span></a>        <span class="c1"># self.serializer = best_serializer_for_standard_data((DataFormats.binary,</span>
</span><span id="Lmdb-144"><a href="#Lmdb-144"><span class="linenos">144</span></a>        <span class="c1">#                                    Tags.can_use_bytes,</span>
</span><span id="Lmdb-145"><a href="#Lmdb-145"><span class="linenos">145</span></a>        <span class="c1">#                                    Tags.decode_str_as_str,</span>
</span><span id="Lmdb-146"><a href="#Lmdb-146"><span class="linenos">146</span></a>        <span class="c1">#                                    Tags.decode_list_as_list,</span>
</span><span id="Lmdb-147"><a href="#Lmdb-147"><span class="linenos">147</span></a>        <span class="c1">#                                    Tags.decode_bytes_as_bytes,</span>
</span><span id="Lmdb-148"><a href="#Lmdb-148"><span class="linenos">148</span></a>        <span class="c1">#                                    Tags.superficial,</span>
</span><span id="Lmdb-149"><a href="#Lmdb-149"><span class="linenos">149</span></a>        <span class="c1">#                                    Tags.current_platform,</span>
</span><span id="Lmdb-150"><a href="#Lmdb-150"><span class="linenos">150</span></a>        <span class="c1">#                                    Tags.multi_platform),</span>
</span><span id="Lmdb-151"><a href="#Lmdb-151"><span class="linenos">151</span></a>        <span class="c1">#                                   TestDataType.small,</span>
</span><span id="Lmdb-152"><a href="#Lmdb-152"><span class="linenos">152</span></a>        <span class="c1">#                                   0.1)</span>
</span><span id="Lmdb-153"><a href="#Lmdb-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="Lmdb-154"><a href="#Lmdb-154"><span class="linenos">154</span></a>
</span><span id="Lmdb-155"><a href="#Lmdb-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Lmdb-156"><a href="#Lmdb-156"><span class="linenos">156</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_db_environment_path</span><span class="p">,</span>
</span><span id="Lmdb-157"><a href="#Lmdb-157"><span class="linenos">157</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_open_databases</span><span class="p">,</span>
</span><span id="Lmdb-158"><a href="#Lmdb-158"><span class="linenos">158</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_drop_db</span><span class="p">,</span>
</span><span id="Lmdb-159"><a href="#Lmdb-159"><span class="linenos">159</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_sync</span><span class="p">,</span>
</span><span id="Lmdb-160"><a href="#Lmdb-160"><span class="linenos">160</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="Lmdb-161"><a href="#Lmdb-161"><span class="linenos">161</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get_items</span><span class="p">,</span>
</span><span id="Lmdb-162"><a href="#Lmdb-162"><span class="linenos">162</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get_all_items</span><span class="p">,</span>
</span><span id="Lmdb-163"><a href="#Lmdb-163"><span class="linenos">163</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put</span><span class="p">,</span>
</span><span id="Lmdb-164"><a href="#Lmdb-164"><span class="linenos">164</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put_items</span><span class="p">,</span>
</span><span id="Lmdb-165"><a href="#Lmdb-165"><span class="linenos">165</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_delete</span><span class="p">,</span>
</span><span id="Lmdb-166"><a href="#Lmdb-166"><span class="linenos">166</span></a>            <span class="mi">10</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_delete_items</span><span class="p">,</span>
</span><span id="Lmdb-167"><a href="#Lmdb-167"><span class="linenos">167</span></a>            <span class="mi">11</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_open_db_environment</span><span class="p">,</span>
</span><span id="Lmdb-168"><a href="#Lmdb-168"><span class="linenos">168</span></a>        <span class="p">}</span>
</span><span id="Lmdb-169"><a href="#Lmdb-169"><span class="linenos">169</span></a>
</span><span id="Lmdb-170"><a href="#Lmdb-170"><span class="linenos">170</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="Lmdb-171"><a href="#Lmdb-171"><span class="linenos">171</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="Lmdb-172"><a href="#Lmdb-172"><span class="linenos">172</span></a>            <span class="s1">&#39;db_names&#39;</span><span class="p">:</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_names</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span>
</span><span id="Lmdb-173"><a href="#Lmdb-173"><span class="linenos">173</span></a>            <span class="s1">&#39;writes num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span><span class="p">,</span>
</span><span id="Lmdb-174"><a href="#Lmdb-174"><span class="linenos">174</span></a>            <span class="s1">&#39;reads num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span><span class="p">,</span>
</span><span id="Lmdb-175"><a href="#Lmdb-175"><span class="linenos">175</span></a>            <span class="s1">&#39;deletes num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span><span class="p">,</span>
</span><span id="Lmdb-176"><a href="#Lmdb-176"><span class="linenos">176</span></a>            <span class="s1">&#39;db drops num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span><span class="p">,</span>
</span><span id="Lmdb-177"><a href="#Lmdb-177"><span class="linenos">177</span></a>        <span class="p">}</span>
</span><span id="Lmdb-178"><a href="#Lmdb-178"><span class="linenos">178</span></a>
</span><span id="Lmdb-179"><a href="#Lmdb-179"><span class="linenos">179</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="Lmdb-180"><a href="#Lmdb-180"><span class="linenos">180</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-181"><a href="#Lmdb-181"><span class="linenos">181</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">try_resolve_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Lmdb-182"><a href="#Lmdb-182"><span class="linenos">182</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb-183"><a href="#Lmdb-183"><span class="linenos">183</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-184"><a href="#Lmdb-184"><span class="linenos">184</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb-185"><a href="#Lmdb-185"><span class="linenos">185</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="Lmdb-186"><a href="#Lmdb-186"><span class="linenos">186</span></a>
</span><span id="Lmdb-187"><a href="#Lmdb-187"><span class="linenos">187</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Lmdb-188"><a href="#Lmdb-188"><span class="linenos">188</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb-189"><a href="#Lmdb-189"><span class="linenos">189</span></a>        
</span><span id="Lmdb-190"><a href="#Lmdb-190"><span class="linenos">190</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb-191"><a href="#Lmdb-191"><span class="linenos">191</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="Lmdb-192"><a href="#Lmdb-192"><span class="linenos">192</span></a>
</span><span id="Lmdb-193"><a href="#Lmdb-193"><span class="linenos">193</span></a>        <span class="n">data_cache_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span>
</span><span id="Lmdb-194"><a href="#Lmdb-194"><span class="linenos">194</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">data_cache_buff</span><span class="p">)()</span>
</span><span id="Lmdb-195"><a href="#Lmdb-195"><span class="linenos">195</span></a>        
</span><span id="Lmdb-196"><a href="#Lmdb-196"><span class="linenos">196</span></a>        <span class="n">read_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span>
</span><span id="Lmdb-197"><a href="#Lmdb-197"><span class="linenos">197</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">read_queue_buff</span><span class="p">)()</span>
</span><span id="Lmdb-198"><a href="#Lmdb-198"><span class="linenos">198</span></a>        
</span><span id="Lmdb-199"><a href="#Lmdb-199"><span class="linenos">199</span></a>        <span class="n">massive_read_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span>
</span><span id="Lmdb-200"><a href="#Lmdb-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">massive_read_queue_buff</span><span class="p">)()</span>
</span><span id="Lmdb-201"><a href="#Lmdb-201"><span class="linenos">201</span></a>        
</span><span id="Lmdb-202"><a href="#Lmdb-202"><span class="linenos">202</span></a>        <span class="n">deletion_cache_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span>
</span><span id="Lmdb-203"><a href="#Lmdb-203"><span class="linenos">203</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">deletion_cache_buff</span><span class="p">)()</span>
</span><span id="Lmdb-204"><a href="#Lmdb-204"><span class="linenos">204</span></a>        
</span><span id="Lmdb-205"><a href="#Lmdb-205"><span class="linenos">205</span></a>        <span class="n">get_all_items_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span>
</span><span id="Lmdb-206"><a href="#Lmdb-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">get_all_items_queue_buff</span><span class="p">)()</span>
</span><span id="Lmdb-207"><a href="#Lmdb-207"><span class="linenos">207</span></a>
</span><span id="Lmdb-208"><a href="#Lmdb-208"><span class="linenos">208</span></a>        <span class="c1"># put</span>
</span><span id="Lmdb-209"><a href="#Lmdb-209"><span class="linenos">209</span></a>        <span class="k">def</span> <span class="nf">put_handler</span><span class="p">(</span><span class="n">db_environment</span><span class="p">,</span> <span class="n">databases</span><span class="p">):</span>
</span><span id="Lmdb-210"><a href="#Lmdb-210"><span class="linenos">210</span></a>            <span class="n">db_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-211"><a href="#Lmdb-211"><span class="linenos">211</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-212"><a href="#Lmdb-212"><span class="linenos">212</span></a>                <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb-213"><a href="#Lmdb-213"><span class="linenos">213</span></a>                    <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">data_cache_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb-214"><a href="#Lmdb-214"><span class="linenos">214</span></a>                        <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="Lmdb-215"><a href="#Lmdb-215"><span class="linenos">215</span></a>                        <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">],</span> <span class="n">dupdata</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="Lmdb-216"><a href="#Lmdb-216"><span class="linenos">216</span></a>
</span><span id="Lmdb-217"><a href="#Lmdb-217"><span class="linenos">217</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="Lmdb-218"><a href="#Lmdb-218"><span class="linenos">218</span></a>            <span class="k">except</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">MapFullError</span><span class="p">:</span>
</span><span id="Lmdb-219"><a href="#Lmdb-219"><span class="linenos">219</span></a>                <span class="k">raise</span> <span class="n">DBError</span><span class="o">.</span><span class="n">from_exception</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb-220"><a href="#Lmdb-220"><span class="linenos">220</span></a>        
</span><span id="Lmdb-221"><a href="#Lmdb-221"><span class="linenos">221</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">,</span> <span class="n">put_handler</span><span class="p">)</span>
</span><span id="Lmdb-222"><a href="#Lmdb-222"><span class="linenos">222</span></a>        
</span><span id="Lmdb-223"><a href="#Lmdb-223"><span class="linenos">223</span></a>        <span class="c1"># delete</span>
</span><span id="Lmdb-224"><a href="#Lmdb-224"><span class="linenos">224</span></a>        <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">deletion_cache_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb-225"><a href="#Lmdb-225"><span class="linenos">225</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb-226"><a href="#Lmdb-226"><span class="linenos">226</span></a>                <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="Lmdb-227"><a href="#Lmdb-227"><span class="linenos">227</span></a>                <span class="n">txn</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span>
</span><span id="Lmdb-228"><a href="#Lmdb-228"><span class="linenos">228</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Lmdb-229"><a href="#Lmdb-229"><span class="linenos">229</span></a>
</span><span id="Lmdb-230"><a href="#Lmdb-230"><span class="linenos">230</span></a>        <span class="c1"># drop</span>
</span><span id="Lmdb-231"><a href="#Lmdb-231"><span class="linenos">231</span></a>        <span class="n">drop_db_requests_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span>
</span><span id="Lmdb-232"><a href="#Lmdb-232"><span class="linenos">232</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">drop_db_requests_buff</span><span class="p">)()</span>
</span><span id="Lmdb-233"><a href="#Lmdb-233"><span class="linenos">233</span></a>        <span class="n">dropped_databases</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="Lmdb-234"><a href="#Lmdb-234"><span class="linenos">234</span></a>        <span class="n">processed_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="Lmdb-235"><a href="#Lmdb-235"><span class="linenos">235</span></a>        
</span><span id="Lmdb-236"><a href="#Lmdb-236"><span class="linenos">236</span></a>        <span class="k">def</span> <span class="nf">drop_handler</span><span class="p">(</span><span class="n">db_environment</span><span class="p">,</span> <span class="n">databases</span><span class="p">):</span>
</span><span id="Lmdb-237"><a href="#Lmdb-237"><span class="linenos">237</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">request</span> <span class="ow">in</span> <span class="n">drop_db_requests_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb-238"><a href="#Lmdb-238"><span class="linenos">238</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coroutines</span><span class="p">:</span>
</span><span id="Lmdb-239"><a href="#Lmdb-239"><span class="linenos">239</span></a>                    <span class="k">continue</span>
</span><span id="Lmdb-240"><a href="#Lmdb-240"><span class="linenos">240</span></a>                
</span><span id="Lmdb-241"><a href="#Lmdb-241"><span class="linenos">241</span></a>                <span class="n">db_id</span><span class="p">,</span> <span class="n">delete_db</span> <span class="o">=</span> <span class="n">request</span>
</span><span id="Lmdb-242"><a href="#Lmdb-242"><span class="linenos">242</span></a>                <span class="k">if</span> <span class="n">db_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">dropped_databases</span><span class="p">:</span>
</span><span id="Lmdb-243"><a href="#Lmdb-243"><span class="linenos">243</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-244"><a href="#Lmdb-244"><span class="linenos">244</span></a>                        <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb-245"><a href="#Lmdb-245"><span class="linenos">245</span></a>                            <span class="n">txn</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">],</span> <span class="n">delete</span><span class="o">=</span><span class="n">delete_db</span><span class="p">)</span>
</span><span id="Lmdb-246"><a href="#Lmdb-246"><span class="linenos">246</span></a>                        
</span><span id="Lmdb-247"><a href="#Lmdb-247"><span class="linenos">247</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Lmdb-248"><a href="#Lmdb-248"><span class="linenos">248</span></a>                    <span class="k">except</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">MapFullError</span><span class="p">:</span>
</span><span id="Lmdb-249"><a href="#Lmdb-249"><span class="linenos">249</span></a>                        <span class="k">raise</span> <span class="n">DBError</span><span class="o">.</span><span class="n">from_exception</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb-250"><a href="#Lmdb-250"><span class="linenos">250</span></a>                    
</span><span id="Lmdb-251"><a href="#Lmdb-251"><span class="linenos">251</span></a>                    <span class="n">dropped_databases</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb-252"><a href="#Lmdb-252"><span class="linenos">252</span></a>                
</span><span id="Lmdb-253"><a href="#Lmdb-253"><span class="linenos">253</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Lmdb-254"><a href="#Lmdb-254"><span class="linenos">254</span></a>                <span class="n">processed_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="Lmdb-255"><a href="#Lmdb-255"><span class="linenos">255</span></a>                    
</span><span id="Lmdb-256"><a href="#Lmdb-256"><span class="linenos">256</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">,</span> <span class="n">drop_handler</span><span class="p">)</span>
</span><span id="Lmdb-257"><a href="#Lmdb-257"><span class="linenos">257</span></a>
</span><span id="Lmdb-258"><a href="#Lmdb-258"><span class="linenos">258</span></a>        <span class="c1"># get</span>
</span><span id="Lmdb-259"><a href="#Lmdb-259"><span class="linenos">259</span></a>        <span class="k">def</span> <span class="nf">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]:</span>
</span><span id="Lmdb-260"><a href="#Lmdb-260"><span class="linenos">260</span></a>            <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="Lmdb-261"><a href="#Lmdb-261"><span class="linenos">261</span></a>            <span class="k">if</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">data_cache_buff</span><span class="p">:</span>
</span><span id="Lmdb-262"><a href="#Lmdb-262"><span class="linenos">262</span></a>                <span class="n">value</span> <span class="o">=</span> <span class="n">data_cache_buff</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span>
</span><span id="Lmdb-263"><a href="#Lmdb-263"><span class="linenos">263</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb-264"><a href="#Lmdb-264"><span class="linenos">264</span></a>                <span class="n">value</span> <span class="o">=</span> <span class="n">txn</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span>
</span><span id="Lmdb-265"><a href="#Lmdb-265"><span class="linenos">265</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Lmdb-266"><a href="#Lmdb-266"><span class="linenos">266</span></a>            
</span><span id="Lmdb-267"><a href="#Lmdb-267"><span class="linenos">267</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-268"><a href="#Lmdb-268"><span class="linenos">268</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-269"><a href="#Lmdb-269"><span class="linenos">269</span></a>                <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb-270"><a href="#Lmdb-270"><span class="linenos">270</span></a>                    <span class="n">exception</span> <span class="o">=</span> <span class="n">DbKeyError</span><span class="p">(</span><span class="n">key_info</span><span class="p">)</span>
</span><span id="Lmdb-271"><a href="#Lmdb-271"><span class="linenos">271</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb-272"><a href="#Lmdb-272"><span class="linenos">272</span></a>                    <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="Lmdb-273"><a href="#Lmdb-273"><span class="linenos">273</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb-274"><a href="#Lmdb-274"><span class="linenos">274</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb-275"><a href="#Lmdb-275"><span class="linenos">275</span></a>            
</span><span id="Lmdb-276"><a href="#Lmdb-276"><span class="linenos">276</span></a>            <span class="k">return</span> <span class="n">value</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="Lmdb-277"><a href="#Lmdb-277"><span class="linenos">277</span></a>            
</span><span id="Lmdb-278"><a href="#Lmdb-278"><span class="linenos">278</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">()</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb-279"><a href="#Lmdb-279"><span class="linenos">279</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">read_queue_buff</span><span class="p">:</span>
</span><span id="Lmdb-280"><a href="#Lmdb-280"><span class="linenos">280</span></a>                <span class="n">value</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="Lmdb-281"><a href="#Lmdb-281"><span class="linenos">281</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="Lmdb-282"><a href="#Lmdb-282"><span class="linenos">282</span></a>            
</span><span id="Lmdb-283"><a href="#Lmdb-283"><span class="linenos">283</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">set_of_key_info</span> <span class="ow">in</span> <span class="n">massive_read_queue_buff</span><span class="p">:</span>
</span><span id="Lmdb-284"><a href="#Lmdb-284"><span class="linenos">284</span></a>                <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-285"><a href="#Lmdb-285"><span class="linenos">285</span></a>                <span class="k">for</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">set_of_key_info</span><span class="p">:</span>
</span><span id="Lmdb-286"><a href="#Lmdb-286"><span class="linenos">286</span></a>                    <span class="n">items</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="Lmdb-287"><a href="#Lmdb-287"><span class="linenos">287</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">items</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Lmdb-288"><a href="#Lmdb-288"><span class="linenos">288</span></a>
</span><span id="Lmdb-289"><a href="#Lmdb-289"><span class="linenos">289</span></a>        <span class="c1"># get all items</span>
</span><span id="Lmdb-290"><a href="#Lmdb-290"><span class="linenos">290</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">db_id</span> <span class="ow">in</span> <span class="n">get_all_items_queue_buff</span><span class="p">:</span>
</span><span id="Lmdb-291"><a href="#Lmdb-291"><span class="linenos">291</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb-292"><a href="#Lmdb-292"><span class="linenos">292</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-293"><a href="#Lmdb-293"><span class="linenos">293</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-294"><a href="#Lmdb-294"><span class="linenos">294</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-295"><a href="#Lmdb-295"><span class="linenos">295</span></a>                    <span class="c1"># for k, v in txn.cursor(db=self.databases[db_id]):</span>
</span><span id="Lmdb-296"><a href="#Lmdb-296"><span class="linenos">296</span></a>                    <span class="c1">#     key = make_key_frozen(self.serializer.loads(k))</span>
</span><span id="Lmdb-297"><a href="#Lmdb-297"><span class="linenos">297</span></a>                    <span class="c1">#     value = self.serializer.loads(v)</span>
</span><span id="Lmdb-298"><a href="#Lmdb-298"><span class="linenos">298</span></a>                    <span class="c1">#     result[key] = value</span>
</span><span id="Lmdb-299"><a href="#Lmdb-299"><span class="linenos">299</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="p">{</span><span class="n">make_key_frozen</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">k</span><span class="p">)):</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])}</span>
</span><span id="Lmdb-300"><a href="#Lmdb-300"><span class="linenos">300</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="Lmdb-301"><a href="#Lmdb-301"><span class="linenos">301</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb-302"><a href="#Lmdb-302"><span class="linenos">302</span></a>                    <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb-303"><a href="#Lmdb-303"><span class="linenos">303</span></a>                
</span><span id="Lmdb-304"><a href="#Lmdb-304"><span class="linenos">304</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="Lmdb-305"><a href="#Lmdb-305"><span class="linenos">305</span></a>        
</span><span id="Lmdb-306"><a href="#Lmdb-306"><span class="linenos">306</span></a>        <span class="c1"># sync</span>
</span><span id="Lmdb-307"><a href="#Lmdb-307"><span class="linenos">307</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="Lmdb-308"><a href="#Lmdb-308"><span class="linenos">308</span></a>        
</span><span id="Lmdb-309"><a href="#Lmdb-309"><span class="linenos">309</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Lmdb-310"><a href="#Lmdb-310"><span class="linenos">310</span></a>
</span><span id="Lmdb-311"><a href="#Lmdb-311"><span class="linenos">311</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span><span id="Lmdb-312"><a href="#Lmdb-312"><span class="linenos">312</span></a>
</span><span id="Lmdb-313"><a href="#Lmdb-313"><span class="linenos">313</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Lmdb-314"><a href="#Lmdb-314"><span class="linenos">314</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span><span class="p">))</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="ow">or</span> <span class="p">((</span><span class="ow">not</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">))</span> <span class="ow">and</span> <span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span><span class="p">))</span> <span class="ow">and</span> <span class="p">((</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">)))</span>
</span><span id="Lmdb-315"><a href="#Lmdb-315"><span class="linenos">315</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="Lmdb-316"><a href="#Lmdb-316"><span class="linenos">316</span></a>    
</span><span id="Lmdb-317"><a href="#Lmdb-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="Lmdb-318"><a href="#Lmdb-318"><span class="linenos">318</span></a>        <span class="n">time_since_last_sync_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span>
</span><span id="Lmdb-319"><a href="#Lmdb-319"><span class="linenos">319</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">&gt;</span> <span class="n">time_since_last_sync_time</span><span class="p">:</span>
</span><span id="Lmdb-320"><a href="#Lmdb-320"><span class="linenos">320</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">-</span> <span class="n">time_since_last_sync_time</span>
</span><span id="Lmdb-321"><a href="#Lmdb-321"><span class="linenos">321</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb-322"><a href="#Lmdb-322"><span class="linenos">322</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="mi">0</span>
</span><span id="Lmdb-323"><a href="#Lmdb-323"><span class="linenos">323</span></a>
</span><span id="Lmdb-324"><a href="#Lmdb-324"><span class="linenos">324</span></a>    <span class="k">def</span> <span class="nf">_init_db</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Lmdb-325"><a href="#Lmdb-325"><span class="linenos">325</span></a>        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;self.path_to_db_environment: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="Lmdb-326"><a href="#Lmdb-326"><span class="linenos">326</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="o">=</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span><span class="p">,</span> <span class="n">map_size</span><span class="o">=</span><span class="mi">20</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span><span class="p">,</span> <span class="n">writemap</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">max_dbs</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
</span><span id="Lmdb-327"><a href="#Lmdb-327"><span class="linenos">327</span></a>                                        <span class="n">map_async</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">lock</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">metasync</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">sync</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">meminit</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="Lmdb-328"><a href="#Lmdb-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="kc">None</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_db_name</span><span class="p">)</span>
</span><span id="Lmdb-329"><a href="#Lmdb-329"><span class="linenos">329</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Lmdb-330"><a href="#Lmdb-330"><span class="linenos">330</span></a>    
</span><span id="Lmdb-331"><a href="#Lmdb-331"><span class="linenos">331</span></a>    <span class="k">def</span> <span class="nf">_open_db_environment</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-332"><a href="#Lmdb-332"><span class="linenos">332</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="Lmdb-333"><a href="#Lmdb-333"><span class="linenos">333</span></a>
</span><span id="Lmdb-334"><a href="#Lmdb-334"><span class="linenos">334</span></a>    <span class="k">def</span> <span class="nf">_on_set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-335"><a href="#Lmdb-335"><span class="linenos">335</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">:</span>
</span><span id="Lmdb-336"><a href="#Lmdb-336"><span class="linenos">336</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-337"><a href="#Lmdb-337"><span class="linenos">337</span></a>        
</span><span id="Lmdb-338"><a href="#Lmdb-338"><span class="linenos">338</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb-339"><a href="#Lmdb-339"><span class="linenos">339</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_to_db_environment</span>
</span><span id="Lmdb-340"><a href="#Lmdb-340"><span class="linenos">340</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-341"><a href="#Lmdb-341"><span class="linenos">341</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="Lmdb-342"><a href="#Lmdb-342"><span class="linenos">342</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb-343"><a href="#Lmdb-343"><span class="linenos">343</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb-344"><a href="#Lmdb-344"><span class="linenos">344</span></a>                <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="Lmdb-345"><a href="#Lmdb-345"><span class="linenos">345</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-346"><a href="#Lmdb-346"><span class="linenos">346</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb-347"><a href="#Lmdb-347"><span class="linenos">347</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-348"><a href="#Lmdb-348"><span class="linenos">348</span></a>    
</span><span id="Lmdb-349"><a href="#Lmdb-349"><span class="linenos">349</span></a>    <span class="k">def</span> <span class="nf">_on_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-350"><a href="#Lmdb-350"><span class="linenos">350</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">:</span>
</span><span id="Lmdb-351"><a href="#Lmdb-351"><span class="linenos">351</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Lmdb-352"><a href="#Lmdb-352"><span class="linenos">352</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-353"><a href="#Lmdb-353"><span class="linenos">353</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb-354"><a href="#Lmdb-354"><span class="linenos">354</span></a>            <span class="c1"># self.db_environment.sync(True)</span>
</span><span id="Lmdb-355"><a href="#Lmdb-355"><span class="linenos">355</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="Lmdb-356"><a href="#Lmdb-356"><span class="linenos">356</span></a>        
</span><span id="Lmdb-357"><a href="#Lmdb-357"><span class="linenos">357</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-358"><a href="#Lmdb-358"><span class="linenos">358</span></a>    
</span><span id="Lmdb-359"><a href="#Lmdb-359"><span class="linenos">359</span></a>    <span class="k">def</span> <span class="nf">_on_get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-360"><a href="#Lmdb-360"><span class="linenos">360</span></a>        <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="Lmdb-361"><a href="#Lmdb-361"><span class="linenos">361</span></a>        
</span><span id="Lmdb-362"><a href="#Lmdb-362"><span class="linenos">362</span></a>        <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb-363"><a href="#Lmdb-363"><span class="linenos">363</span></a>        <span class="k">if</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">:</span>
</span><span id="Lmdb-364"><a href="#Lmdb-364"><span class="linenos">364</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">],</span> <span class="kc">None</span>
</span><span id="Lmdb-365"><a href="#Lmdb-365"><span class="linenos">365</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb-366"><a href="#Lmdb-366"><span class="linenos">366</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">key_info</span><span class="p">))</span>
</span><span id="Lmdb-367"><a href="#Lmdb-367"><span class="linenos">367</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-368"><a href="#Lmdb-368"><span class="linenos">368</span></a>            <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-369"><a href="#Lmdb-369"><span class="linenos">369</span></a>    
</span><span id="Lmdb-370"><a href="#Lmdb-370"><span class="linenos">370</span></a>    <span class="k">def</span> <span class="nf">_on_get_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-371"><a href="#Lmdb-371"><span class="linenos">371</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="Lmdb-372"><a href="#Lmdb-372"><span class="linenos">372</span></a>        
</span><span id="Lmdb-373"><a href="#Lmdb-373"><span class="linenos">373</span></a>        <span class="n">raw_keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="Lmdb-374"><a href="#Lmdb-374"><span class="linenos">374</span></a>        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="ow">in</span> <span class="n">keys</span><span class="p">:</span>
</span><span id="Lmdb-375"><a href="#Lmdb-375"><span class="linenos">375</span></a>            <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="Lmdb-376"><a href="#Lmdb-376"><span class="linenos">376</span></a>            
</span><span id="Lmdb-377"><a href="#Lmdb-377"><span class="linenos">377</span></a>            <span class="n">raw_keys</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">))</span>
</span><span id="Lmdb-378"><a href="#Lmdb-378"><span class="linenos">378</span></a>        
</span><span id="Lmdb-379"><a href="#Lmdb-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">raw_keys</span><span class="p">))</span>
</span><span id="Lmdb-380"><a href="#Lmdb-380"><span class="linenos">380</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-381"><a href="#Lmdb-381"><span class="linenos">381</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-382"><a href="#Lmdb-382"><span class="linenos">382</span></a>    
</span><span id="Lmdb-383"><a href="#Lmdb-383"><span class="linenos">383</span></a>    <span class="k">def</span> <span class="nf">_on_get_all_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-384"><a href="#Lmdb-384"><span class="linenos">384</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="Lmdb-385"><a href="#Lmdb-385"><span class="linenos">385</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">db_id</span><span class="p">))</span>
</span><span id="Lmdb-386"><a href="#Lmdb-386"><span class="linenos">386</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-387"><a href="#Lmdb-387"><span class="linenos">387</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-388"><a href="#Lmdb-388"><span class="linenos">388</span></a>    
</span><span id="Lmdb-389"><a href="#Lmdb-389"><span class="linenos">389</span></a>    <span class="k">def</span> <span class="nf">_on_put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-390"><a href="#Lmdb-390"><span class="linenos">390</span></a>        <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="Lmdb-391"><a href="#Lmdb-391"><span class="linenos">391</span></a>        
</span><span id="Lmdb-392"><a href="#Lmdb-392"><span class="linenos">392</span></a>        <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb-393"><a href="#Lmdb-393"><span class="linenos">393</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-394"><a href="#Lmdb-394"><span class="linenos">394</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-395"><a href="#Lmdb-395"><span class="linenos">395</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-396"><a href="#Lmdb-396"><span class="linenos">396</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="Lmdb-397"><a href="#Lmdb-397"><span class="linenos">397</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb-398"><a href="#Lmdb-398"><span class="linenos">398</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb-399"><a href="#Lmdb-399"><span class="linenos">399</span></a>        
</span><span id="Lmdb-400"><a href="#Lmdb-400"><span class="linenos">400</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-401"><a href="#Lmdb-401"><span class="linenos">401</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="Lmdb-402"><a href="#Lmdb-402"><span class="linenos">402</span></a>    
</span><span id="Lmdb-403"><a href="#Lmdb-403"><span class="linenos">403</span></a>    <span class="k">def</span> <span class="nf">_on_put_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">ValueType</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-404"><a href="#Lmdb-404"><span class="linenos">404</span></a>        <span class="n">result_items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-405"><a href="#Lmdb-405"><span class="linenos">405</span></a>        <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">items</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb-406"><a href="#Lmdb-406"><span class="linenos">406</span></a>            <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="Lmdb-407"><a href="#Lmdb-407"><span class="linenos">407</span></a>            <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="Lmdb-408"><a href="#Lmdb-408"><span class="linenos">408</span></a>            
</span><span id="Lmdb-409"><a href="#Lmdb-409"><span class="linenos">409</span></a>            <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb-410"><a href="#Lmdb-410"><span class="linenos">410</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-411"><a href="#Lmdb-411"><span class="linenos">411</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-412"><a href="#Lmdb-412"><span class="linenos">412</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-413"><a href="#Lmdb-413"><span class="linenos">413</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="Lmdb-414"><a href="#Lmdb-414"><span class="linenos">414</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb-415"><a href="#Lmdb-415"><span class="linenos">415</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb-416"><a href="#Lmdb-416"><span class="linenos">416</span></a>            
</span><span id="Lmdb-417"><a href="#Lmdb-417"><span class="linenos">417</span></a>            <span class="n">result_items</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="Lmdb-418"><a href="#Lmdb-418"><span class="linenos">418</span></a>        
</span><span id="Lmdb-419"><a href="#Lmdb-419"><span class="linenos">419</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-420"><a href="#Lmdb-420"><span class="linenos">420</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result_items</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-421"><a href="#Lmdb-421"><span class="linenos">421</span></a>    
</span><span id="Lmdb-422"><a href="#Lmdb-422"><span class="linenos">422</span></a>    <span class="k">def</span> <span class="nf">_on_delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-423"><a href="#Lmdb-423"><span class="linenos">423</span></a>        <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="Lmdb-424"><a href="#Lmdb-424"><span class="linenos">424</span></a>        
</span><span id="Lmdb-425"><a href="#Lmdb-425"><span class="linenos">425</span></a>        <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb-426"><a href="#Lmdb-426"><span class="linenos">426</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-427"><a href="#Lmdb-427"><span class="linenos">427</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-428"><a href="#Lmdb-428"><span class="linenos">428</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-429"><a href="#Lmdb-429"><span class="linenos">429</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="Lmdb-430"><a href="#Lmdb-430"><span class="linenos">430</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb-431"><a href="#Lmdb-431"><span class="linenos">431</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb-432"><a href="#Lmdb-432"><span class="linenos">432</span></a>        
</span><span id="Lmdb-433"><a href="#Lmdb-433"><span class="linenos">433</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-434"><a href="#Lmdb-434"><span class="linenos">434</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="Lmdb-435"><a href="#Lmdb-435"><span class="linenos">435</span></a>    
</span><span id="Lmdb-436"><a href="#Lmdb-436"><span class="linenos">436</span></a>    <span class="k">def</span> <span class="nf">_on_delete_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">ValueType</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-437"><a href="#Lmdb-437"><span class="linenos">437</span></a>        <span class="n">result_items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb-438"><a href="#Lmdb-438"><span class="linenos">438</span></a>        <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">items</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb-439"><a href="#Lmdb-439"><span class="linenos">439</span></a>            <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="Lmdb-440"><a href="#Lmdb-440"><span class="linenos">440</span></a>            <span class="n">key</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</span><span id="Lmdb-441"><a href="#Lmdb-441"><span class="linenos">441</span></a>            
</span><span id="Lmdb-442"><a href="#Lmdb-442"><span class="linenos">442</span></a>            <span class="n">key_info</span> <span class="o">=</span> <span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb-443"><a href="#Lmdb-443"><span class="linenos">443</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-444"><a href="#Lmdb-444"><span class="linenos">444</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-445"><a href="#Lmdb-445"><span class="linenos">445</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-446"><a href="#Lmdb-446"><span class="linenos">446</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="Lmdb-447"><a href="#Lmdb-447"><span class="linenos">447</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb-448"><a href="#Lmdb-448"><span class="linenos">448</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb-449"><a href="#Lmdb-449"><span class="linenos">449</span></a>            
</span><span id="Lmdb-450"><a href="#Lmdb-450"><span class="linenos">450</span></a>            <span class="n">result_items</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="Lmdb-451"><a href="#Lmdb-451"><span class="linenos">451</span></a>        
</span><span id="Lmdb-452"><a href="#Lmdb-452"><span class="linenos">452</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-453"><a href="#Lmdb-453"><span class="linenos">453</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="n">result_items</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-454"><a href="#Lmdb-454"><span class="linenos">454</span></a>    
</span><span id="Lmdb-455"><a href="#Lmdb-455"><span class="linenos">455</span></a>    <span class="k">def</span> <span class="nf">_open_databases</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">DbId</span><span class="p">,</span> <span class="n">DbName</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-456"><a href="#Lmdb-456"><span class="linenos">456</span></a>        <span class="k">for</span> <span class="n">db_id</span><span class="p">,</span> <span class="n">db_name</span> <span class="ow">in</span> <span class="n">db_names</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb-457"><a href="#Lmdb-457"><span class="linenos">457</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">open_db</span><span class="p">(</span><span class="n">db_name</span><span class="p">)</span>
</span><span id="Lmdb-458"><a href="#Lmdb-458"><span class="linenos">458</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">db_names</span><span class="p">[</span><span class="n">db_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">db_name</span>
</span><span id="Lmdb-459"><a href="#Lmdb-459"><span class="linenos">459</span></a>        
</span><span id="Lmdb-460"><a href="#Lmdb-460"><span class="linenos">460</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Lmdb-461"><a href="#Lmdb-461"><span class="linenos">461</span></a>        <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-462"><a href="#Lmdb-462"><span class="linenos">462</span></a>    
</span><span id="Lmdb-463"><a href="#Lmdb-463"><span class="linenos">463</span></a>    <span class="k">def</span> <span class="nf">_drop_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">,</span> <span class="n">delete</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb-464"><a href="#Lmdb-464"><span class="linenos">464</span></a>        <span class="n">coro_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_caller_coro_info</span><span class="o">.</span><span class="n">coro_id</span>
</span><span id="Lmdb-465"><a href="#Lmdb-465"><span class="linenos">465</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span><span class="p">[</span><span class="n">coro_id</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">db_id</span><span class="p">,</span> <span class="n">delete</span><span class="p">)</span>
</span><span id="Lmdb-466"><a href="#Lmdb-466"><span class="linenos">466</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-467"><a href="#Lmdb-467"><span class="linenos">467</span></a>        <span class="k">return</span> <span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb-468"><a href="#Lmdb-468"><span class="linenos">468</span></a>    
</span><span id="Lmdb-469"><a href="#Lmdb-469"><span class="linenos">469</span></a>    <span class="k">def</span> <span class="nf">sync_in_thread_pool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Lmdb-470"><a href="#Lmdb-470"><span class="linenos">470</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db_coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="Lmdb-471"><a href="#Lmdb-471"><span class="linenos">471</span></a>            <span class="k">if</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span>
</span><span id="Lmdb-472"><a href="#Lmdb-472"><span class="linenos">472</span></a>                <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">,</span> <span class="kc">True</span><span class="p">))</span>
</span><span id="Lmdb-473"><a href="#Lmdb-473"><span class="linenos">473</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb-474"><a href="#Lmdb-474"><span class="linenos">474</span></a>                <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb-475"><a href="#Lmdb-475"><span class="linenos">475</span></a>                    <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="Lmdb-476"><a href="#Lmdb-476"><span class="linenos">476</span></a>            
</span><span id="Lmdb-477"><a href="#Lmdb-477"><span class="linenos">477</span></a>            <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">):</span>
</span><span id="Lmdb-478"><a href="#Lmdb-478"><span class="linenos">478</span></a>                <span class="k">def</span> <span class="nf">sync_worker</span><span class="p">():</span>
</span><span id="Lmdb-479"><a href="#Lmdb-479"><span class="linenos">479</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Lmdb-480"><a href="#Lmdb-480"><span class="linenos">480</span></a>                
</span><span id="Lmdb-481"><a href="#Lmdb-481"><span class="linenos">481</span></a>                <span class="k">await</span> <span class="n">task_in_thread_pool</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">sync_worker</span><span class="p">)</span>
</span><span id="Lmdb-482"><a href="#Lmdb-482"><span class="linenos">482</span></a>
</span><span id="Lmdb-483"><a href="#Lmdb-483"><span class="linenos">483</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">)))</span>
</span><span id="Lmdb-484"><a href="#Lmdb-484"><span class="linenos">484</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-485"><a href="#Lmdb-485"><span class="linenos">485</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb-486"><a href="#Lmdb-486"><span class="linenos">486</span></a>            <span class="k">def</span> <span class="nf">make_service_live_for_a_next_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Lmdb-487"><a href="#Lmdb-487"><span class="linenos">487</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb-488"><a href="#Lmdb-488"><span class="linenos">488</span></a>            
</span><span id="Lmdb-489"><a href="#Lmdb-489"><span class="linenos">489</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">,</span> <span class="n">make_service_live_for_a_next_sync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="Lmdb-490"><a href="#Lmdb-490"><span class="linenos">490</span></a>
</span><span id="Lmdb-491"><a href="#Lmdb-491"><span class="linenos">491</span></a>        <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb-492"><a href="#Lmdb-492"><span class="linenos">492</span></a>        <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb-493"><a href="#Lmdb-493"><span class="linenos">493</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb-494"><a href="#Lmdb-494"><span class="linenos">494</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span><span class="o">.</span><span class="n">inline_get</span><span class="p">()</span>
</span><span id="Lmdb-495"><a href="#Lmdb-495"><span class="linenos">495</span></a>        <span class="k">except</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">:</span>
</span><span id="Lmdb-496"><a href="#Lmdb-496"><span class="linenos">496</span></a>            <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Lmdb-497"><a href="#Lmdb-497"><span class="linenos">497</span></a>
</span><span id="Lmdb-498"><a href="#Lmdb-498"><span class="linenos">498</span></a>        <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">sync_db_coro</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">)</span>
</span><span id="Lmdb-499"><a href="#Lmdb-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Lmdb-500"><a href="#Lmdb-500"><span class="linenos">500</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span></pre></div>


    

                            <div id="Lmdb.__init__" class="classattr">
                                        <input id="Lmdb.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Lmdb</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="Lmdb.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Lmdb.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Lmdb.__init__-120"><a href="#Lmdb.__init__-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">):</span>
</span><span id="Lmdb.__init__-121"><a href="#Lmdb.__init__-121"><span class="linenos">121</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">Lmdb</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">loop</span><span class="p">)</span>
</span><span id="Lmdb.__init__-122"><a href="#Lmdb.__init__-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_db_name</span><span class="p">:</span> <span class="n">DbName</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;__default__&#39;</span>
</span><span id="Lmdb.__init__-123"><a href="#Lmdb.__init__-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb.__init__-124"><a href="#Lmdb.__init__-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">RawKeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Lmdb.__init__-125"><a href="#Lmdb.__init__-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Lmdb.__init__-126"><a href="#Lmdb.__init__-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">],</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb.__init__-127"><a href="#Lmdb.__init__-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">],</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb.__init__-128"><a href="#Lmdb.__init__-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">CoroID</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="Lmdb.__init__-129"><a href="#Lmdb.__init__-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">path_to_db_environment</span> <span class="o">=</span> <span class="n">path_relative_to_current_dir</span><span class="p">(</span><span class="s1">&#39;lmdb.db&#39;</span><span class="p">)</span>
</span><span id="Lmdb.__init__-130"><a href="#Lmdb.__init__-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb.__init__-131"><a href="#Lmdb.__init__-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb.__init__-132"><a href="#Lmdb.__init__-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">DbId</span><span class="p">,</span> <span class="n">DbName</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb.__init__-133"><a href="#Lmdb.__init__-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">async_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb.__init__-134"><a href="#Lmdb.__init__-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="Lmdb.__init__-135"><a href="#Lmdb.__init__-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Lmdb.__init__-136"><a href="#Lmdb.__init__-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb.__init__-137"><a href="#Lmdb.__init__-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb.__init__-138"><a href="#Lmdb.__init__-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Lmdb.__init__-139"><a href="#Lmdb.__init__-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Lmdb.__init__-140"><a href="#Lmdb.__init__-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Lmdb.__init__-141"><a href="#Lmdb.__init__-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Lmdb.__init__-142"><a href="#Lmdb.__init__-142"><span class="linenos">142</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb.__init__-143"><a href="#Lmdb.__init__-143"><span class="linenos">143</span></a>        <span class="c1"># self.serializer = best_serializer_for_standard_data((DataFormats.binary,</span>
</span><span id="Lmdb.__init__-144"><a href="#Lmdb.__init__-144"><span class="linenos">144</span></a>        <span class="c1">#                                    Tags.can_use_bytes,</span>
</span><span id="Lmdb.__init__-145"><a href="#Lmdb.__init__-145"><span class="linenos">145</span></a>        <span class="c1">#                                    Tags.decode_str_as_str,</span>
</span><span id="Lmdb.__init__-146"><a href="#Lmdb.__init__-146"><span class="linenos">146</span></a>        <span class="c1">#                                    Tags.decode_list_as_list,</span>
</span><span id="Lmdb.__init__-147"><a href="#Lmdb.__init__-147"><span class="linenos">147</span></a>        <span class="c1">#                                    Tags.decode_bytes_as_bytes,</span>
</span><span id="Lmdb.__init__-148"><a href="#Lmdb.__init__-148"><span class="linenos">148</span></a>        <span class="c1">#                                    Tags.superficial,</span>
</span><span id="Lmdb.__init__-149"><a href="#Lmdb.__init__-149"><span class="linenos">149</span></a>        <span class="c1">#                                    Tags.current_platform,</span>
</span><span id="Lmdb.__init__-150"><a href="#Lmdb.__init__-150"><span class="linenos">150</span></a>        <span class="c1">#                                    Tags.multi_platform),</span>
</span><span id="Lmdb.__init__-151"><a href="#Lmdb.__init__-151"><span class="linenos">151</span></a>        <span class="c1">#                                   TestDataType.small,</span>
</span><span id="Lmdb.__init__-152"><a href="#Lmdb.__init__-152"><span class="linenos">152</span></a>        <span class="c1">#                                   0.1)</span>
</span><span id="Lmdb.__init__-153"><a href="#Lmdb.__init__-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="Lmdb.__init__-154"><a href="#Lmdb.__init__-154"><span class="linenos">154</span></a>
</span><span id="Lmdb.__init__-155"><a href="#Lmdb.__init__-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_request_workers</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Lmdb.__init__-156"><a href="#Lmdb.__init__-156"><span class="linenos">156</span></a>            <span class="mi">0</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_set_db_environment_path</span><span class="p">,</span>
</span><span id="Lmdb.__init__-157"><a href="#Lmdb.__init__-157"><span class="linenos">157</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_open_databases</span><span class="p">,</span>
</span><span id="Lmdb.__init__-158"><a href="#Lmdb.__init__-158"><span class="linenos">158</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_drop_db</span><span class="p">,</span>
</span><span id="Lmdb.__init__-159"><a href="#Lmdb.__init__-159"><span class="linenos">159</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_sync</span><span class="p">,</span>
</span><span id="Lmdb.__init__-160"><a href="#Lmdb.__init__-160"><span class="linenos">160</span></a>            <span class="mi">4</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get</span><span class="p">,</span>
</span><span id="Lmdb.__init__-161"><a href="#Lmdb.__init__-161"><span class="linenos">161</span></a>            <span class="mi">5</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get_items</span><span class="p">,</span>
</span><span id="Lmdb.__init__-162"><a href="#Lmdb.__init__-162"><span class="linenos">162</span></a>            <span class="mi">6</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_get_all_items</span><span class="p">,</span>
</span><span id="Lmdb.__init__-163"><a href="#Lmdb.__init__-163"><span class="linenos">163</span></a>            <span class="mi">7</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put</span><span class="p">,</span>
</span><span id="Lmdb.__init__-164"><a href="#Lmdb.__init__-164"><span class="linenos">164</span></a>            <span class="mi">8</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_put_items</span><span class="p">,</span>
</span><span id="Lmdb.__init__-165"><a href="#Lmdb.__init__-165"><span class="linenos">165</span></a>            <span class="mi">9</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_delete</span><span class="p">,</span>
</span><span id="Lmdb.__init__-166"><a href="#Lmdb.__init__-166"><span class="linenos">166</span></a>            <span class="mi">10</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_delete_items</span><span class="p">,</span>
</span><span id="Lmdb.__init__-167"><a href="#Lmdb.__init__-167"><span class="linenos">167</span></a>            <span class="mi">11</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_open_db_environment</span><span class="p">,</span>
</span><span id="Lmdb.__init__-168"><a href="#Lmdb.__init__-168"><span class="linenos">168</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="Lmdb.default_db_name" class="classattr">
                                <div class="attr variable">
            <span class="name">default_db_name</span><span class="annotation">: bytes</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.default_db_name"></a>
    
    

                            </div>
                            <div id="Lmdb.drop_db_requests" class="classattr">
                                <div class="attr variable">
            <span class="name">drop_db_requests</span><span class="annotation">: Dict[int, Tuple[Hashable, bool]]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.drop_db_requests"></a>
    
    

                            </div>
                            <div id="Lmdb.read_queue" class="classattr">
                                <div class="attr variable">
            <span class="name">read_queue</span><span class="annotation">: List[Tuple[int, Tuple[bytes, Hashable]]]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.read_queue"></a>
    
    

                            </div>
                            <div id="Lmdb.massive_read_queue" class="classattr">
                                <div class="attr variable">
            <span class="name">massive_read_queue</span><span class="annotation">: List[Tuple[int, Set[Tuple[Union[bytes, str, Any], Hashable]]]]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.massive_read_queue"></a>
    
    

                            </div>
                            <div id="Lmdb.data_cache" class="classattr">
                                <div class="attr variable">
            <span class="name">data_cache</span><span class="annotation">: Dict[Tuple[Hashable, Hashable], Any]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.data_cache"></a>
    
    

                            </div>
                            <div id="Lmdb.deletion_cache" class="classattr">
                                <div class="attr variable">
            <span class="name">deletion_cache</span><span class="annotation">: Dict[Tuple[Hashable, Hashable], Any]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.deletion_cache"></a>
    
    

                            </div>
                            <div id="Lmdb.get_all_items_queue" class="classattr">
                                <div class="attr variable">
            <span class="name">get_all_items_queue</span><span class="annotation">: List[Tuple[int, Hashable]]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.get_all_items_queue"></a>
    
    

                            </div>
                            <div id="Lmdb.path_to_db_environment" class="classattr">
                                <div class="attr variable">
            <span class="name">path_to_db_environment</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.path_to_db_environment"></a>
    
    

                            </div>
                            <div id="Lmdb.db_environment" class="classattr">
                                <div class="attr variable">
            <span class="name">db_environment</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.db_environment"></a>
    
    

                            </div>
                            <div id="Lmdb.databases" class="classattr">
                                <div class="attr variable">
            <span class="name">databases</span><span class="annotation">: Dict[Hashable, Any]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.databases"></a>
    
    

                            </div>
                            <div id="Lmdb.db_names" class="classattr">
                                <div class="attr variable">
            <span class="name">db_names</span><span class="annotation">: Dict[Hashable, bytes]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.db_names"></a>
    
    

                            </div>
                            <div id="Lmdb.async_loop" class="classattr">
                                <div class="attr variable">
            <span class="name">async_loop</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.async_loop"></a>
    
    

                            </div>
                            <div id="Lmdb.sync_time_interval" class="classattr">
                                <div class="attr variable">
            <span class="name">sync_time_interval</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.sync_time_interval"></a>
    
    

                            </div>
                            <div id="Lmdb.last_sync_time" class="classattr">
                                <div class="attr variable">
            <span class="name">last_sync_time</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.last_sync_time"></a>
    
    

                            </div>
                            <div id="Lmdb.force_sync" class="classattr">
                                <div class="attr variable">
            <span class="name">force_sync</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.force_sync"></a>
    
    

                            </div>
                            <div id="Lmdb.write_locked" class="classattr">
                                <div class="attr variable">
            <span class="name">write_locked</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.write_locked"></a>
    
    

                            </div>
                            <div id="Lmdb.writes_num" class="classattr">
                                <div class="attr variable">
            <span class="name">writes_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.writes_num"></a>
    
    

                            </div>
                            <div id="Lmdb.reads_num" class="classattr">
                                <div class="attr variable">
            <span class="name">reads_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.reads_num"></a>
    
    

                            </div>
                            <div id="Lmdb.deletes_num" class="classattr">
                                <div class="attr variable">
            <span class="name">deletes_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.deletes_num"></a>
    
    

                            </div>
                            <div id="Lmdb.db_drops_num" class="classattr">
                                <div class="attr variable">
            <span class="name">db_drops_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.db_drops_num"></a>
    
    

                            </div>
                            <div id="Lmdb.write_locked_coro_id" class="classattr">
                                <div class="attr variable">
            <span class="name">write_locked_coro_id</span><span class="annotation">: Union[int, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.write_locked_coro_id"></a>
    
    

                            </div>
                            <div id="Lmdb.serializer" class="classattr">
                                <div class="attr variable">
            <span class="name">serializer</span>

        
    </div>
    <a class="headerlink" href="#Lmdb.serializer"></a>
    
    

                            </div>
                            <div id="Lmdb.get_entity_stats" class="classattr">
                                        <input id="Lmdb.get_entity_stats-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_entity_stats</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">stats_level</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="Lmdb.get_entity_stats-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Lmdb.get_entity_stats"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Lmdb.get_entity_stats-170"><a href="#Lmdb.get_entity_stats-170"><span class="linenos">170</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="Lmdb.get_entity_stats-171"><a href="#Lmdb.get_entity_stats-171"><span class="linenos">171</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="Lmdb.get_entity_stats-172"><a href="#Lmdb.get_entity_stats-172"><span class="linenos">172</span></a>            <span class="s1">&#39;db_names&#39;</span><span class="p">:</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_names</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span>
</span><span id="Lmdb.get_entity_stats-173"><a href="#Lmdb.get_entity_stats-173"><span class="linenos">173</span></a>            <span class="s1">&#39;writes num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span><span class="p">,</span>
</span><span id="Lmdb.get_entity_stats-174"><a href="#Lmdb.get_entity_stats-174"><span class="linenos">174</span></a>            <span class="s1">&#39;reads num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span><span class="p">,</span>
</span><span id="Lmdb.get_entity_stats-175"><a href="#Lmdb.get_entity_stats-175"><span class="linenos">175</span></a>            <span class="s1">&#39;deletes num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span><span class="p">,</span>
</span><span id="Lmdb.get_entity_stats-176"><a href="#Lmdb.get_entity_stats-176"><span class="linenos">176</span></a>            <span class="s1">&#39;db drops num&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span><span class="p">,</span>
</span><span id="Lmdb.get_entity_stats-177"><a href="#Lmdb.get_entity_stats-177"><span class="linenos">177</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="Lmdb.single_task_registration_or_immediate_processing" class="classattr">
                                        <input id="Lmdb.single_task_registration_or_immediate_processing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">single_task_registration_or_immediate_processing</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="Lmdb.single_task_registration_or_immediate_processing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Lmdb.single_task_registration_or_immediate_processing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Lmdb.single_task_registration_or_immediate_processing-179"><a href="#Lmdb.single_task_registration_or_immediate_processing-179"><span class="linenos">179</span></a>    <span class="k">def</span> <span class="nf">single_task_registration_or_immediate_processing</span><span class="p">(</span>
</span><span id="Lmdb.single_task_registration_or_immediate_processing-180"><a href="#Lmdb.single_task_registration_or_immediate_processing-180"><span class="linenos">180</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceProcessingResponse</span><span class="p">:</span>
</span><span id="Lmdb.single_task_registration_or_immediate_processing-181"><a href="#Lmdb.single_task_registration_or_immediate_processing-181"><span class="linenos">181</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">try_resolve_request</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Lmdb.single_task_registration_or_immediate_processing-182"><a href="#Lmdb.single_task_registration_or_immediate_processing-182"><span class="linenos">182</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb.single_task_registration_or_immediate_processing-183"><a href="#Lmdb.single_task_registration_or_immediate_processing-183"><span class="linenos">183</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span>
</span><span id="Lmdb.single_task_registration_or_immediate_processing-184"><a href="#Lmdb.single_task_registration_or_immediate_processing-184"><span class="linenos">184</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb.single_task_registration_or_immediate_processing-185"><a href="#Lmdb.single_task_registration_or_immediate_processing-185"><span class="linenos">185</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="Lmdb.full_processing_iteration" class="classattr">
                                        <input id="Lmdb.full_processing_iteration-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_processing_iteration</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Lmdb.full_processing_iteration-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Lmdb.full_processing_iteration"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Lmdb.full_processing_iteration-187"><a href="#Lmdb.full_processing_iteration-187"><span class="linenos">187</span></a>    <span class="k">def</span> <span class="nf">full_processing_iteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Lmdb.full_processing_iteration-188"><a href="#Lmdb.full_processing_iteration-188"><span class="linenos">188</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb.full_processing_iteration-189"><a href="#Lmdb.full_processing_iteration-189"><span class="linenos">189</span></a>        
</span><span id="Lmdb.full_processing_iteration-190"><a href="#Lmdb.full_processing_iteration-190"><span class="linenos">190</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-191"><a href="#Lmdb.full_processing_iteration-191"><span class="linenos">191</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_init_db</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-192"><a href="#Lmdb.full_processing_iteration-192"><span class="linenos">192</span></a>
</span><span id="Lmdb.full_processing_iteration-193"><a href="#Lmdb.full_processing_iteration-193"><span class="linenos">193</span></a>        <span class="n">data_cache_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span>
</span><span id="Lmdb.full_processing_iteration-194"><a href="#Lmdb.full_processing_iteration-194"><span class="linenos">194</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">data_cache_buff</span><span class="p">)()</span>
</span><span id="Lmdb.full_processing_iteration-195"><a href="#Lmdb.full_processing_iteration-195"><span class="linenos">195</span></a>        
</span><span id="Lmdb.full_processing_iteration-196"><a href="#Lmdb.full_processing_iteration-196"><span class="linenos">196</span></a>        <span class="n">read_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span>
</span><span id="Lmdb.full_processing_iteration-197"><a href="#Lmdb.full_processing_iteration-197"><span class="linenos">197</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">read_queue_buff</span><span class="p">)()</span>
</span><span id="Lmdb.full_processing_iteration-198"><a href="#Lmdb.full_processing_iteration-198"><span class="linenos">198</span></a>        
</span><span id="Lmdb.full_processing_iteration-199"><a href="#Lmdb.full_processing_iteration-199"><span class="linenos">199</span></a>        <span class="n">massive_read_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span>
</span><span id="Lmdb.full_processing_iteration-200"><a href="#Lmdb.full_processing_iteration-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">massive_read_queue_buff</span><span class="p">)()</span>
</span><span id="Lmdb.full_processing_iteration-201"><a href="#Lmdb.full_processing_iteration-201"><span class="linenos">201</span></a>        
</span><span id="Lmdb.full_processing_iteration-202"><a href="#Lmdb.full_processing_iteration-202"><span class="linenos">202</span></a>        <span class="n">deletion_cache_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span>
</span><span id="Lmdb.full_processing_iteration-203"><a href="#Lmdb.full_processing_iteration-203"><span class="linenos">203</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">deletion_cache_buff</span><span class="p">)()</span>
</span><span id="Lmdb.full_processing_iteration-204"><a href="#Lmdb.full_processing_iteration-204"><span class="linenos">204</span></a>        
</span><span id="Lmdb.full_processing_iteration-205"><a href="#Lmdb.full_processing_iteration-205"><span class="linenos">205</span></a>        <span class="n">get_all_items_queue_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span>
</span><span id="Lmdb.full_processing_iteration-206"><a href="#Lmdb.full_processing_iteration-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">get_all_items_queue_buff</span><span class="p">)()</span>
</span><span id="Lmdb.full_processing_iteration-207"><a href="#Lmdb.full_processing_iteration-207"><span class="linenos">207</span></a>
</span><span id="Lmdb.full_processing_iteration-208"><a href="#Lmdb.full_processing_iteration-208"><span class="linenos">208</span></a>        <span class="c1"># put</span>
</span><span id="Lmdb.full_processing_iteration-209"><a href="#Lmdb.full_processing_iteration-209"><span class="linenos">209</span></a>        <span class="k">def</span> <span class="nf">put_handler</span><span class="p">(</span><span class="n">db_environment</span><span class="p">,</span> <span class="n">databases</span><span class="p">):</span>
</span><span id="Lmdb.full_processing_iteration-210"><a href="#Lmdb.full_processing_iteration-210"><span class="linenos">210</span></a>            <span class="n">db_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb.full_processing_iteration-211"><a href="#Lmdb.full_processing_iteration-211"><span class="linenos">211</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-212"><a href="#Lmdb.full_processing_iteration-212"><span class="linenos">212</span></a>                <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-213"><a href="#Lmdb.full_processing_iteration-213"><span class="linenos">213</span></a>                    <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">data_cache_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb.full_processing_iteration-214"><a href="#Lmdb.full_processing_iteration-214"><span class="linenos">214</span></a>                        <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="Lmdb.full_processing_iteration-215"><a href="#Lmdb.full_processing_iteration-215"><span class="linenos">215</span></a>                        <span class="n">txn</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">],</span> <span class="n">dupdata</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-216"><a href="#Lmdb.full_processing_iteration-216"><span class="linenos">216</span></a>
</span><span id="Lmdb.full_processing_iteration-217"><a href="#Lmdb.full_processing_iteration-217"><span class="linenos">217</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">writes_num</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-218"><a href="#Lmdb.full_processing_iteration-218"><span class="linenos">218</span></a>            <span class="k">except</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">MapFullError</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-219"><a href="#Lmdb.full_processing_iteration-219"><span class="linenos">219</span></a>                <span class="k">raise</span> <span class="n">DBError</span><span class="o">.</span><span class="n">from_exception</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-220"><a href="#Lmdb.full_processing_iteration-220"><span class="linenos">220</span></a>        
</span><span id="Lmdb.full_processing_iteration-221"><a href="#Lmdb.full_processing_iteration-221"><span class="linenos">221</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">,</span> <span class="n">put_handler</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-222"><a href="#Lmdb.full_processing_iteration-222"><span class="linenos">222</span></a>        
</span><span id="Lmdb.full_processing_iteration-223"><a href="#Lmdb.full_processing_iteration-223"><span class="linenos">223</span></a>        <span class="c1"># delete</span>
</span><span id="Lmdb.full_processing_iteration-224"><a href="#Lmdb.full_processing_iteration-224"><span class="linenos">224</span></a>        <span class="k">for</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">deletion_cache_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb.full_processing_iteration-225"><a href="#Lmdb.full_processing_iteration-225"><span class="linenos">225</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-226"><a href="#Lmdb.full_processing_iteration-226"><span class="linenos">226</span></a>                <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="Lmdb.full_processing_iteration-227"><a href="#Lmdb.full_processing_iteration-227"><span class="linenos">227</span></a>                <span class="n">txn</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span>
</span><span id="Lmdb.full_processing_iteration-228"><a href="#Lmdb.full_processing_iteration-228"><span class="linenos">228</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">deletes_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Lmdb.full_processing_iteration-229"><a href="#Lmdb.full_processing_iteration-229"><span class="linenos">229</span></a>
</span><span id="Lmdb.full_processing_iteration-230"><a href="#Lmdb.full_processing_iteration-230"><span class="linenos">230</span></a>        <span class="c1"># drop</span>
</span><span id="Lmdb.full_processing_iteration-231"><a href="#Lmdb.full_processing_iteration-231"><span class="linenos">231</span></a>        <span class="n">drop_db_requests_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span>
</span><span id="Lmdb.full_processing_iteration-232"><a href="#Lmdb.full_processing_iteration-232"><span class="linenos">232</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">drop_db_requests_buff</span><span class="p">)()</span>
</span><span id="Lmdb.full_processing_iteration-233"><a href="#Lmdb.full_processing_iteration-233"><span class="linenos">233</span></a>        <span class="n">dropped_databases</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-234"><a href="#Lmdb.full_processing_iteration-234"><span class="linenos">234</span></a>        <span class="n">processed_coroutines</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-235"><a href="#Lmdb.full_processing_iteration-235"><span class="linenos">235</span></a>        
</span><span id="Lmdb.full_processing_iteration-236"><a href="#Lmdb.full_processing_iteration-236"><span class="linenos">236</span></a>        <span class="k">def</span> <span class="nf">drop_handler</span><span class="p">(</span><span class="n">db_environment</span><span class="p">,</span> <span class="n">databases</span><span class="p">):</span>
</span><span id="Lmdb.full_processing_iteration-237"><a href="#Lmdb.full_processing_iteration-237"><span class="linenos">237</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">request</span> <span class="ow">in</span> <span class="n">drop_db_requests_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="Lmdb.full_processing_iteration-238"><a href="#Lmdb.full_processing_iteration-238"><span class="linenos">238</span></a>                <span class="k">if</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">processed_coroutines</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-239"><a href="#Lmdb.full_processing_iteration-239"><span class="linenos">239</span></a>                    <span class="k">continue</span>
</span><span id="Lmdb.full_processing_iteration-240"><a href="#Lmdb.full_processing_iteration-240"><span class="linenos">240</span></a>                
</span><span id="Lmdb.full_processing_iteration-241"><a href="#Lmdb.full_processing_iteration-241"><span class="linenos">241</span></a>                <span class="n">db_id</span><span class="p">,</span> <span class="n">delete_db</span> <span class="o">=</span> <span class="n">request</span>
</span><span id="Lmdb.full_processing_iteration-242"><a href="#Lmdb.full_processing_iteration-242"><span class="linenos">242</span></a>                <span class="k">if</span> <span class="n">db_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">dropped_databases</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-243"><a href="#Lmdb.full_processing_iteration-243"><span class="linenos">243</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-244"><a href="#Lmdb.full_processing_iteration-244"><span class="linenos">244</span></a>                        <span class="k">with</span> <span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">write</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-245"><a href="#Lmdb.full_processing_iteration-245"><span class="linenos">245</span></a>                            <span class="n">txn</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">],</span> <span class="n">delete</span><span class="o">=</span><span class="n">delete_db</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-246"><a href="#Lmdb.full_processing_iteration-246"><span class="linenos">246</span></a>                        
</span><span id="Lmdb.full_processing_iteration-247"><a href="#Lmdb.full_processing_iteration-247"><span class="linenos">247</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">db_drops_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Lmdb.full_processing_iteration-248"><a href="#Lmdb.full_processing_iteration-248"><span class="linenos">248</span></a>                    <span class="k">except</span> <span class="n">lmdb_lib</span><span class="o">.</span><span class="n">MapFullError</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-249"><a href="#Lmdb.full_processing_iteration-249"><span class="linenos">249</span></a>                        <span class="k">raise</span> <span class="n">DBError</span><span class="o">.</span><span class="n">from_exception</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-250"><a href="#Lmdb.full_processing_iteration-250"><span class="linenos">250</span></a>                    
</span><span id="Lmdb.full_processing_iteration-251"><a href="#Lmdb.full_processing_iteration-251"><span class="linenos">251</span></a>                    <span class="n">dropped_databases</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">db_id</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-252"><a href="#Lmdb.full_processing_iteration-252"><span class="linenos">252</span></a>                
</span><span id="Lmdb.full_processing_iteration-253"><a href="#Lmdb.full_processing_iteration-253"><span class="linenos">253</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-254"><a href="#Lmdb.full_processing_iteration-254"><span class="linenos">254</span></a>                <span class="n">processed_coroutines</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-255"><a href="#Lmdb.full_processing_iteration-255"><span class="linenos">255</span></a>                    
</span><span id="Lmdb.full_processing_iteration-256"><a href="#Lmdb.full_processing_iteration-256"><span class="linenos">256</span></a>        <span class="n">lmdb_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">,</span> <span class="n">drop_handler</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-257"><a href="#Lmdb.full_processing_iteration-257"><span class="linenos">257</span></a>
</span><span id="Lmdb.full_processing_iteration-258"><a href="#Lmdb.full_processing_iteration-258"><span class="linenos">258</span></a>        <span class="c1"># get</span>
</span><span id="Lmdb.full_processing_iteration-259"><a href="#Lmdb.full_processing_iteration-259"><span class="linenos">259</span></a>        <span class="k">def</span> <span class="nf">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]:</span>
</span><span id="Lmdb.full_processing_iteration-260"><a href="#Lmdb.full_processing_iteration-260"><span class="linenos">260</span></a>            <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span> <span class="o">=</span> <span class="n">key_info</span>
</span><span id="Lmdb.full_processing_iteration-261"><a href="#Lmdb.full_processing_iteration-261"><span class="linenos">261</span></a>            <span class="k">if</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">data_cache_buff</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-262"><a href="#Lmdb.full_processing_iteration-262"><span class="linenos">262</span></a>                <span class="n">value</span> <span class="o">=</span> <span class="n">data_cache_buff</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span>
</span><span id="Lmdb.full_processing_iteration-263"><a href="#Lmdb.full_processing_iteration-263"><span class="linenos">263</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-264"><a href="#Lmdb.full_processing_iteration-264"><span class="linenos">264</span></a>                <span class="n">value</span> <span class="o">=</span> <span class="n">txn</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span>
</span><span id="Lmdb.full_processing_iteration-265"><a href="#Lmdb.full_processing_iteration-265"><span class="linenos">265</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Lmdb.full_processing_iteration-266"><a href="#Lmdb.full_processing_iteration-266"><span class="linenos">266</span></a>            
</span><span id="Lmdb.full_processing_iteration-267"><a href="#Lmdb.full_processing_iteration-267"><span class="linenos">267</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb.full_processing_iteration-268"><a href="#Lmdb.full_processing_iteration-268"><span class="linenos">268</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-269"><a href="#Lmdb.full_processing_iteration-269"><span class="linenos">269</span></a>                <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-270"><a href="#Lmdb.full_processing_iteration-270"><span class="linenos">270</span></a>                    <span class="n">exception</span> <span class="o">=</span> <span class="n">DbKeyError</span><span class="p">(</span><span class="n">key_info</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-271"><a href="#Lmdb.full_processing_iteration-271"><span class="linenos">271</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-272"><a href="#Lmdb.full_processing_iteration-272"><span class="linenos">272</span></a>                    <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-273"><a href="#Lmdb.full_processing_iteration-273"><span class="linenos">273</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-274"><a href="#Lmdb.full_processing_iteration-274"><span class="linenos">274</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-275"><a href="#Lmdb.full_processing_iteration-275"><span class="linenos">275</span></a>            
</span><span id="Lmdb.full_processing_iteration-276"><a href="#Lmdb.full_processing_iteration-276"><span class="linenos">276</span></a>            <span class="k">return</span> <span class="n">value</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="Lmdb.full_processing_iteration-277"><a href="#Lmdb.full_processing_iteration-277"><span class="linenos">277</span></a>            
</span><span id="Lmdb.full_processing_iteration-278"><a href="#Lmdb.full_processing_iteration-278"><span class="linenos">278</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">()</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-279"><a href="#Lmdb.full_processing_iteration-279"><span class="linenos">279</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">read_queue_buff</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-280"><a href="#Lmdb.full_processing_iteration-280"><span class="linenos">280</span></a>                <span class="n">value</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-281"><a href="#Lmdb.full_processing_iteration-281"><span class="linenos">281</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-282"><a href="#Lmdb.full_processing_iteration-282"><span class="linenos">282</span></a>            
</span><span id="Lmdb.full_processing_iteration-283"><a href="#Lmdb.full_processing_iteration-283"><span class="linenos">283</span></a>            <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">set_of_key_info</span> <span class="ow">in</span> <span class="n">massive_read_queue_buff</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-284"><a href="#Lmdb.full_processing_iteration-284"><span class="linenos">284</span></a>                <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">Exception</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-285"><a href="#Lmdb.full_processing_iteration-285"><span class="linenos">285</span></a>                <span class="k">for</span> <span class="n">key_info</span> <span class="ow">in</span> <span class="n">set_of_key_info</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-286"><a href="#Lmdb.full_processing_iteration-286"><span class="linenos">286</span></a>                    <span class="n">items</span><span class="p">[</span><span class="n">key_info</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_item</span><span class="p">(</span><span class="n">txn</span><span class="p">,</span> <span class="n">key_info</span><span class="p">,</span> <span class="n">data_cache_buff</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-287"><a href="#Lmdb.full_processing_iteration-287"><span class="linenos">287</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">items</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-288"><a href="#Lmdb.full_processing_iteration-288"><span class="linenos">288</span></a>
</span><span id="Lmdb.full_processing_iteration-289"><a href="#Lmdb.full_processing_iteration-289"><span class="linenos">289</span></a>        <span class="c1"># get all items</span>
</span><span id="Lmdb.full_processing_iteration-290"><a href="#Lmdb.full_processing_iteration-290"><span class="linenos">290</span></a>        <span class="k">for</span> <span class="n">coro_id</span><span class="p">,</span> <span class="n">db_id</span> <span class="ow">in</span> <span class="n">get_all_items_queue_buff</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-291"><a href="#Lmdb.full_processing_iteration-291"><span class="linenos">291</span></a>            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">begin</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-292"><a href="#Lmdb.full_processing_iteration-292"><span class="linenos">292</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-293"><a href="#Lmdb.full_processing_iteration-293"><span class="linenos">293</span></a>                <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb.full_processing_iteration-294"><a href="#Lmdb.full_processing_iteration-294"><span class="linenos">294</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-295"><a href="#Lmdb.full_processing_iteration-295"><span class="linenos">295</span></a>                    <span class="c1"># for k, v in txn.cursor(db=self.databases[db_id]):</span>
</span><span id="Lmdb.full_processing_iteration-296"><a href="#Lmdb.full_processing_iteration-296"><span class="linenos">296</span></a>                    <span class="c1">#     key = make_key_frozen(self.serializer.loads(k))</span>
</span><span id="Lmdb.full_processing_iteration-297"><a href="#Lmdb.full_processing_iteration-297"><span class="linenos">297</span></a>                    <span class="c1">#     value = self.serializer.loads(v)</span>
</span><span id="Lmdb.full_processing_iteration-298"><a href="#Lmdb.full_processing_iteration-298"><span class="linenos">298</span></a>                    <span class="c1">#     result[key] = value</span>
</span><span id="Lmdb.full_processing_iteration-299"><a href="#Lmdb.full_processing_iteration-299"><span class="linenos">299</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="p">{</span><span class="n">make_key_frozen</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">k</span><span class="p">)):</span> <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">txn</span><span class="o">.</span><span class="n">cursor</span><span class="p">(</span><span class="n">db</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">databases</span><span class="p">[</span><span class="n">db_id</span><span class="p">])}</span>
</span><span id="Lmdb.full_processing_iteration-300"><a href="#Lmdb.full_processing_iteration-300"><span class="linenos">300</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">reads_num</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-301"><a href="#Lmdb.full_processing_iteration-301"><span class="linenos">301</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="Lmdb.full_processing_iteration-302"><a href="#Lmdb.full_processing_iteration-302"><span class="linenos">302</span></a>                    <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-303"><a href="#Lmdb.full_processing_iteration-303"><span class="linenos">303</span></a>                
</span><span id="Lmdb.full_processing_iteration-304"><a href="#Lmdb.full_processing_iteration-304"><span class="linenos">304</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">register_response</span><span class="p">(</span><span class="n">coro_id</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="Lmdb.full_processing_iteration-305"><a href="#Lmdb.full_processing_iteration-305"><span class="linenos">305</span></a>        
</span><span id="Lmdb.full_processing_iteration-306"><a href="#Lmdb.full_processing_iteration-306"><span class="linenos">306</span></a>        <span class="c1"># sync</span>
</span><span id="Lmdb.full_processing_iteration-307"><a href="#Lmdb.full_processing_iteration-307"><span class="linenos">307</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sync_in_thread_pool</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-308"><a href="#Lmdb.full_processing_iteration-308"><span class="linenos">308</span></a>        
</span><span id="Lmdb.full_processing_iteration-309"><a href="#Lmdb.full_processing_iteration-309"><span class="linenos">309</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="Lmdb.full_processing_iteration-310"><a href="#Lmdb.full_processing_iteration-310"><span class="linenos">310</span></a>
</span><span id="Lmdb.full_processing_iteration-311"><a href="#Lmdb.full_processing_iteration-311"><span class="linenos">311</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">make_dead</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="Lmdb.in_work" class="classattr">
                                        <input id="Lmdb.in_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">in_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="Lmdb.in_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Lmdb.in_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Lmdb.in_work-313"><a href="#Lmdb.in_work-313"><span class="linenos">313</span></a>    <span class="k">def</span> <span class="nf">in_work</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Lmdb.in_work-314"><a href="#Lmdb.in_work-314"><span class="linenos">314</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">read_queue</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">massive_read_queue</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_all_items_queue</span><span class="p">))</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">force_sync</span> <span class="ow">or</span> <span class="p">((</span><span class="ow">not</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span><span class="p">))</span> <span class="ow">and</span> <span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_cache</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">deletion_cache</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">drop_db_requests</span><span class="p">))</span> <span class="ow">and</span> <span class="p">((</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">)))</span>
</span><span id="Lmdb.in_work-315"><a href="#Lmdb.in_work-315"><span class="linenos">315</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">thrifty_in_work</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Will be executed twice per iteration: once before and once after the full_processing_iteration() execution</p>

<p>Raises:
    NotImplementedError: _description_</p>

<p>Returns:
    bool: _description_</p>
</div>


                            </div>
                            <div id="Lmdb.time_left_before_next_event" class="classattr">
                                        <input id="Lmdb.time_left_before_next_event-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">time_left_before_next_event</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="Lmdb.time_left_before_next_event-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Lmdb.time_left_before_next_event"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Lmdb.time_left_before_next_event-317"><a href="#Lmdb.time_left_before_next_event-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">time_left_before_next_event</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]]:</span>
</span><span id="Lmdb.time_left_before_next_event-318"><a href="#Lmdb.time_left_before_next_event-318"><span class="linenos">318</span></a>        <span class="n">time_since_last_sync_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_sync_time</span>
</span><span id="Lmdb.time_left_before_next_event-319"><a href="#Lmdb.time_left_before_next_event-319"><span class="linenos">319</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">&gt;</span> <span class="n">time_since_last_sync_time</span><span class="p">:</span>
</span><span id="Lmdb.time_left_before_next_event-320"><a href="#Lmdb.time_left_before_next_event-320"><span class="linenos">320</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span> <span class="o">-</span> <span class="n">time_since_last_sync_time</span>
</span><span id="Lmdb.time_left_before_next_event-321"><a href="#Lmdb.time_left_before_next_event-321"><span class="linenos">321</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb.time_left_before_next_event-322"><a href="#Lmdb.time_left_before_next_event-322"><span class="linenos">322</span></a>            <span class="k">return</span> <span class="kc">True</span><span class="p">,</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="Lmdb.sync_in_thread_pool" class="classattr">
                                        <input id="Lmdb.sync_in_thread_pool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sync_in_thread_pool</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Lmdb.sync_in_thread_pool-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Lmdb.sync_in_thread_pool"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Lmdb.sync_in_thread_pool-469"><a href="#Lmdb.sync_in_thread_pool-469"><span class="linenos">469</span></a>    <span class="k">def</span> <span class="nf">sync_in_thread_pool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Lmdb.sync_in_thread_pool-470"><a href="#Lmdb.sync_in_thread_pool-470"><span class="linenos">470</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db_coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="Lmdb.sync_in_thread_pool-471"><a href="#Lmdb.sync_in_thread_pool-471"><span class="linenos">471</span></a>            <span class="k">if</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">:</span>
</span><span id="Lmdb.sync_in_thread_pool-472"><a href="#Lmdb.sync_in_thread_pool-472"><span class="linenos">472</span></a>                <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">,</span> <span class="kc">True</span><span class="p">))</span>
</span><span id="Lmdb.sync_in_thread_pool-473"><a href="#Lmdb.sync_in_thread_pool-473"><span class="linenos">473</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Lmdb.sync_in_thread_pool-474"><a href="#Lmdb.sync_in_thread_pool-474"><span class="linenos">474</span></a>                <span class="k">if</span> <span class="n">asyncio_loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Lmdb.sync_in_thread_pool-475"><a href="#Lmdb.sync_in_thread_pool-475"><span class="linenos">475</span></a>                    <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</span><span id="Lmdb.sync_in_thread_pool-476"><a href="#Lmdb.sync_in_thread_pool-476"><span class="linenos">476</span></a>            
</span><span id="Lmdb.sync_in_thread_pool-477"><a href="#Lmdb.sync_in_thread_pool-477"><span class="linenos">477</span></a>            <span class="k">async</span> <span class="k">def</span> <span class="nf">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">):</span>
</span><span id="Lmdb.sync_in_thread_pool-478"><a href="#Lmdb.sync_in_thread_pool-478"><span class="linenos">478</span></a>                <span class="k">def</span> <span class="nf">sync_worker</span><span class="p">():</span>
</span><span id="Lmdb.sync_in_thread_pool-479"><a href="#Lmdb.sync_in_thread_pool-479"><span class="linenos">479</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">db_environment</span><span class="o">.</span><span class="n">sync</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
</span><span id="Lmdb.sync_in_thread_pool-480"><a href="#Lmdb.sync_in_thread_pool-480"><span class="linenos">480</span></a>                
</span><span id="Lmdb.sync_in_thread_pool-481"><a href="#Lmdb.sync_in_thread_pool-481"><span class="linenos">481</span></a>                <span class="k">await</span> <span class="n">task_in_thread_pool</span><span class="p">(</span><span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">sync_worker</span><span class="p">)</span>
</span><span id="Lmdb.sync_in_thread_pool-482"><a href="#Lmdb.sync_in_thread_pool-482"><span class="linenos">482</span></a>
</span><span id="Lmdb.sync_in_thread_pool-483"><a href="#Lmdb.sync_in_thread_pool-483"><span class="linenos">483</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">,</span> <span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">sync_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">)))</span>
</span><span id="Lmdb.sync_in_thread_pool-484"><a href="#Lmdb.sync_in_thread_pool-484"><span class="linenos">484</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb.sync_in_thread_pool-485"><a href="#Lmdb.sync_in_thread_pool-485"><span class="linenos">485</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb.sync_in_thread_pool-486"><a href="#Lmdb.sync_in_thread_pool-486"><span class="linenos">486</span></a>            <span class="k">def</span> <span class="nf">make_service_live_for_a_next_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Lmdb.sync_in_thread_pool-487"><a href="#Lmdb.sync_in_thread_pool-487"><span class="linenos">487</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">make_live</span><span class="p">()</span>
</span><span id="Lmdb.sync_in_thread_pool-488"><a href="#Lmdb.sync_in_thread_pool-488"><span class="linenos">488</span></a>            
</span><span id="Lmdb.sync_in_thread_pool-489"><a href="#Lmdb.sync_in_thread_pool-489"><span class="linenos">489</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">TimerFuncRunner</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sync_time_interval</span><span class="p">,</span> <span class="n">make_service_live_for_a_next_sync</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="Lmdb.sync_in_thread_pool-490"><a href="#Lmdb.sync_in_thread_pool-490"><span class="linenos">490</span></a>
</span><span id="Lmdb.sync_in_thread_pool-491"><a href="#Lmdb.sync_in_thread_pool-491"><span class="linenos">491</span></a>        <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Lmdb.sync_in_thread_pool-492"><a href="#Lmdb.sync_in_thread_pool-492"><span class="linenos">492</span></a>        <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Lmdb.sync_in_thread_pool-493"><a href="#Lmdb.sync_in_thread_pool-493"><span class="linenos">493</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="Lmdb.sync_in_thread_pool-494"><a href="#Lmdb.sync_in_thread_pool-494"><span class="linenos">494</span></a>            <span class="n">asyncio_loop</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">AsyncioLoop</span><span class="p">)</span><span class="o">.</span><span class="n">inline_get</span><span class="p">()</span>
</span><span id="Lmdb.sync_in_thread_pool-495"><a href="#Lmdb.sync_in_thread_pool-495"><span class="linenos">495</span></a>        <span class="k">except</span> <span class="n">AsyncioLoopWasNotSetError</span><span class="p">:</span>
</span><span id="Lmdb.sync_in_thread_pool-496"><a href="#Lmdb.sync_in_thread_pool-496"><span class="linenos">496</span></a>            <span class="n">need_to_ensure_asyncio_loop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Lmdb.sync_in_thread_pool-497"><a href="#Lmdb.sync_in_thread_pool-497"><span class="linenos">497</span></a>
</span><span id="Lmdb.sync_in_thread_pool-498"><a href="#Lmdb.sync_in_thread_pool-498"><span class="linenos">498</span></a>        <span class="n">coro</span><span class="p">:</span> <span class="n">CoroWrapperBase</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="n">sync_db_coro</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">asyncio_loop</span><span class="p">,</span> <span class="n">need_to_ensure_asyncio_loop</span><span class="p">)</span>
</span><span id="Lmdb.sync_in_thread_pool-499"><a href="#Lmdb.sync_in_thread_pool-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Lmdb.sync_in_thread_pool-500"><a href="#Lmdb.sync_in_thread_pool-500"><span class="linenos">500</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">write_locked_coro_id</span> <span class="o">=</span> <span class="n">coro</span><span class="o">.</span><span class="n">coro_id</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service</dt>
                                <dd id="Lmdb.current_caller_coro_info" class="variable">current_caller_coro_info</dd>
                <dd id="Lmdb.iteration" class="function">iteration</dd>
                <dd id="Lmdb.make_response" class="function">make_response</dd>
                <dd id="Lmdb.register_response" class="function">register_response</dd>
                <dd id="Lmdb.put_task" class="function">put_task</dd>
                <dd id="Lmdb.resolve_request" class="function">resolve_request</dd>
                <dd id="Lmdb.try_resolve_request" class="function">try_resolve_request</dd>
                <dd id="Lmdb.in_forground_work" class="function">in_forground_work</dd>
                <dd id="Lmdb.thrifty_in_work" class="function">thrifty_in_work</dd>
                <dd id="Lmdb.is_low_latency" class="function">is_low_latency</dd>
                <dd id="Lmdb.make_live" class="function">make_live</dd>
                <dd id="Lmdb.make_dead" class="function">make_dead</dd>
                <dd id="Lmdb.service_id_impl" class="function">service_id_impl</dd>
                <dd id="Lmdb.service_id" class="function">service_id</dd>
                <dd id="Lmdb.destroy" class="function">destroy</dd>

            </div>
            <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</dt>
                                <dd id="Lmdb.StatsLevel" class="class">StatsLevel</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="LmdbRequest">
                            <input id="LmdbRequest-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LmdbRequest</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</span>):

                <label class="view-source-button" for="LmdbRequest-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest-70"><a href="#LmdbRequest-70"><span class="linenos"> 70</span></a><span class="k">class</span> <span class="nc">LmdbRequest</span><span class="p">(</span><span class="n">ServiceRequest</span><span class="p">):</span>
</span><span id="LmdbRequest-71"><a href="#LmdbRequest-71"><span class="linenos"> 71</span></a>    <span class="k">def</span> <span class="nf">set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-72"><a href="#LmdbRequest-72"><span class="linenos"> 72</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span><span id="LmdbRequest-73"><a href="#LmdbRequest-73"><span class="linenos"> 73</span></a>    
</span><span id="LmdbRequest-74"><a href="#LmdbRequest-74"><span class="linenos"> 74</span></a>    <span class="k">def</span> <span class="nf">open_databases</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">DbId</span><span class="p">,</span> <span class="n">DbName</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-75"><a href="#LmdbRequest-75"><span class="linenos"> 75</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">db_names</span><span class="p">)</span>
</span><span id="LmdbRequest-76"><a href="#LmdbRequest-76"><span class="linenos"> 76</span></a>    
</span><span id="LmdbRequest-77"><a href="#LmdbRequest-77"><span class="linenos"> 77</span></a>    <span class="k">def</span> <span class="nf">drop_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">,</span> <span class="n">delete</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-78"><a href="#LmdbRequest-78"><span class="linenos"> 78</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">db_id</span><span class="p">,</span> <span class="n">delete</span><span class="p">)</span>
</span><span id="LmdbRequest-79"><a href="#LmdbRequest-79"><span class="linenos"> 79</span></a>    
</span><span id="LmdbRequest-80"><a href="#LmdbRequest-80"><span class="linenos"> 80</span></a>    <span class="k">def</span> <span class="nf">sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-81"><a href="#LmdbRequest-81"><span class="linenos"> 81</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span><span id="LmdbRequest-82"><a href="#LmdbRequest-82"><span class="linenos"> 82</span></a>    
</span><span id="LmdbRequest-83"><a href="#LmdbRequest-83"><span class="linenos"> 83</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-84"><a href="#LmdbRequest-84"><span class="linenos"> 84</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="LmdbRequest-85"><a href="#LmdbRequest-85"><span class="linenos"> 85</span></a>    
</span><span id="LmdbRequest-86"><a href="#LmdbRequest-86"><span class="linenos"> 86</span></a>    <span class="k">def</span> <span class="nf">get_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-87"><a href="#LmdbRequest-87"><span class="linenos"> 87</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">keys</span><span class="p">)</span>
</span><span id="LmdbRequest-88"><a href="#LmdbRequest-88"><span class="linenos"> 88</span></a>    
</span><span id="LmdbRequest-89"><a href="#LmdbRequest-89"><span class="linenos"> 89</span></a>    <span class="k">def</span> <span class="nf">get_all_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-90"><a href="#LmdbRequest-90"><span class="linenos"> 90</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="LmdbRequest-91"><a href="#LmdbRequest-91"><span class="linenos"> 91</span></a>    
</span><span id="LmdbRequest-92"><a href="#LmdbRequest-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-93"><a href="#LmdbRequest-93"><span class="linenos"> 93</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="LmdbRequest-94"><a href="#LmdbRequest-94"><span class="linenos"> 94</span></a>    
</span><span id="LmdbRequest-95"><a href="#LmdbRequest-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="nf">put_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-96"><a href="#LmdbRequest-96"><span class="linenos"> 96</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="LmdbRequest-97"><a href="#LmdbRequest-97"><span class="linenos"> 97</span></a>    
</span><span id="LmdbRequest-98"><a href="#LmdbRequest-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-99"><a href="#LmdbRequest-99"><span class="linenos"> 99</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span><span id="LmdbRequest-100"><a href="#LmdbRequest-100"><span class="linenos">100</span></a>    
</span><span id="LmdbRequest-101"><a href="#LmdbRequest-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">delete_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-102"><a href="#LmdbRequest-102"><span class="linenos">102</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="LmdbRequest-103"><a href="#LmdbRequest-103"><span class="linenos">103</span></a>
</span><span id="LmdbRequest-104"><a href="#LmdbRequest-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">open_db_environment</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest-105"><a href="#LmdbRequest-105"><span class="linenos">105</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">11</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="LmdbRequest.set_db_environment_path" class="classattr">
                                        <input id="LmdbRequest.set_db_environment_path-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_db_environment_path</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.set_db_environment_path-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.set_db_environment_path"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.set_db_environment_path-71"><a href="#LmdbRequest.set_db_environment_path-71"><span class="linenos">71</span></a>    <span class="k">def</span> <span class="nf">set_db_environment_path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.set_db_environment_path-72"><a href="#LmdbRequest.set_db_environment_path-72"><span class="linenos">72</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.open_databases" class="classattr">
                                        <input id="LmdbRequest.open_databases-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">open_databases</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.open_databases-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.open_databases"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.open_databases-74"><a href="#LmdbRequest.open_databases-74"><span class="linenos">74</span></a>    <span class="k">def</span> <span class="nf">open_databases</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_names</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">DbId</span><span class="p">,</span> <span class="n">DbName</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.open_databases-75"><a href="#LmdbRequest.open_databases-75"><span class="linenos">75</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">db_names</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.drop_db" class="classattr">
                                        <input id="LmdbRequest.drop_db-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">drop_db</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">db_id</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">delete</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.drop_db-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.drop_db"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.drop_db-77"><a href="#LmdbRequest.drop_db-77"><span class="linenos">77</span></a>    <span class="k">def</span> <span class="nf">drop_db</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span><span class="p">,</span> <span class="n">delete</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.drop_db-78"><a href="#LmdbRequest.drop_db-78"><span class="linenos">78</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">db_id</span><span class="p">,</span> <span class="n">delete</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.sync" class="classattr">
                                        <input id="LmdbRequest.sync-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sync</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.sync-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.sync"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.sync-80"><a href="#LmdbRequest.sync-80"><span class="linenos">80</span></a>    <span class="k">def</span> <span class="nf">sync</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.sync-81"><a href="#LmdbRequest.sync-81"><span class="linenos">81</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.get" class="classattr">
                                        <input id="LmdbRequest.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">key</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>,</span><span class="param">	<span class="n">db_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.get-83"><a href="#LmdbRequest.get-83"><span class="linenos">83</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.get-84"><a href="#LmdbRequest.get-84"><span class="linenos">84</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.get_items" class="classattr">
                                        <input id="LmdbRequest.get_items-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_items</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Hashable</span><span class="p">]]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.get_items-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.get_items"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.get_items-86"><a href="#LmdbRequest.get_items-86"><span class="linenos">86</span></a>    <span class="k">def</span> <span class="nf">get_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keys</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.get_items-87"><a href="#LmdbRequest.get_items-87"><span class="linenos">87</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="n">keys</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.get_all_items" class="classattr">
                                        <input id="LmdbRequest.get_all_items-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_all_items</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">db_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.get_all_items-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.get_all_items"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.get_all_items-89"><a href="#LmdbRequest.get_all_items-89"><span class="linenos">89</span></a>    <span class="k">def</span> <span class="nf">get_all_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.get_all_items-90"><a href="#LmdbRequest.get_all_items-90"><span class="linenos">90</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.put" class="classattr">
                                        <input id="LmdbRequest.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">key</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>,</span><span class="param">	<span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">db_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.put-92"><a href="#LmdbRequest.put-92"><span class="linenos">92</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.put-93"><a href="#LmdbRequest.put-93"><span class="linenos">93</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">7</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.put_items" class="classattr">
                                        <input id="LmdbRequest.put_items-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_items</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Hashable</span><span class="p">],</span> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.put_items-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.put_items"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.put_items-95"><a href="#LmdbRequest.put_items-95"><span class="linenos">95</span></a>    <span class="k">def</span> <span class="nf">put_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.put_items-96"><a href="#LmdbRequest.put_items-96"><span class="linenos">96</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.delete" class="classattr">
                                        <input id="LmdbRequest.delete-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">delete</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">key</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>,</span><span class="param">	<span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">db_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.delete-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.delete"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.delete-98"><a href="#LmdbRequest.delete-98"><span class="linenos">98</span></a>    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">KeyType</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">db_id</span><span class="p">:</span> <span class="n">DbId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.delete-99"><a href="#LmdbRequest.delete-99"><span class="linenos">99</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">db_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.delete_items" class="classattr">
                                        <input id="LmdbRequest.delete_items-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">delete_items</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Hashable</span><span class="p">],</span> <span class="n">Union</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.delete_items-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.delete_items"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.delete_items-101"><a href="#LmdbRequest.delete_items-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">delete_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">items</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ValueType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.delete_items-102"><a href="#LmdbRequest.delete_items-102"><span class="linenos">102</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.open_db_environment" class="classattr">
                                        <input id="LmdbRequest.open_db_environment-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">open_db_environment</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ServiceRequest</span>:</span></span>

                <label class="view-source-button" for="LmdbRequest.open_db_environment-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LmdbRequest.open_db_environment"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LmdbRequest.open_db_environment-104"><a href="#LmdbRequest.open_db_environment-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">open_db_environment</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceRequest</span><span class="p">:</span>
</span><span id="LmdbRequest.open_db_environment-105"><a href="#LmdbRequest.open_db_environment-105"><span class="linenos">105</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_save</span><span class="p">(</span><span class="mi">11</span><span class="p">,</span> <span class="n">path_to_db_environment</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LmdbRequest.default_service_type" class="classattr">
                                <div class="attr variable">
            <span class="name">default_service_type</span><span class="annotation">: Union[type[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.Service], NoneType]</span>        =
<span class="default_value">&lt;class &#39;<a href="#Lmdb">Lmdb</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#LmdbRequest.default_service_type"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.ServiceRequest</dt>
                                <dd id="LmdbRequest.default__request__type__" class="variable">default__request__type__</dd>
                <dd id="LmdbRequest.request_type" class="variable">request_type</dd>
                <dd id="LmdbRequest.args" class="variable">args</dd>
                <dd id="LmdbRequest.kwargs" class="variable">kwargs</dd>
                <dd id="LmdbRequest.provide_to_request_handler" class="variable">provide_to_request_handler</dd>
                <dd id="LmdbRequest.interface" class="function">interface</dd>
                <dd id="LmdbRequest.i" class="function">i</dd>
                <dd id="LmdbRequest.async_interface" class="function">async_interface</dd>
                <dd id="LmdbRequest.ai" class="function">ai</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="KeyType">
                    <div class="attr variable">
            <span class="name">KeyType</span>        =
<span class="default_value">typing.Union[bytes, str, typing.Any]</span>

        
    </div>
    <a class="headerlink" href="#KeyType"></a>
    
    

                </section>
                <section id="RawKeyType">
                    <div class="attr variable">
            <span class="name">RawKeyType</span>        =
<span class="default_value">&lt;class &#39;bytes&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#RawKeyType"></a>
    
    

                </section>
                <section id="ValueType">
                    <div class="attr variable">
            <span class="name">ValueType</span>        =
<span class="default_value">typing.Any</span>

        
    </div>
    <a class="headerlink" href="#ValueType"></a>
    
    

                </section>
                <section id="RawValueType">
                    <div class="attr variable">
            <span class="name">RawValueType</span>        =
<span class="default_value">&lt;class &#39;bytes&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#RawValueType"></a>
    
    

                </section>
                <section id="DbId">
                    <div class="attr variable">
            <span class="name">DbId</span>        =
<span class="default_value">typing.Hashable</span>

        
    </div>
    <a class="headerlink" href="#DbId"></a>
    
    

                </section>
                <section id="DbName">
                    <div class="attr variable">
            <span class="name">DbName</span>        =
<span class="default_value">&lt;class &#39;bytes&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#DbName"></a>
    
    

                </section>
                <section id="DbKeyError">
                            <input id="DbKeyError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">DbKeyError</span><wbr>(<span class="base">builtins.KeyError</span>):

                <label class="view-source-button" for="DbKeyError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DbKeyError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DbKeyError-506"><a href="#DbKeyError-506"><span class="linenos">506</span></a><span class="k">class</span> <span class="nc">DbKeyError</span><span class="p">(</span><span class="ne">KeyError</span><span class="p">):</span>
</span><span id="DbKeyError-507"><a href="#DbKeyError-507"><span class="linenos">507</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key_info</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="DbKeyError-508"><a href="#DbKeyError-508"><span class="linenos">508</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="DbKeyError-509"><a href="#DbKeyError-509"><span class="linenos">509</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">key_info</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]</span> <span class="o">=</span> <span class="n">key_info</span>
</span></pre></div>


            <div class="docstring"><p>Mapping key not found.</p>
</div>


                            <div id="DbKeyError.__init__" class="classattr">
                                        <input id="DbKeyError.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">DbKeyError</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">key_info</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Hashable</span><span class="p">]</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="nb">object</span></span>)</span>

                <label class="view-source-button" for="DbKeyError.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DbKeyError.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DbKeyError.__init__-507"><a href="#DbKeyError.__init__-507"><span class="linenos">507</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key_info</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="DbKeyError.__init__-508"><a href="#DbKeyError.__init__-508"><span class="linenos">508</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="DbKeyError.__init__-509"><a href="#DbKeyError.__init__-509"><span class="linenos">509</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">key_info</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">KeyType</span><span class="p">,</span> <span class="n">DbId</span><span class="p">]</span> <span class="o">=</span> <span class="n">key_info</span>
</span></pre></div>


    

                            </div>
                            <div id="DbKeyError.key_info" class="classattr">
                                <div class="attr variable">
            <span class="name">key_info</span><span class="annotation">: Tuple[Union[bytes, str, Any], Hashable]</span>

        
    </div>
    <a class="headerlink" href="#DbKeyError.key_info"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.BaseException</dt>
                                <dd id="DbKeyError.with_traceback" class="function">with_traceback</dd>
                <dd id="DbKeyError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>