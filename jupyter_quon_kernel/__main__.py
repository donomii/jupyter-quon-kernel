from ipykernel.kernelapp import IPKernelApp
from .kernel import QuonKernel
IPKernelApp.launch_instance(kernel_class=QuonKernel)
