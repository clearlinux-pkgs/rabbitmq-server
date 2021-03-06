#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6B73A36E6026DFCA (info@rabbitmq.com)
#
Name     : rabbitmq-server
Version  : 3.8.3.beta.2
Release  : 60
URL      : https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.3-beta.2/rabbitmq-server-generic-unix-latest-toolchain-3.8.3-beta.2.tar.xz
Source0  : https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.3-beta.2/rabbitmq-server-generic-unix-latest-toolchain-3.8.3-beta.2.tar.xz
Source1  : rabbitmq-server.service
Source2  : rabbitmq-server.tmpfiles
Source3  : https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.3-beta.2/rabbitmq-server-generic-unix-latest-toolchain-3.8.3-beta.2.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause HPND MIT MPL-1.1 MPL-2.0
Requires: rabbitmq-server-bin = %{version}-%{release}
Requires: rabbitmq-server-config = %{version}-%{release}
Requires: rabbitmq-server-license = %{version}-%{release}
Requires: rabbitmq-server-man = %{version}-%{release}
Requires: rabbitmq-server-services = %{version}-%{release}
Requires: otp
BuildRequires : otp
Patch1: 0001-Add-Makefile-and-correct-defaults.patch

%description
Put your EZs here and use rabbitmq-plugins to enable them.

%package bin
Summary: bin components for the rabbitmq-server package.
Group: Binaries
Requires: rabbitmq-server-config = %{version}-%{release}
Requires: rabbitmq-server-license = %{version}-%{release}
Requires: rabbitmq-server-services = %{version}-%{release}

%description bin
bin components for the rabbitmq-server package.


%package config
Summary: config components for the rabbitmq-server package.
Group: Default

%description config
config components for the rabbitmq-server package.


%package doc
Summary: doc components for the rabbitmq-server package.
Group: Documentation
Requires: rabbitmq-server-man = %{version}-%{release}

%description doc
doc components for the rabbitmq-server package.


%package license
Summary: license components for the rabbitmq-server package.
Group: Default

%description license
license components for the rabbitmq-server package.


%package man
Summary: man components for the rabbitmq-server package.
Group: Default

%description man
man components for the rabbitmq-server package.


%package services
Summary: services components for the rabbitmq-server package.
Group: Systemd services

%description services
services components for the rabbitmq-server package.


%prep
%setup -q -n rabbitmq_server-3.8.3-beta.2
cd %{_builddir}/rabbitmq_server-3.8.3-beta.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604604282
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make


%install
export SOURCE_DATE_EPOCH=1604604282
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rabbitmq-server
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-APACHE2 %{buildroot}/usr/share/package-licenses/rabbitmq-server/126723edd4ffead796884f730524deccdbdba7b0
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-APACHE2-ExplorerCanvas %{buildroot}/usr/share/package-licenses/rabbitmq-server/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-APACHE2-excanvas %{buildroot}/usr/share/package-licenses/rabbitmq-server/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-APL2-Stomp-Websocket %{buildroot}/usr/share/package-licenses/rabbitmq-server/a118861172e3884edbc819521f390e11bdb5fb9f
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-BSD-base64js %{buildroot}/usr/share/package-licenses/rabbitmq-server/30567b6415ba032fd62a753813639c8555e7267e
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-BSD-recon %{buildroot}/usr/share/package-licenses/rabbitmq-server/9802eda8562143bc49d55873b49496c2de120c89
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-ISC-cowboy %{buildroot}/usr/share/package-licenses/rabbitmq-server/67b41fbf9be658f57723439684346c6b9917febb
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-EJS %{buildroot}/usr/share/package-licenses/rabbitmq-server/88848a3dbcd10312917ad8ebd686a06cc924ef86
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-EJS10 %{buildroot}/usr/share/package-licenses/rabbitmq-server/668887c1cb5b8e0ba6774448c42c8152119176df
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-Erlware-Commons %{buildroot}/usr/share/package-licenses/rabbitmq-server/3d4f7347b7c13e3807bc84449451071f61995c58
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-Flot %{buildroot}/usr/share/package-licenses/rabbitmq-server/59d7f8d2480093f4a8c1a1f4d481f142176a0007
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-Mochi %{buildroot}/usr/share/package-licenses/rabbitmq-server/9142802977452fd68dcfcddcefb3f7eb73361390
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-Sammy %{buildroot}/usr/share/package-licenses/rabbitmq-server/3d8812f47cf1bca841e7417a83a133e81a5f4190
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-Sammy060 %{buildroot}/usr/share/package-licenses/rabbitmq-server/c865e79d84ee6f58d321b3b3c00fe0ed63a2a4e9
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-jQuery %{buildroot}/usr/share/package-licenses/rabbitmq-server/11dfd9e898fabc7b2c2ed1b0f002ac5150874eba
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MIT-jQuery164 %{buildroot}/usr/share/package-licenses/rabbitmq-server/c9541868f62bcaafd76e3b74bf43515144ff36c8
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MPL %{buildroot}/usr/share/package-licenses/rabbitmq-server/af219e97db4dc8bdd40894a87eed199e724e4988
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MPL-RabbitMQ %{buildroot}/usr/share/package-licenses/rabbitmq-server/af219e97db4dc8bdd40894a87eed199e724e4988
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-MPL2 %{buildroot}/usr/share/package-licenses/rabbitmq-server/8fcc05c0dd9d9c76e948120c9520e4cbe85fb527
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-erlcloud %{buildroot}/usr/share/package-licenses/rabbitmq-server/982208a52a0121a01a21e2afca1497a9e38ce5eb
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-httpc_aws %{buildroot}/usr/share/package-licenses/rabbitmq-server/7792ca84400a4067387e584b16fa9c594a9e3dc6
cp %{_builddir}/rabbitmq_server-3.8.3-beta.2/LICENSE-rabbitmq_aws %{buildroot}/usr/share/package-licenses/rabbitmq-server/7792ca84400a4067387e584b16fa9c594a9e3dc6
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/rabbitmq-server.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/rabbitmq-server.conf
## Remove excluded files
rm -f %{buildroot}/usr/bin/cuttlefish

