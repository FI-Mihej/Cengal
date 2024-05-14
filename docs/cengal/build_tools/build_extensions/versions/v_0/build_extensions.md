---
title: build_extensions
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.build_tools<wbr>.build_extensions<wbr>.versions<wbr>.v_0<wbr>.build_extensions    </h1>

                
                        <input id="mod-build_extensions-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-build_extensions-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>    <span class="s1">&#39;CengalBuildExtension&#39;</span><span class="p">,</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>    <span class="s1">&#39;CengalSetuptoolsBuildExtension&#39;</span><span class="p">,</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>    <span class="s1">&#39;CengalCythonBuildExtension&#39;</span><span class="p">,</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>    <span class="s1">&#39;CengalGeneratorBuildExtension&#39;</span><span class="p">,</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="p">]</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="sd">Module Docstring</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="c1"># from distutils.dist import Distribution</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">os</span> <span class="kn">import</span> <span class="n">environ</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="kn">from</span> <span class="nn">setuptools._distutils.dist</span> <span class="kn">import</span> <span class="n">Distribution</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.path_manager</span> <span class="kn">import</span> <span class="n">path_relative_to_src</span><span class="p">,</span> <span class="n">RelativePath</span><span class="p">,</span> <span class="n">get_relative_path_part</span><span class="p">,</span> <span class="n">sep</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.directory_manager</span> <span class="kn">import</span> <span class="n">current_src_dir</span><span class="p">,</span> <span class="n">change_current_dir</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.directory_manager</span> <span class="kn">import</span> <span class="n">filtered_file_list</span><span class="p">,</span> <span class="n">FilteringType</span><span class="p">,</span> <span class="n">filtered_file_list_traversal</span><span class="p">,</span> <span class="n">file_list_traversal</span><span class="p">,</span> <span class="n">FilteringEntity</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.file_manager</span> <span class="kn">import</span> <span class="n">current_src_file_dir</span><span class="p">,</span> <span class="n">file_exists</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="kn">from</span> <span class="nn">cengal.build_tools.prepare_cflags</span> <span class="kn">import</span> <span class="n">prepare_cflags</span><span class="p">,</span> <span class="n">concat_cflags</span><span class="p">,</span> <span class="n">prepare_compile_time_env</span><span class="p">,</span> <span class="n">adjust_definition_names</span><span class="p">,</span> \
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="n">dict_of_tuples_to_dict</span><span class="p">,</span> <span class="n">list_to_dict</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span><span class="p">,</span> <span class="n">entity_repr_limited_try_qualname</span><span class="p">,</span> <span class="n">pifrl</span><span class="p">,</span> <span class="n">pdi</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="kn">from</span> <span class="nn">cengal.text_processing.text_processing</span> <span class="kn">import</span> <span class="n">find_text</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="kn">from</span> <span class="nn">cengal.system</span> <span class="kn">import</span> <span class="n">OS_TYPE</span><span class="p">,</span> <span class="n">TEMPLATE_MODULE_NAME</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="kn">from</span> <span class="nn">shutil</span> <span class="kn">import</span> <span class="n">rmtree</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="kn">from</span> <span class="nn">os</span> <span class="kn">import</span> <span class="n">remove</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="kn">from</span> <span class="nn">os.path</span> <span class="kn">import</span> <span class="n">splitext</span><span class="p">,</span> <span class="n">normpath</span><span class="p">,</span> <span class="n">join</span> <span class="k">as</span> <span class="n">path_join</span><span class="p">,</span> <span class="n">basename</span><span class="p">,</span> <span class="n">split</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">Extension</span> <span class="k">as</span> <span class="n">SetuptoolsExtension</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="kn">from</span> <span class="nn">Cython.Distutils</span> <span class="kn">import</span> <span class="n">Extension</span> <span class="k">as</span> <span class="n">CythonExtension</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="kn">from</span> <span class="nn">distutils.command.build</span> <span class="kn">import</span> <span class="n">build</span> <span class="k">as</span> <span class="n">build_orig</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="kn">from</span> <span class="nn">distutils.command.build_ext</span> <span class="kn">import</span> <span class="n">build_ext</span> <span class="k">as</span> <span class="n">build_ext_orig</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="kn">from</span> <span class="nn">setuptools.command.sdist</span> <span class="kn">import</span> <span class="n">sdist</span> <span class="k">as</span> <span class="n">sdist_orig</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="kn">import</span> <span class="nn">json</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="kn">import</span> <span class="nn">importlib</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="kn">from</span> <span class="nn">os.path</span> <span class="kn">import</span> <span class="n">isdir</span><span class="p">,</span> <span class="n">exists</span><span class="p">,</span> <span class="n">isfile</span><span class="p">,</span> <span class="n">dirname</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="kn">import</span> <span class="nn">setuptools</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="kn">import</span> <span class="nn">platform</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.path_manager</span> <span class="kn">import</span> <span class="n">RelativePath</span><span class="p">,</span> <span class="n">get_relative_path_part</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.directory_manager</span> <span class="kn">import</span> <span class="n">current_src_dir</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.directory_manager</span> <span class="kn">import</span> <span class="n">file_list_traversal</span><span class="p">,</span> <span class="n">FilteringEntity</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="kn">from</span> <span class="nn">cengal.build_tools.prepare_cflags</span> <span class="kn">import</span> <span class="n">prepare_compile_time_flags</span><span class="p">,</span> <span class="n">prepare_compile_time_env</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="kn">from</span> <span class="nn">cengal.os.execute</span> <span class="kn">import</span> <span class="n">prepare_params</span><span class="p">,</span> <span class="n">escape_text</span><span class="p">,</span> <span class="n">escape_param</span><span class="p">,</span> <span class="n">prepare_command</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a><span class="kn">from</span> <span class="nn">setuptools.discovery</span> <span class="kn">import</span> <span class="n">find_package_path</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a><span class="kn">import</span> <span class="nn">subprocess</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pprint</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">List</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Iterable</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Any</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="k">class</span> <span class="nc">CengalBuildExtension</span><span class="p">:</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    <span class="n">base_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="n">store_as_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_files</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_class</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_class</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="nf">sdist</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="nd">@property</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">path</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>    <span class="nd">@path</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">def</span> <span class="nf">path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="nd">@property</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">dir_path</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="k">return</span> <span class="kc">None</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">dirname</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_path</span><span class="p">)</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="nd">@property</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="nf">dir_path_rel</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RelativePath</span><span class="p">:</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="k">return</span> <span class="kc">None</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dirname</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_path</span><span class="p">))</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>    <span class="nd">@property</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="k">def</span> <span class="nf">module_import_str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="nd">@module_import_str</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">module_import_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    <span class="nd">@property</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    <span class="nd">@property</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="nf">package</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="k">return</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>    
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>    <span class="nd">@property</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>    <span class="k">def</span> <span class="nf">files</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_files</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>    <span class="nd">@files</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="nf">files</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_files</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a><span class="k">class</span> <span class="nc">CengalSetuptoolsBuildExtension</span><span class="p">(</span><span class="n">CengalBuildExtension</span><span class="p">):</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="n">base_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="n">SetuptoolsExtension</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a><span class="k">class</span> <span class="nc">CengalCythonBuildExtension</span><span class="p">(</span><span class="n">CengalBuildExtension</span><span class="p">):</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="n">base_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="n">CythonExtension</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a><span class="k">class</span> <span class="nc">CengalGeneratorBuildExtension</span><span class="p">(</span><span class="n">CengalBuildExtension</span><span class="p">):</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    <span class="n">base_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>    <span class="n">store_as_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>    
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            </section>
                <section id="CengalBuildExtension">
                            <input id="CengalBuildExtension-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CengalBuildExtension</span>:

                <label class="view-source-button" for="CengalBuildExtension-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension-86"><a href="#CengalBuildExtension-86"><span class="linenos"> 86</span></a><span class="k">class</span> <span class="nc">CengalBuildExtension</span><span class="p">:</span>
