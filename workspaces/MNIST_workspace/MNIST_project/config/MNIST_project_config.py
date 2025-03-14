
# # === Configuration options ===

# def set_config(c):
#     c.input_path                   = "workspaces/MNIST_workspace/data/mnist_combined.npz"
#     c.data_dimension               = 1
#     c.compression_ratio            = 2.0
#     c.apply_normalization          = False
#     c.model_name                   = "Conv_AE"
#     c.model_type                    = "convolutional"
#     c.epochs                       = 10
#     c.lr                           = 0.001
#     c.batch_size                   = 512
#     c.early_stopping               = True
#     c.lr_scheduler                 = True




# # === Additional configuration options ===

#     c.early_stopping_patience      = 100
#     c.min_delta                    = 0
#     c.lr_scheduler_patience        = 50
#     c.custom_norm                  = False
#     c.reg_param                    = 0.001
#     c.RHO                          = 0.05
#     c.test_size                    = 0
#     # c.number_of_columns            = 24
#     # c.latent_space_size            = 12
#     c.extra_compression            = False
#     c.intermittent_model_saving    = False
#     c.intermittent_saving_patience = 100
#     c.mse_avg                      = False
#     c.mse_sum                      = True
#     c.emd                          = False
#     c.l1                           = True
#     c.activation_extraction        = False
#     c.deterministic_algorithm      = True
#     c.separate_model_saving        = False
# def set_config(c):
#     c.input_path = "workspaces/MNIST_workspace/data/mnist_combined.npz"
#     c.compression_ratio = 10
#     # c.number_of_columns = 24
#     # c.latent_space_size = 15
#     c.epochs = 10
#     c.early_stopping = False
#     c.early_stopping_patience = 100
#     c.min_delta = 0
#     c.lr_scheduler = True
#     c.lr_scheduler_patience = 50
#     c.model_name = "Conv_AE"
#     c.model_type = "convolutional"
#     c.custom_norm = True
#     c.l1 = True
#     c.reg_param = 0.001
#     c.RHO = 0.05
#     c.lr = 0.001
#     c.batch_size = 60
#     c.test_size = 0
#     c.data_dimension = 2
#     c.apply_normalization = False
#     c.extra_compression = False
#     c.intermittent_model_saving = False
#     c.intermittent_saving_patience = 100
#     c.activation_extraction = False
#     c.deterministic_algorithm = False
#     c.separate_model_saving = False


# # def set_config(c):
# #     c.input_path = "workspaces/CFD_workspace/data/CFDAnimation.npz"
# #     c.data_dimension = 2
# #     c.compression_ratio = 2.0
# #     c.apply_normalization = False
# #     c.model_name = "CFD_dense_AE"
# #     c.epochs = 2
# #     c.lr = 0.001
# #     c.batch_size = 1
# #     c.early_stopping = True
# #     c.lr_scheduler = False

# #     # === Additional configuration options ===

# #     c.early_stopping_patience = 100
# #     c.min_delta = 0
# #     c.lr_scheduler_patience = 50
# #     c.custom_norm = True
# #     c.l1 = True
# #     c.reg_param = 0.001
# #     c.RHO = 0.05
# #     c.test_size = 0
# #     c.extra_compression = False
# #     c.intermittent_model_saving = False
# #     c.intermittent_saving_patience = 100
# #     c.mse_avg = False
# #     c.mse_sum = True
# #     c.emd = False
# #     c.l1 = True
# #     c.activation_extraction = False
# #     c.deterministic_algorithm = False

# === Configuration options ===


def set_config(c):
    c.input_path = "workspaces/MNIST_workspace/data/mnist_new.npz"
    c.data_dimension = 1
    c.compression_ratio = 2
    c.apply_normalization = True
    c.model_name = "AE"
    c.epochs = 10
    c.lr = 0.001
    c.batch_size = 512
    c.early_stopping = True
    c.lr_scheduler = True
    c.save_error_bounded_deltas = False
    c.error_bounded_requirement = 10

    # === Additional configuration options ===

    c.early_stopping_patience = 100
    c.min_delta = 0
    c.lr_scheduler_patience = 50
    c.custom_norm = False
    c.reg_param = 0.001
    c.RHO = 0.05
    c.test_size = 0
    # c.number_of_columns = 24
    # c.latent_space_size = 15
    c.extra_compression = False
    c.intermittent_model_saving = False
    c.intermittent_saving_patience = 100
    c.mse_avg = False
    c.mse_sum = True
    c.emd = False
    c.l1 = True
    c.activation_extraction = True
    c.deterministic_algorithm = False
    c.type_list = [
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "float64",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "float64",
        "float64",
        "float64",
        "int",
        "int",
    ]
    c.convert_to_blocks = False
    c.separate_model_saving = False
