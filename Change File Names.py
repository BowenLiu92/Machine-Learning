basedir = 'C:\Programming\Machine Learning\Image Classification\Training\Image_Label'
for i, f in enumerate(os.listdir(basedir)):
    f_new = 'woman{}.jpg'.format(i+1)
    os.rename(os.path.join(basedir, f), os.path.join(basedir, f_new))