</span><span id="CengalBuildExtension-87"><a href="#CengalBuildExtension-87"><span class="linenos"> 87</span></a>    <span class="n">base_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CengalBuildExtension-88"><a href="#CengalBuildExtension-88"><span class="linenos"> 88</span></a>    <span class="n">store_as_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="CengalBuildExtension-89"><a href="#CengalBuildExtension-89"><span class="linenos"> 89</span></a>
</span><span id="CengalBuildExtension-90"><a href="#CengalBuildExtension-90"><span class="linenos"> 90</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CengalBuildExtension-91"><a href="#CengalBuildExtension-91"><span class="linenos"> 91</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="CengalBuildExtension-92"><a href="#CengalBuildExtension-92"><span class="linenos"> 92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CengalBuildExtension-93"><a href="#CengalBuildExtension-93"><span class="linenos"> 93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CengalBuildExtension-94"><a href="#CengalBuildExtension-94"><span class="linenos"> 94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_files</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="CengalBuildExtension-95"><a href="#CengalBuildExtension-95"><span class="linenos"> 95</span></a>
</span><span id="CengalBuildExtension-96"><a href="#CengalBuildExtension-96"><span class="linenos"> 96</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="CengalBuildExtension-97"><a href="#CengalBuildExtension-97"><span class="linenos"> 97</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_class</span><span class="p">(</span><span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_class</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="CengalBuildExtension-98"><a href="#CengalBuildExtension-98"><span class="linenos"> 98</span></a>    
</span><span id="CengalBuildExtension-99"><a href="#CengalBuildExtension-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">sdist</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="CengalBuildExtension-100"><a href="#CengalBuildExtension-100"><span class="linenos">100</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="CengalBuildExtension-101"><a href="#CengalBuildExtension-101"><span class="linenos">101</span></a>    
</span><span id="CengalBuildExtension-102"><a href="#CengalBuildExtension-102"><span class="linenos">102</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension-103"><a href="#CengalBuildExtension-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">path</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension-104"><a href="#CengalBuildExtension-104"><span class="linenos">104</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span>
</span><span id="CengalBuildExtension-105"><a href="#CengalBuildExtension-105"><span class="linenos">105</span></a>
</span><span id="CengalBuildExtension-106"><a href="#CengalBuildExtension-106"><span class="linenos">106</span></a>    <span class="nd">@path</span><span class="o">.</span><span class="n">setter</span>
</span><span id="CengalBuildExtension-107"><a href="#CengalBuildExtension-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">path</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="CengalBuildExtension-108"><a href="#CengalBuildExtension-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="CengalBuildExtension-109"><a href="#CengalBuildExtension-109"><span class="linenos">109</span></a>    
</span><span id="CengalBuildExtension-110"><a href="#CengalBuildExtension-110"><span class="linenos">110</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension-111"><a href="#CengalBuildExtension-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">dir_path</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension-112"><a href="#CengalBuildExtension-112"><span class="linenos">112</span></a>        <span class="k">return</span> <span class="kc">None</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">dirname</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_path</span><span class="p">)</span>
</span><span id="CengalBuildExtension-113"><a href="#CengalBuildExtension-113"><span class="linenos">113</span></a>    
</span><span id="CengalBuildExtension-114"><a href="#CengalBuildExtension-114"><span class="linenos">114</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension-115"><a href="#CengalBuildExtension-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="nf">dir_path_rel</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RelativePath</span><span class="p">:</span>
</span><span id="CengalBuildExtension-116"><a href="#CengalBuildExtension-116"><span class="linenos">116</span></a>        <span class="k">return</span> <span class="kc">None</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dirname</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_path</span><span class="p">))</span>
</span><span id="CengalBuildExtension-117"><a href="#CengalBuildExtension-117"><span class="linenos">117</span></a>
</span><span id="CengalBuildExtension-118"><a href="#CengalBuildExtension-118"><span class="linenos">118</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension-119"><a href="#CengalBuildExtension-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="nf">module_import_str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension-120"><a href="#CengalBuildExtension-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span>
</span><span id="CengalBuildExtension-121"><a href="#CengalBuildExtension-121"><span class="linenos">121</span></a>    
</span><span id="CengalBuildExtension-122"><a href="#CengalBuildExtension-122"><span class="linenos">122</span></a>    <span class="nd">@module_import_str</span><span class="o">.</span><span class="n">setter</span>
</span><span id="CengalBuildExtension-123"><a href="#CengalBuildExtension-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">module_import_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="CengalBuildExtension-124"><a href="#CengalBuildExtension-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="CengalBuildExtension-125"><a href="#CengalBuildExtension-125"><span class="linenos">125</span></a>
</span><span id="CengalBuildExtension-126"><a href="#CengalBuildExtension-126"><span class="linenos">126</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension-127"><a href="#CengalBuildExtension-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension-128"><a href="#CengalBuildExtension-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span>
</span><span id="CengalBuildExtension-129"><a href="#CengalBuildExtension-129"><span class="linenos">129</span></a>
</span><span id="CengalBuildExtension-130"><a href="#CengalBuildExtension-130"><span class="linenos">130</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension-131"><a href="#CengalBuildExtension-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">package</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension-132"><a href="#CengalBuildExtension-132"><span class="linenos">132</span></a>        <span class="k">return</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</span><span id="CengalBuildExtension-133"><a href="#CengalBuildExtension-133"><span class="linenos">133</span></a>    
</span><span id="CengalBuildExtension-134"><a href="#CengalBuildExtension-134"><span class="linenos">134</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension-135"><a href="#CengalBuildExtension-135"><span class="linenos">135</span></a>    <span class="k">def</span> <span class="nf">files</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension-136"><a href="#CengalBuildExtension-136"><span class="linenos">136</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_files</span>
</span><span id="CengalBuildExtension-137"><a href="#CengalBuildExtension-137"><span class="linenos">137</span></a>    
</span><span id="CengalBuildExtension-138"><a href="#CengalBuildExtension-138"><span class="linenos">138</span></a>    <span class="nd">@files</span><span class="o">.</span><span class="n">setter</span>
</span><span id="CengalBuildExtension-139"><a href="#CengalBuildExtension-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">files</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="CengalBuildExtension-140"><a href="#CengalBuildExtension-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_files</span> <span class="o">=</span> <span class="n">value</span>
</span></pre></div>


    

                            <div id="CengalBuildExtension.__init__" class="classattr">
                                        <input id="CengalBuildExtension.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">CengalBuildExtension</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="CengalBuildExtension.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.__init__-90"><a href="#CengalBuildExtension.__init__-90"><span class="linenos">90</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CengalBuildExtension.__init__-91"><a href="#CengalBuildExtension.__init__-91"><span class="linenos">91</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="CengalBuildExtension.__init__-92"><a href="#CengalBuildExtension.__init__-92"><span class="linenos">92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CengalBuildExtension.__init__-93"><a href="#CengalBuildExtension.__init__-93"><span class="linenos">93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CengalBuildExtension.__init__-94"><a href="#CengalBuildExtension.__init__-94"><span class="linenos">94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_files</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalBuildExtension.base_class" class="classattr">
                                <div class="attr variable">
            <span class="name">base_class</span><span class="annotation">: Union[Type, NoneType]</span>        =