%files
%defattr(-,root,root,-)
/usr/lib/rabbitmq-server/ebin/amqqueue.beam
/usr/lib/rabbitmq-server/ebin/amqqueue_v1.beam
/usr/lib/rabbitmq-server/ebin/background_gc.beam
/usr/lib/rabbitmq-server/ebin/code_server_cache.beam
/usr/lib/rabbitmq-server/ebin/dep_built
/usr/lib/rabbitmq-server/ebin/gatherer.beam
/usr/lib/rabbitmq-server/ebin/gm.beam
/usr/lib/rabbitmq-server/ebin/lager_exchange_backend.beam
/usr/lib/rabbitmq-server/ebin/lqueue.beam
/usr/lib/rabbitmq-server/ebin/mirrored_supervisor_sups.beam
/usr/lib/rabbitmq-server/ebin/pg_local.beam
/usr/lib/rabbitmq-server/ebin/rabbit.app
/usr/lib/rabbitmq-server/ebin/rabbit.beam
/usr/lib/rabbitmq-server/ebin/rabbit_access_control.beam
/usr/lib/rabbitmq-server/ebin/rabbit_alarm.beam
/usr/lib/rabbitmq-server/ebin/rabbit_amqqueue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_amqqueue_process.beam
/usr/lib/rabbitmq-server/ebin/rabbit_amqqueue_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_amqqueue_sup_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_auth_backend_internal.beam
/usr/lib/rabbitmq-server/ebin/rabbit_auth_mechanism_amqplain.beam
/usr/lib/rabbitmq-server/ebin/rabbit_auth_mechanism_cr_demo.beam
/usr/lib/rabbitmq-server/ebin/rabbit_auth_mechanism_plain.beam
/usr/lib/rabbitmq-server/ebin/rabbit_autoheal.beam
/usr/lib/rabbitmq-server/ebin/rabbit_backing_queue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_basic.beam
/usr/lib/rabbitmq-server/ebin/rabbit_binding.beam
/usr/lib/rabbitmq-server/ebin/rabbit_boot_steps.beam
/usr/lib/rabbitmq-server/ebin/rabbit_channel.beam
/usr/lib/rabbitmq-server/ebin/rabbit_channel_interceptor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_channel_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_channel_sup_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_client_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_config.beam
/usr/lib/rabbitmq-server/ebin/rabbit_connection_helper_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_connection_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_connection_tracking.beam
/usr/lib/rabbitmq-server/ebin/rabbit_connection_tracking_handler.beam
/usr/lib/rabbitmq-server/ebin/rabbit_control_pbe.beam
/usr/lib/rabbitmq-server/ebin/rabbit_core_ff.beam
/usr/lib/rabbitmq-server/ebin/rabbit_core_metrics_gc.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validation.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validator_accept_everything.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validator_min_password_length.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validator_password_regexp.beam
/usr/lib/rabbitmq-server/ebin/rabbit_dead_letter.beam
/usr/lib/rabbitmq-server/ebin/rabbit_definitions.beam
/usr/lib/rabbitmq-server/ebin/rabbit_diagnostics.beam
/usr/lib/rabbitmq-server/ebin/rabbit_direct.beam
/usr/lib/rabbitmq-server/ebin/rabbit_disk_monitor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_epmd_monitor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_event_consumer.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_decorator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_parameters.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_direct.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_fanout.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_headers.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_invalid.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_topic.beam
/usr/lib/rabbitmq-server/ebin/rabbit_feature_flags.beam
/usr/lib/rabbitmq-server/ebin/rabbit_ff_extra.beam
/usr/lib/rabbitmq-server/ebin/rabbit_ff_registry.beam
/usr/lib/rabbitmq-server/ebin/rabbit_fhc_helpers.beam
/usr/lib/rabbitmq-server/ebin/rabbit_fifo.beam
/usr/lib/rabbitmq-server/ebin/rabbit_fifo_client.beam
/usr/lib/rabbitmq-server/ebin/rabbit_fifo_index.beam
/usr/lib/rabbitmq-server/ebin/rabbit_file.beam
/usr/lib/rabbitmq-server/ebin/rabbit_framing.beam
/usr/lib/rabbitmq-server/ebin/rabbit_guid.beam
/usr/lib/rabbitmq-server/ebin/rabbit_health_check.beam
/usr/lib/rabbitmq-server/ebin/rabbit_hipe.beam
/usr/lib/rabbitmq-server/ebin/rabbit_lager.beam
/usr/lib/rabbitmq-server/ebin/rabbit_limiter.beam
/usr/lib/rabbitmq-server/ebin/rabbit_log_tail.beam
/usr/lib/rabbitmq-server/ebin/rabbit_looking_glass.beam
/usr/lib/rabbitmq-server/ebin/rabbit_memory_monitor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_metrics.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_coordinator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_master.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_misc.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_mode.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_mode_all.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_mode_exactly.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_mode_nodes.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_slave.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_sync.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mnesia.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mnesia_rename.beam
/usr/lib/rabbitmq-server/ebin/rabbit_msg_file.beam
/usr/lib/rabbitmq-server/ebin/rabbit_msg_store.beam
/usr/lib/rabbitmq-server/ebin/rabbit_msg_store_ets_index.beam
/usr/lib/rabbitmq-server/ebin/rabbit_msg_store_gc.beam
/usr/lib/rabbitmq-server/ebin/rabbit_networking.beam
/usr/lib/rabbitmq-server/ebin/rabbit_node_monitor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_nodes.beam
/usr/lib/rabbitmq-server/ebin/rabbit_parameter_validation.beam
/usr/lib/rabbitmq-server/ebin/rabbit_password.beam
/usr/lib/rabbitmq-server/ebin/rabbit_password_hashing_md5.beam
/usr/lib/rabbitmq-server/ebin/rabbit_password_hashing_sha256.beam
/usr/lib/rabbitmq-server/ebin/rabbit_password_hashing_sha512.beam
/usr/lib/rabbitmq-server/ebin/rabbit_peer_discovery.beam
/usr/lib/rabbitmq-server/ebin/rabbit_peer_discovery_classic_config.beam
/usr/lib/rabbitmq-server/ebin/rabbit_peer_discovery_dns.beam
/usr/lib/rabbitmq-server/ebin/rabbit_plugins.beam
/usr/lib/rabbitmq-server/ebin/rabbit_policies.beam
/usr/lib/rabbitmq-server/ebin/rabbit_policy.beam
/usr/lib/rabbitmq-server/ebin/rabbit_policy_merge_strategy.beam
/usr/lib/rabbitmq-server/ebin/rabbit_prelaunch.beam
/usr/lib/rabbitmq-server/ebin/rabbit_prequeue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_priority_queue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_consumers.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_decorator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_index.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_location_client_local.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_location_min_masters.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_location_random.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_location_validator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_master_location_misc.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_master_locator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_quorum_memory_manager.beam
/usr/lib/rabbitmq-server/ebin/rabbit_quorum_queue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_reader.beam
/usr/lib/rabbitmq-server/ebin/rabbit_recovery_terms.beam
/usr/lib/rabbitmq-server/ebin/rabbit_restartable_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_router.beam
/usr/lib/rabbitmq-server/ebin/rabbit_runtime_parameters.beam
/usr/lib/rabbitmq-server/ebin/rabbit_ssl.beam
/usr/lib/rabbitmq-server/ebin/rabbit_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_sysmon_handler.beam
/usr/lib/rabbitmq-server/ebin/rabbit_sysmon_minder.beam
/usr/lib/rabbitmq-server/ebin/rabbit_table.beam
/usr/lib/rabbitmq-server/ebin/rabbit_trace.beam
/usr/lib/rabbitmq-server/ebin/rabbit_upgrade.beam
/usr/lib/rabbitmq-server/ebin/rabbit_upgrade_functions.beam
/usr/lib/rabbitmq-server/ebin/rabbit_variable_queue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_version.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_limit.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_msg_store.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_process.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_sup_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_sup_wrapper.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vm.beam
/usr/lib/rabbitmq-server/ebin/supervised_lifecycle.beam
/usr/lib/rabbitmq-server/ebin/tcp_listener.beam
/usr/lib/rabbitmq-server/ebin/tcp_listener_sup.beam
/usr/lib/rabbitmq-server/ebin/term_to_binary_compat.beam
/usr/lib/rabbitmq-server/ebin/unconfirmed_messages.beam
/usr/lib/rabbitmq-server/ebin/vhost.beam
/usr/lib/rabbitmq-server/ebin/vhost_v1.beam
/usr/lib/rabbitmq-server/escript/rabbitmq-diagnostics
/usr/lib/rabbitmq-server/escript/rabbitmq-plugins
/usr/lib/rabbitmq-server/escript/rabbitmq-queues
/usr/lib/rabbitmq-server/escript/rabbitmq-upgrade
/usr/lib/rabbitmq-server/escript/rabbitmqctl
/usr/lib/rabbitmq-server/include/amqqueue.hrl
/usr/lib/rabbitmq-server/include/amqqueue_v1.hrl
/usr/lib/rabbitmq-server/include/amqqueue_v2.hrl
/usr/lib/rabbitmq-server/include/gm_specs.hrl
/usr/lib/rabbitmq-server/include/rabbit.hrl
/usr/lib/rabbitmq-server/include/rabbit_core_metrics.hrl
/usr/lib/rabbitmq-server/include/rabbit_framing.hrl
/usr/lib/rabbitmq-server/include/rabbit_log.hrl
/usr/lib/rabbitmq-server/include/rabbit_memory.hrl
/usr/lib/rabbitmq-server/include/rabbit_misc.hrl
/usr/lib/rabbitmq-server/include/rabbit_msg_store.hrl
/usr/lib/rabbitmq-server/include/resource.hrl
/usr/lib/rabbitmq-server/include/vhost.hrl
/usr/lib/rabbitmq-server/include/vhost_v1.hrl
/usr/lib/rabbitmq-server/include/vhost_v2.hrl
/usr/lib/rabbitmq-server/plugins/README
/usr/lib/rabbitmq-server/plugins/accept-0.3.5.ez
/usr/lib/rabbitmq-server/plugins/amqp10_client-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/amqp10_common-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/amqp_client-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/aten-0.5.2.ez
/usr/lib/rabbitmq-server/plugins/base64url-1.0.1.ez
/usr/lib/rabbitmq-server/plugins/cowboy-2.6.1.ez
/usr/lib/rabbitmq-server/plugins/cowlib-2.7.0.ez
/usr/lib/rabbitmq-server/plugins/credentials_obfuscation-1.1.0.ez
/usr/lib/rabbitmq-server/plugins/gen_batch_server-0.8.2.ez
/usr/lib/rabbitmq-server/plugins/goldrush-0.1.9.ez
/usr/lib/rabbitmq-server/plugins/jose-1.8.4.ez
/usr/lib/rabbitmq-server/plugins/jsx-2.9.0.ez
/usr/lib/rabbitmq-server/plugins/lager-3.8.0.ez
/usr/lib/rabbitmq-server/plugins/observer_cli-1.5.2.ez
/usr/lib/rabbitmq-server/plugins/prometheus-4.4.0.ez
/usr/lib/rabbitmq-server/plugins/ra-1.0.5.ez
/usr/lib/rabbitmq-server/plugins/rabbit_common-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_amqp1_0-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_backend_cache-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_backend_http-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_backend_ldap-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_backend_oauth2-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_mechanism_ssl-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_aws-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_consistent_hash_exchange-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_event_exchange-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_federation-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_federation_management-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_jms_topic_exchange-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_management-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_management_agent-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_mqtt-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_aws-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_common-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_consul-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_etcd-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_k8s-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_prometheus-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_random_exchange-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_recent_history_exchange-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_sharding-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_shovel-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_shovel_management-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_stomp-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_top-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_tracing-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_trust_store-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_dispatch-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_mqtt-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_mqtt_examples-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_stomp-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_stomp_examples-3.8.3-beta.2.ez
/usr/lib/rabbitmq-server/plugins/ranch-1.7.1.ez
/usr/lib/rabbitmq-server/plugins/recon-2.5.0.ez
/usr/lib/rabbitmq-server/plugins/stdout_formatter-0.2.2.ez
/usr/lib/rabbitmq-server/plugins/syslog-3.4.5.ez
/usr/lib/rabbitmq-server/plugins/sysmon_handler-1.2.0.ez
/usr/lib/rabbitmq-server/priv/schema/rabbit.schema
/usr/lib/rabbitmq-server/sbin/cuttlefish
/usr/lib/rabbitmq-server/sbin/rabbitmq-defaults
/usr/lib/rabbitmq-server/sbin/rabbitmq-diagnostics
/usr/lib/rabbitmq-server/sbin/rabbitmq-env
/usr/lib/rabbitmq-server/sbin/rabbitmq-plugins
/usr/lib/rabbitmq-server/sbin/rabbitmq-queues
/usr/lib/rabbitmq-server/sbin/rabbitmq-server
/usr/lib/rabbitmq-server/sbin/rabbitmq-upgrade
/usr/lib/rabbitmq-server/sbin/rabbitmqctl

