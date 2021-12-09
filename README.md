# libmicrovmi - The approach to unite the VMI ecosystem

libmicrovmi - seminar paper repository

# Abstract

Virtual machine introspection (VMI) enables the monitoring of virtual machines (VMs) at runtime from the outside.
In the current VMI application landscape, there are already some software solutions (e.g. pyvmidbg, PANDA, PyREBox, Drakvuf, icebox) but most of them have been developed especially for one hypervisor.
The reason for this is that there was no library with which one could develop independently of the underlying virtual machine monitor or emulator.
Libmicrovmi tries to solve exactly this problem by providing a low-level core library, which aims to be cross-platform, hypervisor-agnostic, and emulator-agnostic. Existing VMI applications or other higher-level API's can rebase on top of it.
In this paper, we present the core functionality of libmicrovmi. 
In addition, we also draw a comparison with the de facto standard VMI library libVMI.
Finally, we also analyze the performance of these two libraries in comparison for 3 different use cases (memory dump, register dump, CR3 event). We implemented this by executing these tasks with a Python program, which measures and logs the time required for this. In order to make a statistical evaluation possible, we obtained 100 measured values for each task.

test: www.google.de , www.google.com, https://www.google.de, http://google.com, http://www.schwurbeldobl.de

test