<span class="default_value">None</span>

        
    </div>
    <a class="headerlink" href="#CengalBuildExtension.base_class"></a>
    
    

                            </div>
                            <div id="CengalBuildExtension.store_as_data" class="classattr">
                                <div class="attr variable">
            <span class="name">store_as_data</span><span class="annotation">: bool</span>        =
<span class="default_value">False</span>

        
    </div>
    <a class="headerlink" href="#CengalBuildExtension.store_as_data"></a>
    
    

                            </div>
                            <div id="CengalBuildExtension.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span>

        
    </div>
    <a class="headerlink" href="#CengalBuildExtension.kwargs"></a>
    
    

                            </div>
                            <div id="CengalBuildExtension.sdist" class="classattr">
                                        <input id="CengalBuildExtension.sdist-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sdist</span><span class="signature pdoc-code condensed">(<span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="CengalBuildExtension.sdist-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.sdist"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.sdist-99"><a href="#CengalBuildExtension.sdist-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">sdist</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="CengalBuildExtension.sdist-100"><a href="#CengalBuildExtension.sdist-100"><span class="linenos">100</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalBuildExtension.path" class="classattr">
                                        <input id="CengalBuildExtension.path-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">path</span><span class="annotation">: str</span>

                <label class="view-source-button" for="CengalBuildExtension.path-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.path"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.path-102"><a href="#CengalBuildExtension.path-102"><span class="linenos">102</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension.path-103"><a href="#CengalBuildExtension.path-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">path</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension.path-104"><a href="#CengalBuildExtension.path-104"><span class="linenos">104</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalBuildExtension.dir_path" class="classattr">
                                        <input id="CengalBuildExtension.dir_path-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">dir_path</span><span class="annotation">: str</span>

                <label class="view-source-button" for="CengalBuildExtension.dir_path-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.dir_path"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.dir_path-110"><a href="#CengalBuildExtension.dir_path-110"><span class="linenos">110</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension.dir_path-111"><a href="#CengalBuildExtension.dir_path-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">dir_path</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension.dir_path-112"><a href="#CengalBuildExtension.dir_path-112"><span class="linenos">112</span></a>        <span class="k">return</span> <span class="kc">None</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">dirname</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_path</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalBuildExtension.dir_path_rel" class="classattr">
                                        <input id="CengalBuildExtension.dir_path_rel-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">dir_path_rel</span><span class="annotation">: cengal.file_system.path_manager.versions.v_0.path_manager.RelativePath</span>

                <label class="view-source-button" for="CengalBuildExtension.dir_path_rel-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.dir_path_rel"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.dir_path_rel-114"><a href="#CengalBuildExtension.dir_path_rel-114"><span class="linenos">114</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension.dir_path_rel-115"><a href="#CengalBuildExtension.dir_path_rel-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="nf">dir_path_rel</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RelativePath</span><span class="p">:</span>
