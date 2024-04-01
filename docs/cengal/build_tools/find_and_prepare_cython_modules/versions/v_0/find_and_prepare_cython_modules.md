---
title: find_and_prepare_cython_modules
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.build_tools<wbr>.find_and_prepare_cython_modules<wbr>.versions<wbr>.v_0<wbr>.find_and_prepare_cython_modules    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-find_and_prepare_cython_modules-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-find_and_prepare_cython_modules-view-source"><span>View Source</span></label>

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
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="c1"># from distutils.dist import Distribution</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">os</span> <span class="kn">import</span> <span class="n">environ</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">setuptools._distutils.dist</span> <span class="kn">import</span> <span class="n">Distribution</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.path_manager</span> <span class="kn">import</span> <span class="n">path_relative_to_src</span><span class="p">,</span> <span class="n">RelativePath</span><span class="p">,</span> <span class="n">get_relative_path_part</span><span class="p">,</span> <span class="n">sep</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.directory_manager</span> <span class="kn">import</span> <span class="n">current_src_dir</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.directory_manager</span> <span class="kn">import</span> <span class="n">filtered_file_list</span><span class="p">,</span> <span class="n">FilteringType</span><span class="p">,</span> <span class="n">filtered_file_list_traversal</span><span class="p">,</span> <span class="n">file_list_traversal</span><span class="p">,</span> <span class="n">FilteringEntity</span><span class="p">,</span> \
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="n">change_current_dir</span><span class="p">,</span> <span class="n">secure_current_dir</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">cengal.build_tools.prepare_cflags</span> <span class="kn">import</span> <span class="n">prepare_cflags</span><span class="p">,</span> <span class="n">concat_cflags</span><span class="p">,</span> <span class="n">prepare_compile_time_env</span><span class="p">,</span> <span class="n">prepare_cflags_dict</span><span class="p">,</span> <span class="n">prepare_given_cflags_dict</span><span class="p">,</span> \
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="n">prepare_pyx_flags_dict</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span><span class="p">,</span> <span class="n">entity_repr_limited_try_qualname</span><span class="p">,</span> <span class="n">pifrl</span><span class="p">,</span> <span class="n">pdi</span><span class="p">,</span> <span class="n">class_properties_values_including_overrided</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="kn">from</span> <span class="nn">cengal.hardware.info.cpu</span> <span class="kn">import</span> <span class="n">cpu_info</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="kn">from</span> <span class="nn">cengal.system</span> <span class="kn">import</span> <span class="n">OS_TYPE</span><span class="p">,</span> <span class="n">TEMPLATE_MODULE_NAME</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="kn">from</span> <span class="nn">shutil</span> <span class="kn">import</span> <span class="n">rmtree</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="kn">from</span> <span class="nn">os</span> <span class="kn">import</span> <span class="n">remove</span><span class="p">,</span> <span class="n">getcwd</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="kn">from</span> <span class="nn">os.path</span> <span class="kn">import</span> <span class="n">splitext</span><span class="p">,</span> <span class="n">normpath</span><span class="p">,</span> <span class="n">join</span> <span class="k">as</span> <span class="n">path_join</span><span class="p">,</span> <span class="n">basename</span><span class="p">,</span> <span class="n">split</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">Extension</span> <span class="k">as</span> <span class="n">SetuptoolsExtension</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="kn">from</span> <span class="nn">Cython.Distutils</span> <span class="kn">import</span> <span class="n">Extension</span> <span class="k">as</span> <span class="n">CythonExtension</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="kn">from</span> <span class="nn">distutils.command.build</span> <span class="kn">import</span> <span class="n">build</span> <span class="k">as</span> <span class="n">build_orig</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="kn">from</span> <span class="nn">distutils.command.build_ext</span> <span class="kn">import</span> <span class="n">build_ext</span> <span class="k">as</span> <span class="n">build_ext_orig</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="kn">from</span> <span class="nn">setuptools.command.sdist</span> <span class="kn">import</span> <span class="n">sdist</span> <span class="k">as</span> <span class="n">sdist_orig</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="kn">import</span> <span class="nn">json</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="kn">import</span> <span class="nn">importlib</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="kn">from</span> <span class="nn">os.path</span> <span class="kn">import</span> <span class="n">isdir</span><span class="p">,</span> <span class="n">exists</span><span class="p">,</span> <span class="n">isfile</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="kn">import</span> <span class="nn">setuptools</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="kn">import</span> <span class="nn">platform</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.path_manager</span> <span class="kn">import</span> <span class="n">RelativePath</span><span class="p">,</span> <span class="n">get_relative_path_part</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.directory_manager</span> <span class="kn">import</span> <span class="n">current_src_dir</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.directory_manager</span> <span class="kn">import</span> <span class="n">file_list_traversal</span><span class="p">,</span> <span class="n">FilteringEntity</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="kn">from</span> <span class="nn">cengal.os.execute</span> <span class="kn">import</span> <span class="n">prepare_params</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="kn">from</span> <span class="nn">setuptools.discovery</span> <span class="kn">import</span> <span class="n">find_package_path</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="kn">import</span> <span class="nn">subprocess</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="kn">from</span> <span class="nn">cengal.build_tools.build_extensions</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pprint</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">List</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Iterable</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Set</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="n">_PYTHON_VERSION</span> <span class="o">=</span> <span class="n">platform</span><span class="o">.</span><span class="n">python_version_tuple</span><span class="p">()</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a><span class="n">BUILD_CONFIG_FILENAME</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;__build_config.py&#39;</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a><span class="n">GITKEEP_FILE_NAME</span> <span class="o">=</span> <span class="s1">&#39;.gitkeep&#39;</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="n">MANIFEST_INCLUDED_FILES_FILE_NAME</span> <span class="o">=</span> <span class="s1">&#39;MANIFEST.in&#39;</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="n">MANIFEST_INCLUDED_FILES_TEMPLATE_FILE_NAME</span> <span class="o">=</span> <span class="s1">&#39;MANIFEST.in.template&#39;</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="n">cython_file_ext</span> <span class="o">=</span> <span class="s1">&#39;.pyx&#39;</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="n">cython_transpiled_ext</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;.c&#39;</span><span class="p">}</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="n">compilable_ext</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;.pyx&#39;</span><span class="p">,</span> <span class="s1">&#39;.cpp&#39;</span><span class="p">,</span> <span class="s1">&#39;.c++&#39;</span><span class="p">,</span> <span class="s1">&#39;.cxx&#39;</span><span class="p">,</span> <span class="s1">&#39;.cc&#39;</span><span class="p">}</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a><span class="n">codegen_files_ext</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;.c&#39;</span><span class="p">,</span> <span class="s1">&#39;.cpp&#39;</span><span class="p">,</span> <span class="s1">&#39;.c++&#39;</span><span class="p">,</span> <span class="s1">&#39;.cxx&#39;</span><span class="p">,</span> <span class="s1">&#39;.cc&#39;</span><span class="p">}</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="n">headers_ext</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;.h&#39;</span><span class="p">,</span> <span class="s1">&#39;.hpp&#39;</span><span class="p">,</span> <span class="s1">&#39;.h++&#39;</span><span class="p">,</span> <span class="s1">&#39;.hh&#39;</span><span class="p">,</span> <span class="s1">&#39;.hxx&#39;</span><span class="p">}</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="n">libs_ext</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;.lib&#39;</span><span class="p">,</span> <span class="s1">&#39;.dll&#39;</span><span class="p">,</span> <span class="s1">&#39;.so&#39;</span><span class="p">}</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="n">all_ext</span> <span class="o">=</span> <span class="n">cython_transpiled_ext</span> <span class="o">|</span> <span class="n">compilable_ext</span> <span class="o">|</span> <span class="n">headers_ext</span> <span class="o">|</span> <span class="n">libs_ext</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="k">def</span> <span class="nf">find_good_packages</span><span class="p">(</span><span class="n">where</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="n">exclude</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(),</span> <span class="n">include</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;*&#39;</span><span class="p">,),</span> 
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>                       <span class="n">modules_to_ignore</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(),</span> <span class="n">python_2_modules</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()):</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>    <span class="n">all_packages</span> <span class="o">=</span> <span class="n">setuptools</span><span class="o">.</span><span class="n">find_packages</span><span class="p">(</span><span class="n">where</span><span class="p">,</span> <span class="n">exclude</span><span class="p">,</span> <span class="n">include</span><span class="p">)</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    <span class="n">good_packages</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">for</span> <span class="n">package</span> <span class="ow">in</span> <span class="n">all_packages</span><span class="p">:</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="n">is_good</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">modules_to_ignore</span><span class="p">:</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>            <span class="k">if</span> <span class="n">package</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">item</span><span class="p">):</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>                <span class="n">is_good</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>                <span class="k">break</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="k">if</span> <span class="s1">&#39;3&#39;</span> <span class="o">==</span> <span class="n">_PYTHON_VERSION</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">python_2_modules</span><span class="p">:</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>                <span class="k">if</span> <span class="n">package</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">item</span><span class="p">):</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>                    <span class="n">is_good</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>                    <span class="k">break</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="k">if</span> <span class="n">is_good</span><span class="p">:</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>            <span class="n">good_packages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">package</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>    <span class="k">return</span> <span class="n">good_packages</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a><span class="k">def</span> <span class="nf">find_package_data_filter</span><span class="p">(</span><span class="n">filtering_entity</span><span class="p">:</span> <span class="n">FilteringEntity</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="k">if</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">dirpath</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">dirname</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">filename</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="n">dirpath</span><span class="p">,</span> <span class="n">filename</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="k">return</span> <span class="n">GITKEEP_FILE_NAME</span> <span class="o">!=</span> <span class="n">filename</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">aggregated</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="k">def</span> <span class="nf">find_package_data</span><span class="p">(</span><span class="n">package_src_relative_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">good_packages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">root_rel</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RelativePath</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>    <span class="n">depth</span> <span class="o">=</span> <span class="n">depth</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>    <span class="n">depth</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>    <span class="n">root_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">current_src_dir</span><span class="p">())</span> <span class="k">if</span> <span class="n">root_rel</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">root_rel</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    <span class="n">root_path</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">root_path</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>    <span class="n">package_src_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">root_rel</span><span class="p">(</span><span class="n">package_src_relative_path</span><span class="p">))</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="n">package_src_path</span> <span class="o">=</span> <span class="n">package_src_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">package_src_path</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>    <span class="n">packages_data_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="n">manifest_included_files</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="k">for</span> <span class="n">package_name</span> <span class="ow">in</span> <span class="n">good_packages</span><span class="p">:</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="n">package_path</span> <span class="o">=</span> <span class="n">find_package_path</span><span class="p">(</span><span class="n">package_name</span><span class="p">,</span> <span class="nb">dict</span><span class="p">(),</span> <span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="n">package_full_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="n">package_path</span><span class="p">)</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="n">package_full_path_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">package_full_path</span><span class="p">)</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="n">package_data</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="n">possible_data_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">package_full_path_rel</span><span class="p">(</span><span class="s1">&#39;data&#39;</span><span class="p">)</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="k">if</span> <span class="n">exists</span><span class="p">(</span><span class="n">possible_data_dir</span><span class="p">)</span> <span class="ow">and</span> <span class="n">isdir</span><span class="p">(</span><span class="n">possible_data_dir</span><span class="p">):</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>            <span class="n">possible_data_dir_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">possible_data_dir</span><span class="p">)</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>            <span class="n">travers_result</span> <span class="o">=</span> <span class="n">file_list_traversal</span><span class="p">(</span><span class="n">possible_data_dir</span><span class="p">,</span> <span class="n">find_package_data_filter</span><span class="p">,</span> <span class="n">remove_empty_dirpaths</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>            <span class="k">for</span> <span class="n">dirpath</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">travers_result</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>                <span class="n">dirpath_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>                <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">filenames</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>                    <span class="n">file_full_path</span> <span class="o">=</span> <span class="n">dirpath_rel</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>                    <span class="n">package_data</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">file_full_path</span><span class="p">,</span> <span class="n">package_full_path</span><span class="p">))</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>                    <span class="n">manifest_included_files</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">file_full_path</span><span class="p">,</span> <span class="n">root_path</span><span class="p">))</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>        <span class="n">pyx_files</span> <span class="o">=</span> <span class="n">filtered_file_list_traversal</span><span class="p">(</span><span class="n">package_full_path</span><span class="p">,</span> <span class="n">FilteringType</span><span class="o">.</span><span class="n">including</span><span class="p">,</span> <span class="p">{</span><span class="s1">&#39;.pyx&#39;</span><span class="p">},</span> <span class="n">remove_empty_items</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="k">for</span> <span class="n">dirpath</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">pyx_files</span><span class="p">:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>            <span class="n">dirpath_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">filenames</span><span class="p">:</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>                <span class="n">file_full_path</span> <span class="o">=</span> <span class="n">dirpath_rel</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>                <span class="n">package_data</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">file_full_path</span><span class="p">,</span> <span class="n">package_full_path</span><span class="p">))</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>                <span class="n">manifest_included_files</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">file_full_path</span><span class="p">,</span> <span class="n">root_path</span><span class="p">))</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="k">if</span> <span class="n">package_data</span><span class="p">:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            <span class="n">packages_data_dict</span><span class="p">[</span><span class="n">package_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">package_data</span><span class="p">)</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>    <span class="k">return</span> <span class="n">packages_data_dict</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">manifest_included_files</span><span class="p">)</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="k">def</span> <span class="nf">generate_manifest_included_files</span><span class="p">(</span><span class="n">manifest_included_files</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">root_rel</span><span class="p">:</span> <span class="n">RelativePath</span><span class="p">):</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>    <span class="n">manifest_included_files_template_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="n">MANIFEST_INCLUDED_FILES_TEMPLATE_FILE_NAME</span><span class="p">)</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>    <span class="n">manifest_included_files_template_contents</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>    <span class="k">if</span> <span class="n">exists</span><span class="p">(</span><span class="n">manifest_included_files_template_path</span><span class="p">)</span> <span class="ow">and</span> <span class="n">isfile</span><span class="p">(</span><span class="n">manifest_included_files_template_path</span><span class="p">):</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">manifest_included_files_template_path</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>            <span class="n">manifest_included_files_template_contents</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>    <span class="n">manifest_included_files_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="n">MANIFEST_INCLUDED_FILES_FILE_NAME</span><span class="p">)</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">manifest_included_files_path</span><span class="p">,</span> <span class="s1">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="k">if</span> <span class="n">manifest_included_files_template_contents</span><span class="p">:</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">manifest_included_files_template_contents</span> <span class="o">+</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>        <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">manifest_included_files</span><span class="p">:</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;include </span><span class="si">{</span><span class="n">file</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="k">def</span> <span class="nf">get_file_name_without_extension</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="n">file_name</span> <span class="o">=</span> <span class="n">basename</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>  <span class="c1"># Get the base name from the path</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>    <span class="n">file_name_without_extension</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">file_name</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># Split the file name and extension, and take only the file name part</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="k">return</span> <span class="n">file_name_without_extension</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a><span class="k">def</span> <span class="nf">remove_header_files</span><span class="p">(</span><span class="n">ext_modules</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CythonExtension</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CythonExtension</span><span class="p">]:</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    <span class="k">for</span> <span class="n">ext_module</span> <span class="ow">in</span> <span class="n">ext_modules</span><span class="p">:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">):</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>            <span class="n">new_sources</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>            <span class="k">for</span> <span class="n">source</span> <span class="ow">in</span> <span class="n">ext_module</span><span class="o">.</span><span class="n">sources</span><span class="p">:</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>                <span class="n">_</span><span class="p">,</span> <span class="n">file_extension</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">source</span><span class="p">)</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>                <span class="k">if</span> <span class="n">file_extension</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">headers_ext</span><span class="p">:</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>                    <span class="n">new_sources</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">source</span><span class="p">)</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>            
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>            <span class="n">ext_module</span><span class="o">.</span><span class="n">sources</span> <span class="o">=</span> <span class="n">new_sources</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>    
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>    <span class="k">return</span> <span class="n">ext_modules</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="k">def</span> <span class="nf">extend_file_names_to_root_relative_paths</span><span class="p">(</span><span class="n">root_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">dir_path_obj</span><span class="p">:</span> <span class="n">RelativePath</span><span class="p">,</span> <span class="n">file_names_or_path</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>    <span class="k">for</span> <span class="n">file_name_or_path</span> <span class="ow">in</span> <span class="n">file_names_or_path</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">file_name_or_path</span><span class="p">:</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>            <span class="k">continue</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>        <span class="n">owner_path</span><span class="p">,</span> <span class="n">file_name</span> <span class="o">=</span> <span class="n">split</span><span class="p">(</span><span class="n">file_name_or_path</span><span class="p">)</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="n">file_name</span> <span class="o">=</span> <span class="n">file_name</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="k">if</span> <span class="n">owner_path</span><span class="p">:</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">file_name_or_path</span><span class="p">)</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">path_join</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file_name</span><span class="p">),</span> <span class="n">root_path</span><span class="p">)))</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>    
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a><span class="k">def</span> <span class="nf">process_macros</span><span class="p">(</span><span class="n">ext_modules</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CythonExtension</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CythonExtension</span><span class="p">]:</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    <span class="k">for</span> <span class="n">ext_module</span> <span class="ow">in</span> <span class="n">ext_modules</span><span class="p">:</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">):</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="s1">&#39;compile_time_env&#39;</span><span class="p">):</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>                <span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">ext_module</span><span class="o">.</span><span class="n">compile_time_env</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>                <span class="n">compile_time_env</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>            
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="s1">&#39;cython_compile_time_env&#39;</span><span class="p">):</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>                <span class="n">cython_compile_time_env</span> <span class="o">=</span> <span class="n">ext_module</span><span class="o">.</span><span class="n">cython_compile_time_env</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>                <span class="n">compile_time_env</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">cython_compile_time_env</span><span class="p">)</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>                <span class="n">ext_module</span><span class="o">.</span><span class="n">cython_compile_time_env</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="n">ext_module</span><span class="o">.</span><span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">compile_time_env</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="s1">&#39;define_macros&#39;</span><span class="p">):</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>                <span class="n">define_macros</span> <span class="o">=</span> <span class="n">ext_module</span><span class="o">.</span><span class="n">define_macros</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>                <span class="n">define_macros</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>            
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">define_macros</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>                <span class="n">define_macros</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">define_macros</span><span class="o">.</span><span class="n">items</span><span class="p">())</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>            
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            <span class="n">new_define_macros</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>            <span class="k">for</span> <span class="n">macros_name</span><span class="p">,</span> <span class="n">macros_value</span> <span class="ow">in</span> <span class="n">define_macros</span><span class="p">:</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>                <span class="n">macros_value</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">macros_value</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>                <span class="n">macros_value</span> <span class="o">=</span> <span class="n">macros_value</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">macros_value</span><span class="p">:</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>                    <span class="n">macros_value</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>                
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>                <span class="n">new_define_macros</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">macros_name</span><span class="p">,</span> <span class="n">macros_value</span><span class="p">))</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>            
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>            <span class="n">ext_module</span><span class="o">.</span><span class="n">define_macros</span> <span class="o">=</span> <span class="n">define_macros</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>    <span class="k">return</span> <span class="n">ext_modules</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a><span class="k">def</span> <span class="nf">find_and_prepare_cython_modules</span><span class="p">(</span><span class="n">package_src_relative_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">additional_cflags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">depth</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">root_rel</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RelativePath</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>    <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="n">depth</span> <span class="o">=</span> <span class="n">depth</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="n">depth</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        <span class="n">root_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">current_src_dir</span><span class="p">(</span><span class="n">depth</span><span class="p">))</span> <span class="k">if</span> <span class="n">root_rel</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">root_rel</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>        <span class="n">root_path</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="n">package_src_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">root_rel</span><span class="p">(</span><span class="n">package_src_relative_path</span><span class="p">))</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="n">package_src_path</span> <span class="o">=</span> <span class="n">package_src_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="n">travers_result</span> <span class="o">=</span> <span class="n">filtered_file_list_traversal</span><span class="p">(</span><span class="n">package_src_path</span><span class="p">,</span> <span class="n">FilteringType</span><span class="o">.</span><span class="n">off</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">remove_empty_items</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">use_spinner</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="k">for</span> <span class="n">dir_path</span><span class="p">,</span> <span class="n">dirs</span><span class="p">,</span> <span class="n">files</span> <span class="ow">in</span> <span class="n">travers_result</span><span class="p">:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>            <span class="k">if</span> <span class="s1">&#39;__pycache__&#39;</span> <span class="ow">in</span> <span class="n">dirs</span><span class="p">:</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>                <span class="n">pycache_path</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dir_path</span><span class="p">)(</span><span class="s1">&#39;__pycache__&#39;</span><span class="p">)</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>                    <span class="n">rmtree</span><span class="p">(</span><span class="n">pycache_path</span><span class="p">)</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>                <span class="k">except</span> <span class="ne">OSError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="n">get_exception</span><span class="p">())</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="k">def</span> <span class="nf">filter</span><span class="p">(</span><span class="n">filtering_entity</span><span class="p">:</span> <span class="n">FilteringEntity</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>            <span class="k">if</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">dirpath</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>                <span class="c1"># Ignore package_src/_template_module</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>                <span class="n">dirpath</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>                <span class="n">rel_path</span> <span class="o">=</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dirpath</span><span class="p">,</span> <span class="n">package_src_path</span><span class="p">)</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                <span class="n">rel_path</span> <span class="o">=</span> <span class="n">rel_path</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>                <span class="k">if</span> <span class="n">rel_path</span><span class="p">:</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>                    <span class="n">rel_path_parts</span> <span class="o">=</span> <span class="n">rel_path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>                    <span class="k">if</span> <span class="n">rel_path_parts</span> <span class="ow">and</span> <span class="n">TEMPLATE_MODULE_NAME</span> <span class="o">==</span> <span class="n">rel_path_parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>                        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>                
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">dirname</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>            <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">filename</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>                <span class="n">dirpath</span><span class="p">,</span> <span class="n">filename</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>                <span class="k">if</span> <span class="n">BUILD_CONFIG_FILENAME</span> <span class="o">==</span> <span class="n">filename</span><span class="p">:</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>                
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>                <span class="n">file_name</span><span class="p">,</span> <span class="n">file_extension</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>                <span class="k">if</span> <span class="n">file_extension</span> <span class="ow">in</span> <span class="n">all_ext</span><span class="p">:</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>                
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>            <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">aggregated</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>                <span class="k">return</span> <span class="n">data</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>                <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>            
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="n">travers_result</span> <span class="o">=</span> <span class="n">file_list_traversal</span><span class="p">(</span><span class="n">package_src_path</span><span class="p">,</span> <span class="nb">filter</span><span class="p">,</span> <span class="n">remove_empty_dirpaths</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>        <span class="c1"># travers_result = filtered_file_list_traversal(package_src_path, FilteringType.including, {&#39;.pyx&#39;, &#39;.c&#39;, &#39;.lib&#39;, &#39;.dll&#39;, &#39;.so&#39;}, remove_empty_items=True, use_spinner=False)</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>        
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="k">for</span> <span class="n">dir_path</span><span class="p">,</span> <span class="n">dirs</span><span class="p">,</span> <span class="n">files</span> <span class="ow">in</span> <span class="n">travers_result</span><span class="p">:</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>            <span class="c1"># Ignore package_src/_template_module</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>            <span class="n">rel_path</span> <span class="o">=</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path</span><span class="p">,</span> <span class="n">package_src_path</span><span class="p">)</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>            <span class="n">rel_path</span> <span class="o">=</span> <span class="n">rel_path</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>            <span class="k">if</span> <span class="n">rel_path</span><span class="p">:</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>                <span class="n">rel_path_parts</span> <span class="o">=</span> <span class="n">rel_path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>                <span class="k">if</span> <span class="n">rel_path_parts</span> <span class="ow">and</span> <span class="n">TEMPLATE_MODULE_NAME</span> <span class="o">==</span> <span class="n">rel_path_parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>                    <span class="k">continue</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>            <span class="n">dir_path_obj</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dir_path</span><span class="p">)</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>            <span class="n">extensions</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>            <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>                <span class="n">filename</span><span class="p">,</span> <span class="n">file_extension</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>                <span class="k">if</span> <span class="n">file_extension</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">extensions</span><span class="p">:</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>                    <span class="n">extensions</span><span class="p">[</span><span class="n">file_extension</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>                
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>                <span class="n">extensions</span><span class="p">[</span><span class="n">file_extension</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>            
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>            <span class="n">is_exctension</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>            <span class="n">build_config</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>            <span class="k">if</span> <span class="n">BUILD_CONFIG_FILENAME</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>                <span class="n">build_config_module_name</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">BUILD_CONFIG_FILENAME</span><span class="p">)</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>                <span class="n">build_config_full_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">dir_path_obj</span><span class="p">(</span><span class="n">build_config_module_name</span><span class="p">)</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>                <span class="n">name</span> <span class="o">=</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">build_config_full_path</span><span class="p">,</span> <span class="n">root_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">))</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>                <span class="n">name_parts</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>                <span class="n">module_full_name</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">name_part</span> <span class="k">for</span> <span class="n">name_part</span> <span class="ow">in</span> <span class="n">name_parts</span> <span class="k">if</span> <span class="n">name_part</span><span class="p">])</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>                <span class="n">build_config_module</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">import_module</span><span class="p">(</span><span class="n">module_full_name</span><span class="p">)</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>                <span class="n">build_config</span> <span class="o">=</span> <span class="n">build_config_module</span><span class="o">.</span><span class="n">build_config</span><span class="p">()</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>                <span class="n">is_exctension</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>            <span class="n">sub_result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>            <span class="k">if</span> <span class="p">(</span><span class="n">cython_file_ext</span> <span class="ow">in</span> <span class="n">extensions</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">build_config</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>                <span class="k">for</span> <span class="n">file_extension</span><span class="p">,</span> <span class="n">files</span> <span class="ow">in</span> <span class="n">extensions</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>                    <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>                        <span class="k">if</span> <span class="n">file_extension</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="p">(</span><span class="n">compilable_ext</span> <span class="o">|</span> <span class="n">headers_ext</span><span class="p">):</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>                            <span class="n">is_exctension</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>                            <span class="n">sub_result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">path_join</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file</span><span class="p">),</span> <span class="n">root_path</span><span class="p">)))</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>                        
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>                        <span class="k">if</span> <span class="n">file_extension</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="n">codegen_files_ext</span><span class="p">:</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>                            <span class="n">filename</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>                            <span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">&#39;__cython&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">&#39;__compiled&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">&#39;__python&#39;</span><span class="p">):</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>                                <span class="k">try</span><span class="p">:</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>                                    <span class="n">remove</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>                                <span class="k">except</span> <span class="ne">OSError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>                                    <span class="nb">print</span><span class="p">(</span><span class="n">get_exception</span><span class="p">())</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>                                <span class="n">is_exctension</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>                                <span class="n">sub_result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">path_join</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file</span><span class="p">),</span> <span class="n">root_path</span><span class="p">)))</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>                        
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>                        <span class="k">if</span> <span class="n">file_extension</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="n">libs_ext</span><span class="p">:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>                            <span class="k">try</span><span class="p">:</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>                                <span class="n">remove</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>                            <span class="k">except</span> <span class="ne">OSError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>                                <span class="nb">print</span><span class="p">(</span><span class="n">get_exception</span><span class="p">())</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>            
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="k">if</span> <span class="n">is_exctension</span><span class="p">:</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>                <span class="n">name</span> <span class="o">=</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">),</span> <span class="n">root_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">))</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>                <span class="n">name_parts</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>                <span class="k">if</span> <span class="n">build_config</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>                    <span class="k">if</span> <span class="mi">1</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)</span> <span class="ow">and</span> <span class="n">sub_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="n">cython_file_ext</span><span class="p">):</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>                        <span class="n">name_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">get_file_name_without_extension</span><span class="p">(</span><span class="n">sub_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>                        <span class="n">name_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;cython_module&#39;</span><span class="p">)</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>                    
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>                    <span class="n">name</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">name_part</span> <span class="k">for</span> <span class="n">name_part</span> <span class="ow">in</span> <span class="n">name_parts</span> <span class="k">if</span> <span class="n">name_part</span><span class="p">])</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>                    <span class="n">extension</span><span class="p">:</span> <span class="n">CythonExtension</span> <span class="o">=</span> <span class="n">CythonExtension</span><span class="p">(</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>                        <span class="n">name</span><span class="p">,</span> 
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>                        <span class="n">sources</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)),</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>                        <span class="n">language</span><span class="o">=</span><span class="s2">&quot;c&quot;</span><span class="p">,</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>                        <span class="c1"># cython_compile_time_env=prepare_cflags_dict(additional_cflags),</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>                        <span class="n">define_macros</span><span class="o">=</span><span class="n">prepare_cflags_dict</span><span class="p">(</span><span class="n">additional_cflags</span><span class="p">),</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>                    <span class="p">)</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">build_config</span><span class="p">,</span> <span class="p">(</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">)):</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>                        <span class="n">extension_type</span> <span class="o">=</span> <span class="n">CythonExtension</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>                        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">build_config</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>                            <span class="n">extension_type</span><span class="p">,</span> <span class="n">build_config</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>                            <span class="n">extension_type</span> <span class="o">=</span> <span class="n">extension_type</span> <span class="k">if</span> <span class="n">extension_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">CythonExtension</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>                        
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>                        <span class="k">if</span> <span class="s1">&#39;Windows&#39;</span> <span class="o">==</span> <span class="n">OS_TYPE</span><span class="p">:</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>                            <span class="c1"># CythonExtension :raises setuptools.errors.PlatformError: if &#39;runtime_library_dirs&#39; is specified on Windows. (since v63)</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>                            <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;runtime_library_dirs&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>                        
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>                        <span class="n">name_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">build_config</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">])</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>                        <span class="n">name</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">name_part</span> <span class="k">for</span> <span class="n">name_part</span> <span class="ow">in</span> <span class="n">name_parts</span> <span class="k">if</span> <span class="n">name_part</span><span class="p">])</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>                        <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;name&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>                        <span class="n">cython_compile_time_env</span><span class="o">=</span><span class="n">prepare_cflags_dict</span><span class="p">(</span><span class="n">additional_cflags</span><span class="p">)</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>                        <span class="k">if</span> <span class="s1">&#39;cython_compile_time_env&#39;</span> <span class="ow">in</span> <span class="n">build_config</span><span class="p">:</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>                            <span class="n">cython_compile_time_env</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">build_config</span><span class="p">[</span><span class="s1">&#39;cython_compile_time_env&#39;</span><span class="p">])</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>                            <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;cython_compile_time_env&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>                        <span class="n">define_macros</span><span class="o">=</span><span class="n">prepare_cflags_dict</span><span class="p">(</span><span class="n">additional_cflags</span><span class="p">)</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>                        <span class="k">if</span> <span class="s1">&#39;define_macros&#39;</span> <span class="ow">in</span> <span class="n">build_config</span><span class="p">:</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>                            <span class="n">define_macros</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">build_config</span><span class="p">[</span><span class="s1">&#39;define_macros&#39;</span><span class="p">])</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>                            <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;define_macros&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>                        
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>                        <span class="n">sources</span> <span class="o">=</span> <span class="n">extend_file_names_to_root_relative_paths</span><span class="p">(</span><span class="n">root_path</span><span class="p">,</span> <span class="n">dir_path_obj</span><span class="p">,</span> <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;sources&#39;</span><span class="p">,</span> <span class="nb">list</span><span class="p">()))</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>                        <span class="n">sources</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>                        
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>                        <span class="n">extension</span><span class="p">:</span> <span class="n">CythonExtension</span> <span class="o">=</span> <span class="n">extension_type</span><span class="p">(</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>                            <span class="n">name</span><span class="p">,</span> 
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>                            <span class="n">sources</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">sources</span><span class="p">)),</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>                            <span class="c1"># cython_compile_time_env=cython_compile_time_env,</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>                            <span class="n">define_macros</span><span class="o">=</span><span class="n">define_macros</span><span class="p">,</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>                            <span class="o">**</span><span class="n">build_config</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>                        <span class="p">)</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>                    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">build_config</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">):</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>                        <span class="n">build_config</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">dir_path_obj</span><span class="p">(</span><span class="n">BUILD_CONFIG_FILENAME</span><span class="p">)</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>                        <span class="n">build_config</span><span class="o">.</span><span class="n">module_import_str</span> <span class="o">=</span> <span class="n">module_full_name</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>                        <span class="n">build_config</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>                        <span class="n">extension</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>                        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unknown build_config type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">build_config</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>                
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">extension</span><span class="p">)</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>        
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a><span class="k">class</span> <span class="nc">BuildConfig</span><span class="p">:</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">additional_pyx_flags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">find_package_data</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">root_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a><span class="k">class</span> <span class="nc">sdist</span><span class="p">(</span><span class="n">sdist_orig</span><span class="p">):</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>            
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;sdist command is currently being run&quot;</span><span class="p">)</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>            <span class="n">environ</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;True&#39;</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>            <span class="n">packages_data_dict</span><span class="p">,</span> <span class="n">manifest_included_files</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">find_package_data</span><span class="p">()</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>            <span class="n">generate_manifest_included_files</span><span class="p">(</span><span class="n">manifest_included_files</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">root_rel</span><span class="p">)</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a><span class="k">class</span> <span class="nc">build</span><span class="p">(</span><span class="n">build_orig</span><span class="p">):</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>    <span class="k">def</span> <span class="nf">finalize_options</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>            <span class="n">setuptools_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)]</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>            <span class="n">cython_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)]</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>            <span class="n">cengal_extensions</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">)))</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>            <span class="n">cengal_result_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span><span class="p">()</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions</span><span class="p">]</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>            <span class="n">setuptools_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)])</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>            <span class="n">cython_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)])</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>            <span class="n">cengal_extensions_store_as_data</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">))</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>        
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">finalize_options</span><span class="p">()</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>            <span class="n">package_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>            
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions_store_as_data</span><span class="p">:</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>                    <span class="n">files</span> <span class="o">=</span> <span class="n">ext</span><span class="p">()</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>                    <span class="k">if</span> <span class="n">files</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>                        <span class="k">continue</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">package</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">package_data</span><span class="p">:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>                        <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>                    
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>                    <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">files</span><span class="p">)</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>                <span class="kn">from</span> <span class="nn">Cython.Build</span> <span class="kn">import</span> <span class="n">cythonize</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>                <span class="n">result_ext_modules</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>                    <span class="n">cwd_before_cythonize</span> <span class="o">=</span> <span class="n">getcwd</span><span class="p">()</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>                    <span class="n">pyx_flags_dict</span> <span class="o">=</span> <span class="n">prepare_pyx_flags_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">additional_pyx_flags</span><span class="p">)</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>                    <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">remove_header_files</span><span class="p">(</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>                        <span class="n">cythonize</span><span class="p">(</span><span class="n">process_macros</span><span class="p">(</span><span class="n">cython_extensions</span><span class="p">),</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>                        <span class="n">compiler_directives</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;language_level&#39;</span><span class="p">:</span> <span class="s1">&#39;3&#39;</span><span class="p">},</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>                        <span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">pyx_flags_dict</span><span class="p">,</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>                        <span class="p">)))</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;DEBUG: </span><span class="si">{</span><span class="n">cwd_before_cythonize</span><span class="si">=}</span><span class="s1"> | </span><span class="si">{</span><span class="n">getcwd</span><span class="p">()</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>                    <span class="k">for</span> <span class="n">extension</span> <span class="ow">in</span> <span class="n">cython_extensions</span><span class="p">:</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>                        <span class="n">pprint</span><span class="p">(</span><span class="n">class_properties_values_including_overrided</span><span class="p">(</span><span class="n">extension</span><span class="p">))</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>                    
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>                    <span class="k">raise</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>                
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>                <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">setuptools_extensions</span><span class="p">)</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">result_ext_modules</span><span class="p">:</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="s1">&#39;extra_compile_args&#39;</span><span class="p">):</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>                    
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>                    
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>                    <span class="k">if</span> <span class="s1">&#39;Darwin&#39;</span> <span class="o">==</span> <span class="n">OS_TYPE</span><span class="p">:</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>                        <span class="k">if</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_x86</span><span class="p">:</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;x86_64&#39;</span><span class="p">]</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>                        <span class="k">elif</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_arm</span><span class="p">:</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;arm64&#39;</span><span class="p">]</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>                
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="o">=</span> <span class="n">package_data</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="o">=</span> <span class="n">result_ext_modules</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>                    <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>                    <span class="nb">print</span><span class="p">()</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a><span class="k">class</span> <span class="nc">build_ext</span><span class="p">(</span><span class="n">build_ext_orig</span><span class="p">):</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>    <span class="k">def</span> <span class="nf">finalize_options</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>            <span class="n">setuptools_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)]</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>            <span class="n">cython_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)]</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>            <span class="n">cengal_extensions</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">)))</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>            <span class="n">cengal_result_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span><span class="p">()</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions</span><span class="p">]</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>            <span class="n">setuptools_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)])</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>            <span class="n">cython_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)])</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>            <span class="n">cengal_extensions_store_as_data</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">))</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>        
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">finalize_options</span><span class="p">()</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>            <span class="n">package_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>            
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions_store_as_data</span><span class="p">:</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>                    <span class="n">files</span> <span class="o">=</span> <span class="n">ext</span><span class="p">()</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>                    <span class="k">if</span> <span class="n">files</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>                        <span class="k">continue</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">package</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">package_data</span><span class="p">:</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>                        <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>                    
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>                    <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">files</span><span class="p">)</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>                <span class="kn">from</span> <span class="nn">Cython.Build</span> <span class="kn">import</span> <span class="n">cythonize</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>                <span class="n">result_ext_modules</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>                    <span class="n">cwd_before_cythonize</span> <span class="o">=</span> <span class="n">getcwd</span><span class="p">()</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>                    <span class="n">pyx_flags_dict</span> <span class="o">=</span> <span class="n">prepare_pyx_flags_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">additional_pyx_flags</span><span class="p">)</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>                    <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">remove_header_files</span><span class="p">(</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>                        <span class="n">cythonize</span><span class="p">(</span><span class="n">process_macros</span><span class="p">(</span><span class="n">cython_extensions</span><span class="p">),</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>                        <span class="n">compiler_directives</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;language_level&#39;</span><span class="p">:</span> <span class="s1">&#39;3&#39;</span><span class="p">},</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>                        <span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">pyx_flags_dict</span><span class="p">,</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>                        <span class="p">)))</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;DEBUG: </span><span class="si">{</span><span class="n">cwd_before_cythonize</span><span class="si">=}</span><span class="s1"> | </span><span class="si">{</span><span class="n">getcwd</span><span class="p">()</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>                    <span class="k">for</span> <span class="n">extension</span> <span class="ow">in</span> <span class="n">cython_extensions</span><span class="p">:</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>                        <span class="n">pprint</span><span class="p">(</span><span class="n">class_properties_values_including_overrided</span><span class="p">(</span><span class="n">extension</span><span class="p">))</span>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>                    
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>                    <span class="k">raise</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a>                
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>                <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">setuptools_extensions</span><span class="p">)</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">result_ext_modules</span><span class="p">:</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="s1">&#39;extra_compile_args&#39;</span><span class="p">):</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>                    
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a>                    
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>                    <span class="k">if</span> <span class="s1">&#39;Darwin&#39;</span> <span class="o">==</span> <span class="n">OS_TYPE</span><span class="p">:</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>                        <span class="k">if</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_x86</span><span class="p">:</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;x86_64&#39;</span><span class="p">]</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>                        <span class="k">elif</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_arm</span><span class="p">:</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;arm64&#39;</span><span class="p">]</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>                
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="o">=</span> <span class="n">package_data</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="o">=</span> <span class="n">result_ext_modules</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>                    <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>                    <span class="nb">print</span><span class="p">()</span>
</span></pre></div>


            </section>
                <section id="BUILD_CONFIG_FILENAME">
                    <div class="attr variable">
            <span class="name">BUILD_CONFIG_FILENAME</span><span class="annotation">: str</span>        =
<span class="default_value">&#39;__build_config.py&#39;</span>

        
    </div>
    <a class="headerlink" href="#BUILD_CONFIG_FILENAME"></a>
    
    

                </section>
                <section id="GITKEEP_FILE_NAME">
                    <div class="attr variable">
            <span class="name">GITKEEP_FILE_NAME</span>        =
<span class="default_value">&#39;.gitkeep&#39;</span>

        
    </div>
    <a class="headerlink" href="#GITKEEP_FILE_NAME"></a>
    
    

                </section>
                <section id="MANIFEST_INCLUDED_FILES_FILE_NAME">
                    <div class="attr variable">
            <span class="name">MANIFEST_INCLUDED_FILES_FILE_NAME</span>        =
<span class="default_value">&#39;MANIFEST.in&#39;</span>

        
    </div>
    <a class="headerlink" href="#MANIFEST_INCLUDED_FILES_FILE_NAME"></a>
    
    

                </section>
                <section id="MANIFEST_INCLUDED_FILES_TEMPLATE_FILE_NAME">
                    <div class="attr variable">
            <span class="name">MANIFEST_INCLUDED_FILES_TEMPLATE_FILE_NAME</span>        =
<span class="default_value">&#39;MANIFEST.in.template&#39;</span>

        
    </div>
    <a class="headerlink" href="#MANIFEST_INCLUDED_FILES_TEMPLATE_FILE_NAME"></a>
    
    

                </section>
                <section id="cython_file_ext">
                    <div class="attr variable">
            <span class="name">cython_file_ext</span>        =
<span class="default_value">&#39;.pyx&#39;</span>

        
    </div>
    <a class="headerlink" href="#cython_file_ext"></a>
    
    

                </section>
                <section id="cython_transpiled_ext">
                    <div class="attr variable">
            <span class="name">cython_transpiled_ext</span>        =
<span class="default_value">{&#39;.c&#39;}</span>

        
    </div>
    <a class="headerlink" href="#cython_transpiled_ext"></a>
    
    

                </section>
                <section id="compilable_ext">
                    <div class="attr variable">
            <span class="name">compilable_ext</span>        =
<span class="default_value">{&#39;.pyx&#39;, &#39;.c++&#39;, &#39;.cc&#39;, &#39;.cxx&#39;, &#39;.cpp&#39;}</span>

        
    </div>
    <a class="headerlink" href="#compilable_ext"></a>
    
    

                </section>
                <section id="codegen_files_ext">
                    <div class="attr variable">
            <span class="name">codegen_files_ext</span>        =
<span class="default_value">{&#39;.c++&#39;, &#39;.cc&#39;, &#39;.c&#39;, &#39;.cxx&#39;, &#39;.cpp&#39;}</span>

        
    </div>
    <a class="headerlink" href="#codegen_files_ext"></a>
    
    

                </section>
                <section id="headers_ext">
                    <div class="attr variable">
            <span class="name">headers_ext</span>        =
<span class="default_value">{&#39;.hxx&#39;, &#39;.hpp&#39;, &#39;.hh&#39;, &#39;.h&#39;, &#39;.h++&#39;}</span>

        
    </div>
    <a class="headerlink" href="#headers_ext"></a>
    
    

                </section>
                <section id="libs_ext">
                    <div class="attr variable">
            <span class="name">libs_ext</span>        =
<span class="default_value">{&#39;.so&#39;, &#39;.lib&#39;, &#39;.dll&#39;}</span>

        
    </div>
    <a class="headerlink" href="#libs_ext"></a>
    
    

                </section>
                <section id="all_ext">
                    <div class="attr variable">
            <span class="name">all_ext</span>        =
<input id="all_ext-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="all_ext-view-value"></label><span class="default_value">{&#39;.pyx&#39;, &#39;.c++&#39;, &#39;.hxx&#39;, &#39;.hpp&#39;, &#39;.hh&#39;, &#39;.h++&#39;, &#39;.lib&#39;, &#39;.dll&#39;, &#39;.cc&#39;, &#39;.c&#39;, &#39;.h&#39;, &#39;.so&#39;, &#39;.cxx&#39;, &#39;.cpp&#39;}</span>

        
    </div>
    <a class="headerlink" href="#all_ext"></a>
    
    

                </section>
                <section id="find_good_packages">
                            <input id="find_good_packages-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_good_packages</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">where</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span>,</span><span class="param">	<span class="n">exclude</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">()</span>,</span><span class="param">	<span class="n">include</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;*&#39;</span><span class="p">,)</span>,</span><span class="param">	<span class="n">modules_to_ignore</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">()</span>,</span><span class="param">	<span class="n">python_2_modules</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">()</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="find_good_packages-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_good_packages"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_good_packages-95"><a href="#find_good_packages-95"><span class="linenos"> 95</span></a><span class="k">def</span> <span class="nf">find_good_packages</span><span class="p">(</span><span class="n">where</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="n">exclude</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(),</span> <span class="n">include</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;*&#39;</span><span class="p">,),</span> 
</span><span id="find_good_packages-96"><a href="#find_good_packages-96"><span class="linenos"> 96</span></a>                       <span class="n">modules_to_ignore</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(),</span> <span class="n">python_2_modules</span><span class="p">:</span> <span class="n">Iterable</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()):</span>
</span><span id="find_good_packages-97"><a href="#find_good_packages-97"><span class="linenos"> 97</span></a>    <span class="n">all_packages</span> <span class="o">=</span> <span class="n">setuptools</span><span class="o">.</span><span class="n">find_packages</span><span class="p">(</span><span class="n">where</span><span class="p">,</span> <span class="n">exclude</span><span class="p">,</span> <span class="n">include</span><span class="p">)</span>
</span><span id="find_good_packages-98"><a href="#find_good_packages-98"><span class="linenos"> 98</span></a>    <span class="n">good_packages</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="find_good_packages-99"><a href="#find_good_packages-99"><span class="linenos"> 99</span></a>    <span class="k">for</span> <span class="n">package</span> <span class="ow">in</span> <span class="n">all_packages</span><span class="p">:</span>
</span><span id="find_good_packages-100"><a href="#find_good_packages-100"><span class="linenos">100</span></a>        <span class="n">is_good</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="find_good_packages-101"><a href="#find_good_packages-101"><span class="linenos">101</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">modules_to_ignore</span><span class="p">:</span>
</span><span id="find_good_packages-102"><a href="#find_good_packages-102"><span class="linenos">102</span></a>            <span class="k">if</span> <span class="n">package</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">item</span><span class="p">):</span>
</span><span id="find_good_packages-103"><a href="#find_good_packages-103"><span class="linenos">103</span></a>                <span class="n">is_good</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="find_good_packages-104"><a href="#find_good_packages-104"><span class="linenos">104</span></a>                <span class="k">break</span>
</span><span id="find_good_packages-105"><a href="#find_good_packages-105"><span class="linenos">105</span></a>
</span><span id="find_good_packages-106"><a href="#find_good_packages-106"><span class="linenos">106</span></a>        <span class="k">if</span> <span class="s1">&#39;3&#39;</span> <span class="o">==</span> <span class="n">_PYTHON_VERSION</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="find_good_packages-107"><a href="#find_good_packages-107"><span class="linenos">107</span></a>            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">python_2_modules</span><span class="p">:</span>
</span><span id="find_good_packages-108"><a href="#find_good_packages-108"><span class="linenos">108</span></a>                <span class="k">if</span> <span class="n">package</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">item</span><span class="p">):</span>
</span><span id="find_good_packages-109"><a href="#find_good_packages-109"><span class="linenos">109</span></a>                    <span class="n">is_good</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="find_good_packages-110"><a href="#find_good_packages-110"><span class="linenos">110</span></a>                    <span class="k">break</span>
</span><span id="find_good_packages-111"><a href="#find_good_packages-111"><span class="linenos">111</span></a>
</span><span id="find_good_packages-112"><a href="#find_good_packages-112"><span class="linenos">112</span></a>        <span class="k">if</span> <span class="n">is_good</span><span class="p">:</span>
</span><span id="find_good_packages-113"><a href="#find_good_packages-113"><span class="linenos">113</span></a>            <span class="n">good_packages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">package</span><span class="p">)</span>
</span><span id="find_good_packages-114"><a href="#find_good_packages-114"><span class="linenos">114</span></a>
</span><span id="find_good_packages-115"><a href="#find_good_packages-115"><span class="linenos">115</span></a>    <span class="k">return</span> <span class="n">good_packages</span>
</span></pre></div>


    

                </section>
                <section id="find_package_data_filter">
                            <input id="find_package_data_filter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_package_data_filter</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">filtering_entity</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">file_system</span><span class="o">.</span><span class="n">directory_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">directory_manager</span><span class="o">.</span><span class="n">FilteringEntity</span>,</span><span class="param">	<span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="find_package_data_filter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_package_data_filter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_package_data_filter-118"><a href="#find_package_data_filter-118"><span class="linenos">118</span></a><span class="k">def</span> <span class="nf">find_package_data_filter</span><span class="p">(</span><span class="n">filtering_entity</span><span class="p">:</span> <span class="n">FilteringEntity</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="find_package_data_filter-119"><a href="#find_package_data_filter-119"><span class="linenos">119</span></a>    <span class="k">if</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">dirpath</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="find_package_data_filter-120"><a href="#find_package_data_filter-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="find_package_data_filter-121"><a href="#find_package_data_filter-121"><span class="linenos">121</span></a>    <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">dirname</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="find_package_data_filter-122"><a href="#find_package_data_filter-122"><span class="linenos">122</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="find_package_data_filter-123"><a href="#find_package_data_filter-123"><span class="linenos">123</span></a>    <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">filename</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="find_package_data_filter-124"><a href="#find_package_data_filter-124"><span class="linenos">124</span></a>        <span class="n">dirpath</span><span class="p">,</span> <span class="n">filename</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="find_package_data_filter-125"><a href="#find_package_data_filter-125"><span class="linenos">125</span></a>        <span class="k">return</span> <span class="n">GITKEEP_FILE_NAME</span> <span class="o">!=</span> <span class="n">filename</span>
</span><span id="find_package_data_filter-126"><a href="#find_package_data_filter-126"><span class="linenos">126</span></a>    <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">aggregated</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="find_package_data_filter-127"><a href="#find_package_data_filter-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="find_package_data_filter-128"><a href="#find_package_data_filter-128"><span class="linenos">128</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="find_package_data_filter-129"><a href="#find_package_data_filter-129"><span class="linenos">129</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="find_package_data">
                            <input id="find_package_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_package_data</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">package_src_relative_path</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">good_packages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>,</span><span class="param">	<span class="n">depth</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>,</span><span class="param">	<span class="n">root_rel</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">file_system</span><span class="o">.</span><span class="n">path_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">path_manager</span><span class="o">.</span><span class="n">RelativePath</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="find_package_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_package_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_package_data-132"><a href="#find_package_data-132"><span class="linenos">132</span></a><span class="k">def</span> <span class="nf">find_package_data</span><span class="p">(</span><span class="n">package_src_relative_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">good_packages</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">root_rel</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RelativePath</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="find_package_data-133"><a href="#find_package_data-133"><span class="linenos">133</span></a>    <span class="n">depth</span> <span class="o">=</span> <span class="n">depth</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="find_package_data-134"><a href="#find_package_data-134"><span class="linenos">134</span></a>    <span class="n">depth</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="find_package_data-135"><a href="#find_package_data-135"><span class="linenos">135</span></a>    <span class="n">root_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">current_src_dir</span><span class="p">())</span> <span class="k">if</span> <span class="n">root_rel</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">root_rel</span>
</span><span id="find_package_data-136"><a href="#find_package_data-136"><span class="linenos">136</span></a>    <span class="n">root_path</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="find_package_data-137"><a href="#find_package_data-137"><span class="linenos">137</span></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">root_path</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="find_package_data-138"><a href="#find_package_data-138"><span class="linenos">138</span></a>    <span class="n">package_src_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">root_rel</span><span class="p">(</span><span class="n">package_src_relative_path</span><span class="p">))</span>
</span><span id="find_package_data-139"><a href="#find_package_data-139"><span class="linenos">139</span></a>    <span class="n">package_src_path</span> <span class="o">=</span> <span class="n">package_src_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="find_package_data-140"><a href="#find_package_data-140"><span class="linenos">140</span></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">package_src_path</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="find_package_data-141"><a href="#find_package_data-141"><span class="linenos">141</span></a>
</span><span id="find_package_data-142"><a href="#find_package_data-142"><span class="linenos">142</span></a>    <span class="n">packages_data_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="find_package_data-143"><a href="#find_package_data-143"><span class="linenos">143</span></a>    <span class="n">manifest_included_files</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="find_package_data-144"><a href="#find_package_data-144"><span class="linenos">144</span></a>    <span class="k">for</span> <span class="n">package_name</span> <span class="ow">in</span> <span class="n">good_packages</span><span class="p">:</span>
</span><span id="find_package_data-145"><a href="#find_package_data-145"><span class="linenos">145</span></a>        <span class="n">package_path</span> <span class="o">=</span> <span class="n">find_package_path</span><span class="p">(</span><span class="n">package_name</span><span class="p">,</span> <span class="nb">dict</span><span class="p">(),</span> <span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="find_package_data-146"><a href="#find_package_data-146"><span class="linenos">146</span></a>        <span class="n">package_full_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="n">package_path</span><span class="p">)</span>
</span><span id="find_package_data-147"><a href="#find_package_data-147"><span class="linenos">147</span></a>        <span class="n">package_full_path_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">package_full_path</span><span class="p">)</span>
</span><span id="find_package_data-148"><a href="#find_package_data-148"><span class="linenos">148</span></a>        <span class="n">package_data</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="find_package_data-149"><a href="#find_package_data-149"><span class="linenos">149</span></a>        <span class="n">possible_data_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">package_full_path_rel</span><span class="p">(</span><span class="s1">&#39;data&#39;</span><span class="p">)</span>
</span><span id="find_package_data-150"><a href="#find_package_data-150"><span class="linenos">150</span></a>        <span class="k">if</span> <span class="n">exists</span><span class="p">(</span><span class="n">possible_data_dir</span><span class="p">)</span> <span class="ow">and</span> <span class="n">isdir</span><span class="p">(</span><span class="n">possible_data_dir</span><span class="p">):</span>
</span><span id="find_package_data-151"><a href="#find_package_data-151"><span class="linenos">151</span></a>            <span class="n">possible_data_dir_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">possible_data_dir</span><span class="p">)</span>
</span><span id="find_package_data-152"><a href="#find_package_data-152"><span class="linenos">152</span></a>            <span class="n">travers_result</span> <span class="o">=</span> <span class="n">file_list_traversal</span><span class="p">(</span><span class="n">possible_data_dir</span><span class="p">,</span> <span class="n">find_package_data_filter</span><span class="p">,</span> <span class="n">remove_empty_dirpaths</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="find_package_data-153"><a href="#find_package_data-153"><span class="linenos">153</span></a>            <span class="k">for</span> <span class="n">dirpath</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">travers_result</span><span class="p">:</span>
</span><span id="find_package_data-154"><a href="#find_package_data-154"><span class="linenos">154</span></a>                <span class="n">dirpath_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span>
</span><span id="find_package_data-155"><a href="#find_package_data-155"><span class="linenos">155</span></a>                <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">filenames</span><span class="p">:</span>
</span><span id="find_package_data-156"><a href="#find_package_data-156"><span class="linenos">156</span></a>                    <span class="n">file_full_path</span> <span class="o">=</span> <span class="n">dirpath_rel</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
</span><span id="find_package_data-157"><a href="#find_package_data-157"><span class="linenos">157</span></a>                    <span class="n">package_data</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">file_full_path</span><span class="p">,</span> <span class="n">package_full_path</span><span class="p">))</span>
</span><span id="find_package_data-158"><a href="#find_package_data-158"><span class="linenos">158</span></a>                    <span class="n">manifest_included_files</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">file_full_path</span><span class="p">,</span> <span class="n">root_path</span><span class="p">))</span>
</span><span id="find_package_data-159"><a href="#find_package_data-159"><span class="linenos">159</span></a>        
</span><span id="find_package_data-160"><a href="#find_package_data-160"><span class="linenos">160</span></a>        <span class="n">pyx_files</span> <span class="o">=</span> <span class="n">filtered_file_list_traversal</span><span class="p">(</span><span class="n">package_full_path</span><span class="p">,</span> <span class="n">FilteringType</span><span class="o">.</span><span class="n">including</span><span class="p">,</span> <span class="p">{</span><span class="s1">&#39;.pyx&#39;</span><span class="p">},</span> <span class="n">remove_empty_items</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="find_package_data-161"><a href="#find_package_data-161"><span class="linenos">161</span></a>        <span class="k">for</span> <span class="n">dirpath</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">pyx_files</span><span class="p">:</span>
</span><span id="find_package_data-162"><a href="#find_package_data-162"><span class="linenos">162</span></a>            <span class="n">dirpath_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span>
</span><span id="find_package_data-163"><a href="#find_package_data-163"><span class="linenos">163</span></a>            <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">filenames</span><span class="p">:</span>
</span><span id="find_package_data-164"><a href="#find_package_data-164"><span class="linenos">164</span></a>                <span class="n">file_full_path</span> <span class="o">=</span> <span class="n">dirpath_rel</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
</span><span id="find_package_data-165"><a href="#find_package_data-165"><span class="linenos">165</span></a>                <span class="n">package_data</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">file_full_path</span><span class="p">,</span> <span class="n">package_full_path</span><span class="p">))</span>
</span><span id="find_package_data-166"><a href="#find_package_data-166"><span class="linenos">166</span></a>                <span class="n">manifest_included_files</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">file_full_path</span><span class="p">,</span> <span class="n">root_path</span><span class="p">))</span>
</span><span id="find_package_data-167"><a href="#find_package_data-167"><span class="linenos">167</span></a>        
</span><span id="find_package_data-168"><a href="#find_package_data-168"><span class="linenos">168</span></a>        <span class="k">if</span> <span class="n">package_data</span><span class="p">:</span>
</span><span id="find_package_data-169"><a href="#find_package_data-169"><span class="linenos">169</span></a>            <span class="n">packages_data_dict</span><span class="p">[</span><span class="n">package_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">package_data</span><span class="p">)</span>
</span><span id="find_package_data-170"><a href="#find_package_data-170"><span class="linenos">170</span></a>
</span><span id="find_package_data-171"><a href="#find_package_data-171"><span class="linenos">171</span></a>    <span class="k">return</span> <span class="n">packages_data_dict</span><span class="p">,</span> <span class="nb">list</span><span class="p">(</span><span class="n">manifest_included_files</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="generate_manifest_included_files">
                            <input id="generate_manifest_included_files-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">generate_manifest_included_files</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">manifest_included_files</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>,</span><span class="param">	<span class="n">root_rel</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">file_system</span><span class="o">.</span><span class="n">path_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">path_manager</span><span class="o">.</span><span class="n">RelativePath</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="generate_manifest_included_files-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#generate_manifest_included_files"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="generate_manifest_included_files-174"><a href="#generate_manifest_included_files-174"><span class="linenos">174</span></a><span class="k">def</span> <span class="nf">generate_manifest_included_files</span><span class="p">(</span><span class="n">manifest_included_files</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">root_rel</span><span class="p">:</span> <span class="n">RelativePath</span><span class="p">):</span>
</span><span id="generate_manifest_included_files-175"><a href="#generate_manifest_included_files-175"><span class="linenos">175</span></a>    <span class="n">manifest_included_files_template_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="n">MANIFEST_INCLUDED_FILES_TEMPLATE_FILE_NAME</span><span class="p">)</span>
</span><span id="generate_manifest_included_files-176"><a href="#generate_manifest_included_files-176"><span class="linenos">176</span></a>    <span class="n">manifest_included_files_template_contents</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="generate_manifest_included_files-177"><a href="#generate_manifest_included_files-177"><span class="linenos">177</span></a>    <span class="k">if</span> <span class="n">exists</span><span class="p">(</span><span class="n">manifest_included_files_template_path</span><span class="p">)</span> <span class="ow">and</span> <span class="n">isfile</span><span class="p">(</span><span class="n">manifest_included_files_template_path</span><span class="p">):</span>
</span><span id="generate_manifest_included_files-178"><a href="#generate_manifest_included_files-178"><span class="linenos">178</span></a>        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">manifest_included_files_template_path</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
</span><span id="generate_manifest_included_files-179"><a href="#generate_manifest_included_files-179"><span class="linenos">179</span></a>            <span class="n">manifest_included_files_template_contents</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
</span><span id="generate_manifest_included_files-180"><a href="#generate_manifest_included_files-180"><span class="linenos">180</span></a>
</span><span id="generate_manifest_included_files-181"><a href="#generate_manifest_included_files-181"><span class="linenos">181</span></a>    <span class="n">manifest_included_files_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="n">MANIFEST_INCLUDED_FILES_FILE_NAME</span><span class="p">)</span>
</span><span id="generate_manifest_included_files-182"><a href="#generate_manifest_included_files-182"><span class="linenos">182</span></a>    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">manifest_included_files_path</span><span class="p">,</span> <span class="s1">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
</span><span id="generate_manifest_included_files-183"><a href="#generate_manifest_included_files-183"><span class="linenos">183</span></a>        <span class="k">if</span> <span class="n">manifest_included_files_template_contents</span><span class="p">:</span>
</span><span id="generate_manifest_included_files-184"><a href="#generate_manifest_included_files-184"><span class="linenos">184</span></a>            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">manifest_included_files_template_contents</span> <span class="o">+</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="generate_manifest_included_files-185"><a href="#generate_manifest_included_files-185"><span class="linenos">185</span></a>        
</span><span id="generate_manifest_included_files-186"><a href="#generate_manifest_included_files-186"><span class="linenos">186</span></a>        <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">manifest_included_files</span><span class="p">:</span>
</span><span id="generate_manifest_included_files-187"><a href="#generate_manifest_included_files-187"><span class="linenos">187</span></a>            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;include </span><span class="si">{</span><span class="n">file</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="get_file_name_without_extension">
                            <input id="get_file_name_without_extension-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_file_name_without_extension</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">path</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_file_name_without_extension-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_file_name_without_extension"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_file_name_without_extension-190"><a href="#get_file_name_without_extension-190"><span class="linenos">190</span></a><span class="k">def</span> <span class="nf">get_file_name_without_extension</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
</span><span id="get_file_name_without_extension-191"><a href="#get_file_name_without_extension-191"><span class="linenos">191</span></a>    <span class="n">file_name</span> <span class="o">=</span> <span class="n">basename</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>  <span class="c1"># Get the base name from the path</span>
</span><span id="get_file_name_without_extension-192"><a href="#get_file_name_without_extension-192"><span class="linenos">192</span></a>    <span class="n">file_name_without_extension</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">file_name</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1"># Split the file name and extension, and take only the file name part</span>
</span><span id="get_file_name_without_extension-193"><a href="#get_file_name_without_extension-193"><span class="linenos">193</span></a>    <span class="k">return</span> <span class="n">file_name_without_extension</span>
</span></pre></div>


    

                </section>
                <section id="remove_header_files">
                            <input id="remove_header_files-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_header_files</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">ext_modules</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Cython</span><span class="o">.</span><span class="n">Distutils</span><span class="o">.</span><span class="n">extension</span><span class="o">.</span><span class="n">Extension</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Sequence</span><span class="p">[</span><span class="n">Cython</span><span class="o">.</span><span class="n">Distutils</span><span class="o">.</span><span class="n">extension</span><span class="o">.</span><span class="n">Extension</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="remove_header_files-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#remove_header_files"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="remove_header_files-196"><a href="#remove_header_files-196"><span class="linenos">196</span></a><span class="k">def</span> <span class="nf">remove_header_files</span><span class="p">(</span><span class="n">ext_modules</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CythonExtension</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CythonExtension</span><span class="p">]:</span>
</span><span id="remove_header_files-197"><a href="#remove_header_files-197"><span class="linenos">197</span></a>    <span class="k">for</span> <span class="n">ext_module</span> <span class="ow">in</span> <span class="n">ext_modules</span><span class="p">:</span>
</span><span id="remove_header_files-198"><a href="#remove_header_files-198"><span class="linenos">198</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">):</span>
</span><span id="remove_header_files-199"><a href="#remove_header_files-199"><span class="linenos">199</span></a>            <span class="n">new_sources</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="remove_header_files-200"><a href="#remove_header_files-200"><span class="linenos">200</span></a>            <span class="k">for</span> <span class="n">source</span> <span class="ow">in</span> <span class="n">ext_module</span><span class="o">.</span><span class="n">sources</span><span class="p">:</span>
</span><span id="remove_header_files-201"><a href="#remove_header_files-201"><span class="linenos">201</span></a>                <span class="n">_</span><span class="p">,</span> <span class="n">file_extension</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">source</span><span class="p">)</span>
</span><span id="remove_header_files-202"><a href="#remove_header_files-202"><span class="linenos">202</span></a>                <span class="k">if</span> <span class="n">file_extension</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">headers_ext</span><span class="p">:</span>
</span><span id="remove_header_files-203"><a href="#remove_header_files-203"><span class="linenos">203</span></a>                    <span class="n">new_sources</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">source</span><span class="p">)</span>
</span><span id="remove_header_files-204"><a href="#remove_header_files-204"><span class="linenos">204</span></a>            
</span><span id="remove_header_files-205"><a href="#remove_header_files-205"><span class="linenos">205</span></a>            <span class="n">ext_module</span><span class="o">.</span><span class="n">sources</span> <span class="o">=</span> <span class="n">new_sources</span>
</span><span id="remove_header_files-206"><a href="#remove_header_files-206"><span class="linenos">206</span></a>    
</span><span id="remove_header_files-207"><a href="#remove_header_files-207"><span class="linenos">207</span></a>    <span class="k">return</span> <span class="n">ext_modules</span>
</span></pre></div>


    

                </section>
                <section id="extend_file_names_to_root_relative_paths">
                            <input id="extend_file_names_to_root_relative_paths-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">extend_file_names_to_root_relative_paths</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">root_path</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">dir_path_obj</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">file_system</span><span class="o">.</span><span class="n">path_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">path_manager</span><span class="o">.</span><span class="n">RelativePath</span>,</span><span class="param">	<span class="n">file_names_or_path</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="extend_file_names_to_root_relative_paths-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#extend_file_names_to_root_relative_paths"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="extend_file_names_to_root_relative_paths-210"><a href="#extend_file_names_to_root_relative_paths-210"><span class="linenos">210</span></a><span class="k">def</span> <span class="nf">extend_file_names_to_root_relative_paths</span><span class="p">(</span><span class="n">root_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">dir_path_obj</span><span class="p">:</span> <span class="n">RelativePath</span><span class="p">,</span> <span class="n">file_names_or_path</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="extend_file_names_to_root_relative_paths-211"><a href="#extend_file_names_to_root_relative_paths-211"><span class="linenos">211</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="extend_file_names_to_root_relative_paths-212"><a href="#extend_file_names_to_root_relative_paths-212"><span class="linenos">212</span></a>    <span class="k">for</span> <span class="n">file_name_or_path</span> <span class="ow">in</span> <span class="n">file_names_or_path</span><span class="p">:</span>
</span><span id="extend_file_names_to_root_relative_paths-213"><a href="#extend_file_names_to_root_relative_paths-213"><span class="linenos">213</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">file_name_or_path</span><span class="p">:</span>
</span><span id="extend_file_names_to_root_relative_paths-214"><a href="#extend_file_names_to_root_relative_paths-214"><span class="linenos">214</span></a>            <span class="k">continue</span>
</span><span id="extend_file_names_to_root_relative_paths-215"><a href="#extend_file_names_to_root_relative_paths-215"><span class="linenos">215</span></a>        
</span><span id="extend_file_names_to_root_relative_paths-216"><a href="#extend_file_names_to_root_relative_paths-216"><span class="linenos">216</span></a>        <span class="n">owner_path</span><span class="p">,</span> <span class="n">file_name</span> <span class="o">=</span> <span class="n">split</span><span class="p">(</span><span class="n">file_name_or_path</span><span class="p">)</span>
</span><span id="extend_file_names_to_root_relative_paths-217"><a href="#extend_file_names_to_root_relative_paths-217"><span class="linenos">217</span></a>        <span class="n">file_name</span> <span class="o">=</span> <span class="n">file_name</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="extend_file_names_to_root_relative_paths-218"><a href="#extend_file_names_to_root_relative_paths-218"><span class="linenos">218</span></a>        <span class="k">if</span> <span class="n">owner_path</span><span class="p">:</span>
</span><span id="extend_file_names_to_root_relative_paths-219"><a href="#extend_file_names_to_root_relative_paths-219"><span class="linenos">219</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">file_name_or_path</span><span class="p">)</span>
</span><span id="extend_file_names_to_root_relative_paths-220"><a href="#extend_file_names_to_root_relative_paths-220"><span class="linenos">220</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="extend_file_names_to_root_relative_paths-221"><a href="#extend_file_names_to_root_relative_paths-221"><span class="linenos">221</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">path_join</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file_name</span><span class="p">),</span> <span class="n">root_path</span><span class="p">)))</span>
</span><span id="extend_file_names_to_root_relative_paths-222"><a href="#extend_file_names_to_root_relative_paths-222"><span class="linenos">222</span></a>    
</span><span id="extend_file_names_to_root_relative_paths-223"><a href="#extend_file_names_to_root_relative_paths-223"><span class="linenos">223</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="process_macros">
                            <input id="process_macros-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">process_macros</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">ext_modules</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Cython</span><span class="o">.</span><span class="n">Distutils</span><span class="o">.</span><span class="n">extension</span><span class="o">.</span><span class="n">Extension</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Sequence</span><span class="p">[</span><span class="n">Cython</span><span class="o">.</span><span class="n">Distutils</span><span class="o">.</span><span class="n">extension</span><span class="o">.</span><span class="n">Extension</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="process_macros-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#process_macros"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="process_macros-226"><a href="#process_macros-226"><span class="linenos">226</span></a><span class="k">def</span> <span class="nf">process_macros</span><span class="p">(</span><span class="n">ext_modules</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CythonExtension</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">CythonExtension</span><span class="p">]:</span>
</span><span id="process_macros-227"><a href="#process_macros-227"><span class="linenos">227</span></a>    <span class="k">for</span> <span class="n">ext_module</span> <span class="ow">in</span> <span class="n">ext_modules</span><span class="p">:</span>
</span><span id="process_macros-228"><a href="#process_macros-228"><span class="linenos">228</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">):</span>
</span><span id="process_macros-229"><a href="#process_macros-229"><span class="linenos">229</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="s1">&#39;compile_time_env&#39;</span><span class="p">):</span>
</span><span id="process_macros-230"><a href="#process_macros-230"><span class="linenos">230</span></a>                <span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">ext_module</span><span class="o">.</span><span class="n">compile_time_env</span>
</span><span id="process_macros-231"><a href="#process_macros-231"><span class="linenos">231</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="process_macros-232"><a href="#process_macros-232"><span class="linenos">232</span></a>                <span class="n">compile_time_env</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="process_macros-233"><a href="#process_macros-233"><span class="linenos">233</span></a>            
</span><span id="process_macros-234"><a href="#process_macros-234"><span class="linenos">234</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="s1">&#39;cython_compile_time_env&#39;</span><span class="p">):</span>
</span><span id="process_macros-235"><a href="#process_macros-235"><span class="linenos">235</span></a>                <span class="n">cython_compile_time_env</span> <span class="o">=</span> <span class="n">ext_module</span><span class="o">.</span><span class="n">cython_compile_time_env</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="process_macros-236"><a href="#process_macros-236"><span class="linenos">236</span></a>                <span class="n">compile_time_env</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">cython_compile_time_env</span><span class="p">)</span>
</span><span id="process_macros-237"><a href="#process_macros-237"><span class="linenos">237</span></a>                <span class="n">ext_module</span><span class="o">.</span><span class="n">cython_compile_time_env</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="process_macros-238"><a href="#process_macros-238"><span class="linenos">238</span></a>            
</span><span id="process_macros-239"><a href="#process_macros-239"><span class="linenos">239</span></a>            <span class="n">ext_module</span><span class="o">.</span><span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">compile_time_env</span>
</span><span id="process_macros-240"><a href="#process_macros-240"><span class="linenos">240</span></a>
</span><span id="process_macros-241"><a href="#process_macros-241"><span class="linenos">241</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext_module</span><span class="p">,</span> <span class="s1">&#39;define_macros&#39;</span><span class="p">):</span>
</span><span id="process_macros-242"><a href="#process_macros-242"><span class="linenos">242</span></a>                <span class="n">define_macros</span> <span class="o">=</span> <span class="n">ext_module</span><span class="o">.</span><span class="n">define_macros</span>
</span><span id="process_macros-243"><a href="#process_macros-243"><span class="linenos">243</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="process_macros-244"><a href="#process_macros-244"><span class="linenos">244</span></a>                <span class="n">define_macros</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="process_macros-245"><a href="#process_macros-245"><span class="linenos">245</span></a>            
</span><span id="process_macros-246"><a href="#process_macros-246"><span class="linenos">246</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">define_macros</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="process_macros-247"><a href="#process_macros-247"><span class="linenos">247</span></a>                <span class="n">define_macros</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">define_macros</span><span class="o">.</span><span class="n">items</span><span class="p">())</span>
</span><span id="process_macros-248"><a href="#process_macros-248"><span class="linenos">248</span></a>            
</span><span id="process_macros-249"><a href="#process_macros-249"><span class="linenos">249</span></a>            <span class="n">new_define_macros</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="process_macros-250"><a href="#process_macros-250"><span class="linenos">250</span></a>            <span class="k">for</span> <span class="n">macros_name</span><span class="p">,</span> <span class="n">macros_value</span> <span class="ow">in</span> <span class="n">define_macros</span><span class="p">:</span>
</span><span id="process_macros-251"><a href="#process_macros-251"><span class="linenos">251</span></a>                <span class="n">macros_value</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">macros_value</span><span class="p">)</span>
</span><span id="process_macros-252"><a href="#process_macros-252"><span class="linenos">252</span></a>                <span class="n">macros_value</span> <span class="o">=</span> <span class="n">macros_value</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="process_macros-253"><a href="#process_macros-253"><span class="linenos">253</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">macros_value</span><span class="p">:</span>
</span><span id="process_macros-254"><a href="#process_macros-254"><span class="linenos">254</span></a>                    <span class="n">macros_value</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="process_macros-255"><a href="#process_macros-255"><span class="linenos">255</span></a>                
</span><span id="process_macros-256"><a href="#process_macros-256"><span class="linenos">256</span></a>                <span class="n">new_define_macros</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">macros_name</span><span class="p">,</span> <span class="n">macros_value</span><span class="p">))</span>
</span><span id="process_macros-257"><a href="#process_macros-257"><span class="linenos">257</span></a>            
</span><span id="process_macros-258"><a href="#process_macros-258"><span class="linenos">258</span></a>            <span class="n">ext_module</span><span class="o">.</span><span class="n">define_macros</span> <span class="o">=</span> <span class="n">define_macros</span>
</span><span id="process_macros-259"><a href="#process_macros-259"><span class="linenos">259</span></a>
</span><span id="process_macros-260"><a href="#process_macros-260"><span class="linenos">260</span></a>    <span class="k">return</span> <span class="n">ext_modules</span>
</span></pre></div>


    

                </section>
                <section id="find_and_prepare_cython_modules">
                            <input id="find_and_prepare_cython_modules-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_and_prepare_cython_modules</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">package_src_relative_path</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">additional_cflags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>,</span><span class="param">	<span class="n">depth</span><span class="o">=</span><span class="mi">1</span>,</span><span class="param">	<span class="n">root_rel</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">file_system</span><span class="o">.</span><span class="n">path_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">path_manager</span><span class="o">.</span><span class="n">RelativePath</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="find_and_prepare_cython_modules-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_and_prepare_cython_modules"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_and_prepare_cython_modules-263"><a href="#find_and_prepare_cython_modules-263"><span class="linenos">263</span></a><span class="k">def</span> <span class="nf">find_and_prepare_cython_modules</span><span class="p">(</span><span class="n">package_src_relative_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">additional_cflags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">depth</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">root_rel</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RelativePath</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="find_and_prepare_cython_modules-264"><a href="#find_and_prepare_cython_modules-264"><span class="linenos">264</span></a>    <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="find_and_prepare_cython_modules-265"><a href="#find_and_prepare_cython_modules-265"><span class="linenos">265</span></a>        <span class="n">depth</span> <span class="o">=</span> <span class="n">depth</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="find_and_prepare_cython_modules-266"><a href="#find_and_prepare_cython_modules-266"><span class="linenos">266</span></a>        <span class="n">depth</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="find_and_prepare_cython_modules-267"><a href="#find_and_prepare_cython_modules-267"><span class="linenos">267</span></a>        <span class="n">root_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">current_src_dir</span><span class="p">(</span><span class="n">depth</span><span class="p">))</span> <span class="k">if</span> <span class="n">root_rel</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">root_rel</span>
</span><span id="find_and_prepare_cython_modules-268"><a href="#find_and_prepare_cython_modules-268"><span class="linenos">268</span></a>        <span class="n">root_path</span> <span class="o">=</span> <span class="n">root_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-269"><a href="#find_and_prepare_cython_modules-269"><span class="linenos">269</span></a>        <span class="n">package_src_rel</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">root_rel</span><span class="p">(</span><span class="n">package_src_relative_path</span><span class="p">))</span>
</span><span id="find_and_prepare_cython_modules-270"><a href="#find_and_prepare_cython_modules-270"><span class="linenos">270</span></a>        <span class="n">package_src_path</span> <span class="o">=</span> <span class="n">package_src_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-271"><a href="#find_and_prepare_cython_modules-271"><span class="linenos">271</span></a>
</span><span id="find_and_prepare_cython_modules-272"><a href="#find_and_prepare_cython_modules-272"><span class="linenos">272</span></a>        <span class="n">travers_result</span> <span class="o">=</span> <span class="n">filtered_file_list_traversal</span><span class="p">(</span><span class="n">package_src_path</span><span class="p">,</span> <span class="n">FilteringType</span><span class="o">.</span><span class="n">off</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">remove_empty_items</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">use_spinner</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-273"><a href="#find_and_prepare_cython_modules-273"><span class="linenos">273</span></a>        <span class="k">for</span> <span class="n">dir_path</span><span class="p">,</span> <span class="n">dirs</span><span class="p">,</span> <span class="n">files</span> <span class="ow">in</span> <span class="n">travers_result</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-274"><a href="#find_and_prepare_cython_modules-274"><span class="linenos">274</span></a>            <span class="k">if</span> <span class="s1">&#39;__pycache__&#39;</span> <span class="ow">in</span> <span class="n">dirs</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-275"><a href="#find_and_prepare_cython_modules-275"><span class="linenos">275</span></a>                <span class="n">pycache_path</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dir_path</span><span class="p">)(</span><span class="s1">&#39;__pycache__&#39;</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-276"><a href="#find_and_prepare_cython_modules-276"><span class="linenos">276</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-277"><a href="#find_and_prepare_cython_modules-277"><span class="linenos">277</span></a>                    <span class="n">rmtree</span><span class="p">(</span><span class="n">pycache_path</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-278"><a href="#find_and_prepare_cython_modules-278"><span class="linenos">278</span></a>                <span class="k">except</span> <span class="ne">OSError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-279"><a href="#find_and_prepare_cython_modules-279"><span class="linenos">279</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="n">get_exception</span><span class="p">())</span>
</span><span id="find_and_prepare_cython_modules-280"><a href="#find_and_prepare_cython_modules-280"><span class="linenos">280</span></a>
</span><span id="find_and_prepare_cython_modules-281"><a href="#find_and_prepare_cython_modules-281"><span class="linenos">281</span></a>
</span><span id="find_and_prepare_cython_modules-282"><a href="#find_and_prepare_cython_modules-282"><span class="linenos">282</span></a>        <span class="k">def</span> <span class="nf">filter</span><span class="p">(</span><span class="n">filtering_entity</span><span class="p">:</span> <span class="n">FilteringEntity</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="find_and_prepare_cython_modules-283"><a href="#find_and_prepare_cython_modules-283"><span class="linenos">283</span></a>            <span class="k">if</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">dirpath</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-284"><a href="#find_and_prepare_cython_modules-284"><span class="linenos">284</span></a>                <span class="c1"># Ignore package_src/_template_module</span>
</span><span id="find_and_prepare_cython_modules-285"><a href="#find_and_prepare_cython_modules-285"><span class="linenos">285</span></a>                <span class="n">dirpath</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="find_and_prepare_cython_modules-286"><a href="#find_and_prepare_cython_modules-286"><span class="linenos">286</span></a>                <span class="n">rel_path</span> <span class="o">=</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dirpath</span><span class="p">,</span> <span class="n">package_src_path</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-287"><a href="#find_and_prepare_cython_modules-287"><span class="linenos">287</span></a>                <span class="n">rel_path</span> <span class="o">=</span> <span class="n">rel_path</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="find_and_prepare_cython_modules-288"><a href="#find_and_prepare_cython_modules-288"><span class="linenos">288</span></a>                <span class="k">if</span> <span class="n">rel_path</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-289"><a href="#find_and_prepare_cython_modules-289"><span class="linenos">289</span></a>                    <span class="n">rel_path_parts</span> <span class="o">=</span> <span class="n">rel_path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-290"><a href="#find_and_prepare_cython_modules-290"><span class="linenos">290</span></a>                    <span class="k">if</span> <span class="n">rel_path_parts</span> <span class="ow">and</span> <span class="n">TEMPLATE_MODULE_NAME</span> <span class="o">==</span> <span class="n">rel_path_parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="find_and_prepare_cython_modules-291"><a href="#find_and_prepare_cython_modules-291"><span class="linenos">291</span></a>                        <span class="k">return</span> <span class="kc">False</span>
</span><span id="find_and_prepare_cython_modules-292"><a href="#find_and_prepare_cython_modules-292"><span class="linenos">292</span></a>                
</span><span id="find_and_prepare_cython_modules-293"><a href="#find_and_prepare_cython_modules-293"><span class="linenos">293</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="find_and_prepare_cython_modules-294"><a href="#find_and_prepare_cython_modules-294"><span class="linenos">294</span></a>            <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">dirname</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-295"><a href="#find_and_prepare_cython_modules-295"><span class="linenos">295</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="find_and_prepare_cython_modules-296"><a href="#find_and_prepare_cython_modules-296"><span class="linenos">296</span></a>            <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">filename</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-297"><a href="#find_and_prepare_cython_modules-297"><span class="linenos">297</span></a>                <span class="n">dirpath</span><span class="p">,</span> <span class="n">filename</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="find_and_prepare_cython_modules-298"><a href="#find_and_prepare_cython_modules-298"><span class="linenos">298</span></a>                <span class="k">if</span> <span class="n">BUILD_CONFIG_FILENAME</span> <span class="o">==</span> <span class="n">filename</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-299"><a href="#find_and_prepare_cython_modules-299"><span class="linenos">299</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="find_and_prepare_cython_modules-300"><a href="#find_and_prepare_cython_modules-300"><span class="linenos">300</span></a>                
</span><span id="find_and_prepare_cython_modules-301"><a href="#find_and_prepare_cython_modules-301"><span class="linenos">301</span></a>                <span class="n">file_name</span><span class="p">,</span> <span class="n">file_extension</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-302"><a href="#find_and_prepare_cython_modules-302"><span class="linenos">302</span></a>                <span class="k">if</span> <span class="n">file_extension</span> <span class="ow">in</span> <span class="n">all_ext</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-303"><a href="#find_and_prepare_cython_modules-303"><span class="linenos">303</span></a>                    <span class="k">return</span> <span class="kc">True</span>
</span><span id="find_and_prepare_cython_modules-304"><a href="#find_and_prepare_cython_modules-304"><span class="linenos">304</span></a>                
</span><span id="find_and_prepare_cython_modules-305"><a href="#find_and_prepare_cython_modules-305"><span class="linenos">305</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="find_and_prepare_cython_modules-306"><a href="#find_and_prepare_cython_modules-306"><span class="linenos">306</span></a>            <span class="k">elif</span> <span class="n">FilteringEntity</span><span class="o">.</span><span class="n">aggregated</span> <span class="o">==</span> <span class="n">filtering_entity</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-307"><a href="#find_and_prepare_cython_modules-307"><span class="linenos">307</span></a>                <span class="k">return</span> <span class="n">data</span>
</span><span id="find_and_prepare_cython_modules-308"><a href="#find_and_prepare_cython_modules-308"><span class="linenos">308</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-309"><a href="#find_and_prepare_cython_modules-309"><span class="linenos">309</span></a>                <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="find_and_prepare_cython_modules-310"><a href="#find_and_prepare_cython_modules-310"><span class="linenos">310</span></a>            
</span><span id="find_and_prepare_cython_modules-311"><a href="#find_and_prepare_cython_modules-311"><span class="linenos">311</span></a>        <span class="n">travers_result</span> <span class="o">=</span> <span class="n">file_list_traversal</span><span class="p">(</span><span class="n">package_src_path</span><span class="p">,</span> <span class="nb">filter</span><span class="p">,</span> <span class="n">remove_empty_dirpaths</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-312"><a href="#find_and_prepare_cython_modules-312"><span class="linenos">312</span></a>        <span class="c1"># travers_result = filtered_file_list_traversal(package_src_path, FilteringType.including, {&#39;.pyx&#39;, &#39;.c&#39;, &#39;.lib&#39;, &#39;.dll&#39;, &#39;.so&#39;}, remove_empty_items=True, use_spinner=False)</span>
</span><span id="find_and_prepare_cython_modules-313"><a href="#find_and_prepare_cython_modules-313"><span class="linenos">313</span></a>        
</span><span id="find_and_prepare_cython_modules-314"><a href="#find_and_prepare_cython_modules-314"><span class="linenos">314</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="find_and_prepare_cython_modules-315"><a href="#find_and_prepare_cython_modules-315"><span class="linenos">315</span></a>        <span class="k">for</span> <span class="n">dir_path</span><span class="p">,</span> <span class="n">dirs</span><span class="p">,</span> <span class="n">files</span> <span class="ow">in</span> <span class="n">travers_result</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-316"><a href="#find_and_prepare_cython_modules-316"><span class="linenos">316</span></a>            <span class="c1"># Ignore package_src/_template_module</span>
</span><span id="find_and_prepare_cython_modules-317"><a href="#find_and_prepare_cython_modules-317"><span class="linenos">317</span></a>            <span class="n">rel_path</span> <span class="o">=</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path</span><span class="p">,</span> <span class="n">package_src_path</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-318"><a href="#find_and_prepare_cython_modules-318"><span class="linenos">318</span></a>            <span class="n">rel_path</span> <span class="o">=</span> <span class="n">rel_path</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</span><span id="find_and_prepare_cython_modules-319"><a href="#find_and_prepare_cython_modules-319"><span class="linenos">319</span></a>            <span class="k">if</span> <span class="n">rel_path</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-320"><a href="#find_and_prepare_cython_modules-320"><span class="linenos">320</span></a>                <span class="n">rel_path_parts</span> <span class="o">=</span> <span class="n">rel_path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-321"><a href="#find_and_prepare_cython_modules-321"><span class="linenos">321</span></a>                <span class="k">if</span> <span class="n">rel_path_parts</span> <span class="ow">and</span> <span class="n">TEMPLATE_MODULE_NAME</span> <span class="o">==</span> <span class="n">rel_path_parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="find_and_prepare_cython_modules-322"><a href="#find_and_prepare_cython_modules-322"><span class="linenos">322</span></a>                    <span class="k">continue</span>
</span><span id="find_and_prepare_cython_modules-323"><a href="#find_and_prepare_cython_modules-323"><span class="linenos">323</span></a>
</span><span id="find_and_prepare_cython_modules-324"><a href="#find_and_prepare_cython_modules-324"><span class="linenos">324</span></a>            <span class="n">dir_path_obj</span> <span class="o">=</span> <span class="n">RelativePath</span><span class="p">(</span><span class="n">dir_path</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-325"><a href="#find_and_prepare_cython_modules-325"><span class="linenos">325</span></a>            <span class="n">extensions</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="find_and_prepare_cython_modules-326"><a href="#find_and_prepare_cython_modules-326"><span class="linenos">326</span></a>            <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-327"><a href="#find_and_prepare_cython_modules-327"><span class="linenos">327</span></a>                <span class="n">filename</span><span class="p">,</span> <span class="n">file_extension</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-328"><a href="#find_and_prepare_cython_modules-328"><span class="linenos">328</span></a>                <span class="k">if</span> <span class="n">file_extension</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">extensions</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-329"><a href="#find_and_prepare_cython_modules-329"><span class="linenos">329</span></a>                    <span class="n">extensions</span><span class="p">[</span><span class="n">file_extension</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="find_and_prepare_cython_modules-330"><a href="#find_and_prepare_cython_modules-330"><span class="linenos">330</span></a>                
</span><span id="find_and_prepare_cython_modules-331"><a href="#find_and_prepare_cython_modules-331"><span class="linenos">331</span></a>                <span class="n">extensions</span><span class="p">[</span><span class="n">file_extension</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-332"><a href="#find_and_prepare_cython_modules-332"><span class="linenos">332</span></a>            
</span><span id="find_and_prepare_cython_modules-333"><a href="#find_and_prepare_cython_modules-333"><span class="linenos">333</span></a>            <span class="n">is_exctension</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="find_and_prepare_cython_modules-334"><a href="#find_and_prepare_cython_modules-334"><span class="linenos">334</span></a>            <span class="n">build_config</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="find_and_prepare_cython_modules-335"><a href="#find_and_prepare_cython_modules-335"><span class="linenos">335</span></a>            <span class="k">if</span> <span class="n">BUILD_CONFIG_FILENAME</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-336"><a href="#find_and_prepare_cython_modules-336"><span class="linenos">336</span></a>                <span class="n">build_config_module_name</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">BUILD_CONFIG_FILENAME</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-337"><a href="#find_and_prepare_cython_modules-337"><span class="linenos">337</span></a>                <span class="n">build_config_full_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">dir_path_obj</span><span class="p">(</span><span class="n">build_config_module_name</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-338"><a href="#find_and_prepare_cython_modules-338"><span class="linenos">338</span></a>                <span class="n">name</span> <span class="o">=</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">build_config_full_path</span><span class="p">,</span> <span class="n">root_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">))</span>
</span><span id="find_and_prepare_cython_modules-339"><a href="#find_and_prepare_cython_modules-339"><span class="linenos">339</span></a>                <span class="n">name_parts</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-340"><a href="#find_and_prepare_cython_modules-340"><span class="linenos">340</span></a>                <span class="n">module_full_name</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">name_part</span> <span class="k">for</span> <span class="n">name_part</span> <span class="ow">in</span> <span class="n">name_parts</span> <span class="k">if</span> <span class="n">name_part</span><span class="p">])</span>
</span><span id="find_and_prepare_cython_modules-341"><a href="#find_and_prepare_cython_modules-341"><span class="linenos">341</span></a>                <span class="n">build_config_module</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">import_module</span><span class="p">(</span><span class="n">module_full_name</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-342"><a href="#find_and_prepare_cython_modules-342"><span class="linenos">342</span></a>                <span class="n">build_config</span> <span class="o">=</span> <span class="n">build_config_module</span><span class="o">.</span><span class="n">build_config</span><span class="p">()</span>
</span><span id="find_and_prepare_cython_modules-343"><a href="#find_and_prepare_cython_modules-343"><span class="linenos">343</span></a>                <span class="n">is_exctension</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="find_and_prepare_cython_modules-344"><a href="#find_and_prepare_cython_modules-344"><span class="linenos">344</span></a>
</span><span id="find_and_prepare_cython_modules-345"><a href="#find_and_prepare_cython_modules-345"><span class="linenos">345</span></a>            <span class="n">sub_result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="find_and_prepare_cython_modules-346"><a href="#find_and_prepare_cython_modules-346"><span class="linenos">346</span></a>            <span class="k">if</span> <span class="p">(</span><span class="n">cython_file_ext</span> <span class="ow">in</span> <span class="n">extensions</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">build_config</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="find_and_prepare_cython_modules-347"><a href="#find_and_prepare_cython_modules-347"><span class="linenos">347</span></a>                <span class="k">for</span> <span class="n">file_extension</span><span class="p">,</span> <span class="n">files</span> <span class="ow">in</span> <span class="n">extensions</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="find_and_prepare_cython_modules-348"><a href="#find_and_prepare_cython_modules-348"><span class="linenos">348</span></a>                    <span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-349"><a href="#find_and_prepare_cython_modules-349"><span class="linenos">349</span></a>                        <span class="k">if</span> <span class="n">file_extension</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="p">(</span><span class="n">compilable_ext</span> <span class="o">|</span> <span class="n">headers_ext</span><span class="p">):</span>
</span><span id="find_and_prepare_cython_modules-350"><a href="#find_and_prepare_cython_modules-350"><span class="linenos">350</span></a>                            <span class="n">is_exctension</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="find_and_prepare_cython_modules-351"><a href="#find_and_prepare_cython_modules-351"><span class="linenos">351</span></a>                            <span class="n">sub_result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">path_join</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file</span><span class="p">),</span> <span class="n">root_path</span><span class="p">)))</span>
</span><span id="find_and_prepare_cython_modules-352"><a href="#find_and_prepare_cython_modules-352"><span class="linenos">352</span></a>                        
</span><span id="find_and_prepare_cython_modules-353"><a href="#find_and_prepare_cython_modules-353"><span class="linenos">353</span></a>                        <span class="k">if</span> <span class="n">file_extension</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="n">codegen_files_ext</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-354"><a href="#find_and_prepare_cython_modules-354"><span class="linenos">354</span></a>                            <span class="n">filename</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">splitext</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-355"><a href="#find_and_prepare_cython_modules-355"><span class="linenos">355</span></a>                            <span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">&#39;__cython&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">&#39;__compiled&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">&#39;__python&#39;</span><span class="p">):</span>
</span><span id="find_and_prepare_cython_modules-356"><a href="#find_and_prepare_cython_modules-356"><span class="linenos">356</span></a>                                <span class="k">try</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-357"><a href="#find_and_prepare_cython_modules-357"><span class="linenos">357</span></a>                                    <span class="n">remove</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>
</span><span id="find_and_prepare_cython_modules-358"><a href="#find_and_prepare_cython_modules-358"><span class="linenos">358</span></a>                                <span class="k">except</span> <span class="ne">OSError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-359"><a href="#find_and_prepare_cython_modules-359"><span class="linenos">359</span></a>                                    <span class="nb">print</span><span class="p">(</span><span class="n">get_exception</span><span class="p">())</span>
</span><span id="find_and_prepare_cython_modules-360"><a href="#find_and_prepare_cython_modules-360"><span class="linenos">360</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-361"><a href="#find_and_prepare_cython_modules-361"><span class="linenos">361</span></a>                                <span class="n">is_exctension</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="find_and_prepare_cython_modules-362"><a href="#find_and_prepare_cython_modules-362"><span class="linenos">362</span></a>                                <span class="n">sub_result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">path_join</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file</span><span class="p">),</span> <span class="n">root_path</span><span class="p">)))</span>
</span><span id="find_and_prepare_cython_modules-363"><a href="#find_and_prepare_cython_modules-363"><span class="linenos">363</span></a>                        
</span><span id="find_and_prepare_cython_modules-364"><a href="#find_and_prepare_cython_modules-364"><span class="linenos">364</span></a>                        <span class="k">if</span> <span class="n">file_extension</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="ow">in</span> <span class="n">libs_ext</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-365"><a href="#find_and_prepare_cython_modules-365"><span class="linenos">365</span></a>                            <span class="k">try</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-366"><a href="#find_and_prepare_cython_modules-366"><span class="linenos">366</span></a>                                <span class="n">remove</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>
</span><span id="find_and_prepare_cython_modules-367"><a href="#find_and_prepare_cython_modules-367"><span class="linenos">367</span></a>                            <span class="k">except</span> <span class="ne">OSError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-368"><a href="#find_and_prepare_cython_modules-368"><span class="linenos">368</span></a>                                <span class="nb">print</span><span class="p">(</span><span class="n">get_exception</span><span class="p">())</span>
</span><span id="find_and_prepare_cython_modules-369"><a href="#find_and_prepare_cython_modules-369"><span class="linenos">369</span></a>            
</span><span id="find_and_prepare_cython_modules-370"><a href="#find_and_prepare_cython_modules-370"><span class="linenos">370</span></a>            <span class="k">if</span> <span class="n">is_exctension</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-371"><a href="#find_and_prepare_cython_modules-371"><span class="linenos">371</span></a>                <span class="n">name</span> <span class="o">=</span> <span class="n">get_relative_path_part</span><span class="p">(</span><span class="n">dir_path_obj</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">),</span> <span class="n">root_rel</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">))</span>
</span><span id="find_and_prepare_cython_modules-372"><a href="#find_and_prepare_cython_modules-372"><span class="linenos">372</span></a>                <span class="n">name_parts</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-373"><a href="#find_and_prepare_cython_modules-373"><span class="linenos">373</span></a>                <span class="k">if</span> <span class="n">build_config</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-374"><a href="#find_and_prepare_cython_modules-374"><span class="linenos">374</span></a>                    <span class="k">if</span> <span class="mi">1</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)</span> <span class="ow">and</span> <span class="n">sub_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="n">cython_file_ext</span><span class="p">):</span>
</span><span id="find_and_prepare_cython_modules-375"><a href="#find_and_prepare_cython_modules-375"><span class="linenos">375</span></a>                        <span class="n">name_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">get_file_name_without_extension</span><span class="p">(</span><span class="n">sub_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</span><span id="find_and_prepare_cython_modules-376"><a href="#find_and_prepare_cython_modules-376"><span class="linenos">376</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-377"><a href="#find_and_prepare_cython_modules-377"><span class="linenos">377</span></a>                        <span class="n">name_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;cython_module&#39;</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-378"><a href="#find_and_prepare_cython_modules-378"><span class="linenos">378</span></a>                    
</span><span id="find_and_prepare_cython_modules-379"><a href="#find_and_prepare_cython_modules-379"><span class="linenos">379</span></a>                    <span class="n">name</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">name_part</span> <span class="k">for</span> <span class="n">name_part</span> <span class="ow">in</span> <span class="n">name_parts</span> <span class="k">if</span> <span class="n">name_part</span><span class="p">])</span>
</span><span id="find_and_prepare_cython_modules-380"><a href="#find_and_prepare_cython_modules-380"><span class="linenos">380</span></a>                    <span class="n">extension</span><span class="p">:</span> <span class="n">CythonExtension</span> <span class="o">=</span> <span class="n">CythonExtension</span><span class="p">(</span>
</span><span id="find_and_prepare_cython_modules-381"><a href="#find_and_prepare_cython_modules-381"><span class="linenos">381</span></a>                        <span class="n">name</span><span class="p">,</span> 
</span><span id="find_and_prepare_cython_modules-382"><a href="#find_and_prepare_cython_modules-382"><span class="linenos">382</span></a>                        <span class="n">sources</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)),</span>
</span><span id="find_and_prepare_cython_modules-383"><a href="#find_and_prepare_cython_modules-383"><span class="linenos">383</span></a>                        <span class="n">language</span><span class="o">=</span><span class="s2">&quot;c&quot;</span><span class="p">,</span>
</span><span id="find_and_prepare_cython_modules-384"><a href="#find_and_prepare_cython_modules-384"><span class="linenos">384</span></a>                        <span class="c1"># cython_compile_time_env=prepare_cflags_dict(additional_cflags),</span>
</span><span id="find_and_prepare_cython_modules-385"><a href="#find_and_prepare_cython_modules-385"><span class="linenos">385</span></a>                        <span class="n">define_macros</span><span class="o">=</span><span class="n">prepare_cflags_dict</span><span class="p">(</span><span class="n">additional_cflags</span><span class="p">),</span>
</span><span id="find_and_prepare_cython_modules-386"><a href="#find_and_prepare_cython_modules-386"><span class="linenos">386</span></a>                    <span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-387"><a href="#find_and_prepare_cython_modules-387"><span class="linenos">387</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-388"><a href="#find_and_prepare_cython_modules-388"><span class="linenos">388</span></a>                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">build_config</span><span class="p">,</span> <span class="p">(</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">)):</span>
</span><span id="find_and_prepare_cython_modules-389"><a href="#find_and_prepare_cython_modules-389"><span class="linenos">389</span></a>                        <span class="n">extension_type</span> <span class="o">=</span> <span class="n">CythonExtension</span>
</span><span id="find_and_prepare_cython_modules-390"><a href="#find_and_prepare_cython_modules-390"><span class="linenos">390</span></a>                        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">build_config</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="find_and_prepare_cython_modules-391"><a href="#find_and_prepare_cython_modules-391"><span class="linenos">391</span></a>                            <span class="n">extension_type</span><span class="p">,</span> <span class="n">build_config</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="find_and_prepare_cython_modules-392"><a href="#find_and_prepare_cython_modules-392"><span class="linenos">392</span></a>                            <span class="n">extension_type</span> <span class="o">=</span> <span class="n">extension_type</span> <span class="k">if</span> <span class="n">extension_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">CythonExtension</span>
</span><span id="find_and_prepare_cython_modules-393"><a href="#find_and_prepare_cython_modules-393"><span class="linenos">393</span></a>                        
</span><span id="find_and_prepare_cython_modules-394"><a href="#find_and_prepare_cython_modules-394"><span class="linenos">394</span></a>                        <span class="k">if</span> <span class="s1">&#39;Windows&#39;</span> <span class="o">==</span> <span class="n">OS_TYPE</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-395"><a href="#find_and_prepare_cython_modules-395"><span class="linenos">395</span></a>                            <span class="c1"># CythonExtension :raises setuptools.errors.PlatformError: if &#39;runtime_library_dirs&#39; is specified on Windows. (since v63)</span>
</span><span id="find_and_prepare_cython_modules-396"><a href="#find_and_prepare_cython_modules-396"><span class="linenos">396</span></a>                            <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;runtime_library_dirs&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-397"><a href="#find_and_prepare_cython_modules-397"><span class="linenos">397</span></a>                        
</span><span id="find_and_prepare_cython_modules-398"><a href="#find_and_prepare_cython_modules-398"><span class="linenos">398</span></a>                        <span class="n">name_parts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">build_config</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">])</span>
</span><span id="find_and_prepare_cython_modules-399"><a href="#find_and_prepare_cython_modules-399"><span class="linenos">399</span></a>                        <span class="n">name</span> <span class="o">=</span> <span class="s1">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">name_part</span> <span class="k">for</span> <span class="n">name_part</span> <span class="ow">in</span> <span class="n">name_parts</span> <span class="k">if</span> <span class="n">name_part</span><span class="p">])</span>
</span><span id="find_and_prepare_cython_modules-400"><a href="#find_and_prepare_cython_modules-400"><span class="linenos">400</span></a>                        <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;name&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-401"><a href="#find_and_prepare_cython_modules-401"><span class="linenos">401</span></a>
</span><span id="find_and_prepare_cython_modules-402"><a href="#find_and_prepare_cython_modules-402"><span class="linenos">402</span></a>                        <span class="n">cython_compile_time_env</span><span class="o">=</span><span class="n">prepare_cflags_dict</span><span class="p">(</span><span class="n">additional_cflags</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-403"><a href="#find_and_prepare_cython_modules-403"><span class="linenos">403</span></a>                        <span class="k">if</span> <span class="s1">&#39;cython_compile_time_env&#39;</span> <span class="ow">in</span> <span class="n">build_config</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-404"><a href="#find_and_prepare_cython_modules-404"><span class="linenos">404</span></a>                            <span class="n">cython_compile_time_env</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">build_config</span><span class="p">[</span><span class="s1">&#39;cython_compile_time_env&#39;</span><span class="p">])</span>
</span><span id="find_and_prepare_cython_modules-405"><a href="#find_and_prepare_cython_modules-405"><span class="linenos">405</span></a>                            <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;cython_compile_time_env&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-406"><a href="#find_and_prepare_cython_modules-406"><span class="linenos">406</span></a>
</span><span id="find_and_prepare_cython_modules-407"><a href="#find_and_prepare_cython_modules-407"><span class="linenos">407</span></a>                        <span class="n">define_macros</span><span class="o">=</span><span class="n">prepare_cflags_dict</span><span class="p">(</span><span class="n">additional_cflags</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-408"><a href="#find_and_prepare_cython_modules-408"><span class="linenos">408</span></a>                        <span class="k">if</span> <span class="s1">&#39;define_macros&#39;</span> <span class="ow">in</span> <span class="n">build_config</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-409"><a href="#find_and_prepare_cython_modules-409"><span class="linenos">409</span></a>                            <span class="n">define_macros</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">build_config</span><span class="p">[</span><span class="s1">&#39;define_macros&#39;</span><span class="p">])</span>
</span><span id="find_and_prepare_cython_modules-410"><a href="#find_and_prepare_cython_modules-410"><span class="linenos">410</span></a>                            <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;define_macros&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-411"><a href="#find_and_prepare_cython_modules-411"><span class="linenos">411</span></a>                        
</span><span id="find_and_prepare_cython_modules-412"><a href="#find_and_prepare_cython_modules-412"><span class="linenos">412</span></a>                        <span class="n">sources</span> <span class="o">=</span> <span class="n">extend_file_names_to_root_relative_paths</span><span class="p">(</span><span class="n">root_path</span><span class="p">,</span> <span class="n">dir_path_obj</span><span class="p">,</span> <span class="n">build_config</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;sources&#39;</span><span class="p">,</span> <span class="nb">list</span><span class="p">()))</span>
</span><span id="find_and_prepare_cython_modules-413"><a href="#find_and_prepare_cython_modules-413"><span class="linenos">413</span></a>                        <span class="n">sources</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-414"><a href="#find_and_prepare_cython_modules-414"><span class="linenos">414</span></a>                        
</span><span id="find_and_prepare_cython_modules-415"><a href="#find_and_prepare_cython_modules-415"><span class="linenos">415</span></a>                        <span class="n">extension</span><span class="p">:</span> <span class="n">CythonExtension</span> <span class="o">=</span> <span class="n">extension_type</span><span class="p">(</span>
</span><span id="find_and_prepare_cython_modules-416"><a href="#find_and_prepare_cython_modules-416"><span class="linenos">416</span></a>                            <span class="n">name</span><span class="p">,</span> 
</span><span id="find_and_prepare_cython_modules-417"><a href="#find_and_prepare_cython_modules-417"><span class="linenos">417</span></a>                            <span class="n">sources</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">sources</span><span class="p">)),</span>
</span><span id="find_and_prepare_cython_modules-418"><a href="#find_and_prepare_cython_modules-418"><span class="linenos">418</span></a>                            <span class="c1"># cython_compile_time_env=cython_compile_time_env,</span>
</span><span id="find_and_prepare_cython_modules-419"><a href="#find_and_prepare_cython_modules-419"><span class="linenos">419</span></a>                            <span class="n">define_macros</span><span class="o">=</span><span class="n">define_macros</span><span class="p">,</span>
</span><span id="find_and_prepare_cython_modules-420"><a href="#find_and_prepare_cython_modules-420"><span class="linenos">420</span></a>                            <span class="o">**</span><span class="n">build_config</span>
</span><span id="find_and_prepare_cython_modules-421"><a href="#find_and_prepare_cython_modules-421"><span class="linenos">421</span></a>                        <span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-422"><a href="#find_and_prepare_cython_modules-422"><span class="linenos">422</span></a>                    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">build_config</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">):</span>
</span><span id="find_and_prepare_cython_modules-423"><a href="#find_and_prepare_cython_modules-423"><span class="linenos">423</span></a>                        <span class="n">build_config</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">dir_path_obj</span><span class="p">(</span><span class="n">BUILD_CONFIG_FILENAME</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-424"><a href="#find_and_prepare_cython_modules-424"><span class="linenos">424</span></a>                        <span class="n">build_config</span><span class="o">.</span><span class="n">module_import_str</span> <span class="o">=</span> <span class="n">module_full_name</span>
</span><span id="find_and_prepare_cython_modules-425"><a href="#find_and_prepare_cython_modules-425"><span class="linenos">425</span></a>                        <span class="n">build_config</span><span class="o">.</span><span class="n">files</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-426"><a href="#find_and_prepare_cython_modules-426"><span class="linenos">426</span></a>                        <span class="n">extension</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="find_and_prepare_cython_modules-427"><a href="#find_and_prepare_cython_modules-427"><span class="linenos">427</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-428"><a href="#find_and_prepare_cython_modules-428"><span class="linenos">428</span></a>                        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unknown build_config type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">build_config</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-429"><a href="#find_and_prepare_cython_modules-429"><span class="linenos">429</span></a>                
</span><span id="find_and_prepare_cython_modules-430"><a href="#find_and_prepare_cython_modules-430"><span class="linenos">430</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">extension</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-431"><a href="#find_and_prepare_cython_modules-431"><span class="linenos">431</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="find_and_prepare_cython_modules-432"><a href="#find_and_prepare_cython_modules-432"><span class="linenos">432</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">sub_result</span><span class="p">)</span>
</span><span id="find_and_prepare_cython_modules-433"><a href="#find_and_prepare_cython_modules-433"><span class="linenos">433</span></a>        
</span><span id="find_and_prepare_cython_modules-434"><a href="#find_and_prepare_cython_modules-434"><span class="linenos">434</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="BuildConfig">
                            <input id="BuildConfig-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">BuildConfig</span>:

                <label class="view-source-button" for="BuildConfig-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BuildConfig"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BuildConfig-437"><a href="#BuildConfig-437"><span class="linenos">437</span></a><span class="k">class</span> <span class="nc">BuildConfig</span><span class="p">:</span>
</span><span id="BuildConfig-438"><a href="#BuildConfig-438"><span class="linenos">438</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="BuildConfig-439"><a href="#BuildConfig-439"><span class="linenos">439</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="BuildConfig-440"><a href="#BuildConfig-440"><span class="linenos">440</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="BuildConfig-441"><a href="#BuildConfig-441"><span class="linenos">441</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">additional_pyx_flags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="BuildConfig-442"><a href="#BuildConfig-442"><span class="linenos">442</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">find_package_data</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BuildConfig-443"><a href="#BuildConfig-443"><span class="linenos">443</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">root_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            <div id="BuildConfig.package_build_is_in_debug_mode" class="classattr">
                                <div class="attr variable">
            <span class="name">package_build_is_in_debug_mode</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#BuildConfig.package_build_is_in_debug_mode"></a>
    
    

                            </div>
                            <div id="BuildConfig.package_build_is_in_sdist_mode" class="classattr">
                                <div class="attr variable">
            <span class="name">package_build_is_in_sdist_mode</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#BuildConfig.package_build_is_in_sdist_mode"></a>
    
    

                            </div>
                            <div id="BuildConfig.additional_pyx_flags" class="classattr">
                                <div class="attr variable">
            <span class="name">additional_pyx_flags</span><span class="annotation">: Dict[str, Tuple[bool, Union[str, int]]]</span>

        
    </div>
    <a class="headerlink" href="#BuildConfig.additional_pyx_flags"></a>
    
    

                            </div>
                            <div id="BuildConfig.find_package_data" class="classattr">
                                <div class="attr variable">
            <span class="name">find_package_data</span><span class="annotation">: Callable</span>

        
    </div>
    <a class="headerlink" href="#BuildConfig.find_package_data"></a>
    
    

                            </div>
                            <div id="BuildConfig.root_rel" class="classattr">
                                <div class="attr variable">
            <span class="name">root_rel</span><span class="annotation">: cengal.file_system.path_manager.versions.v_0.path_manager.RelativePath</span>

        
    </div>
    <a class="headerlink" href="#BuildConfig.root_rel"></a>
    
    

                            </div>
                </section>
                <section id="sdist">
                            <input id="sdist-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">sdist</span><wbr>(<span class="base">setuptools.command.sdist.sdist</span>):

                <label class="view-source-button" for="sdist-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#sdist"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="sdist-446"><a href="#sdist-446"><span class="linenos">446</span></a><span class="k">class</span> <span class="nc">sdist</span><span class="p">(</span><span class="n">sdist_orig</span><span class="p">):</span>
</span><span id="sdist-447"><a href="#sdist-447"><span class="linenos">447</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="sdist-448"><a href="#sdist-448"><span class="linenos">448</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="sdist-449"><a href="#sdist-449"><span class="linenos">449</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span><span id="sdist-450"><a href="#sdist-450"><span class="linenos">450</span></a>
</span><span id="sdist-451"><a href="#sdist-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="sdist-452"><a href="#sdist-452"><span class="linenos">452</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="sdist-453"><a href="#sdist-453"><span class="linenos">453</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="sdist-454"><a href="#sdist-454"><span class="linenos">454</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="sdist-455"><a href="#sdist-455"><span class="linenos">455</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="sdist-456"><a href="#sdist-456"><span class="linenos">456</span></a>            
</span><span id="sdist-457"><a href="#sdist-457"><span class="linenos">457</span></a>            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;sdist command is currently being run&quot;</span><span class="p">)</span>
</span><span id="sdist-458"><a href="#sdist-458"><span class="linenos">458</span></a>            <span class="n">environ</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;True&#39;</span>
</span><span id="sdist-459"><a href="#sdist-459"><span class="linenos">459</span></a>            <span class="n">packages_data_dict</span><span class="p">,</span> <span class="n">manifest_included_files</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">find_package_data</span><span class="p">()</span>
</span><span id="sdist-460"><a href="#sdist-460"><span class="linenos">460</span></a>            <span class="n">generate_manifest_included_files</span><span class="p">(</span><span class="n">manifest_included_files</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">root_rel</span><span class="p">)</span>
</span><span id="sdist-461"><a href="#sdist-461"><span class="linenos">461</span></a>        
</span><span id="sdist-462"><a href="#sdist-462"><span class="linenos">462</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Smart sdist that finds anything supported by revision control</p>
</div>


                            <div id="sdist.__init__" class="classattr">
                                        <input id="sdist.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">sdist</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">dist</span><span class="p">:</span> <span class="n">setuptools</span><span class="o">.</span><span class="n">_distutils</span><span class="o">.</span><span class="n">dist</span><span class="o">.</span><span class="n">Distribution</span>,</span><span class="param">	<span class="n">build_config</span><span class="p">:</span> <span class="n"><a href="#BuildConfig">BuildConfig</a></span></span>)</span>

                <label class="view-source-button" for="sdist.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#sdist.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="sdist.__init__-447"><a href="#sdist.__init__-447"><span class="linenos">447</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="sdist.__init__-448"><a href="#sdist.__init__-448"><span class="linenos">448</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="sdist.__init__-449"><a href="#sdist.__init__-449"><span class="linenos">449</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Construct the command for dist, updating
vars(self) with any keyword parameters.</p>
</div>


                            </div>
                            <div id="sdist.build_config" class="classattr">
                                <div class="attr variable">
            <span class="name">build_config</span><span class="annotation">: <a href="#BuildConfig">BuildConfig</a></span>

        
    </div>
    <a class="headerlink" href="#sdist.build_config"></a>
    
    

                            </div>
                            <div id="sdist.run" class="classattr">
                                        <input id="sdist.run-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="sdist.run-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#sdist.run"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="sdist.run-451"><a href="#sdist.run-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="sdist.run-452"><a href="#sdist.run-452"><span class="linenos">452</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="sdist.run-453"><a href="#sdist.run-453"><span class="linenos">453</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="sdist.run-454"><a href="#sdist.run-454"><span class="linenos">454</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="sdist.run-455"><a href="#sdist.run-455"><span class="linenos">455</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="sdist.run-456"><a href="#sdist.run-456"><span class="linenos">456</span></a>            
</span><span id="sdist.run-457"><a href="#sdist.run-457"><span class="linenos">457</span></a>            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;sdist command is currently being run&quot;</span><span class="p">)</span>
</span><span id="sdist.run-458"><a href="#sdist.run-458"><span class="linenos">458</span></a>            <span class="n">environ</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;True&#39;</span>
</span><span id="sdist.run-459"><a href="#sdist.run-459"><span class="linenos">459</span></a>            <span class="n">packages_data_dict</span><span class="p">,</span> <span class="n">manifest_included_files</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">find_package_data</span><span class="p">()</span>
</span><span id="sdist.run-460"><a href="#sdist.run-460"><span class="linenos">460</span></a>            <span class="n">generate_manifest_included_files</span><span class="p">(</span><span class="n">manifest_included_files</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">root_rel</span><span class="p">)</span>
</span><span id="sdist.run-461"><a href="#sdist.run-461"><span class="linenos">461</span></a>        
</span><span id="sdist.run-462"><a href="#sdist.run-462"><span class="linenos">462</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>A command's raison d'etre: carry out the action it exists to
perform, controlled by the options initialized in
'initialize_options()', customized by other commands, the setup
script, the command-line, and config files, and finalized in
'finalize_options()'.  All terminal output and filesystem
interaction should be done by 'run()'.</p>

<p>This method must be implemented by all command classes.</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>setuptools.command.sdist.sdist</dt>
                                <dd id="sdist.user_options" class="variable">user_options</dd>
                <dd id="sdist.negative_opt" class="variable">negative_opt</dd>
                <dd id="sdist.README_EXTENSIONS" class="variable">README_EXTENSIONS</dd>
                <dd id="sdist.READMES" class="variable">READMES</dd>
                <dd id="sdist.initialize_options" class="function">initialize_options</dd>
                <dd id="sdist.make_distribution" class="function">make_distribution</dd>
                <dd id="sdist.add_defaults" class="function">add_defaults</dd>
                <dd id="sdist.check_readme" class="function">check_readme</dd>
                <dd id="sdist.make_release_tree" class="function">make_release_tree</dd>
                <dd id="sdist.read_manifest" class="function">read_manifest</dd>

            </div>
            <div><dt>distutils.command.sdist.sdist</dt>
                                <dd id="sdist.description" class="variable">description</dd>
                <dd id="sdist.checking_metadata" class="function">checking_metadata</dd>
                <dd id="sdist.boolean_options" class="variable">boolean_options</dd>
                <dd id="sdist.help_options" class="variable">help_options</dd>
                <dd id="sdist.sub_commands" class="variable">sub_commands</dd>
                <dd id="sdist.finalize_options" class="function">finalize_options</dd>
                <dd id="sdist.check_metadata" class="function">check_metadata</dd>
                <dd id="sdist.get_file_list" class="function">get_file_list</dd>
                <dd id="sdist.read_template" class="function">read_template</dd>
                <dd id="sdist.prune_file_list" class="function">prune_file_list</dd>
                <dd id="sdist.write_manifest" class="function">write_manifest</dd>
                <dd id="sdist.get_archive_files" class="function">get_archive_files</dd>

            </div>
            <div><dt>setuptools.Command</dt>
                                <dd id="sdist.command_consumes_arguments" class="variable">command_consumes_arguments</dd>
                <dd id="sdist.ensure_string_list" class="function">ensure_string_list</dd>
                <dd id="sdist.reinitialize_command" class="function">reinitialize_command</dd>

            </div>
            <div><dt>distutils.cmd.Command</dt>
                                <dd id="sdist.distribution" class="variable">distribution</dd>
                <dd id="sdist.verbose" class="variable">verbose</dd>
                <dd id="sdist.force" class="variable">force</dd>
                <dd id="sdist.help" class="variable">help</dd>
                <dd id="sdist.finalized" class="variable">finalized</dd>
                <dd id="sdist.ensure_finalized" class="function">ensure_finalized</dd>
                <dd id="sdist.dump_options" class="function">dump_options</dd>
                <dd id="sdist.announce" class="function">announce</dd>
                <dd id="sdist.debug_print" class="function">debug_print</dd>
                <dd id="sdist.ensure_string" class="function">ensure_string</dd>
                <dd id="sdist.ensure_filename" class="function">ensure_filename</dd>
                <dd id="sdist.ensure_dirname" class="function">ensure_dirname</dd>
                <dd id="sdist.get_command_name" class="function">get_command_name</dd>
                <dd id="sdist.set_undefined_options" class="function">set_undefined_options</dd>
                <dd id="sdist.get_finalized_command" class="function">get_finalized_command</dd>
                <dd id="sdist.run_command" class="function">run_command</dd>
                <dd id="sdist.get_sub_commands" class="function">get_sub_commands</dd>
                <dd id="sdist.warn" class="function">warn</dd>
                <dd id="sdist.execute" class="function">execute</dd>
                <dd id="sdist.mkpath" class="function">mkpath</dd>
                <dd id="sdist.copy_file" class="function">copy_file</dd>
                <dd id="sdist.copy_tree" class="function">copy_tree</dd>
                <dd id="sdist.move_file" class="function">move_file</dd>
                <dd id="sdist.spawn" class="function">spawn</dd>
                <dd id="sdist.make_archive" class="function">make_archive</dd>
                <dd id="sdist.make_file" class="function">make_file</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="build">
                            <input id="build-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">build</span><wbr>(<span class="base">distutils.command.build.build</span>):

                <label class="view-source-button" for="build-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#build"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="build-465"><a href="#build-465"><span class="linenos">465</span></a><span class="k">class</span> <span class="nc">build</span><span class="p">(</span><span class="n">build_orig</span><span class="p">):</span>
</span><span id="build-466"><a href="#build-466"><span class="linenos">466</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build-467"><a href="#build-467"><span class="linenos">467</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="build-468"><a href="#build-468"><span class="linenos">468</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span><span id="build-469"><a href="#build-469"><span class="linenos">469</span></a>
</span><span id="build-470"><a href="#build-470"><span class="linenos">470</span></a>    <span class="k">def</span> <span class="nf">finalize_options</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="build-471"><a href="#build-471"><span class="linenos">471</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="build-472"><a href="#build-472"><span class="linenos">472</span></a>            <span class="n">setuptools_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)]</span>
</span><span id="build-473"><a href="#build-473"><span class="linenos">473</span></a>            <span class="n">cython_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)]</span>
</span><span id="build-474"><a href="#build-474"><span class="linenos">474</span></a>            <span class="n">cengal_extensions</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">)))</span>
</span><span id="build-475"><a href="#build-475"><span class="linenos">475</span></a>            <span class="n">cengal_result_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span><span class="p">()</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions</span><span class="p">]</span>
</span><span id="build-476"><a href="#build-476"><span class="linenos">476</span></a>            <span class="n">setuptools_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)])</span>
</span><span id="build-477"><a href="#build-477"><span class="linenos">477</span></a>            <span class="n">cython_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)])</span>
</span><span id="build-478"><a href="#build-478"><span class="linenos">478</span></a>            <span class="n">cengal_extensions_store_as_data</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">))</span>
</span><span id="build-479"><a href="#build-479"><span class="linenos">479</span></a>
</span><span id="build-480"><a href="#build-480"><span class="linenos">480</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build-481"><a href="#build-481"><span class="linenos">481</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="build-482"><a href="#build-482"><span class="linenos">482</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="build-483"><a href="#build-483"><span class="linenos">483</span></a>        
</span><span id="build-484"><a href="#build-484"><span class="linenos">484</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">finalize_options</span><span class="p">()</span>
</span><span id="build-485"><a href="#build-485"><span class="linenos">485</span></a>
</span><span id="build-486"><a href="#build-486"><span class="linenos">486</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="build-487"><a href="#build-487"><span class="linenos">487</span></a>            <span class="n">package_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="build-488"><a href="#build-488"><span class="linenos">488</span></a>            
</span><span id="build-489"><a href="#build-489"><span class="linenos">489</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build-490"><a href="#build-490"><span class="linenos">490</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions_store_as_data</span><span class="p">:</span>
</span><span id="build-491"><a href="#build-491"><span class="linenos">491</span></a>                    <span class="n">files</span> <span class="o">=</span> <span class="n">ext</span><span class="p">()</span>
</span><span id="build-492"><a href="#build-492"><span class="linenos">492</span></a>                    <span class="k">if</span> <span class="n">files</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build-493"><a href="#build-493"><span class="linenos">493</span></a>                        <span class="k">continue</span>
</span><span id="build-494"><a href="#build-494"><span class="linenos">494</span></a>
</span><span id="build-495"><a href="#build-495"><span class="linenos">495</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">package</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">package_data</span><span class="p">:</span>
</span><span id="build-496"><a href="#build-496"><span class="linenos">496</span></a>                        <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build-497"><a href="#build-497"><span class="linenos">497</span></a>                    
</span><span id="build-498"><a href="#build-498"><span class="linenos">498</span></a>                    <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">files</span><span class="p">)</span>
</span><span id="build-499"><a href="#build-499"><span class="linenos">499</span></a>
</span><span id="build-500"><a href="#build-500"><span class="linenos">500</span></a>                <span class="kn">from</span> <span class="nn">Cython.Build</span> <span class="kn">import</span> <span class="n">cythonize</span>
</span><span id="build-501"><a href="#build-501"><span class="linenos">501</span></a>                <span class="n">result_ext_modules</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build-502"><a href="#build-502"><span class="linenos">502</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="build-503"><a href="#build-503"><span class="linenos">503</span></a>                    <span class="n">cwd_before_cythonize</span> <span class="o">=</span> <span class="n">getcwd</span><span class="p">()</span>
</span><span id="build-504"><a href="#build-504"><span class="linenos">504</span></a>                    <span class="n">pyx_flags_dict</span> <span class="o">=</span> <span class="n">prepare_pyx_flags_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">additional_pyx_flags</span><span class="p">)</span>
</span><span id="build-505"><a href="#build-505"><span class="linenos">505</span></a>                    <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">remove_header_files</span><span class="p">(</span>
</span><span id="build-506"><a href="#build-506"><span class="linenos">506</span></a>                        <span class="n">cythonize</span><span class="p">(</span><span class="n">process_macros</span><span class="p">(</span><span class="n">cython_extensions</span><span class="p">),</span>
</span><span id="build-507"><a href="#build-507"><span class="linenos">507</span></a>                        <span class="n">compiler_directives</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;language_level&#39;</span><span class="p">:</span> <span class="s1">&#39;3&#39;</span><span class="p">},</span>
</span><span id="build-508"><a href="#build-508"><span class="linenos">508</span></a>                        <span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">pyx_flags_dict</span><span class="p">,</span>
</span><span id="build-509"><a href="#build-509"><span class="linenos">509</span></a>                        <span class="p">)))</span>
</span><span id="build-510"><a href="#build-510"><span class="linenos">510</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="build-511"><a href="#build-511"><span class="linenos">511</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;DEBUG: </span><span class="si">{</span><span class="n">cwd_before_cythonize</span><span class="si">=}</span><span class="s1"> | </span><span class="si">{</span><span class="n">getcwd</span><span class="p">()</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="build-512"><a href="#build-512"><span class="linenos">512</span></a>                    <span class="k">for</span> <span class="n">extension</span> <span class="ow">in</span> <span class="n">cython_extensions</span><span class="p">:</span>
</span><span id="build-513"><a href="#build-513"><span class="linenos">513</span></a>                        <span class="n">pprint</span><span class="p">(</span><span class="n">class_properties_values_including_overrided</span><span class="p">(</span><span class="n">extension</span><span class="p">))</span>
</span><span id="build-514"><a href="#build-514"><span class="linenos">514</span></a>                    
</span><span id="build-515"><a href="#build-515"><span class="linenos">515</span></a>                    <span class="k">raise</span>
</span><span id="build-516"><a href="#build-516"><span class="linenos">516</span></a>                
</span><span id="build-517"><a href="#build-517"><span class="linenos">517</span></a>                <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">setuptools_extensions</span><span class="p">)</span>
</span><span id="build-518"><a href="#build-518"><span class="linenos">518</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">result_ext_modules</span><span class="p">:</span>
</span><span id="build-519"><a href="#build-519"><span class="linenos">519</span></a>                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="s1">&#39;extra_compile_args&#39;</span><span class="p">):</span>
</span><span id="build-520"><a href="#build-520"><span class="linenos">520</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build-521"><a href="#build-521"><span class="linenos">521</span></a>                    
</span><span id="build-522"><a href="#build-522"><span class="linenos">522</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build-523"><a href="#build-523"><span class="linenos">523</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build-524"><a href="#build-524"><span class="linenos">524</span></a>                    
</span><span id="build-525"><a href="#build-525"><span class="linenos">525</span></a>                    <span class="k">if</span> <span class="s1">&#39;Darwin&#39;</span> <span class="o">==</span> <span class="n">OS_TYPE</span><span class="p">:</span>
</span><span id="build-526"><a href="#build-526"><span class="linenos">526</span></a>                        <span class="k">if</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_x86</span><span class="p">:</span>
</span><span id="build-527"><a href="#build-527"><span class="linenos">527</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;x86_64&#39;</span><span class="p">]</span>
</span><span id="build-528"><a href="#build-528"><span class="linenos">528</span></a>                        <span class="k">elif</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_arm</span><span class="p">:</span>
</span><span id="build-529"><a href="#build-529"><span class="linenos">529</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;arm64&#39;</span><span class="p">]</span>
</span><span id="build-530"><a href="#build-530"><span class="linenos">530</span></a>                
</span><span id="build-531"><a href="#build-531"><span class="linenos">531</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="o">=</span> <span class="n">package_data</span>
</span><span id="build-532"><a href="#build-532"><span class="linenos">532</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="o">=</span> <span class="n">result_ext_modules</span>
</span><span id="build-533"><a href="#build-533"><span class="linenos">533</span></a>
</span><span id="build-534"><a href="#build-534"><span class="linenos">534</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build-535"><a href="#build-535"><span class="linenos">535</span></a>                    <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="build-536"><a href="#build-536"><span class="linenos">536</span></a>                    <span class="nb">print</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Setuptools internal actions are organized using a <em>command design pattern</em>.
This means that each action (or group of closely related actions) executed during
the build should be implemented as a <code>Command</code> subclass.</p>

<p>These commands are abstractions and do not necessarily correspond to a command that
can (or should) be executed via a terminal, in a CLI fashion (although historically
they would).</p>

<p>When creating a new command from scratch, custom defined classes <strong>SHOULD</strong> inherit
from <code>setuptools.Command</code> and implement a few mandatory methods.
Between these mandatory methods, are listed:</p>

<p>.. method:: initialize_options(self)</p>

<pre><code>Set or (reset) all options/attributes/caches used by the command
to their default values. Note that these values may be overwritten during
the build.
</code></pre>

<p>.. method:: finalize_options(self)</p>

<pre><code>Set final values for all options/attributes used by the command.
Most of the time, each option/attribute/cache should only be set if it does not
have any value yet (e.g. ``if self.attr is None: self.attr = val``).
</code></pre>

<p>.. method:: run(self)</p>

<pre><code>Execute the actions intended by the command.
(Side effects **SHOULD** only take place when ``run`` is executed,
for example, creating new files or writing to the terminal output).
</code></pre>

<p>A useful analogy for command classes is to think of them as subroutines with local
variables called "options".  The options are "declared" in <code><a href="#build.initialize_options">initialize_options()</a></code>
and "defined" (given their final values, aka "finalized") in <code><a href="#build.finalize_options">finalize_options()</a></code>,
both of which must be defined by every command class. The "body" of the subroutine,
(where it does all the work) is the <code><a href="#build.run">run()</a></code> method.
Between <code><a href="#build.initialize_options">initialize_options()</a></code> and <code><a href="#build.finalize_options">finalize_options()</a></code>, <code>setuptools</code> may set
the values for options/attributes based on user's input (or circumstance),
which means that the implementation should be careful to not overwrite values in
<code><a href="#build.finalize_options">finalize_options</a></code> unless necessary.</p>

<p>Please note that other commands (or other parts of setuptools) may also overwrite
the values of the command's options/attributes multiple times during the build
process.
Therefore it is important to consistently implement <code><a href="#build.initialize_options">initialize_options()</a></code> and
<code><a href="#build.finalize_options">finalize_options()</a></code>. For example, all derived attributes (or attributes that
depend on the value of other attributes) <strong>SHOULD</strong> be recomputed in
<code><a href="#build.finalize_options">finalize_options</a></code>.</p>

<p>When overwriting existing commands, custom defined classes <strong>MUST</strong> abide by the
same APIs implemented by the original class. They also <strong>SHOULD</strong> inherit from the
original class.</p>
</div>


                            <div id="build.__init__" class="classattr">
                                        <input id="build.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">build</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">dist</span><span class="p">:</span> <span class="n">setuptools</span><span class="o">.</span><span class="n">_distutils</span><span class="o">.</span><span class="n">dist</span><span class="o">.</span><span class="n">Distribution</span>,</span><span class="param">	<span class="n">build_config</span><span class="p">:</span> <span class="n"><a href="#BuildConfig">BuildConfig</a></span></span>)</span>

                <label class="view-source-button" for="build.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#build.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="build.__init__-466"><a href="#build.__init__-466"><span class="linenos">466</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build.__init__-467"><a href="#build.__init__-467"><span class="linenos">467</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="build.__init__-468"><a href="#build.__init__-468"><span class="linenos">468</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Construct the command for dist, updating
vars(self) with any keyword parameters.</p>
</div>


                            </div>
                            <div id="build.build_config" class="classattr">
                                <div class="attr variable">
            <span class="name">build_config</span><span class="annotation">: <a href="#BuildConfig">BuildConfig</a></span>

        
    </div>
    <a class="headerlink" href="#build.build_config"></a>
    
    

                            </div>
                            <div id="build.finalize_options" class="classattr">
                                        <input id="build.finalize_options-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">finalize_options</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="build.finalize_options-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#build.finalize_options"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="build.finalize_options-470"><a href="#build.finalize_options-470"><span class="linenos">470</span></a>    <span class="k">def</span> <span class="nf">finalize_options</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="build.finalize_options-471"><a href="#build.finalize_options-471"><span class="linenos">471</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="build.finalize_options-472"><a href="#build.finalize_options-472"><span class="linenos">472</span></a>            <span class="n">setuptools_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)]</span>
</span><span id="build.finalize_options-473"><a href="#build.finalize_options-473"><span class="linenos">473</span></a>            <span class="n">cython_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)]</span>
</span><span id="build.finalize_options-474"><a href="#build.finalize_options-474"><span class="linenos">474</span></a>            <span class="n">cengal_extensions</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">)))</span>
</span><span id="build.finalize_options-475"><a href="#build.finalize_options-475"><span class="linenos">475</span></a>            <span class="n">cengal_result_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span><span class="p">()</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions</span><span class="p">]</span>
</span><span id="build.finalize_options-476"><a href="#build.finalize_options-476"><span class="linenos">476</span></a>            <span class="n">setuptools_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)])</span>
</span><span id="build.finalize_options-477"><a href="#build.finalize_options-477"><span class="linenos">477</span></a>            <span class="n">cython_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)])</span>
</span><span id="build.finalize_options-478"><a href="#build.finalize_options-478"><span class="linenos">478</span></a>            <span class="n">cengal_extensions_store_as_data</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">))</span>
</span><span id="build.finalize_options-479"><a href="#build.finalize_options-479"><span class="linenos">479</span></a>
</span><span id="build.finalize_options-480"><a href="#build.finalize_options-480"><span class="linenos">480</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build.finalize_options-481"><a href="#build.finalize_options-481"><span class="linenos">481</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="build.finalize_options-482"><a href="#build.finalize_options-482"><span class="linenos">482</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="build.finalize_options-483"><a href="#build.finalize_options-483"><span class="linenos">483</span></a>        
</span><span id="build.finalize_options-484"><a href="#build.finalize_options-484"><span class="linenos">484</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">finalize_options</span><span class="p">()</span>
</span><span id="build.finalize_options-485"><a href="#build.finalize_options-485"><span class="linenos">485</span></a>
</span><span id="build.finalize_options-486"><a href="#build.finalize_options-486"><span class="linenos">486</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="build.finalize_options-487"><a href="#build.finalize_options-487"><span class="linenos">487</span></a>            <span class="n">package_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="build.finalize_options-488"><a href="#build.finalize_options-488"><span class="linenos">488</span></a>            
</span><span id="build.finalize_options-489"><a href="#build.finalize_options-489"><span class="linenos">489</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build.finalize_options-490"><a href="#build.finalize_options-490"><span class="linenos">490</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions_store_as_data</span><span class="p">:</span>
</span><span id="build.finalize_options-491"><a href="#build.finalize_options-491"><span class="linenos">491</span></a>                    <span class="n">files</span> <span class="o">=</span> <span class="n">ext</span><span class="p">()</span>
</span><span id="build.finalize_options-492"><a href="#build.finalize_options-492"><span class="linenos">492</span></a>                    <span class="k">if</span> <span class="n">files</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build.finalize_options-493"><a href="#build.finalize_options-493"><span class="linenos">493</span></a>                        <span class="k">continue</span>
</span><span id="build.finalize_options-494"><a href="#build.finalize_options-494"><span class="linenos">494</span></a>
</span><span id="build.finalize_options-495"><a href="#build.finalize_options-495"><span class="linenos">495</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">package</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">package_data</span><span class="p">:</span>
</span><span id="build.finalize_options-496"><a href="#build.finalize_options-496"><span class="linenos">496</span></a>                        <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build.finalize_options-497"><a href="#build.finalize_options-497"><span class="linenos">497</span></a>                    
</span><span id="build.finalize_options-498"><a href="#build.finalize_options-498"><span class="linenos">498</span></a>                    <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">files</span><span class="p">)</span>
</span><span id="build.finalize_options-499"><a href="#build.finalize_options-499"><span class="linenos">499</span></a>
</span><span id="build.finalize_options-500"><a href="#build.finalize_options-500"><span class="linenos">500</span></a>                <span class="kn">from</span> <span class="nn">Cython.Build</span> <span class="kn">import</span> <span class="n">cythonize</span>
</span><span id="build.finalize_options-501"><a href="#build.finalize_options-501"><span class="linenos">501</span></a>                <span class="n">result_ext_modules</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build.finalize_options-502"><a href="#build.finalize_options-502"><span class="linenos">502</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="build.finalize_options-503"><a href="#build.finalize_options-503"><span class="linenos">503</span></a>                    <span class="n">cwd_before_cythonize</span> <span class="o">=</span> <span class="n">getcwd</span><span class="p">()</span>
</span><span id="build.finalize_options-504"><a href="#build.finalize_options-504"><span class="linenos">504</span></a>                    <span class="n">pyx_flags_dict</span> <span class="o">=</span> <span class="n">prepare_pyx_flags_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">additional_pyx_flags</span><span class="p">)</span>
</span><span id="build.finalize_options-505"><a href="#build.finalize_options-505"><span class="linenos">505</span></a>                    <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">remove_header_files</span><span class="p">(</span>
</span><span id="build.finalize_options-506"><a href="#build.finalize_options-506"><span class="linenos">506</span></a>                        <span class="n">cythonize</span><span class="p">(</span><span class="n">process_macros</span><span class="p">(</span><span class="n">cython_extensions</span><span class="p">),</span>
</span><span id="build.finalize_options-507"><a href="#build.finalize_options-507"><span class="linenos">507</span></a>                        <span class="n">compiler_directives</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;language_level&#39;</span><span class="p">:</span> <span class="s1">&#39;3&#39;</span><span class="p">},</span>
</span><span id="build.finalize_options-508"><a href="#build.finalize_options-508"><span class="linenos">508</span></a>                        <span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">pyx_flags_dict</span><span class="p">,</span>
</span><span id="build.finalize_options-509"><a href="#build.finalize_options-509"><span class="linenos">509</span></a>                        <span class="p">)))</span>
</span><span id="build.finalize_options-510"><a href="#build.finalize_options-510"><span class="linenos">510</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="build.finalize_options-511"><a href="#build.finalize_options-511"><span class="linenos">511</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;DEBUG: </span><span class="si">{</span><span class="n">cwd_before_cythonize</span><span class="si">=}</span><span class="s1"> | </span><span class="si">{</span><span class="n">getcwd</span><span class="p">()</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="build.finalize_options-512"><a href="#build.finalize_options-512"><span class="linenos">512</span></a>                    <span class="k">for</span> <span class="n">extension</span> <span class="ow">in</span> <span class="n">cython_extensions</span><span class="p">:</span>
</span><span id="build.finalize_options-513"><a href="#build.finalize_options-513"><span class="linenos">513</span></a>                        <span class="n">pprint</span><span class="p">(</span><span class="n">class_properties_values_including_overrided</span><span class="p">(</span><span class="n">extension</span><span class="p">))</span>
</span><span id="build.finalize_options-514"><a href="#build.finalize_options-514"><span class="linenos">514</span></a>                    
</span><span id="build.finalize_options-515"><a href="#build.finalize_options-515"><span class="linenos">515</span></a>                    <span class="k">raise</span>
</span><span id="build.finalize_options-516"><a href="#build.finalize_options-516"><span class="linenos">516</span></a>                
</span><span id="build.finalize_options-517"><a href="#build.finalize_options-517"><span class="linenos">517</span></a>                <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">setuptools_extensions</span><span class="p">)</span>
</span><span id="build.finalize_options-518"><a href="#build.finalize_options-518"><span class="linenos">518</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">result_ext_modules</span><span class="p">:</span>
</span><span id="build.finalize_options-519"><a href="#build.finalize_options-519"><span class="linenos">519</span></a>                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="s1">&#39;extra_compile_args&#39;</span><span class="p">):</span>
</span><span id="build.finalize_options-520"><a href="#build.finalize_options-520"><span class="linenos">520</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build.finalize_options-521"><a href="#build.finalize_options-521"><span class="linenos">521</span></a>                    
</span><span id="build.finalize_options-522"><a href="#build.finalize_options-522"><span class="linenos">522</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build.finalize_options-523"><a href="#build.finalize_options-523"><span class="linenos">523</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build.finalize_options-524"><a href="#build.finalize_options-524"><span class="linenos">524</span></a>                    
</span><span id="build.finalize_options-525"><a href="#build.finalize_options-525"><span class="linenos">525</span></a>                    <span class="k">if</span> <span class="s1">&#39;Darwin&#39;</span> <span class="o">==</span> <span class="n">OS_TYPE</span><span class="p">:</span>
</span><span id="build.finalize_options-526"><a href="#build.finalize_options-526"><span class="linenos">526</span></a>                        <span class="k">if</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_x86</span><span class="p">:</span>
</span><span id="build.finalize_options-527"><a href="#build.finalize_options-527"><span class="linenos">527</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;x86_64&#39;</span><span class="p">]</span>
</span><span id="build.finalize_options-528"><a href="#build.finalize_options-528"><span class="linenos">528</span></a>                        <span class="k">elif</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_arm</span><span class="p">:</span>
</span><span id="build.finalize_options-529"><a href="#build.finalize_options-529"><span class="linenos">529</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;arm64&#39;</span><span class="p">]</span>
</span><span id="build.finalize_options-530"><a href="#build.finalize_options-530"><span class="linenos">530</span></a>                
</span><span id="build.finalize_options-531"><a href="#build.finalize_options-531"><span class="linenos">531</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="o">=</span> <span class="n">package_data</span>
</span><span id="build.finalize_options-532"><a href="#build.finalize_options-532"><span class="linenos">532</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="o">=</span> <span class="n">result_ext_modules</span>
</span><span id="build.finalize_options-533"><a href="#build.finalize_options-533"><span class="linenos">533</span></a>
</span><span id="build.finalize_options-534"><a href="#build.finalize_options-534"><span class="linenos">534</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build.finalize_options-535"><a href="#build.finalize_options-535"><span class="linenos">535</span></a>                    <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="build.finalize_options-536"><a href="#build.finalize_options-536"><span class="linenos">536</span></a>                    <span class="nb">print</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Set final values for all the options that this command supports.
This is always called as late as possible, ie.  after any option
assignments from the command-line or from other commands have been
done.  Thus, this is the place to code option dependencies: if
'foo' depends on 'bar', then it is safe to set 'foo' from 'bar' as
long as 'foo' still has the same value it was assigned in
'initialize_options()'.</p>

<p>This method must be implemented by all command classes.</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>distutils.command.build.build</dt>
                                <dd id="build.description" class="variable">description</dd>
                <dd id="build.user_options" class="variable">user_options</dd>
                <dd id="build.boolean_options" class="variable">boolean_options</dd>
                <dd id="build.help_options" class="variable">help_options</dd>
                <dd id="build.initialize_options" class="function">initialize_options</dd>
                <dd id="build.run" class="function">run</dd>
                <dd id="build.has_pure_modules" class="function">has_pure_modules</dd>
                <dd id="build.has_c_libraries" class="function">has_c_libraries</dd>
                <dd id="build.has_ext_modules" class="function">has_ext_modules</dd>
                <dd id="build.has_scripts" class="function">has_scripts</dd>
                <dd id="build.sub_commands" class="variable">sub_commands</dd>

            </div>
            <div><dt>setuptools.Command</dt>
                                <dd id="build.command_consumes_arguments" class="variable">command_consumes_arguments</dd>
                <dd id="build.ensure_string_list" class="function">ensure_string_list</dd>
                <dd id="build.reinitialize_command" class="function">reinitialize_command</dd>

            </div>
            <div><dt>distutils.cmd.Command</dt>
                                <dd id="build.distribution" class="variable">distribution</dd>
                <dd id="build.verbose" class="variable">verbose</dd>
                <dd id="build.force" class="variable">force</dd>
                <dd id="build.help" class="variable">help</dd>
                <dd id="build.finalized" class="variable">finalized</dd>
                <dd id="build.ensure_finalized" class="function">ensure_finalized</dd>
                <dd id="build.dump_options" class="function">dump_options</dd>
                <dd id="build.announce" class="function">announce</dd>
                <dd id="build.debug_print" class="function">debug_print</dd>
                <dd id="build.ensure_string" class="function">ensure_string</dd>
                <dd id="build.ensure_filename" class="function">ensure_filename</dd>
                <dd id="build.ensure_dirname" class="function">ensure_dirname</dd>
                <dd id="build.get_command_name" class="function">get_command_name</dd>
                <dd id="build.set_undefined_options" class="function">set_undefined_options</dd>
                <dd id="build.get_finalized_command" class="function">get_finalized_command</dd>
                <dd id="build.run_command" class="function">run_command</dd>
                <dd id="build.get_sub_commands" class="function">get_sub_commands</dd>
                <dd id="build.warn" class="function">warn</dd>
                <dd id="build.execute" class="function">execute</dd>
                <dd id="build.mkpath" class="function">mkpath</dd>
                <dd id="build.copy_file" class="function">copy_file</dd>
                <dd id="build.copy_tree" class="function">copy_tree</dd>
                <dd id="build.move_file" class="function">move_file</dd>
                <dd id="build.spawn" class="function">spawn</dd>
                <dd id="build.make_archive" class="function">make_archive</dd>
                <dd id="build.make_file" class="function">make_file</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="build_ext">
                            <input id="build_ext-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">build_ext</span><wbr>(<span class="base">distutils.command.build_ext.build_ext</span>):

                <label class="view-source-button" for="build_ext-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#build_ext"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="build_ext-539"><a href="#build_ext-539"><span class="linenos">539</span></a><span class="k">class</span> <span class="nc">build_ext</span><span class="p">(</span><span class="n">build_ext_orig</span><span class="p">):</span>
</span><span id="build_ext-540"><a href="#build_ext-540"><span class="linenos">540</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build_ext-541"><a href="#build_ext-541"><span class="linenos">541</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="build_ext-542"><a href="#build_ext-542"><span class="linenos">542</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span><span id="build_ext-543"><a href="#build_ext-543"><span class="linenos">543</span></a>
</span><span id="build_ext-544"><a href="#build_ext-544"><span class="linenos">544</span></a>    <span class="k">def</span> <span class="nf">finalize_options</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="build_ext-545"><a href="#build_ext-545"><span class="linenos">545</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="build_ext-546"><a href="#build_ext-546"><span class="linenos">546</span></a>            <span class="n">setuptools_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)]</span>
</span><span id="build_ext-547"><a href="#build_ext-547"><span class="linenos">547</span></a>            <span class="n">cython_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)]</span>
</span><span id="build_ext-548"><a href="#build_ext-548"><span class="linenos">548</span></a>            <span class="n">cengal_extensions</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">)))</span>
</span><span id="build_ext-549"><a href="#build_ext-549"><span class="linenos">549</span></a>            <span class="n">cengal_result_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span><span class="p">()</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions</span><span class="p">]</span>
</span><span id="build_ext-550"><a href="#build_ext-550"><span class="linenos">550</span></a>            <span class="n">setuptools_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)])</span>
</span><span id="build_ext-551"><a href="#build_ext-551"><span class="linenos">551</span></a>            <span class="n">cython_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)])</span>
</span><span id="build_ext-552"><a href="#build_ext-552"><span class="linenos">552</span></a>            <span class="n">cengal_extensions_store_as_data</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">))</span>
</span><span id="build_ext-553"><a href="#build_ext-553"><span class="linenos">553</span></a>
</span><span id="build_ext-554"><a href="#build_ext-554"><span class="linenos">554</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build_ext-555"><a href="#build_ext-555"><span class="linenos">555</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="build_ext-556"><a href="#build_ext-556"><span class="linenos">556</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="build_ext-557"><a href="#build_ext-557"><span class="linenos">557</span></a>        
</span><span id="build_ext-558"><a href="#build_ext-558"><span class="linenos">558</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">finalize_options</span><span class="p">()</span>
</span><span id="build_ext-559"><a href="#build_ext-559"><span class="linenos">559</span></a>
</span><span id="build_ext-560"><a href="#build_ext-560"><span class="linenos">560</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="build_ext-561"><a href="#build_ext-561"><span class="linenos">561</span></a>            <span class="n">package_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="build_ext-562"><a href="#build_ext-562"><span class="linenos">562</span></a>            
</span><span id="build_ext-563"><a href="#build_ext-563"><span class="linenos">563</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build_ext-564"><a href="#build_ext-564"><span class="linenos">564</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions_store_as_data</span><span class="p">:</span>
</span><span id="build_ext-565"><a href="#build_ext-565"><span class="linenos">565</span></a>                    <span class="n">files</span> <span class="o">=</span> <span class="n">ext</span><span class="p">()</span>
</span><span id="build_ext-566"><a href="#build_ext-566"><span class="linenos">566</span></a>                    <span class="k">if</span> <span class="n">files</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build_ext-567"><a href="#build_ext-567"><span class="linenos">567</span></a>                        <span class="k">continue</span>
</span><span id="build_ext-568"><a href="#build_ext-568"><span class="linenos">568</span></a>
</span><span id="build_ext-569"><a href="#build_ext-569"><span class="linenos">569</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">package</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">package_data</span><span class="p">:</span>
</span><span id="build_ext-570"><a href="#build_ext-570"><span class="linenos">570</span></a>                        <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build_ext-571"><a href="#build_ext-571"><span class="linenos">571</span></a>                    
</span><span id="build_ext-572"><a href="#build_ext-572"><span class="linenos">572</span></a>                    <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">files</span><span class="p">)</span>
</span><span id="build_ext-573"><a href="#build_ext-573"><span class="linenos">573</span></a>
</span><span id="build_ext-574"><a href="#build_ext-574"><span class="linenos">574</span></a>                <span class="kn">from</span> <span class="nn">Cython.Build</span> <span class="kn">import</span> <span class="n">cythonize</span>
</span><span id="build_ext-575"><a href="#build_ext-575"><span class="linenos">575</span></a>                <span class="n">result_ext_modules</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build_ext-576"><a href="#build_ext-576"><span class="linenos">576</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="build_ext-577"><a href="#build_ext-577"><span class="linenos">577</span></a>                    <span class="n">cwd_before_cythonize</span> <span class="o">=</span> <span class="n">getcwd</span><span class="p">()</span>
</span><span id="build_ext-578"><a href="#build_ext-578"><span class="linenos">578</span></a>                    <span class="n">pyx_flags_dict</span> <span class="o">=</span> <span class="n">prepare_pyx_flags_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">additional_pyx_flags</span><span class="p">)</span>
</span><span id="build_ext-579"><a href="#build_ext-579"><span class="linenos">579</span></a>                    <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">remove_header_files</span><span class="p">(</span>
</span><span id="build_ext-580"><a href="#build_ext-580"><span class="linenos">580</span></a>                        <span class="n">cythonize</span><span class="p">(</span><span class="n">process_macros</span><span class="p">(</span><span class="n">cython_extensions</span><span class="p">),</span>
</span><span id="build_ext-581"><a href="#build_ext-581"><span class="linenos">581</span></a>                        <span class="n">compiler_directives</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;language_level&#39;</span><span class="p">:</span> <span class="s1">&#39;3&#39;</span><span class="p">},</span>
</span><span id="build_ext-582"><a href="#build_ext-582"><span class="linenos">582</span></a>                        <span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">pyx_flags_dict</span><span class="p">,</span>
</span><span id="build_ext-583"><a href="#build_ext-583"><span class="linenos">583</span></a>                        <span class="p">)))</span>
</span><span id="build_ext-584"><a href="#build_ext-584"><span class="linenos">584</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="build_ext-585"><a href="#build_ext-585"><span class="linenos">585</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;DEBUG: </span><span class="si">{</span><span class="n">cwd_before_cythonize</span><span class="si">=}</span><span class="s1"> | </span><span class="si">{</span><span class="n">getcwd</span><span class="p">()</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="build_ext-586"><a href="#build_ext-586"><span class="linenos">586</span></a>                    <span class="k">for</span> <span class="n">extension</span> <span class="ow">in</span> <span class="n">cython_extensions</span><span class="p">:</span>
</span><span id="build_ext-587"><a href="#build_ext-587"><span class="linenos">587</span></a>                        <span class="n">pprint</span><span class="p">(</span><span class="n">class_properties_values_including_overrided</span><span class="p">(</span><span class="n">extension</span><span class="p">))</span>
</span><span id="build_ext-588"><a href="#build_ext-588"><span class="linenos">588</span></a>                    
</span><span id="build_ext-589"><a href="#build_ext-589"><span class="linenos">589</span></a>                    <span class="k">raise</span>
</span><span id="build_ext-590"><a href="#build_ext-590"><span class="linenos">590</span></a>                
</span><span id="build_ext-591"><a href="#build_ext-591"><span class="linenos">591</span></a>                <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">setuptools_extensions</span><span class="p">)</span>
</span><span id="build_ext-592"><a href="#build_ext-592"><span class="linenos">592</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">result_ext_modules</span><span class="p">:</span>
</span><span id="build_ext-593"><a href="#build_ext-593"><span class="linenos">593</span></a>                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="s1">&#39;extra_compile_args&#39;</span><span class="p">):</span>
</span><span id="build_ext-594"><a href="#build_ext-594"><span class="linenos">594</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build_ext-595"><a href="#build_ext-595"><span class="linenos">595</span></a>                    
</span><span id="build_ext-596"><a href="#build_ext-596"><span class="linenos">596</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build_ext-597"><a href="#build_ext-597"><span class="linenos">597</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build_ext-598"><a href="#build_ext-598"><span class="linenos">598</span></a>                    
</span><span id="build_ext-599"><a href="#build_ext-599"><span class="linenos">599</span></a>                    <span class="k">if</span> <span class="s1">&#39;Darwin&#39;</span> <span class="o">==</span> <span class="n">OS_TYPE</span><span class="p">:</span>
</span><span id="build_ext-600"><a href="#build_ext-600"><span class="linenos">600</span></a>                        <span class="k">if</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_x86</span><span class="p">:</span>
</span><span id="build_ext-601"><a href="#build_ext-601"><span class="linenos">601</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;x86_64&#39;</span><span class="p">]</span>
</span><span id="build_ext-602"><a href="#build_ext-602"><span class="linenos">602</span></a>                        <span class="k">elif</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_arm</span><span class="p">:</span>
</span><span id="build_ext-603"><a href="#build_ext-603"><span class="linenos">603</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;arm64&#39;</span><span class="p">]</span>
</span><span id="build_ext-604"><a href="#build_ext-604"><span class="linenos">604</span></a>                
</span><span id="build_ext-605"><a href="#build_ext-605"><span class="linenos">605</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="o">=</span> <span class="n">package_data</span>
</span><span id="build_ext-606"><a href="#build_ext-606"><span class="linenos">606</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="o">=</span> <span class="n">result_ext_modules</span>
</span><span id="build_ext-607"><a href="#build_ext-607"><span class="linenos">607</span></a>
</span><span id="build_ext-608"><a href="#build_ext-608"><span class="linenos">608</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build_ext-609"><a href="#build_ext-609"><span class="linenos">609</span></a>                    <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="build_ext-610"><a href="#build_ext-610"><span class="linenos">610</span></a>                    <span class="nb">print</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Setuptools internal actions are organized using a <em>command design pattern</em>.
This means that each action (or group of closely related actions) executed during
the build should be implemented as a <code>Command</code> subclass.</p>

<p>These commands are abstractions and do not necessarily correspond to a command that
can (or should) be executed via a terminal, in a CLI fashion (although historically
they would).</p>

<p>When creating a new command from scratch, custom defined classes <strong>SHOULD</strong> inherit
from <code>setuptools.Command</code> and implement a few mandatory methods.
Between these mandatory methods, are listed:</p>

<p>.. method:: initialize_options(self)</p>

<pre><code>Set or (reset) all options/attributes/caches used by the command
to their default values. Note that these values may be overwritten during
the build.
</code></pre>

<p>.. method:: finalize_options(self)</p>

<pre><code>Set final values for all options/attributes used by the command.
Most of the time, each option/attribute/cache should only be set if it does not
have any value yet (e.g. ``if self.attr is None: self.attr = val``).
</code></pre>

<p>.. method:: run(self)</p>

<pre><code>Execute the actions intended by the command.
(Side effects **SHOULD** only take place when ``run`` is executed,
for example, creating new files or writing to the terminal output).
</code></pre>

<p>A useful analogy for command classes is to think of them as subroutines with local
variables called "options".  The options are "declared" in <code><a href="#build_ext.initialize_options">initialize_options()</a></code>
and "defined" (given their final values, aka "finalized") in <code><a href="#build_ext.finalize_options">finalize_options()</a></code>,
both of which must be defined by every command class. The "body" of the subroutine,
(where it does all the work) is the <code><a href="#build_ext.run">run()</a></code> method.
Between <code><a href="#build_ext.initialize_options">initialize_options()</a></code> and <code><a href="#build_ext.finalize_options">finalize_options()</a></code>, <code>setuptools</code> may set
the values for options/attributes based on user's input (or circumstance),
which means that the implementation should be careful to not overwrite values in
<code><a href="#build_ext.finalize_options">finalize_options</a></code> unless necessary.</p>

<p>Please note that other commands (or other parts of setuptools) may also overwrite
the values of the command's options/attributes multiple times during the build
process.
Therefore it is important to consistently implement <code><a href="#build_ext.initialize_options">initialize_options()</a></code> and
<code><a href="#build_ext.finalize_options">finalize_options()</a></code>. For example, all derived attributes (or attributes that
depend on the value of other attributes) <strong>SHOULD</strong> be recomputed in
<code><a href="#build_ext.finalize_options">finalize_options</a></code>.</p>

<p>When overwriting existing commands, custom defined classes <strong>MUST</strong> abide by the
same APIs implemented by the original class. They also <strong>SHOULD</strong> inherit from the
original class.</p>
</div>


                            <div id="build_ext.__init__" class="classattr">
                                        <input id="build_ext.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">build_ext</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">dist</span><span class="p">:</span> <span class="n">setuptools</span><span class="o">.</span><span class="n">_distutils</span><span class="o">.</span><span class="n">dist</span><span class="o">.</span><span class="n">Distribution</span>,</span><span class="param">	<span class="n">build_config</span><span class="p">:</span> <span class="n"><a href="#BuildConfig">BuildConfig</a></span></span>)</span>

                <label class="view-source-button" for="build_ext.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#build_ext.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="build_ext.__init__-540"><a href="#build_ext.__init__-540"><span class="linenos">540</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dist</span><span class="p">:</span> <span class="n">Distribution</span><span class="p">,</span> <span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build_ext.__init__-541"><a href="#build_ext.__init__-541"><span class="linenos">541</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="p">:</span> <span class="n">BuildConfig</span> <span class="o">=</span> <span class="n">build_config</span>
</span><span id="build_ext.__init__-542"><a href="#build_ext.__init__-542"><span class="linenos">542</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dist</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Construct the command for dist, updating
vars(self) with any keyword parameters.</p>
</div>


                            </div>
                            <div id="build_ext.build_config" class="classattr">
                                <div class="attr variable">
            <span class="name">build_config</span><span class="annotation">: <a href="#BuildConfig">BuildConfig</a></span>

        
    </div>
    <a class="headerlink" href="#build_ext.build_config"></a>
    
    

                            </div>
                            <div id="build_ext.finalize_options" class="classattr">
                                        <input id="build_ext.finalize_options-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">finalize_options</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="build_ext.finalize_options-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#build_ext.finalize_options"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="build_ext.finalize_options-544"><a href="#build_ext.finalize_options-544"><span class="linenos">544</span></a>    <span class="k">def</span> <span class="nf">finalize_options</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="build_ext.finalize_options-545"><a href="#build_ext.finalize_options-545"><span class="linenos">545</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="build_ext.finalize_options-546"><a href="#build_ext.finalize_options-546"><span class="linenos">546</span></a>            <span class="n">setuptools_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)]</span>
