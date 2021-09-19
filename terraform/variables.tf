variable "do_token" {
  description = "Token"
  type        = string
}

variable "image" {
  description = "Linux distro"
  type        = string
  default     = "ubuntu-20-04-x64"
}

variable "public_key" {
  description = "SSH public key path"
  type        = string
  default     = "/home/costa/.ssh/sample.pub"
}