</span><span id="CengalBuildExtension.dir_path_rel-116"><a href="#CengalBuildExtension.dir_path_rel-116"><span class="linenos">116</span></a>        <span class="k">return</span> <span class="kc">None</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_path</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dirname</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_path</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalBuildExtension.module_import_str" class="classattr">
                                        <input id="CengalBuildExtension.module_import_str-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">module_import_str</span><span class="annotation">: str</span>

                <label class="view-source-button" for="CengalBuildExtension.module_import_str-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.module_import_str"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.module_import_str-118"><a href="#CengalBuildExtension.module_import_str-118"><span class="linenos">118</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension.module_import_str-119"><a href="#CengalBuildExtension.module_import_str-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="nf">module_import_str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension.module_import_str-120"><a href="#CengalBuildExtension.module_import_str-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalBuildExtension.name" class="classattr">
                                        <input id="CengalBuildExtension.name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">name</span><span class="annotation">: str</span>

                <label class="view-source-button" for="CengalBuildExtension.name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.name-126"><a href="#CengalBuildExtension.name-126"><span class="linenos">126</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension.name-127"><a href="#CengalBuildExtension.name-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension.name-128"><a href="#CengalBuildExtension.name-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalBuildExtension.package" class="classattr">
                                        <input id="CengalBuildExtension.package-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">package</span><span class="annotation">: str</span>

                <label class="view-source-button" for="CengalBuildExtension.package-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.package"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.package-130"><a href="#CengalBuildExtension.package-130"><span class="linenos">130</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension.package-131"><a href="#CengalBuildExtension.package-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">package</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension.package-132"><a href="#CengalBuildExtension.package-132"><span class="linenos">132</span></a>        <span class="k">return</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_module_import_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalBuildExtension.files" class="classattr">
                                        <input id="CengalBuildExtension.files-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">files</span><span class="annotation">: str</span>

                <label class="view-source-button" for="CengalBuildExtension.files-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalBuildExtension.files"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalBuildExtension.files-134"><a href="#CengalBuildExtension.files-134"><span class="linenos">134</span></a>    <span class="nd">@property</span>
