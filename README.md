# pulumi-python-proxmox
For use with cloud-init code to push to on-prem proxmox cluster for automating creation of VMs

## Plan

1. Get basic cloud-init code that works with Proxmox for the VM or container you want to build.
    1. K3os?
    1. go hardcore with kubeadm?
1. Get networking and auth figured out to have GitHub Actions push code back to on-prem proxmox API on the cluster.
1. Test on proxmox cluster.