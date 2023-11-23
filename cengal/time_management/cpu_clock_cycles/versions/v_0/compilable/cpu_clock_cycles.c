// Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


#if defined(IS_X86)

#ifdef _MSC_VER

#include <intrin.h>

extern unsigned long long c_cpu_clock_cycles() {
    unsigned int ui;
    unsigned long long cycles = __rdtscp(&ui);
    return cycles;
}

#else

extern unsigned long long c_cpu_clock_cycles()
{
    unsigned long long result;
    asm volatile(
        "RDTSCP;"
        "SHLQ $32,%%rdx;"
        "ORQ %%rdx,%%rax;"
        "MOVQ %%rax,%0;"
        :"=r"(result)
        :
        :"rdx","rax", "rcx"
    );
    return result;
}

#endif

#elif defined(IS_ARM)

extern u64 c_cpu_clock_cycles()
{
    u64 result;
    asm volatile(
        "mrs %0, cntvct_el0"
        : "=r" (result)
    );

    return result;
}

#else

extern unsigned long long c_cpu_clock_cycles()
{
    return 0;
}

#endif