</span><span id="CengalBuildExtension.files-135"><a href="#CengalBuildExtension.files-135"><span class="linenos">135</span></a>    <span class="k">def</span> <span class="nf">files</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="CengalBuildExtension.files-136"><a href="#CengalBuildExtension.files-136"><span class="linenos">136</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_files</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="CengalSetuptoolsBuildExtension">
                            <input id="CengalSetuptoolsBuildExtension-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CengalSetuptoolsBuildExtension</span><wbr>(<span class="base"><a href="#CengalBuildExtension">CengalBuildExtension</a></span>):

                <label class="view-source-button" for="CengalSetuptoolsBuildExtension-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalSetuptoolsBuildExtension"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalSetuptoolsBuildExtension-143"><a href="#CengalSetuptoolsBuildExtension-143"><span class="linenos">143</span></a><span class="k">class</span> <span class="nc">CengalSetuptoolsBuildExtension</span><span class="p">(</span><span class="n">CengalBuildExtension</span><span class="p">):</span>
</span><span id="CengalSetuptoolsBuildExtension-144"><a href="#CengalSetuptoolsBuildExtension-144"><span class="linenos">144</span></a>    <span class="n">base_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="n">SetuptoolsExtension</span>
</span><span id="CengalSetuptoolsBuildExtension-145"><a href="#CengalSetuptoolsBuildExtension-145"><span class="linenos">145</span></a>
</span><span id="CengalSetuptoolsBuildExtension-146"><a href="#CengalSetuptoolsBuildExtension-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CengalSetuptoolsBuildExtension-147"><a href="#CengalSetuptoolsBuildExtension-147"><span class="linenos">147</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="CengalSetuptoolsBuildExtension.__init__" class="classattr">
                                        <input id="CengalSetuptoolsBuildExtension.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">CengalSetuptoolsBuildExtension</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="CengalSetuptoolsBuildExtension.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalSetuptoolsBuildExtension.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalSetuptoolsBuildExtension.__init__-146"><a href="#CengalSetuptoolsBuildExtension.__init__-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CengalSetuptoolsBuildExtension.__init__-147"><a href="#CengalSetuptoolsBuildExtension.__init__-147"><span class="linenos">147</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalSetuptoolsBuildExtension.base_class" class="classattr">
                                <div class="attr variable">
            <span class="name">base_class</span><span class="annotation">: Union[Type, NoneType]</span>        =
