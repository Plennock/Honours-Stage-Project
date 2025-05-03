# QSafeML
Adapting the SafeML method of Machine learning safety monitoring, using quantum distance metrics to comptue the saftey and confidence of hybrid quantum-classical machine learning models.

## Description
The rise of machine learning in safety-critical systems has paralleled advancements in quantum computing, leading to the emerging field of Quantum Machine Learning (QML). While safety monitoring has progressed in classical ML, existing methods are not directly applicable to QML due to fundamental differences in quantum computation. Given the novelty of QML, dedicated safety mechanisms remain underdeveloped. This paper introduces Q-SafeML, a safety monitoring approach for QML. The method builds on SafeML, a recent method that utilises statistical distance measures to assess model accuracy and provide confidence on the reasoning of an algorithm. An adapted version of Q-SafeML incorporates quantum-centric distance measures, aligning with the probabilistic nature of QML outputs. Q-SafeML detects distances between operational and training data addressing the concept drifts in the context of QML. Experiments on QCNN and VQC Models show that this enables informed human oversight, enhancing system transparency and safety. 

## Code Structure
Examples Included in this repository detail approaches to applying the Quantum SafeML method to two diferent case implementations of Hybrid Quantum-Classical amchien elanring mdoels. Hybrid models are chosen specifically to better accomodate for the computational limitations of the classical devices quanutm simulations will be ran on, and to act more intermediately when bridging the gap between this intially entirely classical method and the quantum machine learning domain. 

## Brief coverage of VQC example
Following our VQC example notebook, we begin with Importing Necessary libraries. for this implementation, it includes:
- Qiskit
- Qiskit Machine Leanring
- Numpy
- Pandas
- Sklearn
- Matplotlib
- scipy
We then move to creatign functiosn for data covnersion, ensuring our passed data fits the format of our impleemnted quantum distance emtrics, of which there is:
- Quantum Relative entropy
- Trace distance
- bures distance
- Fidelity

Next, we employ Qiskit machine leanring to instantiate VQC and fit it to our chosen datasets.

After this, we take a sampel class, in thsi example just the first class, and view the distance emtrics for the correcta dn incorrect rpediction sets. We do this for each dataset our model trianed on to garner the following results:

| #  | Dataset   | Bures Distance | Trace Distance | Fidelity | Quantum Relative Entropy | True Accuracy |
|----|-----------|----------------|----------------|----------|---------------------------|----------------|
| 0  | Iris      | 0.7695         | 0.5208         | 0.4347   | 1.0000                    | 0.5667         |
| 1  | Wine      | 0.8832         | 0.3467         | 0.2982   | 1.0000                    | 0.3056         |
| 2  | Family    | 0.3021         | 0.0710         | 0.9098   | 0.1810                    | 0.3000         |
| 3  | Transport | 0.3559         | 0.1549         | 0.8735   | 0.2960                    | 0.2188         |

## 📦 Quantum SafeML (`QSafeML`)

**Quantum SafeML** is a proof-of-concept framework that extends the [SafeML](https://doi.org/10.1016/j.artint.2021.103537) safety monitoring methodology to quantum machine learning (QML) systems. It adapts classical out-of-distribution detection principles for quantum classifiers using quantum-specific distance metrics like **trace distance**, **Bures distance**, and **quantum fidelity**.

This project implements Quantum SafeML on QML models including:
- Variational Quantum Classifiers (VQC),
- Quantum Neural Networks (QNN), and
- Quantum Kernel-based Classifiers (QSVC),

using IBM's [Qiskit](https://qiskit.org/) simulator.

💡 The approach allows monitoring and identifying prediction uncertainty in quantum models—critical for building safe and trustworthy quantum AI in domains such as healthcare, robotics, and cybersecurity.

📄 Project conducted as part of a BSc dissertation at the **University of Hull** under the supervision of [Dr Koorosh Aslansefat](https://www.hull.ac.uk/staff-directory/koorosh-aslansefat).

🎓 [Thesis PDF](./Oliver_BSc_Thesis.pdf)

🎥 Watch the project walkthrough:


[![Watch the video](http://img.youtube.com/vi/ndlLo0g1R7E/0.jpg)](https://www.youtube.com/watch?v=ndlLo0g1R7E)

🌐 More info: [Project Website](https://plennock.github.io/Honours-Stage-Project/)



## Contribution
Overall, this project serves as a support of the bridging of the gap between quanutm comptuing and machien learning, bopth of which have shown significant potential to effect the future. Quanutm machine leanring's vast potential must be accompanied by adequate safety monitoring standrds, and so a logical step to beginthe dialouge surrounding this domain is an adaptation of an existing classical machine learning safety monitoring method onto a hybrid system.
