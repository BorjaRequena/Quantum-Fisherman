# Quantum Fisher(man)
> Quantum Fisher(man) project developed for the <a href='https://quantum-journal.org/papers/q-2020-05-25-269/pdf/'>IBM Qiskit Hackathon 2021](https://qiskithackathoneurope.bemyapp.com). We provide efficient ways to obtain the quantum Fisher information from quantum circuits, which allows the optimization through advanced techniques such as the [quantum natural gradient</a>, as well as to study the loss landscape of such circuits. 


## Quantum Fisher information

The Fisher information is a key metric widely used in physics and optimization. It has recently gathered great interest due to its applications in Machine Learning (ML), as it provides information about the local curvature of the Loss function, which can be leveraged to enhance vanilla gradient descent algorithms to perform [natural gradient](https://direct.mit.edu/neco/article/10/2/251/6143/Natural-Gradient-Works-Efficiently-in-Learning).

Its quantum version, the quantum Fisher information (QFI), plays a fundamental role in [multiple fields of quantum physics](https://arxiv.org/abs/2103.15191) such as quantum metrology, quantum information processing and quantum many-body physics. Furthermore, it lies at the core of recent quantum algorithms, such as the [quantum natural gradient](https://quantum-journal.org/papers/q-2020-05-25-269/pdf/), variational quantum imaginary time evolution or [quantum Boltzmann machines](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.8.021050).

However, the QFI is not directly related to any physical observable, which makes it very hard to measure. While fileds like quantum sensing or quantum machine learning would greatly benefit from it, its elevetaed cost makes it impractical to use in actual applications. 

## Efficient estimation of the quantum Fisher information

In many situations, we must rely on approximate methods to estimate the QFI in the most efficient way. Recent works have proposed stochastic methods to obtain the QFI focusing on variational quantum circuits (VQCs).

In this project, we build a Qiskit toolkit to implement, analyze and test such novel techniques to efficiently estimate the QFI. We focus on two methods [based on randomized measurements](https://arxiv.org/abs/2104.00519) and [simultaneous perturbation stochastic approximation (SPSA)](https://arxiv.org/abs/2103.09232).