<span class="default_value">&lt;class &#39;setuptools.extension.Extension&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#CengalSetuptoolsBuildExtension.base_class"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#CengalBuildExtension">CengalBuildExtension</a></dt>
                                <dd id="CengalSetuptoolsBuildExtension.store_as_data" class="variable"><a href="#CengalBuildExtension.store_as_data">store_as_data</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.kwargs" class="variable"><a href="#CengalBuildExtension.kwargs">kwargs</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.sdist" class="function"><a href="#CengalBuildExtension.sdist">sdist</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.path" class="variable"><a href="#CengalBuildExtension.path">path</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.dir_path" class="variable"><a href="#CengalBuildExtension.dir_path">dir_path</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.dir_path_rel" class="variable"><a href="#CengalBuildExtension.dir_path_rel">dir_path_rel</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.module_import_str" class="variable"><a href="#CengalBuildExtension.module_import_str">module_import_str</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.name" class="variable"><a href="#CengalBuildExtension.name">name</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.package" class="variable"><a href="#CengalBuildExtension.package">package</a></dd>
                <dd id="CengalSetuptoolsBuildExtension.files" class="variable"><a href="#CengalBuildExtension.files">files</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CengalCythonBuildExtension">
                            <input id="CengalCythonBuildExtension-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CengalCythonBuildExtension</span><wbr>(<span class="base"><a href="#CengalBuildExtension">CengalBuildExtension</a></span>):

                <label class="view-source-button" for="CengalCythonBuildExtension-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalCythonBuildExtension"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalCythonBuildExtension-150"><a href="#CengalCythonBuildExtension-150"><span class="linenos">150</span></a><span class="k">class</span> <span class="nc">CengalCythonBuildExtension</span><span class="p">(</span><span class="n">CengalBuildExtension</span><span class="p">):</span>