</span><span id="build_ext.finalize_options-547"><a href="#build_ext.finalize_options-547"><span class="linenos">547</span></a>            <span class="n">cython_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)]</span>
</span><span id="build_ext.finalize_options-548"><a href="#build_ext.finalize_options-548"><span class="linenos">548</span></a>            <span class="n">cengal_extensions</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">)))</span>
</span><span id="build_ext.finalize_options-549"><a href="#build_ext.finalize_options-549"><span class="linenos">549</span></a>            <span class="n">cengal_result_extensions</span> <span class="o">=</span> <span class="p">[</span><span class="n">ext</span><span class="p">()</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions</span><span class="p">]</span>
</span><span id="build_ext.finalize_options-550"><a href="#build_ext.finalize_options-550"><span class="linenos">550</span></a>            <span class="n">setuptools_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">SetuptoolsExtension</span><span class="p">)])</span>
</span><span id="build_ext.finalize_options-551"><a href="#build_ext.finalize_options-551"><span class="linenos">551</span></a>            <span class="n">cython_extensions</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_result_extensions</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CythonExtension</span><span class="p">)])</span>
</span><span id="build_ext.finalize_options-552"><a href="#build_ext.finalize_options-552"><span class="linenos">552</span></a>            <span class="n">cengal_extensions_store_as_data</span> <span class="o">=</span> <span class="p">(</span><span class="n">ext</span> <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="k">if</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="n">CengalBuildExtension</span><span class="p">)</span> <span class="ow">and</span> <span class="n">ext</span><span class="o">.</span><span class="n">store_as_data</span><span class="p">))</span>
</span><span id="build_ext.finalize_options-553"><a href="#build_ext.finalize_options-553"><span class="linenos">553</span></a>
</span><span id="build_ext.finalize_options-554"><a href="#build_ext.finalize_options-554"><span class="linenos">554</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-555"><a href="#build_ext.finalize_options-555"><span class="linenos">555</span></a>                <span class="kn">import</span> <span class="nn">debugpy</span>
</span><span id="build_ext.finalize_options-556"><a href="#build_ext.finalize_options-556"><span class="linenos">556</span></a>                <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-557"><a href="#build_ext.finalize_options-557"><span class="linenos">557</span></a>        
</span><span id="build_ext.finalize_options-558"><a href="#build_ext.finalize_options-558"><span class="linenos">558</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">finalize_options</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-559"><a href="#build_ext.finalize_options-559"><span class="linenos">559</span></a>
</span><span id="build_ext.finalize_options-560"><a href="#build_ext.finalize_options-560"><span class="linenos">560</span></a>        <span class="k">with</span> <span class="n">secure_current_dir</span><span class="p">():</span>
</span><span id="build_ext.finalize_options-561"><a href="#build_ext.finalize_options-561"><span class="linenos">561</span></a>            <span class="n">package_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-562"><a href="#build_ext.finalize_options-562"><span class="linenos">562</span></a>            
</span><span id="build_ext.finalize_options-563"><a href="#build_ext.finalize_options-563"><span class="linenos">563</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_sdist_mode</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-564"><a href="#build_ext.finalize_options-564"><span class="linenos">564</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">cengal_extensions_store_as_data</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-565"><a href="#build_ext.finalize_options-565"><span class="linenos">565</span></a>                    <span class="n">files</span> <span class="o">=</span> <span class="n">ext</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-566"><a href="#build_ext.finalize_options-566"><span class="linenos">566</span></a>                    <span class="k">if</span> <span class="n">files</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-567"><a href="#build_ext.finalize_options-567"><span class="linenos">567</span></a>                        <span class="k">continue</span>
</span><span id="build_ext.finalize_options-568"><a href="#build_ext.finalize_options-568"><span class="linenos">568</span></a>
</span><span id="build_ext.finalize_options-569"><a href="#build_ext.finalize_options-569"><span class="linenos">569</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">package</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">package_data</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-570"><a href="#build_ext.finalize_options-570"><span class="linenos">570</span></a>                        <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-571"><a href="#build_ext.finalize_options-571"><span class="linenos">571</span></a>                    
</span><span id="build_ext.finalize_options-572"><a href="#build_ext.finalize_options-572"><span class="linenos">572</span></a>                    <span class="n">package_data</span><span class="p">[</span><span class="n">ext</span><span class="o">.</span><span class="n">package</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">files</span><span class="p">)</span>
</span><span id="build_ext.finalize_options-573"><a href="#build_ext.finalize_options-573"><span class="linenos">573</span></a>
</span><span id="build_ext.finalize_options-574"><a href="#build_ext.finalize_options-574"><span class="linenos">574</span></a>                <span class="kn">from</span> <span class="nn">Cython.Build</span> <span class="kn">import</span> <span class="n">cythonize</span>
</span><span id="build_ext.finalize_options-575"><a href="#build_ext.finalize_options-575"><span class="linenos">575</span></a>                <span class="n">result_ext_modules</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-576"><a href="#build_ext.finalize_options-576"><span class="linenos">576</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-577"><a href="#build_ext.finalize_options-577"><span class="linenos">577</span></a>                    <span class="n">cwd_before_cythonize</span> <span class="o">=</span> <span class="n">getcwd</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-578"><a href="#build_ext.finalize_options-578"><span class="linenos">578</span></a>                    <span class="n">pyx_flags_dict</span> <span class="o">=</span> <span class="n">prepare_pyx_flags_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">additional_pyx_flags</span><span class="p">)</span>
</span><span id="build_ext.finalize_options-579"><a href="#build_ext.finalize_options-579"><span class="linenos">579</span></a>                    <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">remove_header_files</span><span class="p">(</span>
</span><span id="build_ext.finalize_options-580"><a href="#build_ext.finalize_options-580"><span class="linenos">580</span></a>                        <span class="n">cythonize</span><span class="p">(</span><span class="n">process_macros</span><span class="p">(</span><span class="n">cython_extensions</span><span class="p">),</span>
</span><span id="build_ext.finalize_options-581"><a href="#build_ext.finalize_options-581"><span class="linenos">581</span></a>                        <span class="n">compiler_directives</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;language_level&#39;</span><span class="p">:</span> <span class="s1">&#39;3&#39;</span><span class="p">},</span>
</span><span id="build_ext.finalize_options-582"><a href="#build_ext.finalize_options-582"><span class="linenos">582</span></a>                        <span class="n">compile_time_env</span> <span class="o">=</span> <span class="n">pyx_flags_dict</span><span class="p">,</span>
</span><span id="build_ext.finalize_options-583"><a href="#build_ext.finalize_options-583"><span class="linenos">583</span></a>                        <span class="p">)))</span>
</span><span id="build_ext.finalize_options-584"><a href="#build_ext.finalize_options-584"><span class="linenos">584</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-585"><a href="#build_ext.finalize_options-585"><span class="linenos">585</span></a>                    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;DEBUG: </span><span class="si">{</span><span class="n">cwd_before_cythonize</span><span class="si">=}</span><span class="s1"> | </span><span class="si">{</span><span class="n">getcwd</span><span class="p">()</span><span class="si">=}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="build_ext.finalize_options-586"><a href="#build_ext.finalize_options-586"><span class="linenos">586</span></a>                    <span class="k">for</span> <span class="n">extension</span> <span class="ow">in</span> <span class="n">cython_extensions</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-587"><a href="#build_ext.finalize_options-587"><span class="linenos">587</span></a>                        <span class="n">pprint</span><span class="p">(</span><span class="n">class_properties_values_including_overrided</span><span class="p">(</span><span class="n">extension</span><span class="p">))</span>
</span><span id="build_ext.finalize_options-588"><a href="#build_ext.finalize_options-588"><span class="linenos">588</span></a>                    
</span><span id="build_ext.finalize_options-589"><a href="#build_ext.finalize_options-589"><span class="linenos">589</span></a>                    <span class="k">raise</span>
</span><span id="build_ext.finalize_options-590"><a href="#build_ext.finalize_options-590"><span class="linenos">590</span></a>                
</span><span id="build_ext.finalize_options-591"><a href="#build_ext.finalize_options-591"><span class="linenos">591</span></a>                <span class="n">result_ext_modules</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">setuptools_extensions</span><span class="p">)</span>
</span><span id="build_ext.finalize_options-592"><a href="#build_ext.finalize_options-592"><span class="linenos">592</span></a>                <span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">result_ext_modules</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-593"><a href="#build_ext.finalize_options-593"><span class="linenos">593</span></a>                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">ext</span><span class="p">,</span> <span class="s1">&#39;extra_compile_args&#39;</span><span class="p">):</span>
</span><span id="build_ext.finalize_options-594"><a href="#build_ext.finalize_options-594"><span class="linenos">594</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-595"><a href="#build_ext.finalize_options-595"><span class="linenos">595</span></a>                    
</span><span id="build_ext.finalize_options-596"><a href="#build_ext.finalize_options-596"><span class="linenos">596</span></a>                    <span class="k">if</span> <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-597"><a href="#build_ext.finalize_options-597"><span class="linenos">597</span></a>                        <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-598"><a href="#build_ext.finalize_options-598"><span class="linenos">598</span></a>                    
</span><span id="build_ext.finalize_options-599"><a href="#build_ext.finalize_options-599"><span class="linenos">599</span></a>                    <span class="k">if</span> <span class="s1">&#39;Darwin&#39;</span> <span class="o">==</span> <span class="n">OS_TYPE</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-600"><a href="#build_ext.finalize_options-600"><span class="linenos">600</span></a>                        <span class="k">if</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_x86</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-601"><a href="#build_ext.finalize_options-601"><span class="linenos">601</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;x86_64&#39;</span><span class="p">]</span>
</span><span id="build_ext.finalize_options-602"><a href="#build_ext.finalize_options-602"><span class="linenos">602</span></a>                        <span class="k">elif</span> <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">is_arm</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-603"><a href="#build_ext.finalize_options-603"><span class="linenos">603</span></a>                            <span class="n">ext</span><span class="o">.</span><span class="n">extra_compile_args</span> <span class="o">+=</span> <span class="p">[</span><span class="s1">&#39;-arch&#39;</span><span class="p">,</span> <span class="s1">&#39;arm64&#39;</span><span class="p">]</span>
</span><span id="build_ext.finalize_options-604"><a href="#build_ext.finalize_options-604"><span class="linenos">604</span></a>                
</span><span id="build_ext.finalize_options-605"><a href="#build_ext.finalize_options-605"><span class="linenos">605</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">package_data</span> <span class="o">=</span> <span class="n">package_data</span>
</span><span id="build_ext.finalize_options-606"><a href="#build_ext.finalize_options-606"><span class="linenos">606</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">distribution</span><span class="o">.</span><span class="n">ext_modules</span> <span class="o">=</span> <span class="n">result_ext_modules</span>
</span><span id="build_ext.finalize_options-607"><a href="#build_ext.finalize_options-607"><span class="linenos">607</span></a>
</span><span id="build_ext.finalize_options-608"><a href="#build_ext.finalize_options-608"><span class="linenos">608</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_config</span><span class="o">.</span><span class="n">package_build_is_in_debug_mode</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span>
</span><span id="build_ext.finalize_options-609"><a href="#build_ext.finalize_options-609"><span class="linenos">609</span></a>                    <span class="n">debugpy</span><span class="o">.</span><span class="n">breakpoint</span><span class="p">()</span>
</span><span id="build_ext.finalize_options-610"><a href="#build_ext.finalize_options-610"><span class="linenos">610</span></a>                    <span class="nb">print</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Set final values for all the options that this command supports.
This is always called as late as possible, ie.  after any option
assignments from the command-line or from other commands have been
done.  Thus, this is the place to code option dependencies: if
'foo' depends on 'bar', then it is safe to set 'foo' from 'bar' as
long as 'foo' still has the same value it was assigned in
'initialize_options()'.</p>

<p>This method must be implemented by all command classes.</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>distutils.command.build_ext.build_ext</dt>
                                <dd id="build_ext.description" class="variable">description</dd>
                <dd id="build_ext.sep_by" class="variable">sep_by</dd>
                <dd id="build_ext.user_options" class="variable">user_options</dd>
                <dd id="build_ext.boolean_options" class="variable">boolean_options</dd>
                <dd id="build_ext.help_options" class="variable">help_options</dd>
                <dd id="build_ext.initialize_options" class="function">initialize_options</dd>
                <dd id="build_ext.run" class="function">run</dd>
                <dd id="build_ext.check_extensions_list" class="function">check_extensions_list</dd>
                <dd id="build_ext.get_source_files" class="function">get_source_files</dd>
                <dd id="build_ext.get_outputs" class="function">get_outputs</dd>
                <dd id="build_ext.build_extensions" class="function">build_extensions</dd>
                <dd id="build_ext.build_extension" class="function">build_extension</dd>
                <dd id="build_ext.swig_sources" class="function">swig_sources</dd>
                <dd id="build_ext.find_swig" class="function">find_swig</dd>
                <dd id="build_ext.get_ext_fullpath" class="function">get_ext_fullpath</dd>
                <dd id="build_ext.get_ext_fullname" class="function">get_ext_fullname</dd>
                <dd id="build_ext.get_ext_filename" class="function">get_ext_filename</dd>
                <dd id="build_ext.get_export_symbols" class="function">get_export_symbols</dd>
                <dd id="build_ext.get_libraries" class="function">get_libraries</dd>

            </div>
            <div><dt>setuptools.Command</dt>
                                <dd id="build_ext.command_consumes_arguments" class="variable">command_consumes_arguments</dd>
                <dd id="build_ext.ensure_string_list" class="function">ensure_string_list</dd>
                <dd id="build_ext.reinitialize_command" class="function">reinitialize_command</dd>

            </div>
            <div><dt>distutils.cmd.Command</dt>
                                <dd id="build_ext.sub_commands" class="variable">sub_commands</dd>
                <dd id="build_ext.distribution" class="variable">distribution</dd>
                <dd id="build_ext.verbose" class="variable">verbose</dd>
                <dd id="build_ext.force" class="variable">force</dd>
                <dd id="build_ext.help" class="variable">help</dd>
                <dd id="build_ext.finalized" class="variable">finalized</dd>
                <dd id="build_ext.ensure_finalized" class="function">ensure_finalized</dd>
                <dd id="build_ext.dump_options" class="function">dump_options</dd>
                <dd id="build_ext.announce" class="function">announce</dd>
                <dd id="build_ext.debug_print" class="function">debug_print</dd>
                <dd id="build_ext.ensure_string" class="function">ensure_string</dd>
                <dd id="build_ext.ensure_filename" class="function">ensure_filename</dd>
                <dd id="build_ext.ensure_dirname" class="function">ensure_dirname</dd>
                <dd id="build_ext.get_command_name" class="function">get_command_name</dd>
                <dd id="build_ext.set_undefined_options" class="function">set_undefined_options</dd>
                <dd id="build_ext.get_finalized_command" class="function">get_finalized_command</dd>
                <dd id="build_ext.run_command" class="function">run_command</dd>
                <dd id="build_ext.get_sub_commands" class="function">get_sub_commands</dd>
                <dd id="build_ext.warn" class="function">warn</dd>
                <dd id="build_ext.execute" class="function">execute</dd>
                <dd id="build_ext.mkpath" class="function">mkpath</dd>
                <dd id="build_ext.copy_file" class="function">copy_file</dd>
                <dd id="build_ext.copy_tree" class="function">copy_tree</dd>
                <dd id="build_ext.move_file" class="function">move_file</dd>
                <dd id="build_ext.spawn" class="function">spawn</dd>
                <dd id="build_ext.make_archive" class="function">make_archive</dd>
                <dd id="build_ext.make_file" class="function">make_file</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>