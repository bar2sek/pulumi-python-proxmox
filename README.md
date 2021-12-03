# pulumi-python-proxmox
For use with cloud-init code to push to on-prem proxmox cluster for automating creation of VMs

## Overall Idea

1. Get basic cloud-init code that works with Proxmox for the VM template you want to build.
    1. K3os?
    1. go hardcore with kubeadm?
1. Get networking and auth figured out to have GitHub Actions push code back to on-prem proxmox API on the cluster.
1. Test on proxmox cluster.

## What I'm thinking at the moment:

In code repo, I can craft what I want a VM to be, then execute an Action to push it to my proxmox cluster and that will spin it up and place it neatly on my platform.

For example, I have a worker VM running on a node in my cluster. I'd like to have a template of that VM, complete with cloud-init instructions of how and what to setup for my specific cluster like networking and keys and everything, so it can be slid into what is existing and running without any fuss.

[Self-registering compact k3OS clusters to Rancher Server via cloud-init](https://faun.pub/self-registering-compact-k3os-clusters-to-rancher-server-via-cloud-init-d4a89028c1f8)

## Why mess with a hypervisor or VMs at all?? do Kubernetes on bare metal and full git-ops with argoCD? Keep it SIMPLE

[Kubernetes on bare-metal in 10 minutes](https://blog.alexellis.io/kubernetes-in-10-minutes/)

All of the services I want to run on my homelab are containerized anyway, why not run k8s right on the hardware (Ubuntu)

- master node
- 2 worker nodes
- seperate on-prem backup node
- off-prem backups of the on-prem backups