</span><span id="CengalCythonBuildExtension-151"><a href="#CengalCythonBuildExtension-151"><span class="linenos">151</span></a>    <span class="n">base_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="n">CythonExtension</span>
</span><span id="CengalCythonBuildExtension-152"><a href="#CengalCythonBuildExtension-152"><span class="linenos">152</span></a>
</span><span id="CengalCythonBuildExtension-153"><a href="#CengalCythonBuildExtension-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CengalCythonBuildExtension-154"><a href="#CengalCythonBuildExtension-154"><span class="linenos">154</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="CengalCythonBuildExtension.__init__" class="classattr">
                                        <input id="CengalCythonBuildExtension.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">CengalCythonBuildExtension</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="CengalCythonBuildExtension.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalCythonBuildExtension.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalCythonBuildExtension.__init__-153"><a href="#CengalCythonBuildExtension.__init__-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CengalCythonBuildExtension.__init__-154"><a href="#CengalCythonBuildExtension.__init__-154"><span class="linenos">154</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalCythonBuildExtension.base_class" class="classattr">
                                <div class="attr variable">
            <span class="name">base_class</span><span class="annotation">: Union[Type, NoneType]</span>        =
<span class="default_value">&lt;class &#39;Cython.Distutils.extension.Extension&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#CengalCythonBuildExtension.base_class"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#CengalBuildExtension">CengalBuildExtension</a></dt>
                                <dd id="CengalCythonBuildExtension.store_as_data" class="variable"><a href="#CengalBuildExtension.store_as_data">store_as_data</a></dd>
                <dd id="CengalCythonBuildExtension.kwargs" class="variable"><a href="#CengalBuildExtension.kwargs">kwargs</a></dd>
                <dd id="CengalCythonBuildExtension.sdist" class="function"><a href="#CengalBuildExtension.sdist">sdist</a></dd>
                <dd id="CengalCythonBuildExtension.path" class="variable"><a href="#CengalBuildExtension.path">path</a></dd>
                <dd id="CengalCythonBuildExtension.dir_path" class="variable"><a href="#CengalBuildExtension.dir_path">dir_path</a></dd>
                <dd id="CengalCythonBuildExtension.dir_path_rel" class="variable"><a href="#CengalBuildExtension.dir_path_rel">dir_path_rel</a></dd>
                <dd id="CengalCythonBuildExtension.module_import_str" class="variable"><a href="#CengalBuildExtension.module_import_str">module_import_str</a></dd>
                <dd id="CengalCythonBuildExtension.name" class="variable"><a href="#CengalBuildExtension.name">name</a></dd>
                <dd id="CengalCythonBuildExtension.package" class="variable"><a href="#CengalBuildExtension.package">package</a></dd>
                <dd id="CengalCythonBuildExtension.files" class="variable"><a href="#CengalBuildExtension.files">files</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CengalGeneratorBuildExtension">
                            <input id="CengalGeneratorBuildExtension-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CengalGeneratorBuildExtension</span><wbr>(<span class="base"><a href="#CengalBuildExtension">CengalBuildExtension</a></span>):

                <label class="view-source-button" for="CengalGeneratorBuildExtension-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalGeneratorBuildExtension"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalGeneratorBuildExtension-157"><a href="#CengalGeneratorBuildExtension-157"><span class="linenos">157</span></a><span class="k">class</span> <span class="nc">CengalGeneratorBuildExtension</span><span class="p">(</span><span class="n">CengalBuildExtension</span><span class="p">):</span>
