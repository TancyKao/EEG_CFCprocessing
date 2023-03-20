CFC Analysis
=================================

.. _1_Read_EEG_dataset:
.. _2_Detect_Slow_wave_event:
.. _3_Detect_Spindle_event:
.. _4_Graphic_User_Interface:
.. _5_Methodology_of_Event:


All the data analysis based on the Python package "Wonambi". 

1. Read EEG dataset 
-------------------

The first step is set up EEG dataset for wonambi. You can find the script in "general_setup.py"

1.1. Identify the path of Python code 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/general_setup.py
   :language: python
   :linenos:
   :start-after: tag::path_function[]
   :end-before: end::path_function[]

1.2. Identify the path of each individual folder 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/general_setup.py
   :language: python
   :linenos:
   :start-after: tag::root_function[]
   :end-before: end::root_function[]

1.3. Identify the excel file containing the subject's EEG info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/general_setup.py
   :language: python
   :linenos:
   :start-after: tag::ind_function[]
   :end-before: end::ind_function[]


1.4. Identify the channel to be analyzed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/general_setup.py
   :language: python
   :linenos:
   :start-after: tag::chan_function[]
   :end-before: end::chan_function[]



Output file
^^^^^^^^^^^
The output file will be in the following format:

- root_dir/subject/wonambi: new directory for outputs    
- <Subject-ID>.xml = annotations file with scored staging, artefacts and arousals


2. Detect Slow wave event 
-------------------------

2.1. Identify the path of Python code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/Whales_setup_swa.py
   :language: python
   :linenos:
   :start-after: tag::path_function[]
   :end-before: end::path_function[]


2.2. Identify the path of each individual folder 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/Whales_setup_swa.py
   :language: python
   :linenos:
   :start-after: tag::root_function[]
   :end-before: end::root_function[]

2.3. Identify the excel file containing the subject's EEG info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/Whales_setup_swa.py
   :language: python
   :linenos:
   :start-after: tag::ind_function[]
   :end-before: end::ind_function[]

2.4. Setup SWA method
^^^^^^^^^^^^^^^^^^^^^^^

Define the SWA method to use. For the details of each method, refer to the `Wonambi Methods documentation <https://wonambi-python.github.io/gui/methods.html>`

.. literalinclude:: pycode/Whales_setup_swa.py
   :language: python
   :linenos:
   :start-after: tag::SWA_function[]
   :end-before: end::SWA_function[]


2.5. Setup SWA parameters
^^^^^^^^^^^^^^^^^^^^^^^^^

Define the sampling frequency and stage to observe SWA

.. literalinclude:: pycode/Whales_setup_swa.py
   :language: python
   :linenos:
   :start-after: tag::par_function[]
   :end-before: end::par_function[]


2.6. Identify the channel to be analyzed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/Whales_setup_swa.py
   :language: python
   :linenos:
   :start-after: tag::chan_function[]
   :end-before: end::chan_function[]


Output file
^^^^^^^^^^^

- A new annotation file per subject, with individual marked SWA labelled by
 
 the method name (e.g. 'Staresina2015') as well as the consensus events labelled
 
 'swa'.


- A CSV output is generated for each subject, containing the SWA parameters.


3. Detect Spindle event
------------------------

3.1. Identify the path of Python code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/Whales_setup_spindle.py
   :language: python
   :linenos:
   :start-after: tag::path_function[]
   :end-before: end::path_function[]


3.2. Identify the path of each individual folder 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/Whales_setup_spindle.py
   :language: python
   :linenos:
   :start-after: tag::root_function[]
   :end-before: end::root_function[]

3.3. Identify the excel file containing the subject's EEG info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/Whales_setup_spindle.py
   :language: python
   :linenos:
   :start-after: tag::ind_function[]
   :end-before: end::ind_function[]


3.4. Setup Spindle method
^^^^^^^^^^^^^^^^^^^^^^^^^

Define the Spindle method to use. For the details of each method, refer to the `Wonambi Methods documentation` <https://wonambi-python.github.io/gui/methods.html>

.. literalinclude:: pycode/Whales_setup_spindle.py
   :language: python
   :linenos:
   :start-after: tag::Spindle_function[]
   :end-before: end::Spindle_function[]


3.5. Setup Spindle parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define the sampling frequency and stage to observe SWA.

.. literalinclude:: pycode/Whales_setup_spindle.py
   :language: python
   :linenos:
   :start-after: tag::par_function[]
   :end-before: end::par_function[]


3.6. Identify the channel to be analyzed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: pycode/Whales_setup_spindle.py
   :language: python
   :linenos:
   :start-after: tag::chan_function[]
   :end-before: end::chan_function[]


3.7. Setup frequency and duration for Spindle event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You could define the frequency range and duration to detect the spindle.

.. literalinclude:: pycode/Whales_setup_spindle.py
   :language: python
   :linenos:
   :start-after: tag::freq_function[]
   :end-before: end::freq_function[]


Output file
^^^^^^^^^^^
A new annotation file per subject, with individual marked spindles labelled by
 the method name (e.g. 'Moelle2011') as well as the consensus events labelled
 'spindle'.

A CSV output is generated for each subject, containing the spindle parameters.


4. Graphic User Interface
-------------------------

Alternatively, you can use Wonambi graphic interface to detect SWA and spindle events.

`Wonambi GUI documentation` <https://wonambi-python.github.io/gui/open.html>



5. Methodology of Events
------------------------

The methodology of detecting events in the Wonambi can be found 

<https://wonambi-python.github.io/gui/methods.html>



6. Output data
------------------------

.. image:: img/wonambiout.png
    :width: 400px
    :align: center
    :height: 500px
    :alt: alternate text

The script will create a new directory wonambi for all files that will be created by wonambi to be stored, including:
•  e.g. ID_01.xml - annotations file 
•  backups - (of annotations files etc.)
•  cfc - outputs for cross-frequency-coupling analyses
•  event detection output - The output file name will be labeled as '[subjectID][ChannelName][Event][Method][Freqrange].csv'.

For example, for subject 'ID_01', channel 'E20', event type 'SWA', using the 'Massimini2004' method, and a frequency range of '0.1 to 4 Hz', the output file name would be 'ID_01_E20_slowwave_detsw_Massimini2004_0.10-4.00Hz.csv'.