%files bin
%defattr(-,root,root,-)
/usr/bin/rabbitmq-defaults
/usr/bin/rabbitmq-diagnostics
/usr/bin/rabbitmq-env
/usr/bin/rabbitmq-plugins
/usr/bin/rabbitmq-server
/usr/bin/rabbitmqctl

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/rabbitmq-server.conf

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/rabbitmq\-server/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rabbitmq-server/11dfd9e898fabc7b2c2ed1b0f002ac5150874eba
/usr/share/package-licenses/rabbitmq-server/126723edd4ffead796884f730524deccdbdba7b0
/usr/share/package-licenses/rabbitmq-server/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/rabbitmq-server/30567b6415ba032fd62a753813639c8555e7267e
/usr/share/package-licenses/rabbitmq-server/3d4f7347b7c13e3807bc84449451071f61995c58
/usr/share/package-licenses/rabbitmq-server/3d8812f47cf1bca841e7417a83a133e81a5f4190
/usr/share/package-licenses/rabbitmq-server/59d7f8d2480093f4a8c1a1f4d481f142176a0007
/usr/share/package-licenses/rabbitmq-server/668887c1cb5b8e0ba6774448c42c8152119176df
/usr/share/package-licenses/rabbitmq-server/67b41fbf9be658f57723439684346c6b9917febb
/usr/share/package-licenses/rabbitmq-server/7792ca84400a4067387e584b16fa9c594a9e3dc6
/usr/share/package-licenses/rabbitmq-server/88848a3dbcd10312917ad8ebd686a06cc924ef86
/usr/share/package-licenses/rabbitmq-server/8fcc05c0dd9d9c76e948120c9520e4cbe85fb527
/usr/share/package-licenses/rabbitmq-server/9142802977452fd68dcfcddcefb3f7eb73361390
/usr/share/package-licenses/rabbitmq-server/9802eda8562143bc49d55873b49496c2de120c89
/usr/share/package-licenses/rabbitmq-server/982208a52a0121a01a21e2afca1497a9e38ce5eb
/usr/share/package-licenses/rabbitmq-server/a118861172e3884edbc819521f390e11bdb5fb9f
/usr/share/package-licenses/rabbitmq-server/af219e97db4dc8bdd40894a87eed199e724e4988
/usr/share/package-licenses/rabbitmq-server/c865e79d84ee6f58d321b3b3c00fe0ed63a2a4e9
/usr/share/package-licenses/rabbitmq-server/c9541868f62bcaafd76e3b74bf43515144ff36c8
/usr/share/package-licenses/rabbitmq-server/de33ead2bee64352544ce0aa9e410c0c44fdf7d9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/rabbitmq-env.conf.5.gz
/usr/share/man/man8/rabbitmq-diagnostics.8.gz
/usr/share/man/man8/rabbitmq-echopid.8.gz
/usr/share/man/man8/rabbitmq-plugins.8.gz
/usr/share/man/man8/rabbitmq-queues.8.gz
/usr/share/man/man8/rabbitmq-server.8.gz
/usr/share/man/man8/rabbitmq-service.8.gz
/usr/share/man/man8/rabbitmq-upgrade.8.gz
/usr/share/man/man8/rabbitmqctl.8.gz

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rabbitmq-server.service