</span><span id="CengalGeneratorBuildExtension-158"><a href="#CengalGeneratorBuildExtension-158"><span class="linenos">158</span></a>    <span class="n">base_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CengalGeneratorBuildExtension-159"><a href="#CengalGeneratorBuildExtension-159"><span class="linenos">159</span></a>    <span class="n">store_as_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="CengalGeneratorBuildExtension-160"><a href="#CengalGeneratorBuildExtension-160"><span class="linenos">160</span></a>
</span><span id="CengalGeneratorBuildExtension-161"><a href="#CengalGeneratorBuildExtension-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CengalGeneratorBuildExtension-162"><a href="#CengalGeneratorBuildExtension-162"><span class="linenos">162</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="CengalGeneratorBuildExtension-163"><a href="#CengalGeneratorBuildExtension-163"><span class="linenos">163</span></a>    
</span><span id="CengalGeneratorBuildExtension-164"><a href="#CengalGeneratorBuildExtension-164"><span class="linenos">164</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CengalGeneratorBuildExtension-165"><a href="#CengalGeneratorBuildExtension-165"><span class="linenos">165</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="CengalGeneratorBuildExtension.__init__" class="classattr">
                                        <input id="CengalGeneratorBuildExtension.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">CengalGeneratorBuildExtension</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="CengalGeneratorBuildExtension.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CengalGeneratorBuildExtension.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CengalGeneratorBuildExtension.__init__-161"><a href="#CengalGeneratorBuildExtension.__init__-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CengalGeneratorBuildExtension.__init__-162"><a href="#CengalGeneratorBuildExtension.__init__-162"><span class="linenos">162</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CengalGeneratorBuildExtension.base_class" class="classattr">
                                <div class="attr variable">
            <span class="name">base_class</span><span class="annotation">: Union[Type, NoneType]</span>        =
<span class="default_value">None</span>

        
    </div>
    <a class="headerlink" href="#CengalGeneratorBuildExtension.base_class"></a>
    
    

                            </div>
                            <div id="CengalGeneratorBuildExtension.store_as_data" class="classattr">
                                <div class="attr variable">
            <span class="name">store_as_data</span><span class="annotation">: bool</span>        =
<span class="default_value">True</span>

        
    </div>
    <a class="headerlink" href="#CengalGeneratorBuildExtension.store_as_data"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#CengalBuildExtension">CengalBuildExtension</a></dt>
                                <dd id="CengalGeneratorBuildExtension.kwargs" class="variable"><a href="#CengalBuildExtension.kwargs">kwargs</a></dd>
                <dd id="CengalGeneratorBuildExtension.sdist" class="function"><a href="#CengalBuildExtension.sdist">sdist</a></dd>
                <dd id="CengalGeneratorBuildExtension.path" class="variable"><a href="#CengalBuildExtension.path">path</a></dd>
                <dd id="CengalGeneratorBuildExtension.dir_path" class="variable"><a href="#CengalBuildExtension.dir_path">dir_path</a></dd>
                <dd id="CengalGeneratorBuildExtension.dir_path_rel" class="variable"><a href="#CengalBuildExtension.dir_path_rel">dir_path_rel</a></dd>
                <dd id="CengalGeneratorBuildExtension.module_import_str" class="variable"><a href="#CengalBuildExtension.module_import_str">module_import_str</a></dd>
                <dd id="CengalGeneratorBuildExtension.name" class="variable"><a href="#CengalBuildExtension.name">name</a></dd>
                <dd id="CengalGeneratorBuildExtension.package" class="variable"><a href="#CengalBuildExtension.package">package</a></dd>
                <dd id="CengalGeneratorBuildExtension.files" class="variable"><a href="#CengalBuildExtension.files">files</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>