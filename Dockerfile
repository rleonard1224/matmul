FROM nvidia/cuda:10.1-devel

ENV PATH /opt/conda/bin:$PATH
ENV BLENDER_VERSION 2.90
ENV BLENDER_XZ_URL https://mirror.clarkson.edu/blender/release/Blender$BLENDER_VERSION/blender-$BLENDER_VERSION.1-linux64.tar.xz

RUN apt-get update && \
	apt-get install -y \
		wget \
		curl \
		libfreetype6 \
		libgl1-mesa-dev \
		libglu1-mesa \
		libxi6 \
		libxrender1 \
		xz-utils \
		curl \ 
		gcc \
		g++ \
		git \
		vim &&\ 
	apt-get -y autoremove && \
	rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    conda create -n blender python=3.7 -y && \
    echo "conda activate blender" >> ~/.bashrc

SHELL ["conda", "run", "-n", "blender", "/bin/bash", "-c"]

RUN conda install -c conda-forge cupy -y

RUN pip install numpy numba scipy matplotlib ipython notebook pycuda

# Installing Blender
RUN mkdir /usr/local/blender && \
    wget "$BLENDER_XZ_URL" && \
    tar -xf blender*.xz -C /usr/local/blender --strip-components=1 && \
    rm blender*.xz

ENV PATH $PATH:/usr/local/blender/

RUN mv /usr/local/blender/${BLENDER_VERSION}/python/ /usr/local/blender/${BLENDER_VERSION}/python_old && \
		ln -s /opt/conda/envs/blender/ /usr/local/blender/${BLENDER_VERSION}/python

WORKDIR /workspace/